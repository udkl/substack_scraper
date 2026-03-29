*Opinions are my own and do not represent past, present, and/or future employers. All content is based on public information and independent research. This newsletter is not financial advice, and readers should always do their own research before investing in any security. I am invested in the semiconductor industry. As of the date of this publication, I currently hold a long position in Intel Corporation (INTC). Feel free to reach out at jasonschips@gmail.com.*

---

Subscribe to make your biggest long beat earnings this quarter.

Subscribed

---

**I built a tool using Claude Code to automate DCF valuation.**

**[Check it out: dcfmodel.ai](http://www.dcfmodel.ai)**

---

## Pre-Earnings Vibe Check

*(This section was written prior to the earnings call to communicate the prevailing narrative and provide a contrast to post-earnings sentiment)*

There are several narratives and developments that have vaulted Intel from the low of below $20 last year to over $50 today.

First, in a geopolitical environment that is becoming more charged day-by-day, Intel sits in an advantageous position. Some call them “the only US leading edge chipmaker,” others “The United States of Fabs.” I personally prefer the name USSMC (United States Semiconductor Manufacturing Company). Any which way you slice it, US leaders recognize we cannot keep relying on the geopolitically fragile Taiwan as our sole source for chips.

The obvious relevant developments here are the US stake in Intel, which formalized the government’s commitment to Intel’s survival in August 2025, and Nvidia’s partnership announcement in September, which took the stock from $25 to $33 and marked the real start of the rally. The Nvidia deal included both a $5 billion investment and a commitment to co-develop custom Xeon CPUs integrated with NVLink technology. If the government stake signaled that Washington wanted Intel to survive, the Nvidia partnership signaled that Washington had made calls - that the message to the industry’s biggest winner was “go help Intel.”

Second, leading edge capacity is tighter than it’s ever been. See based Irrational Analysis article:

[![](https://substackcdn.com/image/fetch/$s_!hHWs!,w_56,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba1efe89-1235-4b7c-8017-ab2c1ecf5526_521x521.png)Irrational Analysis

[Fab]ulous Failures

Irrational Analysis is heavily invested in the semiconductor industry…

Read more

2 months ago · 107 likes · 12 comments · Irrational Analysis](https://irrationalanalysis.substack.com/p/fabulous-failures?utm_source=substack&utm_campaign=post_embed&utm_medium=web)

If you’ve been following the semiconductor equipment world or have investments in semicap stocks, you may have noticed a minor rally across most of the big names. (That was sarcasm, they are up an average of 30% YTD.) As Intel has capacity that mostly goes unused in normal markets since the fabless folks don’t care to redesign their products for a whole new foundry using an entirely different PDK, this tightness may finally force their hand. When TSMC can only allocate 80% of requested wafers and every hyperscaler is scrambling for supply, the calculus changes. Fabless companies that spent years avoiding the painful switch to Intel’s PDK may have no choice but to start qualifying a second source - and once they make that investment, Intel gains the learning volume it needs to improve yields, which attracts more customers, which generates more volume. The chicken-and-egg problem that has plagued Intel Foundry starts to unwind.

Plus, their process technology has been steadily improving. Yields are less bad now, and importantly, heading in the right direction - the rumor heading into earnings was that 18A yields had reached around 60%, well ahead of the 40-50% the market expected six months ago. Apple’s commitment of lower-end MacBook chips to Intel’s 18A-P node in November was the first major validation of this progress, and Google’s commitment of TPU packaging to Intel’s EMIB technology added another proof point. Two of the most demanding customers in the world looked at Intel’s roadmap and said yes.

Third, CPU shortage. Turns out that Claude Code is a thing now. [Even the mainstream is seeing this.](https://www.wsj.com/tech/ai/anthropic-claude-code-ai-7a46460e?gaa_at=eafs&gaa_n=AWEtsqcLWMZ2MjB7xRwEcR3u8yStsxK3QxCWKgeDztRU42wqZCPd8YBrScl-Qk7eJFQ%3D&gaa_ts=69730933&gaa_sig=IeZTU-YcKzelv4MzSfQK87dKCeh4ob3eo3HdN3ASsYs94w45C9uavYYRQSfP_kW6upDJ035Ng39eI8wLE3UL6g%3D%3D)

Being the first major adoption wave of agentic AI, Claude Code has shown the world, and many investors, what agentic AI is capable of and how much standard server CPU processing power is needed to complete all those tool calls, MCP servers, sandbox environments, and CI/CD pipelines that agentic workloads spawn. Each user prompt can trigger dozens of CPU-bound subprocesses - code compilation, test execution, API calls, browser rendering - and agents invoke these tools at 10-100x the speed of human users. The CPU, long viewed as the boring part of the AI stack, suddenly matters again. Intel’s CFO put it well on tonight’s call:

> “The world is shifting from human-prompted requests to persistent and recursive commands driven by computer-to-computer interactions. The CPU’s central function coordinating this traffic will drive not only traditional server refresh, but new demand that grows the installed base.”

This isn’t a refresh cycle. It’s a structural expansion of CPU demand driven by workloads that didn’t exist eighteen months ago.

## The Earnings

[![](https://substackcdn.com/image/fetch/$s_!aaFi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f4f2392-2b7e-4dcc-9a5c-3c5673babfea_1392x780.png)](https://substackcdn.com/image/fetch/$s_!aaFi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f4f2392-2b7e-4dcc-9a5c-3c5673babfea_1392x780.png)

Ouch.

#### Press Release

[![](https://substackcdn.com/image/fetch/$s_!fePQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc42d474-e549-4fd4-baf9-e7e64d76789f_1558x219.png)](https://substackcdn.com/image/fetch/$s_!fePQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc42d474-e549-4fd4-baf9-e7e64d76789f_1558x219.png)

On the headline, they missed guide gross margins by almost 200 bps and revenue midpoint by 3%.

Now for the actual call…

### Key Negative Themes

#### 1. Supply Management Failure

Intel fumbled supply badly. Six months ago, hyperscalers were signaling core count increases but flat units. Management planned to that. Then unit demand surged in Q3/Q4, and Intel got caught flat-footed. They burned through finished goods inventory in H2 2025 to meet demand, and now that buffer is gone - down to 40% of peak levels. Q1 is now “hand to mouth” as Zinsner put it.

The result: revenue would have been “meaningfully higher” with adequate supply, and Intel would be “well above seasonal” on guidance if not constrained. Instead, both CCG and DCAI are declining into Q1 despite supposedly prioritizing data center. They’re explicitly deprioritizing low-end client to preserve different products for different priority customers, which means ceding share. When asked directly about competitive dynamics, management dodged with vague language about “jockeying for position.”

AMD will fill some of this gap, which is of course very bad. Intel’s saving grace may be that the entire industry is capacity constrained, but that’s bad comfort when you’re the one leaving revenue on the table.

#### 2. 18A Yields Are the Real Problem

The “supply constraint” narrative has holes. If demand is through the roof and Intel has its own fabs, why are gross margins sinking? Why is Panther Lake (their different marquee 18A product) dilutive to corporate average? Why are they increasing outsourcing to TSMC for client different products when TSMC itself is extremely supply constrained?

The answer is yields. Lip-Bu said it directly: yields are “still below what I want them to be.” They’re seeing 7-8% improvement per month but remain focused on “variation” and “defect density” - yield engineering language for “we’re not there yet.” If 18A yields were at the 60% level some rumors estimated, Panther Lake would be margin accretive, not dilutive. They wouldn’t be shipping different products to TSMC and nuking their own gross margins in the process.

The capex answer confirms this: they’re increasing tool spending but not capacity. You don’t add capacity to a low-yielding node - that just multiplies losses. You fix yields first, then scale. My read is 18A yields are probably 40-50%, good enough to ship different products, not good enough to scale profitably.

#### 3. No 14A Capacity Build-Out

Intel is holding back on 14A capacity spend until customers commit, which Lip-Bu expects in H2 2026 through H1 2027. On its face, this is capital discipline. But it’s also a tell.

If the US government were deeply involved behind the scenes - if the domestic manufacturing push were as locked in as the bull case assumes - building tools now would be relatively low risk. The fact that Intel isn’t doing so, and isn’t signaling any implicit government backstop, suggests the policy tailwind may be less concrete than the 50% rally priced in. This is a show-me story, and on 14A capacity, they’re not showing us anything yet.

### Key Positive Themes

#### 1. Yes ASICs Go Attack Broadcom

Lost in the noise: Intel’s custom ASIC business hit a $1 billion run rate in Q4, growing 50% year-over-year and 26% sequentially. Lip-Bu is “committing significantly more resources, focus, and investment dollars” to this segment.

This matters for two reasons. First, it’s a $100 billion TAM where Intel has a structural advantage - they’re a foundry themselves, which means they can offer design services, IP, manufacturing, and advanced packaging as a bundled solution. No other ASIC house can do that. Second, ASIC wins pull customers into the foundry relationship. A hyperscaler designing custom silicon with Intel is a hyperscaler building trust in Intel’s manufacturing. This is a pipeline for 14A external revenue that isn’t getting enough attention.

#### 2. The 14A Thesis Remains Intact

The main long-term investment case was about 14A external foundry revenue starting in 2028. Not much of that changed tonight.

The most important exchange on the call came from Vivek’s question about test chips. At PDK 0.5, customers can begin test chip designs - this is late-stage engagement in the foundry qualification process. Lip-Bu confirmed they released PDK 0.5 at year-end, and critically, that customers are already “looking at test chips.” That language suggests test chips have been received and are under evaluation. He also noted that Intel’s PDKs are now viewed as “industry standard” - a meaningful credibility milestone.

> “I think first of all, I think the engagement with our potential external customer on the 14, they are very active right now. A couple of key customers are working with us. We expect them to really go through the milestone basis on 0.5 PDK and then starting to look at the test chip and look at how is our year performance. And it’s going to be a process to work with them.”

The stated timeline on the call: risk production in late 2027, volume production in 2028. Customer commitment decisions in H2 2026 through H1 2027. Advanced packaging revenue - which Zinsner now says will be “well north of $1 billion” per opportunity, larger than he expected 12-18 months ago - comes even sooner, with customer ramps starting H2 2026. Some customers are willing to prepay to secure capacity.

#### 3. Capex Is Less Bearish Than It Looks

Guidance of “flat to slightly down” capex sounds like retrenchment. But context matters: Intel previously guided capex down meaningfully. Flat to down slightly is actually a raise from prior expectations.

More importantly, the composition of spend is shifting. Intel is “down significantly in space” - they have enough cleanroom footprint. What they’re increasing is tool spending, which is the binding constraint on wafer output. Every marginal dollar of capex now goes directly to production capacity rather than building shells. Zinsner said they’re “ramping up tool spending quite a bit in 2026 relative to 2025” and increasing wafer starts “pretty much across the board across Intel 7, Intel 3, and 18A.”

This is the right capital allocation for their current situation: fix yields with existing tools, add tools to existing cleanrooms, scale capacity once 14A customers commit. It’s not the aggressive posture bulls wanted, but it’s not retreat either.

## Conclusion

So where does tonight leave the three narratives? Let’s rank the 3 pre-earnings narratives:

**The CPU shortage story took the most damage** - Intel fumbled supply, will cede share to AMD in the near term, and management’s explanation that they simply didn’t anticipate the unit surge isn’t confidence-inspiring.

**The leading edge capacity narrative is bruised but not broken**; 18A yields are clearly worse than the 60% rumor suggested, but 14A development remains on track and the test chip engagements with external customers are progressing.

**The government thesis suffered the least direct damage**, but the lack of aggressive 14A tool spending is a soft tell - if Washington were truly backstopping this, you’d expect Intel to be locking in ASML slots now rather than waiting for customer commitments.

The key metrics I’m watching from here are tool orders and customer announcements. Intel specifically guided to customer commitment decisions in H2 2026 through H1 2027. If that window passes without a major foundry win, we have a problem. But if they start hiking capex on tools before those announcements, that’s the leading indicator that good news is coming - you don’t buy the equipment unless you know the volume is locked in.

I’m still long but not adding on this dip. Intel was a crowded trade heading into tonight - third best performing S&P stock, every PM and their mom looking for US semiconductor exposure. There’s probably more unwind ahead near term. The theme of Intel is perpetual hopium: near-term challenges but long-term indispensability. That did not change today. My model still shows a multibagger if 14A does its thing, (with 164k WSPM of leading-edge cleanroom space according to Alex, check out his very detailed writeup) and I’m not abandoning one of my first and longest semis positions on a messy quarter.

[![](https://substackcdn.com/image/fetch/$s_!b4qE!,w_56,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbd19ea5-c652-4196-9312-f7c0dbf4481f_1920x1920.jpeg)Alex\_Intel\_

The Definitive Edition: Analysis of Every Single Intel Fab Across the US, Ireland, Israel, and Malaysia

(You don’t wanna know how long the face swaps took)Thanks for reading! Subscribe for free to receive new posts and support my work…

Read more

2 months ago · 30 likes · 10 comments · Alex\_Intel\_](https://alexintel.substack.com/p/the-definitive-edition-analysis-of?utm_source=substack&utm_campaign=post_embed&utm_medium=web)

---

Subscribe to make Intel go up.

Subscribed