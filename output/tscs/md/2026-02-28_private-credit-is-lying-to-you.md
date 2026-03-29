On Wednesday, Blue Owl Capital permanently shut the exit door on its retail investors.

By Thursday, activist funds were offering to buy their trapped positions at 65 cents on the dollar.

By Friday, the stock hit a 52-week low.

That is a 72-hour sequence that does not happen to a $307 billion asset manager unless something has gone structurally wrong.

But Blue Owl is not the story. Blue Owl is the weakest link in a chain that runs through $1.7 trillion in private credit, $507 billion in BDC assets, and a software sector that just lost $830 billion in market value in three weeks.

The chain connects AI product launches in January to leveraged loan books marked at par in February, and the gap between those two realities is where the actual risk sits.

[![](https://substackcdn.com/image/fetch/$s_!oQUe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2716505c-07f4-4ab0-af15-79e5f8de6359_2259x1257.png)](https://substackcdn.com/image/fetch/$s_!oQUe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2716505c-07f4-4ab0-af15-79e5f8de6359_2259x1257.png)

Here is what happened. DeepSeek released an open-source reasoning model that matched frontier AI performance at a fraction of the cost. Anthropic launched enterprise workflow automation that landed directly on the business models private credit had been lending against for a decade. Salesforce disclosed “lengthening sales cycles” for the first time.

Intuit flagged “competitive pressure from AI-native alternatives.” The software sector, which had been the single best borrower profile in private credit (recurring revenue, high margins, predictable cash flows, low capex), started repricing from “2030 disruption risk” to “2026 reality.”

The market moved. The marks did not.

That is the entire thesis of this piece, compressed into one sentence. The underlying economics of hundreds of leveraged software companies are deteriorating on a timeline measured in months, while the marks that determine their stated value (and the management fees earned on that stated value, and the NAVs reported to investors based on that stated value) update on a timeline measured in quarters. The gap is widening.

Fitch tracks a 5.7% default rate. Managers report sub-2%. Goldman estimates 15% of private credit borrowers can no longer fully service their interest obligations from cash flow. The DOJ has publicly warned about “creative marks.”

This is not 2007. The transmission mechanism to the banking system does not exist, the scale is different, and the Fed has room to cut. But that comparison, comfortable as it is to dismiss, is answering the wrong question. The right question is simpler and more uncomfortable: what happens when a $1.7 trillion market built on the assumption that software cash flows are permanent meets an AI cost curve that is making them optional?

Over the next 12,000 words, we answer it. We map the exposure across every tier of the private credit ecosystem. We quantify the gap between reported and actual default rates. We explain why recovery assumptions built on historical data are structurally wrong for AI-disrupted software credits. We name names, specific BDCs, specific managers, specific trades on both sides. And we lay out exactly where we think the stress goes next.

This is the most comprehensive analysis of private credit’s AI problem published anywhere. It is also, we think, the most important.

## Why you should be reading TSCS

**If you’re not yet subscribed to TSCS, here is what we do.** We publish institutional-grade equity research and deep-dive analysis before the consensus arrives. We identified the Kitwave & Just Group acquisition setups months before OEP showed up with the bid. We published our AI inference economics framework before the market repriced the sector. Our Datacenter Bible became the go-to infrastructure primer. We called the MSTR bear thesis before it was syndicated across financial media.

7,200+ subscribers. Portfolio managers, analysts, allocators, and investors who want the signal before it becomes noise.

Paid subscribers get the full piece below, including the complete exposure framework, specific trade ideas with entry levels, and the vulnerability mapping across 30+ credits.

Subscribed

### **A note on this collaboration.**

This piece is a joint publication with [Les Barclays](https://open.substack.com/users/46565509-les-barclays?utm_source=mentions).

Les has spent the last six months mapping the fundamentals underneath the AI financing boom. His ["Private Credit's Slow-Motion Reckoning"](https://lesbarclays.substack.com/p/private-credits-slow-motion-reckoning-fc5) called the structural fragility of this market five months before Blue Owl proved him right. His work on [circular AI financing](https://lesbarclays.substack.com/p/corporate-ouroboros), [conduit debt structures](https://lesbarclays.substack.com/p/who-captures-the-value-when-ai-inference), and [Significant Risk Transfers](https://lesbarclays.substack.com/p/the-mechanics-of-significant-risk-transfers) is the best independent coverage of how these financing structures actually work. FT Alphaville called it "a first-principles approach to explaining the technical architecture of modern finance." His structural expertise and my credit/disruption analysis are different skill sets, and the combination is why this piece exists.

[Subscribe to Les Barclays](https://lesbarclays.substack.com/subscribe?utm_source=menu&simple=true&next=https%3A%2F%2Flesbarclays.substack.com%2F%3Futm_campaign%3Dprofile_chips)

## **AI ate the software sector, and private credit owned the tab**

Enterprise software businesses were ideal private credit borrowers: recurring revenue, high margins, predictable cash flows, low capital intensity. Lenders underwrote to revenue multiples and EBITDA, assuming these characteristics persist indefinitely. For a decade, they were right. The model worked beautifully. And then it stopped working, for reasons the models never contemplated.

But “software is in trouble” is lazy framing, and lazy framing is how you lose money.

Not all software is equally exposed. Think of it as a spectrum. On one end, you have workflow automation, horizontal SaaS, CRM, basic legal tech, tax preparation, and low-complexity business process tools.

[![](https://substackcdn.com/image/fetch/$s_!xEyn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b718202-9190-423e-b7a5-0cb3c311ccb7_1405x753.png)](https://substackcdn.com/image/fetch/$s_!xEyn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b718202-9190-423e-b7a5-0cb3c311ccb7_1405x753.png)

These are the companies where the market now believes an AI agent can replicate most of the value proposition at near-zero marginal cost. I want to be careful here, because there is an enormous gap between “demo impressive” and “enterprise production-ready.”

Replacing a Salesforce implementation is not just replicating the CRM logic; it is replicating the integrations, the compliance audit trails, the vendor liability framework, the procurement workflows, and the organizational muscle memory built over years. AI agents are not doing that today. But they do not need to. They need to be good enough that the next contract renewal becomes a negotiation rather than a rubber stamp, good enough that a $500K annual license becomes a $200K annual license, good enough that growth stalls even if churn does not spike.

That margin compression, not outright replacement, is what kills the credit thesis. If your borrower’s revenue growth decelerates from 15% to 3% while carrying 6x leverage, the loan-to-value math breaks regardless of whether a single customer actually switches to an AI agent. And it is that repricing of growth expectations, more than any actual product substitution, that the market is expressing right now.

[![](https://substackcdn.com/image/fetch/$s_!cJUh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55c50baa-853f-47e5-b8e3-ec019696045f_1405x773.png)](https://substackcdn.com/image/fetch/$s_!cJUh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55c50baa-853f-47e5-b8e3-ec019696045f_1405x773.png)

There is a third dimension that most private credit analysis ignores: what is happening to VC-backed software companies. They cannot raise, cannot sell to PE at 2021 multiples, and cannot IPO into a market repricing the sector in real time. They have roughly twelve months to integrate AI and demonstrate a legitimate productivity use case, or they will be deemed guilty until proven innocent.

This matters for private credit in two ways. The VC-backed companies that survive become the competitive threat that compresses margins for private credit borrowers. They are the AI-native alternatives that Intuit flagged in its mid-quarter update.

The ones that fail become a cautionary data point: if venture-funded software companies with no debt and maximum operational flexibility cannot survive AI disruption, what does that imply for leveraged middle-market companies carrying 6-7x? Most VC-backed failures will produce writedowns for venture LPs rather than defaults for credit investors. But their competitive effect on the private credit borrower base is real, and it is accelerating.

On the other end, you have mission-critical infrastructure: cybersecurity platforms, deeply embedded ERP systems (think SAP in a multinational supply chain), industrial control software, and anything that requires regulatory certification or carries liability risk. These businesses face margin pressure from AI, sure. But an AI agent is not replacing CrowdStrike’s endpoint detection next quarter. It is not ripping out a Fortune 500’s SAP implementation because ChatGPT can do invoicing.

The problem for private credit is that the loan books are disproportionately weighted toward the vulnerable end of this spectrum. Public BDC filings make this quantifiable.

The [FT Alphaville](https://open.substack.com/users/444688-ft-alphaville?utm_source=mentions) data, drawing on PitchBook’s BDC database, paints an even more interesting picture of the concentration. BDCs in aggregate hold approximately $507 billion in assets under management. Of that, technology sector exposure is $114 billion. When you include health tech (another $24 billion), total exposure reaches $138 billion, or roughly 27% of the entire BDC universe.

The sector is also structurally concentrated at the manager level: almost half the entire BDC industry is run by just four companies and their subsidiaries (Blackstone, Blue Owl, Ares, and BlackRock), with the largest ten funds accounting for more than half of all assets under management. A fifth of the industry sits in just two funds: Blackstone’s BCRED and Blue Owl’s Credit Income Corp.

[![](https://substackcdn.com/image/fetch/$s_!N4qe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4541b56f-f619-410e-b00f-f16c09610dde_1405x791.png)](https://substackcdn.com/image/fetch/$s_!N4qe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4541b56f-f619-410e-b00f-f16c09610dde_1405x791.png)

What makes this concentration particularly dangerous is the overlap in underlying credits. Toby Nangle’s analysis of individual BDC loan books reveals that the same vulnerable names (Zendesk, Anaplan, The Access Group, PowerSchool Holdings, among others) appear in multiple BDC portfolios, financed at all-in rates of 9-13%, mostly as senior secured first lien. Being in a senior secured, first lien position sounds reassuring in investor presentations, but it is of limited economic value in a failing software business other than as negotiating leverage with other lenders over what scraps of value remain. The correlation risk here is underappreciated: if these overlapping credits deteriorate, the stress hits multiple BDCs simultaneously, and the “diversification” that investors believed they had across different BDC managers turns out to be largely illusory.

[![](https://substackcdn.com/image/fetch/$s_!xiQz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8920c9b1-6b68-473b-a247-20db506b523b_1405x778.png)](https://substackcdn.com/image/fetch/$s_!xiQz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8920c9b1-6b68-473b-a247-20db506b523b_1405x778.png)

OBDC’s schedule of investments as of September 30, 2025 shows software and technology services representing approximately 18-22% of fair value across the portfolio, with meaningful additional exposure through adjacent categories (internet services, business services, data processing) that face similar AI disruption dynamics. Across the broader BDC universe, Fitch estimates technology and software exposure ranges from 15% to over 30% depending on the manager, with tech-focused vehicles like Blue Owl Technology Income Corp sitting at the extreme end.

The concentration exists for two reinforcing reasons, and the second is more damaging than the first. The first, which I have already outlined, is that workflow automation and horizontal SaaS companies were the best private credit borrowers on paper: asset-light, high-margin, beautifully predictable revenue, low capex. They were precisely the kind of business that a lending algorithm loves and a disruption model ignores.

The second reason is vintage-specific and structural. As Matthew Brooker at Bloomberg has documented, many of the buyouts and loans behind these software acquisitions were done at what turned out to be peak valuations for the tech sector, during and just after Covid.

At the same time, rising interest rates shut down the traditional syndicated loan market. Banks were stuck holding leveraged debt they could not sell and lacked capacity for fresh deals. Private credit stepped directly into that breach.

According to Matthew Mish at UBS, direct lenders’ market share in funding buyouts jumped from 15-25% pre-Covid to between 40% and 70% (depending on the quarter) in 2022 and 2023. That concentration of funding at that specific vintage means private credit is now disproportionately exposed to AI disruption not merely because software looked attractive, but because private credit was the only capital available to fund these acquisitions at the moment when valuations were highest and the traditional leveraged loan market had retreated. The selection bias did not just run the wrong way; it ran the wrong way at the worst possible time.

[![](https://substackcdn.com/image/fetch/$s_!oChG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa541add8-46eb-41cc-b54b-5a8d210ec5d0_1405x787.png)](https://substackcdn.com/image/fetch/$s_!oChG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa541add8-46eb-41cc-b54b-5a8d210ec5d0_1405x787.png)

UBS estimates 25-35% of all private credit portfolios now face “elevated AI disruption risk.” Let me translate that from investment bank to English, because vague institutional framing is how sell-side research avoids being wrong while saying nothing useful and it may be closer to the truth than Blue Owl’s headline marks suggest.

[![](https://substackcdn.com/image/fetch/$s_!-MLz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4803ac29-1586-4391-8198-55224ea0d13a_1405x772.png)](https://substackcdn.com/image/fetch/$s_!-MLz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4803ac29-1586-4391-8198-55224ea0d13a_1405x772.png)

“Elevated risk” is a spectrum, and it matters enormously where on that spectrum we land. At one end, it could mean a 5-10% revenue headwind over two years as AI tools compress pricing power, resulting in slightly lower coverage ratios but no defaults. At the other end, it could mean a 30-50% decline in enterprise value as entire software categories get commoditized, blowing out loan-to-value ratios and triggering covenant breaches across the portfolio. The difference between these scenarios is the difference between a mild repricing and a genuine default cycle.

UBS, to their credit, does provide an extreme case: in an “aggressive scenario” they explicitly describe as a tail risk, U.S. private credit default rates could climb to 13% (for context, leveraged loan defaults peaked at roughly 10% during the GFC).

This is a stress-test number, not a forecast.

The useful comparison is not between UBS’s modelled tail and managers’ reported sub-2%, because those numbers are measuring different things under different assumptions. The useful comparison is between Fitch’s 5.7% trailing twelve-month rate (which includes PIK conversions and interest deferrals) and the sub-2% that managers report on earnings calls (which excludes them).

That gap, roughly 3-4x, is the one that should concern allocators, because it exists today, in observable data, with no modelling assumptions required.

[![](https://substackcdn.com/image/fetch/$s_!MFCe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe20bb305-af0a-4abc-bd34-dfcc70be4908_1405x762.png)](https://substackcdn.com/image/fetch/$s_!MFCe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe20bb305-af0a-4abc-bd34-dfcc70be4908_1405x762.png)

My own view sits somewhere in the middle. The 25-35% exposure estimate feels roughly right, but “elevated risk” is not binary. Perhaps 10-15% of private credit portfolios face genuine existential disruption risk (workflow automation, horizontal SaaS, basic legal and tax software). Another 10-15% faces meaningful but manageable margin pressure. And the remainder, the non-software book, faces normal cyclical risk.

The blended outcome is not 13% defaults. It is probably 5-7% true defaults (consistent with Fitch’s current tracking) with another 5-8% in PIK conversions and extend-and-pretend that the headline statistics conveniently exclude.

[![](https://substackcdn.com/image/fetch/$s_!MYT1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F210f77d1-607a-4b8d-81f9-3233de173daf_1405x732.png)](https://substackcdn.com/image/fetch/$s_!MYT1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F210f77d1-607a-4b8d-81f9-3233de173daf_1405x732.png)

The number that actually scares me is the Fitch gap. When independent tracking shows 5.7% and managers report sub-2%, that is not a difference in methodology. It is a difference in incentives.

Managers have every reason to classify PIK conversions, covenant amendments, and maturity extensions as “performing” rather than “defaulted,” because the moment they reclassify, the NAV marks come down, redemptions accelerate, and the fee base shrinks. I am not alleging fraud. I am observing that the accounting framework gives managers extraordinary discretion over when a troubled credit becomes a defaulted one, and that discretion is being exercised in one direction only.

[![](https://substackcdn.com/image/fetch/$s_!O74J!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbb92d37-0c56-4a5e-9aca-29fac7792313_1405x778.png)](https://substackcdn.com/image/fetch/$s_!O74J!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbb92d37-0c56-4a5e-9aca-29fac7792313_1405x778.png)

[![](https://substackcdn.com/image/fetch/$s_!i515!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71ddcb93-78e3-4c2a-b0e0-887d2e8ef7eb_1405x787.png)](https://substackcdn.com/image/fetch/$s_!i515!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71ddcb93-78e3-4c2a-b0e0-887d2e8ef7eb_1405x787.png)

There is a feature of the loan documentation itself that makes all of this worse, and it is one of those things the industry prefers not to discuss publicly.

A substantial proportion of private credit loans originated during the 2021-2023 vintage were structured as covenant-lite or with springing covenants that activate only upon severe deterioration (typically a revolver draw above a threshold). In a traditional leveraged loan with maintenance covenants, credit deterioration triggers a covenant breach, which forces a renegotiation, which in turn forces the lender to acknowledge the problem in its marks.

Covenant-lite structures remove that trigger. The lender can continue marking the loan at or near par as long as the borrower is making interest payments (even if those payments are partially PIK), regardless of how badly the underlying business fundamentals have deteriorated.

The industry professional of 15 years I spoke with described it as “removing the fire alarm from the building. The fire still happens, you just don’t hear about it until the smoke is visible from the street.” For the AI-disrupted software credits specifically, this means the lag between fundamental deterioration and mark recognition that I described in the previous section is even longer than the quarterly reporting cycle alone would suggest. The covenants that would normally force early recognition of stress simply do not exist in many of these loans.

It gets worse. Private credit borrowers routinely report “adjusted EBITDA” that includes cost savings, projected synergies, and pro forma adjustments that inflate the denominator of leverage ratios. A company reported at 5x leverage on adjusted EBITDA might be 7-9x on actual cash EBITDA. This practice is well-documented (S&P has flagged it repeatedly, and Lincoln International’s quarterly reports track the divergence), and in a growth environment the add-backs are at least directionally plausible: if the business is expanding, some portion of the projected savings will materialise.

In a contracting environment, where AI competition is compressing the revenue line, the add-backs that were optimistic-but-arguable become fictional. The leverage math I have been citing throughout this piece (6x as a representative figure for stressed software borrowers) is almost certainly understating the actual leverage at many portfolio companies by 2-3 turns.

At 8-9x true leverage, the margin of safety between “performing credit” and “covenant breach” (to the extent covenants exist) is razor-thin, and the impact of even modest revenue deceleration is amplified.

[![](https://substackcdn.com/image/fetch/$s_!1BJf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee6f7da7-297b-4b4b-9e8c-bac2b8f1aaa4_1405x784.png)](https://substackcdn.com/image/fetch/$s_!1BJf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee6f7da7-297b-4b4b-9e8c-bac2b8f1aaa4_1405x784.png)

There is a further layer of systematic optimism in the data that most investors are not aware of. Alongside the EBITDA add-backs, credit ratings on private credit borrowers are subject to a structural upward bias through the Private Letter Rating process. It costs money to obtain a Private Letter Rating from agencies such as KBRA, Egan Jones, or Morningstar DBRS.

As a result, firms are only likely to seek a new rating if they believe it will be better than their existing one.

Firms that agree with their current rating do not pay for another. Firms that believe their rating is higher than reality certainly do not pay for confirmation. Only firms that believe they deserve a better rating pay for the assessment. This is textbook sample selection bias: the observed distribution of rating changes systematically overstates credit quality because the sample is self-selected by borrowers who expect upgrades.

It also means the migration of rating agencies from the more established (and arguably more conservative) firms to newer entrants, which compete partly on the basis of more issuer-friendly methodologies, is itself an indicator of loosening standards rather than improving credit quality.

To make these default estimates actionable, they need to be translated into losses, and this is where the standard assumptions break down in ways that most analysis of this situation has not yet grappled with.

The historical recovery range for first-lien private credit is 50-65%, per Moody’s. That range is derived from recoveries on businesses where the underlying going-concern value was intact: the company was in distress because of leverage, cyclical weakness, or operational mismanagement, not because its core value proposition was being structurally impaired.

A senior direct lending professional with over 15 years of experience across credit committees and portfolio management, who spoke to me on condition of anonymity, put it bluntly: “The 50-65% recovery assumption is based on collateral that retains value through a restructuring.

For a software company whose recurring revenue is being competed away by AI, the enterprise value that secured the loan is itself the thing being disrupted. The IP has limited standalone value. The customer relationships are the asset, and those relationships are precisely what’s deteriorating.”

[![](https://substackcdn.com/image/fetch/$s_!0hR2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4489a161-5f3a-4485-b040-768cfb7116d1_1405x778.png)](https://substackcdn.com/image/fetch/$s_!0hR2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4489a161-5f3a-4485-b040-768cfb7116d1_1405x778.png)

For non-disrupted credits in the portfolio (industrials, healthcare, business services), the 50-65% range remains reasonable.

For the AI-vulnerable software book specifically, recoveries are more likely to land in the 25-40% range. The logic is straightforward but worth making explicit. Historical 50-65% recoveries assume the acquirer in a restructuring is buying a going concern whose revenue base, while stressed, remains fundamentally intact.

The acquirer pays for the customer relationships, the recurring revenue streams, and the organisational capability. In an AI disruption scenario, those customer relationships are precisely what is deteriorating: the recurring revenue is recurring at lower prices, with shorter contract terms, and against credible competitive alternatives that did not exist when the loan was originated. A distressed acquirer buying a horizontal SaaS company in 2026 is not paying 5-6x revenue as they might have in 2021.

They are paying 2-3x a declining revenue base, which compresses recoveries to the 25-40% range before accounting for the restructuring costs (legal, advisory, operational disruption) that consume another 5-10% of residual value.

The counterargument, that customer contracts retain value even in a disrupted business, is valid for platforms with deep data moats and high switching costs. It is far less valid for workflow automation tools where the switching cost is precisely what AI is reducing. I want to be explicit that 25-40% is a base case for the disrupted portion, not a stress test.

There is one more distinction within the software book that most analysis overlooks, and it matters for how ugly the recoveries actually get: sponsor-backed and non-sponsor-backed credits will produce very different recovery outcomes.

Sponsor-backed companies (those owned by private equity firms) have a parent that can inject equity, negotiate with lenders from a position of institutional sophistication, and manage the workout process.

A PE sponsor with a $2 billion fund is not going to let a portfolio company slip into uncontrolled default if a modest equity injection can buy time for a restructuring. Non-sponsor-backed middle market software companies have no such backstop. When their revenue deteriorates, they are alone with their lenders, and the recovery outcomes are materially worse.

The BDC portfolios under discussion contain a mix of both, and the blended recovery rate will depend heavily on the proportion. Funds with higher concentrations of non-sponsor-backed software credits face the worst end of the 25-40% recovery range; those with predominantly sponsor-backed exposure will fare better, though still below the 50-65% historical norm because even a PE sponsor’s willingness to inject capital has limits when the business thesis itself is impaired.

There is a corollary to this that deserves explicit statement, because it determines how ugly the tail recoveries actually get. When enterprise values fall far enough, PE equity holders will walk away.

Their equity position becomes a deep out-of-the-money option, and the rational economic decision is to stop injecting capital and let the lenders negotiate over what remains. At that point, liens and covenants become largely meaningless, senior secured first lien status notwithstanding, because the restructuring process itself consumes value.

Legal fees, advisory fees, and the operational disruption of a workout eat into whatever residual enterprise value exists. The boring old bank lending adage, that high business risk sectors should carry lower financial risk, feels quite pertinent here, even if it does not sit well with the entrepreneurial approach to private credit lending that characterised the 2021-2023 vintage. The high leverage that was applied to these businesses is now inhibiting their ability to reinvest and stay competitive, which accelerates the very disruption that is compressing their enterprise values.

It is a reflexive loop: leverage constrains adaptation, constrained adaptation accelerates disruption, accelerating disruption compresses enterprise value, compressed enterprise value breaks the leverage math, and at some point the equity holder walks.

At a 5-7% blended default rate, the loss math depends heavily on how you segment the portfolio. On the non-software book, 50-65% recoveries produce implied losses of roughly 2-3.5%, consistent with the standard analysis.

On the software book, at 7% defaults with 30-40% recoveries, implied losses are 4.2-4.9% on that portion. For a fund with 25% software exposure, the blended drag is approximately 1-1.2% on total portfolio return before accounting for the PIK conversions that inflate reported income without generating cash. That sounds manageable in isolation, but it is additive to the income erosion from PIK (where the reported yield overstates actual cash generation), and the combination, real losses plus phantom income, is what compresses NAVs.

The cascading effect on management fees (typically 1-1.5% of NAV) is what makes this a fee revenue problem for the managers even before it becomes a solvency problem for the funds.

[![](https://substackcdn.com/image/fetch/$s_!pOLK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd04dbae-b3af-4a79-b66c-11136ad538eb_1405x775.png)](https://substackcdn.com/image/fetch/$s_!pOLK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd04dbae-b3af-4a79-b66c-11136ad538eb_1405x775.png)

## **Blue Owl: slow-motion liquidity crisis**

Before going further, I want to separate two stories that are being conflated in most coverage, because the conflation is analytically lazy even though it is narratively convenient. The first story is about AI disruption compressing software cash flows and threatening the credit quality of private loans to the sector. That story is market-wide and structural.

The second story is about Blue Owl’s specific governance problems, fund structure failures, and related-party transactions. That story is largely idiosyncratic. The two intersect (Blue Owl’s tech-heavy portfolio makes it disproportionately exposed to the first story), but they are separable, and treating Blue Owl as representative of all private credit is the same extrapolation error that people make every cycle. With that caveat stated clearly, here is the Blue Owl situation on its own terms.

Blue Owl Capital has become the poster child for everything that can go wrong in private credit simultaneously.

[![](https://substackcdn.com/image/fetch/$s_!xtTI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7d1ba8f-e12a-4263-9445-22b081a57a89_1405x776.png)](https://substackcdn.com/image/fetch/$s_!xtTI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7d1ba8f-e12a-4263-9445-22b081a57a89_1405x776.png)

The stock hit a **52-week low of $10.51 on February 20**, down from $23.98 a year earlier. Short interest has climbed to roughly 12.5-13% of float, up over 3 percentage points in 90 days. Here is the sequence of events:

**November 2025**: Blue Owl attempted to merge its non-traded BDC (OBDC II, $1.6 billion) with its publicly traded OBDC. The deal would have imposed a roughly **20% haircut** on OBDC II investors because OBDC traded at a 20% discount to NAV. Fierce investor backlash killed the merger on November 19. This was the first public signal that Blue Owl’s stated NAVs did not reflect reality.

**Late 2025**: Redemption requests surged. Blue Owl Technology Income Corp paid out roughly 15% of assets in the final months of 2025. Across Blue Owl’s tech-focused funds, redemption requests hit **over 15%** by early 2026, far exceeding the quarterly 5% cap.

**February 18-19, 2026**: Blue Owl announced two simultaneous moves. First,it sold $1.4 billion in loans across three funds to three North American pension funds (CalPERS, OMERS, and British Columbia Investment Management) and its own insurance affiliate, Kuvare, at 99.7 cents on the dollar. Second, it permanently ended quarterly redemptions at OBDC II, replacing the 5% tender-offer structure with mandatory “capital distributions.” Management plans to return approximately 30% of OBDC II’s NAV by late March.

**February 20:** Business Insider reported that Blue Owl failed to secure financing for a $4 billion data center project with CoreWeave (rated B+ junk by S&P). One specialty lender told reporters: “We saw it. We passed.” A $500 million bridge loan matures in March. Blue Owl denied the report. The same day, Saba Capital and Cox Capital Partners formally announced tender offers for shares in three Blue Owl BDCs at 20-35% discounts to NAV.

The CoreWeave failure deserves more attention than it has received, because it exposes a second, largely undiscussed risk vector in Blue Owl’s business.

Blue Owl has committed at least $50 billion in data center financing since last year: a $27 billion joint venture with Meta for the Hyperion buildout, a $15 billion AI joint venture with Crusoe for the Stargate project, $7 billion raised for a digital infrastructure fund, and $1.7 billion for a digital infrastructure REIT. This is not a peripheral business line. It is a massive, concentrated bet on AI infrastructure demand, financed through the same leveraged structures that characterise Blue Owl’s software lending.

The analytical distinction that matters here is between the software credit risk (where the collateral is evaporating because the borrowers’ business models are being disrupted) and the data center credit risk (where the collateral is physical infrastructure but the counterparties are often questionable credits themselves).

CoreWeave and Applied Digital are examples of the latter category: highly leveraged data center operators whose equity cushions will vaporise quickly if their businesses deteriorate. The fact that lenders are already balking at CoreWeave’s creditworthiness suggests the market is beginning to price this risk.

For Blue Owl, this means the software disruption story and the data center credit story are additive: the portfolio faces structural impairment on the software side and potential credit deterioration on the infrastructure side simultaneously. Most analysis has treated these as separate narratives. They are not. They are two expressions of the same underlying problem: concentrated lending to sectors whose risk profiles are changing faster than the marking and reporting cycle can capture.

[![](https://substackcdn.com/image/fetch/$s_!Xbq8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea045f13-7dea-490f-8fe4-2962967c1ad0_1405x793.png)](https://substackcdn.com/image/fetch/$s_!Xbq8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea045f13-7dea-490f-8fe4-2962967c1ad0_1405x793.png)

The $1.4 billion loan sale is the most debated transaction, and most of the debate is focused on the wrong question.

Blue Owl’s management argues the sale “validates” their marks. The near-par pricing is genuinely difficult for bears to dismiss: performing senior secured loans do not trade at 99.7 cents in a real credit crisis.

A senior direct lending professional I spoke with offered a more nuanced read: “The 99.7 price is almost certainly accurate for the specific loans sold. Senior secured performing loans to non-software companies in a diversified pool absolutely trade at or near par. Every direct lender I know would do the same thing under redemption pressure. It’s not evidence of fraud. It’s evidence of triage.”

[![](https://substackcdn.com/image/fetch/$s_!ubd4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff17c1698-8ab1-456e-a816-671d25c951a9_1405x782.png)](https://substackcdn.com/image/fetch/$s_!ubd4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff17c1698-8ab1-456e-a816-671d25c951a9_1405x782.png)

The sceptics, including the anonymous [The Credit Strategist](https://open.substack.com/users/7713300-the-credit-strategist?utm_source=mentions) commentary circulating on Substack, make three counterarguments that deserve engagement on their own terms.

First, one of the four buyers was Kuvare, whose asset management arm (Kuvare Asset Management) Blue Owl acquired for $750 million in 2024. Kuvare Holdings remains an independent insurer, but the asset management relationship creates an obvious conflict. Barclays analysts noted some loans may be repackaged into CLOs leveraged 9-10x. This looks like circular financing.

Second, the sold portfolio was 97% senior secured loans from 128 companies across 27 industries, almost certainly the highest-quality, most liquid assets in the book. Selling your best loans at par is not impressive; it’s cherry-picking.

Third, and this is the point that matters most: the loans left behind are not a random sample. They are what remains after the most marketable paper has been extracted.

[![](https://substackcdn.com/image/fetch/$s_!9pJJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0d2331c-22cc-48ce-ba08-450bfba6009d_1405x785.png)](https://substackcdn.com/image/fetch/$s_!9pJJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0d2331c-22cc-48ce-ba08-450bfba6009d_1405x785.png)

The analytical question the market should be asking is not “was 99.7 cents a fair price?” It almost certainly was, for those loans.

The question is: what does the composition of the residual portfolio look like? If Blue Owl sold its most diversified, most liquid, highest-quality senior secured paper, then the remaining book is by definition more concentrated, less liquid, more software-heavy, and likely carries a higher proportion of PIK-accruing credits. The effective software exposure of the residual portfolio may be materially higher than the 18-22% I cited earlier for the pre-sale book. That repriced residual composition is what Saba is pricing when it tenders at 65-80 cents on the dollar.

[![](https://substackcdn.com/image/fetch/$s_!dvoM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f52bf8c-12da-4b46-869b-37ac858aa3b1_1405x756.png)](https://substackcdn.com/image/fetch/$s_!dvoM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f52bf8c-12da-4b46-869b-37ac858aa3b1_1405x756.png)

## **The default rates everyone is quoting measure something different from what you think they measure**

The headline private credit default rate, the number managers cite on earnings calls, has remained below 2% for years.

This figure is not fabricated. It is, however, constructed using a definition of “default” so narrow that it excludes most of the ways a credit can deteriorate in practice.

Fitch’s Private Credit Default Rate hit **5.7% on a trailing twelve-month basis** through November 2025, the highest since early that year, with 13 default events in November alone (double the monthly average). Among companies with EBITDA below $25 million, the default rate was **12.9%**. Critically, 59% of defaults involved interest deferrals or introduction of payment-in-kind (PIK) instead of cash interest, the kind of “extend and pretend” that doesn’t show up in traditional default statistics.

[![](https://substackcdn.com/image/fetch/$s_!OEqG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6cd14f9-b6f6-45fc-bfce-a706831b7be2_1405x782.png)](https://substackcdn.com/image/fetch/$s_!OEqG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6cd14f9-b6f6-45fc-bfce-a706831b7be2_1405x782.png)

The Proskauer Private Credit Default Index rose sharply to **2.46% in Q4 2025** from 1.84% in Q3, with defaults among larger companies (EBITDA above $50 million) doubling in one quarter. Morningstar DBRS reported a trailing twelve-month borrower default rate of **4.0%**, up from 2.8% a year earlier. KBRA recorded a record 61 borrowers at CCC- assessment (worst rating), with downgrades outpacing upgrades for **seven consecutive quarters**. Nearly 30% of companies with debt maturing before year-end 2026 have leverage exceeding 10x or negative EBITDA.

[![](https://substackcdn.com/image/fetch/$s_!Qlwv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95f211f7-4fca-4f79-864f-58025480ec1a_1405x786.png)](https://substackcdn.com/image/fetch/$s_!Qlwv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95f211f7-4fca-4f79-864f-58025480ec1a_1405x786.png)

The gap between headline and true default rates exists because of liability management exercises (LMEs), PIK conversions, and stressed maturity extensions, mechanisms that prevent a technical “default” while the borrower’s credit quality deteriorates. Deutsche Bank forecasts the combined rate climbing to **4.8–5.5% in 2026**.

[![](https://substackcdn.com/image/fetch/$s_!tkLi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0e3103f-7ce4-4e3d-adcb-4e8f537a1b6a_1405x787.png)](https://substackcdn.com/image/fetch/$s_!tkLi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0e3103f-7ce4-4e3d-adcb-4e8f537a1b6a_1405x787.png)

Goldman Sachs estimates roughly 15% of private credit borrowers are no longer generating enough cash to fully service total interest obligations. It is worth pausing on what that actually means: these are borrowers whose cash EBITDA, after accounting for the EBITDA add-backs discussed above, does not cover total interest expense.

Some of these borrowers are servicing through PIK, which is by design in certain subordinated structures.

But in the senior secured first-lien loans that dominate BDC portfolios, PIK was not the original underwriting intent. When a first-lien borrower moves to partial PIK, it is a signal that the cash flow assumptions underpinning the original credit decision have deteriorated, even if the loan technically remains “performing.”

[![](https://substackcdn.com/image/fetch/$s_!yBEF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff961ba1e-8082-4c31-87f6-06d47a1091fb_1405x782.png)](https://substackcdn.com/image/fetch/$s_!yBEF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff961ba1e-8082-4c31-87f6-06d47a1091fb_1405x782.png)

Public BDCs now receive an estimated 8–9% of investment income via PIK (borrowers paying interest with more debt rather than cash), though the figure varies enormously by manager, from under 5% at some BDCs to over 24% at Monroe Capital.

The most instructive data point may be BDC market pricing. Blue Owl’s OBDC trades at a **25.5% discount to NAV**. FS KKR Capital trades at a **30–35% discount** and recently cut its base dividend by 29.7%. Even Ares Capital, the sector’s blue chip, trades at a **4.4% discount**, having slipped from its historical premium.

The BDC sector average discount is approximately 15%. BDC discounts reflect a package of factors: liquidity risk, management fee drag, market sentiment, and mark scepticism.

But when the average discount is 15% and the worst names trade at 25-35% below stated NAV, the market is telling you that some combination of stale marks and structural illiquidity makes stated NAV an unreliable measure of realisable value. The precise decomposition between “marks are wrong” and “the vehicle structure imposes a liquidity cost” is debatable. The direction is not.

[![](https://substackcdn.com/image/fetch/$s_!ndCv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd715284d-eb10-45bd-9e9f-a43087401dc6_1405x793.png)](https://substackcdn.com/image/fetch/$s_!ndCv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd715284d-eb10-45bd-9e9f-a43087401dc6_1405x793.png)

## **The FinTwit narrative is just getting started**

The private credit selloff has generated a powerful narrative ecosystem on financial social media, structured around one dominant frame: **is this 2007?**

Mohamed El-Erian set the terms of debate on the morning of February 19, posting on X that Blue Owl could be “a canary-in-the-coalmine moment, similar to August 2007”, referencing the Bear Stearns hedge fund failures that preceded the Global Financial Crisis. He added important caveats (”nowhere near the magnitude”), but the comparison stuck.

Dan Rasmussen of Verdad Capital, a long-standing critic who describes private credit as “high-interest-rate loans that banks wouldn’t touch”, told CNBC directly: “This is a canary in the coal mine. The private markets bubble is finally starting to burst.” The Kobeissi Letter posted viral threads framing the redemption halt as “A WARNING SIGN NOT SEEN SINCE THE GREAT FINANCIAL CRISIS.”

[![](https://substackcdn.com/image/fetch/$s_!IGEN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50a43a8d-34d3-4022-816d-e3674cd5d482_1405x786.png)](https://substackcdn.com/image/fetch/$s_!IGEN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50a43a8d-34d3-4022-816d-e3674cd5d482_1405x786.png)

On the podcast circuit, Jeffrey Gundlach’s recent Odd Lots appearance calling private credit “a powder keg” and semiliquid private-credit ETFs “the ultimate sin” has been widely recirculated. Dan Rasmussen’s January 29 episode on Excess Returns, titled “The Bubble You Can’t Exit”, covered private credit stress, bankruptcy signals, and the dangers of democratizing PE through 401(k)s. Bloomberg’s Odd Lots newsletter on February 20 covered the Blue Owl situation as “private credit escape hatch” with “circular financing” framing.

The Substack ecosystem is producing analytical depth that traditional media cannot match. [John Doe](https://open.substack.com/users/419773967-john-doe?utm_source=mentions) published a comprehensive multi-part series (”AI Bubble, Canary or Continuation: Blue Owl’s Ghosts of 2000/2008”) drawing explicit CDO parallels. [Larry Swedroe](https://open.substack.com/users/125058444-larry-swedroe?utm_source=mentions) ’s Substack amplified the contrarian Cliffwater research note arguing the panic is structural (failed BDC 2.0 model), not credit quality. The Expat Wealth at Work newsletter provided granular data showing average returns from the five largest private credit funds declining from **11.39% (2023) to 8.76% (2024) to 6.22% (first nine months of 2025)**, a trajectory that makes the redemption wave entirely rational.

The full ecosystem I’ve identified, as of February 22 2026, can be found at the end of this post.

The regulatory dimension sharpened as observers noted that Kuvare, a regulated insurance company, was among the buyers, raising questions about whether private credit risks are migrating into the regulated financial system. Senator Elizabeth Warren issued a statement calling the Blue Owl situation evidence of deeper problems in private credit, asking “Do I hear a cockroach?” and demanding federal stress tests on private credit exposures across the $1.7 trillion market.

[![](https://substackcdn.com/image/fetch/$s_!eR2d!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16b18d73-feaa-4e11-9f31-5b839d0832ed_1405x789.png)](https://substackcdn.com/image/fetch/$s_!eR2d!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16b18d73-feaa-4e11-9f31-5b839d0832ed_1405x789.png)

## **Why most coverage of this story is missing the point**

Most financial journalism operates on a binary: “crisis” or “nothing to see here.”

Private credit stress does not present as either. It presents as a slow accumulation of technical deteriorations, each individually insufficient to trigger a headline, but collectively sufficient to transform the risk profile of a $1.7 trillion market.

A PIK conversion does not look like a crisis. A covenant amendment does not look like a crisis. A maturity extension on a struggling software company does not look like a crisis.

Each one, in isolation, is a rational workout decision by a lender managing a troubled credit. But when 59% of defaults involve PIK conversions rather than outright failures, when headline default rates are 3-4x lower than independent tracking, when the DOJ is publicly warning about “creative marks,” these individual workout decisions aggregate into something the binary framing cannot capture: a systematic understatement of credit deterioration that is invisible in the data most investors rely on.

[![](https://substackcdn.com/image/fetch/$s_!NXQ9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbad57c57-7035-4140-b5f6-f801c3a2c808_1405x546.png)](https://substackcdn.com/image/fetch/$s_!NXQ9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbad57c57-7035-4140-b5f6-f801c3a2c808_1405x546.png)

This matters because of how private credit losses actually materialise. In public credit markets, stress is visible in real-time: bond prices move, CDS spreads widen, rating agencies downgrade.

The market’s assessment and the manager’s assessment converge quickly because both are looking at the same observable prices. In private credit, there are no observable prices. The manager marks the book. The auditor reviews the marks annually. The investor sees a NAV that is, at best, a quarterly snapshot of the manager’s own assessment, reported with a lag.

When the underlying credits deteriorate, the information flow to investors is delayed, filtered through the manager’s discretion, and presented in a format (NAV per share, net investment income yield) that is structurally designed to smooth volatility rather than reveal it.

[![](https://substackcdn.com/image/fetch/$s_!JXoS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb06b9db3-bf76-4241-99d1-959069c0d76a_1402x710.png)](https://substackcdn.com/image/fetch/$s_!JXoS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb06b9db3-bf76-4241-99d1-959069c0d76a_1402x710.png)

This is not a conspiracy. It is a feature of the asset class, and in normal environments it is a feature investors willingly accept because the smoothing reduces mark-to-market anxiety and the illiquidity premium compensates for the information disadvantage. The problem arises when a novel risk, one not captured in historical default models, arrives faster than the marking and reporting cycle can process it. AI disruption of software cash flows is that risk. The underlying economics of the borrowers are changing on a timeline measured in months, while the marks that determine NAVs (and therefore management fees, and therefore manager incentives) are updating on a timeline measured in quarters. The gap between reality and reported values is widening, and it will continue to widen until either the risk dissipates or the marks catch up.

[![](https://substackcdn.com/image/fetch/$s_!rofL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f6992dd-011b-456b-a6da-1e8c1ae8edc3_1402x789.png)](https://substackcdn.com/image/fetch/$s_!rofL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f6992dd-011b-456b-a6da-1e8c1ae8edc3_1402x789.png)

The lag is further extended by amendment and extension (A&E) activity, the single largest mechanism keeping headline default rates low and the one least discussed in public coverage. Before a loan technically defaults, the lender and borrower typically negotiate an amendment: covenant relief, maturity extension, sometimes additional PIK or fee income for the lender in exchange for forbearance.

These amendments do not count as defaults in any tracking methodology, including Fitch’s.

They are a third layer of hidden deterioration that sits beneath both manager-reported defaults and Fitch’s broader tracking. According to practitioners I have spoken with, A&E volume in private credit is currently at or near historic highs, which is consistent with a market where borrowers are under genuine cash flow pressure but lenders have every incentive to avoid recognising defaults that would force mark-downs.

[![](https://substackcdn.com/image/fetch/$s_!vTmW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a8bec3f-ce72-4ea5-863b-6e15485eec33_1402x789.png)](https://substackcdn.com/image/fetch/$s_!vTmW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a8bec3f-ce72-4ea5-863b-6e15485eec33_1402x789.png)

Understanding these layered lags, the quarterly reporting cycle, the covenant-lite structures that remove early warning triggers, and the A&E activity that prevents formal default recognition, is essential to interpreting everything that follows.

When I cite the Fitch gap (5.7% trailing default rate versus sub-2% manager-reported), when I discuss Blue Owl’s loan sale at 99.7 cents on the dollar, when I evaluate BDC discounts to NAV, the analytical question is always the same: what does the observable data tell us about the gap between reported values and actual credit quality, and which direction is that gap moving?

[![](https://substackcdn.com/image/fetch/$s_!DFFG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb80aa0f3-5268-4b9d-80d6-6093fb4a254c_1405x756.png)](https://substackcdn.com/image/fetch/$s_!DFFG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb80aa0f3-5268-4b9d-80d6-6093fb4a254c_1405x756.png)

[![](https://substackcdn.com/image/fetch/$s_!Lb7o!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5038c99d-7b64-4e18-b186-947938d6ac00_1402x789.png)](https://substackcdn.com/image/fetch/$s_!Lb7o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5038c99d-7b64-4e18-b186-947938d6ac00_1402x789.png)

The most granular work on these questions has come from independent research: The Endtropy’s multi-part CDO parallels series, Larry Swedroe’s amplification of the Cliffwater structural argument, the Credit Strategist commentary circulating on Substack. I will be drawing on and extending that work throughout this piece.

## **The contrarian case deserves serious consideration**

The bear narrative is compelling, but several data points cut the other way. Institutional investors, CalPERS, OMERS, British Columbia Investment Management, were the **buyers** of Blue Owl’s $1.4 billion in loans.

They are not naive. Bank of America announced a **$25 billion commitment** to private credit on the same day as the Blue Owl selloff, a signal that the largest bank in America sees value. Blackstone reported record $71 billion in Q4 inflows, and TPG raised a record $51 billion in 2025 fundraising. Apollo’s management disclosed they had already reduced software exposure over the prior two years and profited from shorts against First Brands and Tricolor debt.

[![](https://substackcdn.com/image/fetch/$s_!1R-X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff07e9718-7b1e-4061-8623-58205b5c0ed2_1402x446.png)](https://substackcdn.com/image/fetch/$s_!1R-X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff07e9718-7b1e-4061-8623-58205b5c0ed2_1402x446.png)

Before getting to the structural arguments, there is a data point that complicates the blanket disruption narrative in ways the bears have not adequately addressed. ICONIQ’s GenAI survey data (N=298 AI builders, Q4 2025) shows that nearly 70% of AI builders are focused on vertical applications, up from 51% in Q2 2025, not on foundational models. The differentiation battle is not happening at the model layer; it is happening at the application layer, where data, proprietary workflows, and deep integrations matter.

This is significant because it suggests the value in enterprise software is shifting up the stack to whoever owns the data and the workflows, and that is, in many cases, precisely the SaaS incumbents everyone is panic-selling. An AI model that can draft emails does not own the customer relationship data, the compliance audit trails, or the integration layers that a Salesforce implementation represents. The model layer is commoditising exactly as expected (DeepSeek R1 confirmed this), which means the locus of defensibility may actually be moving toward, not away from, entrenched enterprise software platforms.

I want to be careful not to overstate this. The ICONIQ data tells you where builders are focusing, not where disruption will land. But it introduces a meaningful qualification to the blanket disruption thesis. If the model layer commoditises (which DeepSeek confirmed) while the application layer remains defensible through data and workflow ownership, then the incumbents who move fastest to integrate AI into their existing platforms may actually strengthen their competitive positions rather than lose them.

The disruption thesis holds for companies that are pure workflow automation with no proprietary data advantage. It weakens considerably for platforms sitting on years of customer data, compliance audit trails, and integration layers that an AI-native entrant would need years to replicate. The distinction between these two categories is doing most of the analytical work in this piece, and the ICONIQ data suggests the market may be drawing the line in the wrong place for at least some of the names currently being sold indiscriminately.

[![](https://substackcdn.com/image/fetch/$s_!dBd-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ac4d570-7aeb-4530-8a94-a41004cd4f27_1405x789.png)](https://substackcdn.com/image/fetch/$s_!dBd-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ac4d570-7aeb-4530-8a94-a41004cd4f27_1405x789.png)

The Cliffwater research note makes the strongest structural argument for calm: OBDC II’s annualized return of **9.11%** essentially matched the industry benchmark (Cliffwater Direct Lending Index at 9.19%).

The problem was not the asset class but the BDC 2.0 fund structure, a model that has now been abandoned industry-wide in favor of perpetual vehicles. Blue Owl’s newer funds (OCIC, which raised nearly $20 billion over five years) use this updated structure. James Staunton at Berenberg argues the jump from software equity repricing to private credit defaults is “too large”, these are senior secured loans with loan-to-value ratios around **30%**, providing substantial equity cushion even if enterprise values decline.

[![](https://substackcdn.com/image/fetch/$s_!w8WT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5e3ceeb-703e-4f1d-a05e-51bccf19b313_1405x491.png)](https://substackcdn.com/image/fetch/$s_!w8WT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5e3ceeb-703e-4f1d-a05e-51bccf19b313_1405x491.png)

Analyst consensus remains surprisingly bullish: most aggregators show 12 Buy ratings and 3-5 Holds, though Zacks downgraded OWL to Strong Sell on January 27. The median price target sits around $16-$18.50 (implying 50-70% upside from $10.85). The disconnect between Wall Street’s published ratings and the market’s pricing could mean either that analysts are behind the curve, or that the selloff has created a genuinely compelling entry point for investors willing to underwrite the AI disruption risk.

[![](https://substackcdn.com/image/fetch/$s_!ji5k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1117457d-1e85-4967-a23a-93909cb1c03c_1405x674.png)](https://substackcdn.com/image/fetch/$s_!ji5k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1117457d-1e85-4967-a23a-93909cb1c03c_1405x674.png)

There is a stronger version of the bull case that deserves direct engagement, because it is the one most likely to be correct if the bears are wrong. The argument is simple: the market has compressed five years of AI disruption into five weeks of price action, and that compression is itself the mispricing.

Enterprise software replacement cycles are measured in years, not months. Procurement inertia, compliance requirements, integration complexity, vendor lock-in, and organisational switching costs are real frictions that AI agents reduce but do not eliminate. A Fortune 500 company is not ripping out its Salesforce implementation because Claude can draft emails. The disruption is directionally correct, but the market has priced the terminal state without discounting for the transition years. If that argument is right, the selloff is a classic overshoot and mean-reversion is the dominant trade.

[![](https://substackcdn.com/image/fetch/$s_!fpmT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ba93285-1a64-4ff2-b265-9975375973a5_1403x788.png)](https://substackcdn.com/image/fetch/$s_!fpmT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ba93285-1a64-4ff2-b265-9975375973a5_1403x788.png)

I take this seriously, and I want to be explicit about where I think the bulls are right and where I think they are wrong, because the distinction determines which credits survive and which do not.

The bulls are right that deeply embedded software (ERP, cybersecurity, mission-critical infrastructure) faces a multi-year disruption timeline. These systems have tentacles that reach into every corner of an organisation: compliance frameworks, audit trails, integration layers, vendor liability structures, and years of organisational muscle memory. An AI agent cannot replicate that overnight, and the enterprises running these systems are not going to rip them out on the basis of a product demo, no matter how impressive.

For private credit exposures to this category, the pace argument is a strong defence of the underwriting thesis.

[![](https://substackcdn.com/image/fetch/$s_!aT67!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0843341a-cbb8-4872-88c8-47ac3e1a4e01_1403x790.png)](https://substackcdn.com/image/fetch/$s_!aT67!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0843341a-cbb8-4872-88c8-47ac3e1a4e01_1403x790.png)

The bulls are wrong, in my view, about the vulnerable end of the spectrum: workflow automation, horizontal SaaS, basic legal and tax tools. These businesses do not require a full rip-and-replace to destroy the credit thesis.

They require only enough competitive pressure to compress margins and stall growth, and that can happen on a 12-18 month timeline. I have already laid out the arithmetic: a $500K licence becoming a $300K licence across enough renewals decelerates growth from 15% to 3%, and for a borrower carrying 6x leverage, that deceleration alone is the difference between a performing credit and a covenant breach.

[![](https://substackcdn.com/image/fetch/$s_!QiB0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67f3035b-b699-4700-9d3b-d0aca4a3e103_1403x336.png)](https://substackcdn.com/image/fetch/$s_!QiB0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67f3035b-b699-4700-9d3b-d0aca4a3e103_1403x336.png)

The question for each specific credit in a private lending portfolio is which end of that spectrum it sits on. My concern, which I have documented with BDC filing data above, is that the loan books are disproportionately weighted toward the vulnerable end, because those were the businesses that looked best on paper: asset-light, high-margin, predictable revenue, low capex. The portfolio composition reflects it.

[![](https://substackcdn.com/image/fetch/$s_!Ab9v!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9e1d030-e4f8-4e71-be6e-514895d2a362_1402x749.png)](https://substackcdn.com/image/fetch/$s_!Ab9v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9e1d030-e4f8-4e71-be6e-514895d2a362_1402x749.png)

## **Mapping the exposure: who is vulnerable and who is not**

Rather than a simple buy/sell list, I want to give you a framework for evaluating exposure across the private credit ecosystem, because the dispersion in outcomes here is going to be enormous.

The same macro event will produce winners and losers depending on three variables: portfolio composition (what percentage of the loan book sits in AI-vulnerable software categories), fund structure (whether the vehicle has liquidity gates, tender mechanisms, or perpetual structures), and management quality (whether the team anticipated AI disruption or is now scrambling to remark). I will walk through each tier with the specific data points I am watching.

[![](https://substackcdn.com/image/fetch/$s_!V6l9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a0f8bcf-f605-4a5f-8aba-443f5d222c24_1405x479.png)](https://substackcdn.com/image/fetch/$s_!V6l9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a0f8bcf-f605-4a5f-8aba-443f5d222c24_1405x479.png)

### Tier 1: Direct software credit exposure (most vulnerable)

These are the names where AI disruption hits the loan book directly. The key metric across this tier is the gap between stated NAV and market price, which tells you how much the market believes the marks are overstated.

Blue Owl (OWL) is the obvious case: concentrated technology lending (OBDC’s schedule of investments shows 18-22% in software and technology services, with additional exposure through adjacent categories), governance problems documented above, and a stock reflecting severe stress at a 25.5% discount to NAV. But the exposure extends beyond Blue Owl. FS KKR Capital (FSK) trades at a 30-35% discount to NAV and just cut its base dividend by 29.7%, the clearest signal a management team can send that it sees deterioration the headline numbers have not yet captured. Monroe Capital’s BDC carries PIK rates above 24%, the highest in the public BDC universe, meaning nearly a quarter of its reported investment income comes from borrowers paying interest with more debt rather than cash. Golub Capital BDC (GBDC) has meaningful software and technology services exposure in its middle-market book and its discount to NAV has widened from roughly 5% to 12% since January, a less dramatic move than Blue Owl’s but directionally the same signal.

[![](https://substackcdn.com/image/fetch/$s_!hS5W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42ae1184-410d-4db8-9808-9a7c733f1949_1405x786.png)](https://substackcdn.com/image/fetch/$s_!hS5W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42ae1184-410d-4db8-9808-9a7c733f1949_1405x786.png)

The question for investors holding these names is simple: do you trust the stated NAVs? The BDC sector average discount is approximately 15%. If that discount represents the market’s best estimate of mark-to-market overstatement, then the fee revenue being earned on these portfolios (typically 1-1.5% of stated NAV) is partially earned on phantom assets. That is a second-order risk that has not yet been reflected in consensus earnings estimates for the managers.

[![](https://substackcdn.com/image/fetch/$s_!BXJv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78e4421a-15e6-452a-9f8a-d364ee19da31_1402x789.png)](https://substackcdn.com/image/fetch/$s_!BXJv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78e4421a-15e6-452a-9f8a-d364ee19da31_1402x789.png)

### Tier 2: Diversified alternative asset managers (contagion discount, potentially mispriced)

This is where the opportunity may sit, if the stress remains contained. But “if” is doing a lot of work in that sentence, so let me lay out both the case for and the case against buying the contagion discount.

The case for: Ares Management (ARES) has the sector’s strongest credit reputation and its flagship ARCC trades at only a 4.4% discount to NAV, a gap so narrow relative to the 25-35% discounts at weaker BDCs that the market is effectively telling you Ares’s marks are trustworthy. Ares also has meaningful insurance, real estate, and infrastructure businesses that are uncorrelated with software disruption.

Apollo (APO) stands out as the manager that most clearly anticipated this dislocation. David Sambur, co-head of Apollo’s private equity practice, has stated publicly that software valuations need a “much-needed reset” and disclosed that Apollo has zero software exposure in its PE business and less than 2% across its entire platform.

Marc Rowan, Apollo’s CEO and co-founder, has stated the firm aims to cut its direct lending exposure to software by half, from roughly 20% at the start of 2026 to below 10% net exposure in its credit funds. More tellingly, Apollo has taken active bearish positions against specific software credits, betting against the loans of companies including Internet Brands, SonicWall, and Perforce on the basis of disruption risk and weak credit quality.

This is not a manager reacting to a selloff. This is a manager that repositioned its portfolio before the selloff, which is the single most credible signal available about where the smart institutional money believes the risk lies, suggesting a management team that anticipated this dislocation rather than being caught by it.

KKR’s private credit book is one component of a diversified platform spanning infrastructure, real estate, and private equity. Blackstone (BX) reported record inflows even during the selloff.

[![](https://substackcdn.com/image/fetch/$s_!FiLY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5a4b5e2-b119-4b46-b6c5-8008efb3bf91_1402x789.png)](https://substackcdn.com/image/fetch/$s_!FiLY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5a4b5e2-b119-4b46-b6c5-8008efb3bf91_1402x789.png)

The case against: the critical variable is whether the default cycle stays in software or broadens into the leveraged mid-market generally.

BCRED at $79 billion with rising redemption requests is the single most important data point in private credit right now, because if that vehicle gates, the “contagion discount” on diversified managers becomes a “legitimate discount” overnight.

More broadly, if rate cuts come slower than expected and the economy softens, the 6-7x leveraged buyouts that populate every private credit portfolio (not just the software ones) come under pressure too. At that point, the correlation between “software disruption risk” and “traditional credit cycle risk” spikes, and the diversification benefit these managers are priced for evaporates.

I am treating this as a moderate position because the two scenarios produce wildly different outcomes, and I do not have enough information to assign confident probabilities to either. If defaults stay contained in software (my base case, roughly 55-60% probability), these names re-rate 20-30% higher within twelve months. If the cycle broadens (35-40% probability), they have another 15-25% to fall.

[![](https://substackcdn.com/image/fetch/$s_!b8Ns!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb277ec97-2bc5-4f0e-be4e-2f3bdfe7787d_1403x445.png)](https://substackcdn.com/image/fetch/$s_!b8Ns!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb277ec97-2bc5-4f0e-be4e-2f3bdfe7787d_1403x445.png)

### Tier 3: The other side of the trade

If AI genuinely disrupts enterprise software, the disrupted revenue does not disappear. It migrates. Every dollar that a corporation stops paying to a legacy SaaS vendor gets reallocated: to AI-native tools, to the infrastructure those tools run on, or back to the bottom line as productivity gains. The hyperscalers (Microsoft, Google, Amazon) are the obvious beneficiaries, but they are already priced for AI dominance and carry their own capex risk if the infrastructure buildout overshoots demand.

The more interesting question is who provides the picks and shovels for an AI-native enterprise stack. I will name three categories rather than three tickers, because this deserves its own dedicated analysis: enterprise AI deployment platforms (companies that help organisations actually implement and manage AI agents at scale), observability and security tooling for AI workflows (because autonomous agents create novel monitoring and compliance requirements), and edge inference infrastructure (because latency-sensitive enterprise applications will not all run in centralised cloud). If you want specific names, they are coming in a follow-up piece for paid subscribers.

The point for now is that the “AI disrupts SaaS” thesis has a long side, and most commentary is ignoring it entirely.

[![](https://substackcdn.com/image/fetch/$s_!3pEp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9fd242c-73b0-4e48-8fb8-d60761fd59d3_1402x785.png)](https://substackcdn.com/image/fetch/$s_!3pEp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9fd242c-73b0-4e48-8fb8-d60761fd59d3_1402x785.png)

On the short side, two separate trades deserve attention. The direct short on publicly traded software names most exposed to agent-based disruption (Salesforce down 25%, Intuit down 32%, Thomson Reuters down 30% year-to-date) has largely played out.

Remaining downside from here requires a view that the market has still not fully priced the disruption timeline, and after a 25-35% drawdown, the risk/reward on incremental shorts is poor unless you have a specific catalyst in mind (upcoming earnings, contract renewal data, further AI product launches).

[![](https://substackcdn.com/image/fetch/$s_!XQZF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77de96d0-98de-4491-902b-49443cac3570_1403x787.png)](https://substackcdn.com/image/fetch/$s_!XQZF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77de96d0-98de-4491-902b-49443cac3570_1403x787.png)

The second-derivative short is more interesting and, I believe, still mispriced. Private credit managers earn fees (typically 1-1.5% of NAV plus 15-20% incentive fees above a hurdle rate) on stated portfolio values.

If BDC market pricing is correct that stated NAVs are 15-25% overstated, then fee revenue is partially earned on phantom assets. When those marks come down (and they will, because auditors must eventually reconcile marks with observable market prices and realised defaults), management fee revenue compresses mechanically. That compression has not yet been reflected in consensus earnings estimates for any of the publicly traded alternative asset managers. For Blue Owl specifically, where management fees represent the overwhelming majority of revenue, a 15-20% NAV writedown on the technology-exposed portion of the portfolio flows almost directly to the bottom line.

### Tier 4: Hedges for passive exposure

Many investors have private credit exposure without knowing it, through pension funds, insurance products, target-date retirement funds, and increasingly through 401(k) allocations that include alternative sleeves. If you cannot easily assess or reduce that exposure, the simplest hedge is the BIZD ETF (VanEck BDC Income ETF), which is the most liquid publicly traded proxy for private credit.

March 2026 puts on BIZD are relatively inexpensive given the implied volatility in individual BDC names, suggesting the market is pricing idiosyncratic Blue Owl risk rather than broad sector risk. If you believe (as I do) that the stress will spread beyond Blue Owl before it resolves, that is a mispricing.

[![](https://substackcdn.com/image/fetch/$s_!_rJK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5af4b5a4-51ee-4180-a6f5-a203e3f00c9f_1402x645.png)](https://substackcdn.com/image/fetch/$s_!_rJK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5af4b5a4-51ee-4180-a6f5-a203e3f00c9f_1402x645.png)

A final note on sizing and conviction. I am treating the diversified alt manager opportunity (Tier 2) as a moderate position, not a high-conviction trade, because my own analysis contains a tension I have already flagged: if defaults genuinely hit 5-7% across the private credit market, even the diversified managers take meaningful earnings hits. The hedge (Tier 4) I am more convicted on, because the asymmetry is favorable: if I am wrong and the stress is contained to Blue Owl, the puts expire worthless and the cost is modest; if I am right and BCRED or another large vehicle faces redemption pressure, the payoff is substantial. I will publish detailed position sizing and entry levels for subscribers in the follow-up pieces.

[![](https://substackcdn.com/image/fetch/$s_!GyfB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b4d5abb-ab99-40ae-99c9-1a9e69a66a8b_1402x789.png)](https://substackcdn.com/image/fetch/$s_!GyfB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b4d5abb-ab99-40ae-99c9-1a9e69a66a8b_1402x789.png)

## **What I am actually doing with this information**

The framework above tells you how to evaluate the exposure. Here is where I personally sit.

Here is my honest answer, and it is more nuanced than a single ticker.

**The obvious short (which means it is probably too late):** Blue Owl at $10.85 with 12.5% short interest and a management team selling its best assets to its own insurance subsidiary. The bear case writes itself. But 12.5% short interest means the trade is crowded, the borrow is expensive, and the stock is already down 54% from its high. Shorting something that has already halved requires either a catalyst for further decline or a thesis that fair value is materially below $10. If you believe the residual portfolio (after the $1.4 billion cherry-picked loan sale) is worth 60-70 cents on the dollar, the math works. If you think the marks are roughly fair and this is a liquidity event rather than a solvency event, you are shorting a stock that Wall Street has at $16-18.50.

[![](https://substackcdn.com/image/fetch/$s_!9sZ8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1c5bad5-e5aa-4b83-a642-d4feb407784f_1405x786.png)](https://substackcdn.com/image/fetch/$s_!9sZ8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1c5bad5-e5aa-4b83-a642-d4feb407784f_1405x786.png)

My view: the marks are not fair, but 12.5% short interest with an expensive borrow means you are paying a significant carry cost to hold a position in a stock that has already priced in substantial distress. The asymmetry favours the short at $15-16, not at $10.85. I would not initiate here.

The more interesting trade sits in Tier 2 of the framework above: the diversified alternative asset managers trading at contagion discounts. I have already laid out the logic and the risks, so I will not repeat myself. The short version: I find the risk-reward compelling at current levels, but I am sizing it as a moderate position, not a high-conviction one, because the tension between “contained stress” and “broadening default cycle” is real and unresolved.

**The contrarian long (for those with stomach lining):** Blue Owl at 5x earnings with 50-70% implied upside to analyst targets, buying at the point of maximum narrative pessimism. The Saba tender offers at 65-80 cents establish a floor. The pension funds buying the $1.4 billion loan portfolio are not stupid.

If the AI disruption thesis is overblown, or if it takes three years to play out rather than three months, this stock re-rates violently. I am not taking this trade, because I think the AI disruption timeline is faster than the market appreciates. But I respect the logic, and I want to be honest that the bull case has real teeth.

**The macro hedge:** If you have broad exposure to alternative asset managers or private credit through your portfolio (and many people do without realizing it, through pension allocations and insurance products), the simplest hedge is reducing that exposure or buying puts on BDC ETFs. The BIZD (VanEck BDC Income ETF) is the most liquid proxy.

I will be writing dedicated deep-dives on the individual names over the coming weeks. If you are not a paid subscriber, now would be the time.

[![](https://substackcdn.com/image/fetch/$s_!Dyq-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F834c4b4d-fbe2-4b0d-9276-9d61579fdb24_1405x786.png)](https://substackcdn.com/image/fetch/$s_!Dyq-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F834c4b4d-fbe2-4b0d-9276-9d61579fdb24_1405x786.png)

## **So is this 2007?**

No. The comparison is seductive, the engagement incentive to amplify it is enormous, and the analytical case for it is weak. Here is why.

The analogy fails on scale (subprime involved synthetic leverage creating trillions in notional exposure wired into the banking system; private credit at $1.7 trillion is mostly held by institutional investors in locked-up vehicles), on transmission mechanism (in 2007 the risk sat inside bank balance sheets and the interbank lending market; today it sits with pension funds, insurance companies, and endowments that cannot trigger a bank run, only redemption queues and fund gates), and on monetary policy (Bernanke was hiking at 5.25%; today the Fed has room to cut).

Blue Owl gating OBDC II is a problem for Blue Owl’s investors. Bear Stearns’ hedge funds failing was a problem for everyone with a mortgage.

These are not comparable events.

[![](https://substackcdn.com/image/fetch/$s_!4BAx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2d2f32e-6ee2-4401-a032-c5d00d95d278_1402x738.png)](https://substackcdn.com/image/fetch/$s_!4BAx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2d2f32e-6ee2-4401-a032-c5d00d95d278_1402x738.png)

Here is what this *actually* is: the first real-world stress test of the private credit model under a novel risk scenario that historical default models cannot capture. AI disruption of software cash flows was not in anyone’s underwriting assumptions.

The marks are stale, the default rates are understated, and the structural liquidity mismatch (illiquid multi-year loans inside semi-liquid wrappers marketed to retail investors) is a genuine vulnerability.

Blue Owl was the weakest link. Blackstone’s BCRED at $79 billion with $2.1 billion in quarterly redemption requests is the next one to watch. If that vehicle gates, the “canary in the coal mine” framing becomes consensus overnight.

[![](https://substackcdn.com/image/fetch/$s_!_mcb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb905a1c1-8aa5-4b79-9c1f-fe4ba6caefc3_1405x692.png)](https://substackcdn.com/image/fetch/$s_!_mcb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb905a1c1-8aa5-4b79-9c1f-fe4ba6caefc3_1405x692.png)

But “canary in the coal mine” and “this is the next Global Financial Crisis” are wildly different claims. The former is plausible and supported by the data. The latter requires a transmission mechanism to the banking system that, as of today, does not exist.

The canary is singing. The question is whether anyone is listening carefully enough to hear what it is actually saying, rather than what they want it to say.

If you enjoyed this post, consider supporting our work by becoming a paid subscriber.

Subscribed

---

*This article is for informational and educational purposes only and should not be construed as investment advice. The authors may hold positions in securities mentioned. All views expressed are our own. Do your own due diligence before making any investment decisions.*

## Ecosystem

[![](https://substackcdn.com/image/fetch/$s_!CcRa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19ef3326-c1d4-492f-8e43-c7439963bdcb_1405x717.png)](https://substackcdn.com/image/fetch/$s_!CcRa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19ef3326-c1d4-492f-8e43-c7439963bdcb_1405x717.png)

[![](https://substackcdn.com/image/fetch/$s_!US5O!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4c47291-0090-43a7-95e9-f1b1db2840e0_1405x552.png)](https://substackcdn.com/image/fetch/$s_!US5O!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4c47291-0090-43a7-95e9-f1b1db2840e0_1405x552.png)

[![](https://substackcdn.com/image/fetch/$s_!rqvG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c9c7ed-700a-40f4-8da0-bc3934bd3dd8_1405x542.png)](https://substackcdn.com/image/fetch/$s_!rqvG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c9c7ed-700a-40f4-8da0-bc3934bd3dd8_1405x542.png)

[![](https://substackcdn.com/image/fetch/$s_!MB74!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bdd0913-a973-4db3-89f3-51cd61b890e1_1405x513.png)](https://substackcdn.com/image/fetch/$s_!MB74!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bdd0913-a973-4db3-89f3-51cd61b890e1_1405x513.png)

[![](https://substackcdn.com/image/fetch/$s_!8_Zu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e216623-70de-4a35-9e77-a7b84f6ecc45_1405x792.png)](https://substackcdn.com/image/fetch/$s_!8_Zu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e216623-70de-4a35-9e77-a7b84f6ecc45_1405x792.png)

[![](https://substackcdn.com/image/fetch/$s_!eJ1e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc31fdefd-c484-4946-82dd-ccca322e710d_1405x525.png)](https://substackcdn.com/image/fetch/$s_!eJ1e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc31fdefd-c484-4946-82dd-ccca322e710d_1405x525.png)

[![](https://substackcdn.com/image/fetch/$s_!FUvl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b830e45-2fca-41dc-974d-2ed9afec0be3_1405x684.png)](https://substackcdn.com/image/fetch/$s_!FUvl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b830e45-2fca-41dc-974d-2ed9afec0be3_1405x684.png)

[![](https://substackcdn.com/image/fetch/$s_!w4Mp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F766a4283-b130-44fe-9740-1ea37295fb11_1405x491.png)](https://substackcdn.com/image/fetch/$s_!w4Mp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F766a4283-b130-44fe-9740-1ea37295fb11_1405x491.png)

[![](https://substackcdn.com/image/fetch/$s_!OCEW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89bf7d5b-cefd-4f31-9941-459e11b472cc_1405x421.png)](https://substackcdn.com/image/fetch/$s_!OCEW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89bf7d5b-cefd-4f31-9941-459e11b472cc_1405x421.png)

[![](https://substackcdn.com/image/fetch/$s_!bslR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9dd3bb1d-b427-4005-8b29-6f2bbff930d9_1405x421.png)](https://substackcdn.com/image/fetch/$s_!bslR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9dd3bb1d-b427-4005-8b29-6f2bbff930d9_1405x421.png)

[![](https://substackcdn.com/image/fetch/$s_!QbYc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9417cd85-023c-494f-b118-a9b984769d3b_1405x417.png)](https://substackcdn.com/image/fetch/$s_!QbYc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9417cd85-023c-494f-b118-a9b984769d3b_1405x417.png)

[![](https://substackcdn.com/image/fetch/$s_!zOQk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbac65b6-8870-44c8-8d9d-54e96fd2fdd5_1405x333.png)](https://substackcdn.com/image/fetch/$s_!zOQk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbac65b6-8870-44c8-8d9d-54e96fd2fdd5_1405x333.png)

[![](https://substackcdn.com/image/fetch/$s_!5Nv8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1044271-a819-4875-aee9-7520a6634cad_1405x477.png)](https://substackcdn.com/image/fetch/$s_!5Nv8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1044271-a819-4875-aee9-7520a6634cad_1405x477.png)