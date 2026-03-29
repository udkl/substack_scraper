"""
Purpose:
    Scrape paid subscription articles from a Substack newsletter, saving both HTML and Markdown versions.
    You must edit BASE_URL and SITEMAP_STRING below to match your target newsletter.

Instructions:
    - Set BASE_URL to the newsletter's main URL (e.g., "https://newsletter.eng-leadership.com")
    - Set SITEMAP_STRING to the sitemap path (e.g., "/sitemap.xml")
    - Use --paid flag to enable scraping paid content (manual login required)
"""

import requests
from bs4 import BeautifulSoup
import lxml
import markdownify
import json
import os
import hashlib
from selenium import webdriver
from time import sleep
import argparse

# Globals are now configurable via CLI arguments
SITEMAP_STRING = "/sitemap.xml"


def selenium_login():
    driver = webdriver.Chrome()
    driver.get("https://substack.com/sign-in")
    input("After you have logged in and see your account, press Enter here to continue...")
    print("Continuing with scraping...")
    return driver


def get_article_urls_and_lastmod(sitemap_url):
    resp = requests.get(sitemap_url)
    soup = BeautifulSoup(resp.content, "xml")
    url_to_lastmod = {}
    urls = []
    for url_tag in soup.find_all("url"):
        loc = url_tag.find("loc")
        lastmod = url_tag.find("lastmod")
        if loc:
            url_text = loc.text
            urls.append(url_text)
            url_to_lastmod[url_text] = lastmod.text if lastmod else ""
    return urls, url_to_lastmod


def extract_article_html_and_md(soup, assets_dir):
    """
    Extracts article content, downloads images to assets_dir, 
    and returns both HTML and Markdown with local image references.
    """
    import os
    import hashlib

    article_container = soup.find("div", class_="available-content")
    if not article_container:
        # Fallback if the specific class is not found
        article_container = soup.find("article") or soup
        
    # Process images
    for img in article_container.find_all("img"):
        img_url = img.get("src")
        if not img_url:
            continue
            
        try:
            # Create a unique filename based on the URL hash to avoid duplicates and invalid chars
            img_ext = os.path.splitext(img_url.split("?")[0])[1] or ".jpg"
            if len(img_ext) > 5: # sanitize extension
                img_ext = ".jpg"
            
            img_hash = hashlib.md5(img_url.encode()).hexdigest()
            img_filename = f"{img_hash}{img_ext}"
            img_path = os.path.join(assets_dir, img_filename)
            
            # Download image if it doesn't exist
            if not os.path.exists(img_path):
                img_data = requests.get(img_url, timeout=10).content
                with open(img_path, "wb") as f:
                    f.write(img_data)
            
            # Update src to relative path for offline use
            # Assuming files are in /html or /md, they need to go up one level to /assets
            img["src"] = f"../assets/{img_filename}"
        except Exception as e:
            print(f"Failed to download image {img_url}: {e}")

    html_content = str(article_container)
    markdown_content = markdownify.markdownify(html_content, heading_style="ATX")
    return html_content, markdown_content


def scrape_article_selenium(driver, url, assets_dir):
    driver.get(url)
    sleep(10)
    soup = BeautifulSoup(driver.page_source, "lxml")
    return extract_article_html_and_md(soup, assets_dir)


def scrape_article_requests(url, assets_dir):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "lxml")
    return extract_article_html_and_md(soup, assets_dir)


def main():
    parser = argparse.ArgumentParser(description="Substack scraper")
    parser.add_argument("--base-url", required=True, help="Base Substack URL (e.g., https://example.substack.com)")
    parser.add_argument("--output-folder", required=True, help="Directory to store scraped content")
    parser.add_argument("--paid", action="store_true", help="Enable scraping paid content (manual login required)")
    args = parser.parse_args()

    # Configuration based on CLI arguments
    base_url = args.base_url.rstrip("/")
    output_folder = args.output_folder
    sitemap_url = f"{base_url}{SITEMAP_STRING}"
    
    html_dir = os.path.join(output_folder, "html")
    md_dir = os.path.join(output_folder, "md")
    assets_dir = os.path.join(output_folder, "assets")
    urls_log = os.path.join(output_folder, "urls.txt")
    results_file = os.path.join(output_folder, "results.json")

    # Ensure directories exist
    for dir_path in [html_dir, md_dir, assets_dir]:
        os.makedirs(dir_path, exist_ok=True)

    driver = None
    if args.paid:
        print("Paid mode enabled. Manual login required.")
        driver = selenium_login()
    else:
        print("Paid mode not enabled. Scraping free content only.")

    print(f"Fetching sitemap from {sitemap_url}...")
    urls, url_to_lastmod = get_article_urls_and_lastmod(sitemap_url)
    print(f"Found {len(urls)} articles.")
    
    with open(urls_log, "w") as url_file:
        for url in urls:
            url_file.write(url + "\n")
    print(f"Saved URLs to {urls_log}")

    # Load existing results for incremental scraping
    results = []
    if os.path.exists(results_file):
        try:
            with open(results_file, "r") as f:
                results = json.load(f)
        except Exception as e:
            print(f"Error loading {results_file}: {e}")

    existing_urls = {item["url"] for item in results}

    for url in urls:
        # Pre-calculate filenames to check existence
        lastmod = url_to_lastmod.get(url, "")
        date_part = lastmod.split("T")[0] if lastmod else ""
        base_name = url.rstrip("/").split("/")[-1]
        if date_part:
            base_name = f"{date_part}_{base_name}"
            
        html_path = os.path.join(html_dir, base_name + ".html")
        md_path = os.path.join(md_dir, base_name + ".md")

        # Skip if files already exist
        html_exists = os.path.exists(html_path)
        md_exists = os.path.exists(md_path)

        if html_exists and md_exists:
            print(f"Skipping {url} (already preserved on disk)")
            # Ensure it's in the results and existing_urls for this run
            if url not in existing_urls:
                results.append({"url": url, "html_file": html_path, "md_file": md_path})
                existing_urls.add(url)
                # Save results occasionally or at least once if we've added to it
                with open(results_file, "w") as f:
                    json.dump(results, f, indent=2)
            continue

        print(f"Scraping {url}")
        try:
            if args.paid:
                html, md = scrape_article_selenium(driver, url, assets_dir)
            else:
                html, md = scrape_article_requests(url, assets_dir)
            
            if html and md:
                with open(html_path, "w", encoding="utf-8") as f_html:
                    f_html.write(html)
                with open(md_path, "w", encoding="utf-8") as f_md:
                    f_md.write(md)
                
                # Update results
                if url not in existing_urls:
                    results.append({"url": url, "html_file": html_path, "md_file": md_path})
                    existing_urls.add(url)
                    
                # Save results incrementally
                with open(results_file, "w") as f:
                    json.dump(results, f, indent=2)
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")

    print(f"Saved {len(results)} articles to {results_file}")
    if driver:
        driver.quit()


if __name__ == "__main__":
    main()
