The most important satisfies semiconductor manufacturers for advanced chip fabrication is not silicon. It is not copper, cobalt, palladium, or ultra-pure quartz. It is a noble gas that forms underground over geological timescales, escapes permanently into space the moment it is vented, has no synthetic substitute, no futures market, no transparent pricing mechanism, and no way to ramp production in under seven years.

In October 2025, it quietly surpassed MRI machines as the world’s largest end use. Nobody outside the specialty gas industry noticed.

Five months later, Iranian drones shut down the facility that produces a third of global supply.

You have read the panic version of this story. Sherwood ran it. CNBC ran it. Tom’s Hardware ran it. Helium gone, chips disrupted, AI buildout at risk. We are not writing that piece. Not because the disruption is fake, it is real, but because the panic narrative is built on a number that is almost certainly wrong, and the number that replaces it cuts in a direction nobody is discussing.

Here is what we mean. The headline says semiconductors consume 21 to 24% of global helium. That figure is accurate. It is also gross throughput before recycling, and quoting it as net demand is like measuring an oil refinery’s crude intake and calling it consumption without accounting for the fact that most of it comes out the other end as product. Modern advanced fabs recapture 80 to 95% of the helium they use. The semiconductor industry’s actual fresh helium requirement may be closer to 2 to 5% of the global market.

The entire crisis narrative might be anchored to the wrong number.

[![](https://substackcdn.com/image/fetch/$s_!PqbZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e970e4b-07b6-402d-a5cb-642646fc260e_2328x1203.png)](https://substackcdn.com/image/fetch/$s_!PqbZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e970e4b-07b6-402d-a5cb-642646fc260e_2328x1203.png)

But before the bulls exhale: the right number is still scary enough. South Korea sources 64.7% of its helium imports from Qatar and fabricates roughly two-thirds of the world’s memory chips. The memory market entered this crisis with DRAM prices up 240% year over year, finished inventory at three weeks against a four-week floor, and SK Hynix having presold its entire 2026 output. There is no slack. There is no quiet quarter where this lands softly. And the recycling rate that determines whether this is a manageable inconvenience or a binding production constraint is, to be direct, a number nobody can actually measure.

We built the full transmission model: fab-level helium consumption by process step, the nonlinear yield degradation curve that makes conservation self-defeating past a threshold nobody publishes, the distributor allocation mechanics that determine which fabs produce chips and which ones don’t, the China variable that turns a commodity shortage into a geopolitical allocation crisis, and the natural hedge between energy costs and helium scarcity that almost nobody is modelling.

Our base case: a three-to-five month disruption producing meaningful spot price increases and allocation tightening but not binding production constraints at major Korean fabs. Probability: roughly 50%. Tail risk, six months or longer, forcing allocation triage on top of the steepest memory supercycle in the modern era: roughly 25%. Benign resolution within weeks: roughly 25%.

We think the most probable outcome is that the semiconductor industry navigates this with manageable pain and the narrative overshoots reality.

We could be wrong. Below, we show you exactly how to know if we are.

[Share](https://tscsw.substack.com/p/partys-over?utm_source=substack&utm_medium=email&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNDAwMjQ1LCJwb3N0X2lkIjoxOTA4NTk0ODYsImlhdCI6MTc3NDIyNjI1MiwiZXhwIjoxNzc2ODE4MjUyLCJpc3MiOiJwdWItMjM1NDI0NCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.cEzQhJPd-REbcIhCkrFkXcoCImFEavpJEv5V_5LNiCs)

### Why you should be reading TSCS

Everything above is free because you can find some version of it elsewhere.

What follows, the recycling arithmetic that collapses the headline narrative, the nonlinear yield curve nobody is modelling, and the five indicators that will tell you whether this is a footnote or a structural repricing, you cannot.

That is what a TSCS subscription gets you.

Subscribed

Let’s get into it.

## What helium is and why it cannot be ramped

Helium is non-renewable, non-substitutable, and non-rampable. It forms underground over geological timescales, is lost permanently to space the moment it is vented, and can only be recovered economically from natural gas fields where concentrations exceed roughly 0.3% by volume. Fourteen major production facilities worldwide. New capacity takes seven to ten years for greenfield, three to five for brownfield. The USGS projects capacity flat through 2029. Unlike the neon scare of 2022, where air-separated alternatives scaled within months, helium has no manufacturing substitute.

Demand is heading the other way. Overall helium demand grows at roughly 2.5-3.5% annually, but semiconductor-specific demand is growing twice that fast: TechCET documented a 14.6% surge in 2025, with a forward CAGR of 6.3%.

[![](https://substackcdn.com/image/fetch/$s_!hiLj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58095cab-a999-4c41-86ce-c77109a91ca5_1600x880.png)](https://substackcdn.com/image/fetch/$s_!hiLj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58095cab-a999-4c41-86ce-c77109a91ca5_1600x880.png)

IDTechEx projects five-fold growth in semiconductor helium consumption by 2035. Each new fab generation is more helium-intensive than the last: more EUV layers, more deposition steps, more vacuum processes per wafer.

[![](https://substackcdn.com/image/fetch/$s_!Lrgv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ca92fe9-5a75-4e9e-b044-a818af1a75c8_1600x892.png)](https://substackcdn.com/image/fetch/$s_!Lrgv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ca92fe9-5a75-4e9e-b044-a818af1a75c8_1600x892.png)

Annual global demand runs approximately 6 billion cubic feet (BCF) per year. We’ll use BCF throughout. Semiconductors claim roughly 21-24% (about 1.3-1.4 BCF), having surpassed MRI as the single largest end use in October 2025 per TechCET. MRI and cryogenics take roughly 20%, aerospace 13%, welding and leak detection 15%, the rest dispersed.

[![](https://substackcdn.com/image/fetch/$s_!vTBO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1aaf6ba2-573f-40b5-bfa2-005f800cee63_1600x897.png)](https://substackcdn.com/image/fetch/$s_!vTBO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1aaf6ba2-573f-40b5-bfa2-005f800cee63_1600x897.png)

One structural feature shapes everything downstream: **there is no futures market, no exchange, and no transparent price discovery**. Helium trades bilaterally under long-term contracts, with spot handled over the phone between a handful of distributors and their customers. When you read that helium spot prices doubled, that figure comes from consultant estimates, not a ticker. No CME contract. No mechanism for the market to signal scarcity in real time.

[![](https://substackcdn.com/image/fetch/$s_!8H6q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4e94a4a-230e-49b6-aa0f-f696353a948c_1600x898.png)](https://substackcdn.com/image/fetch/$s_!8H6q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4e94a4a-230e-49b6-aa0f-f696353a948c_1600x898.png)

By the time a shortage becomes visible in public reporting, it has been transmitting through private allocation notices for weeks.

**The supply architecture and why a 21-mile strait controls your MRI scan**

Global helium production capacity entering 2026 was approximately 8 to 8.5 BCF per year against 6 BCF of demand, implying roughly 2 to 2.5 BCF of notional surplus. But capacity surplus and actual production surplus are different numbers.

Garvey of Intelligas quantified actual 2025 production at roughly 6.5 BCF against 6.0 BCF of demand, meaning the market entered the crisis with approximately 0.5 BCF of actual surplus, about 8% above consumption.

[![](https://substackcdn.com/image/fetch/$s_!F6EV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F777cb9c9-355a-4a15-89fc-28070edd4769_1600x891.png)](https://substackcdn.com/image/fetch/$s_!F6EV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F777cb9c9-355a-4a15-89fc-28070edd4769_1600x891.png)

That excess was being absorbed into dedicated storage facilities, including a new one that changes the buffer calculus meaningfully.

The mood in October 2025 was comfortable oversupply. Kornbluth noted spot prices well below contract levels. Gazprom delayed Amur’s second helium plant to H1 2026 because the market didn’t need more supply. Garvey wrote that “worldwide supply will continue to be in surplus if the large new sources of helium continue to come onstream as planned.” That “if” is doing a lot of work in retrospect. Five months later, the single largest planned source went offline because a military strike shut down the entire industrial complex it depends on.

In July 2025, Linde commissioned the world’s largest helium storage cavern at the Spindletop salt dome in Jefferson County, Texas, one of only four helium salt caverns on Earth. Total capacity: over 3 BCF. After deducting the roughly 30% cushion gas that salt caverns require, working gas is approximately 2.1 BCF, covering roughly 16-19 months of global semiconductor helium demand at current consumption rates.

Linde, which controls 24.5% of global helium distribution, now sits on a strategic buffer that did not exist during any prior shortage. The fact that most crisis commentary hasn’t registered it tells you how shallow the panic analysis has been.

Caveats: Beaumont serves all end uses, not just semiconductors. Linde’s allocation decisions determine who draws from this buffer and when. Storage is compressed gas, not liquid, so delivery still requires liquefaction and transport. And the actual volume in the cavern may be substantially less than 2.1 BCF working capacity if it hadn’t been fully charged before the crisis.

[![](https://substackcdn.com/image/fetch/$s_!20Rv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2202d7f6-713d-4e15-96f3-0f258d7177db_1600x903.png)](https://substackcdn.com/image/fetch/$s_!20Rv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2202d7f6-713d-4e15-96f3-0f258d7177db_1600x903.png)

Other storage assets include Air Products at a separate Beaumont facility, Air Liquide at Gronau-Epe in Germany, and the Messer Cliffside facility (the former Federal Helium Reserve, acquired by Messer in January 2024), which reinjects surplus crude helium into the field.

Qatar’s capacity alone is approximately 2.6 BCF. Removing it wipes out the 0.5 BCF production surplus and then some, pushing remaining output of roughly 5.5-6 BCF against 6 BCF of demand. But 6 BCF is not a fixed number. In every prior helium shortage, lower-priority demand compressed. Welding shops switch to alternative shielding gases. Research labs defer cryogenic experiments. Non-critical leak detection shifts to hydrogen forming gas. In Shortage 3.0, non-essential demand probably fell 10-15%, freeing roughly 600-900 MCF for priority consumers. If the same happens now, effective demand drops to perhaps 5.1-5.4 BCF against remaining capacity of 5.5-6 BCF. Not comfortable. Not catastrophic. The margin for error is thin but it exists.

[![](https://substackcdn.com/image/fetch/$s_!ta4g!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65493cb6-800a-4036-b98e-e13ae7c96bfa_1600x890.png)](https://substackcdn.com/image/fetch/$s_!ta4g!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65493cb6-800a-4036-b98e-e13ae7c96bfa_1600x890.png)

One nuance the top-line numbers obscure: **not all helium is interchangeable.** Semiconductor fabs require Grade 5.0 or higher (99.999%+ pure). Welding uses Grade 4.7. The remaining 5.5-6 BCF of capacity includes all grades. The capacity to produce and deliver semiconductor-grade helium is a subset, concentrated at specific purification facilities. A market where bulk helium is technically available for pressurization can simultaneously be short of the ultra-pure product Samsung needs for backside wafer cooling.

Most coverage of this crisis ignores the grade distinction entirely, which is like analyzing an oil shortage without distinguishing between crude and jet fuel.

Three countries account for roughly 85% of production.

[![](https://substackcdn.com/image/fetch/$s_!KGEA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff54dd588-3c2f-4611-856d-e8bee6aac4f5_1600x899.png)](https://substackcdn.com/image/fetch/$s_!KGEA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff54dd588-3c2f-4611-856d-e8bee6aac4f5_1600x899.png)

The **United States** produces approximately 4.6 to 5.5 BCF annually, but two-thirds is consumed domestically, limiting exportable surplus to roughly 1.5-1.8 BCF. Even flat out, U.S. plants cannot cover the full Qatar gap without starving domestic consumers. The Federal Helium Reserve, maintained for nearly a century, was sold to Messer in 2024 and now operates as a commercial facility. File under decisions that seemed fine at the time.

**Qatar** is the world’s largest exporter. Three plants at Ras Laffan, roughly 2.6 BCF per year, approximately 33-38% of global supply. The vulnerability is structural: Qatar’s helium is entirely a byproduct of LNG liquefaction, physically integrated with LNG processing trains. When LNG stops, helium stops.

There is no independent helium operation. And Qatar’s Helium 4 plant, the next major source of new global capacity due in 2027, was being built at Ras Laffan. The conflict has not just taken existing supply offline. It has probably delayed the single largest planned expansion by years.

The coupling creates an implication most helium commentary misses: helium restarts on LNG’s schedule, not its own. Helium revenue is perhaps $500 million to $1 billion against Qatar’s $50+ billion in annual LNG income. QatarEnergy’s restart calculus does not involve a single meeting about helium pricing.

Whatever timeline applies to LNG applies to helium, plus incremental time for purification train restart.

So here’s a practical tool. Take your Hormuz view.

Add roughly one month for LNG train restart (re-cooling, equipment inspection, gas requalification). Add two to three months for helium logistics normalization (container repositioning, distributor reallocation, pipeline refilling). That’s your helium timeline. If you think Hormuz reopens in four weeks, helium normalizes in roughly four months. If three months, six to eight. Don’t let helium-specific analysis convince you of a timeline that contradicts your Hormuz view. One caveat: this coupling is tighter on the way down than on the way back up. If Beaumont holds meaningful working gas, if Amur ramps faster than historical trend, or if demand destruction runs deeper than our 10-15% estimate, helium could normalize faster than LNG restarts imply. The framework gives you the outside bound, not a point estimate.

[![](https://substackcdn.com/image/fetch/$s_!Pi9E!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0080d791-4a10-48fc-ac06-97661968a3c4_1600x896.png)](https://substackcdn.com/image/fetch/$s_!Pi9E!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0080d791-4a10-48fc-ac06-97661968a3c4_1600x896.png)

**Russia’s** Gazprom Amur plant has nameplate capacity of roughly 2 BCF per year across three helium production lines. Two lines were operational by end-2023; Kornbluth reported at the October 2025 Helium Super Summit that Russia had surpassed Algeria as the world’s third-largest producer, expected to supply roughly 13% of global helium in 2025. The third line startup was delayed to H1 2026 because the market was oversupplied.

EU sanctions ban Russian helium in Europe, but established routes now serve China, South Korea, Japan, India, Indonesia, and the Middle East. South Korea is already receiving Amur helium. This partially offsets the Qatar loss, and the disruption bull case tends to understate this mitigant. But even at full nameplate, Amur’s 2 BCF cannot replace Qatar’s 2.6 BCF while simultaneously serving Chinese demand.

How much offset Amur actually provides depends on its ramp rate (Gazprom’s helium timelines make Elon’s Mars timelines look conservative) and on how aggressively China bids for the same molecules.

Emerging producers (Saskatchewan, Renergen in South Africa, Algeria) collectively add low single-digit percentages of global supply near-term. They matter to the long-term structural picture. They cannot fill a 2.6 BCF shortfall in 2026.

**The logistics.** Helium ships in cryogenic ISO containers at -268.9°C, boiling off 0.5-1% per day. Normal Qatar-to-customer transit is roughly three weeks. If the outage extends beyond two weeks, distributors begin relocating equipment and revalidating supplier relationships. During Shortage 3.0, the majors redirected containers from Qatari to U.S. routes within four to six weeks, but the process still requires weeks even for the best-resourced players.

One additional buffer: Qatar had been building helium inventory before the crisis. Filled containers were staged at Ras Laffan and at ports. Some were reportedly en route or outside the strait when it closed. If any reached customers, that’s additional weeks of supply not captured in fab-level inventory estimates.

**The distribution oligopoly.** This is the structural detail that ties the supply architecture to the semiconductor impact, and it’s where most analysis stops too early. Linde, Air Liquide, Air Products, and Iwatani collectively control the vast majority of helium distribution. Most volume moves under long-term contracts (3-10 years, take-or-pay). Genuine spot accounts for perhaps 5-8% of volume, and it actually shrinks during shortage because distributors fulfill contractual obligations first. The headline spot spike affects a thin tail.

[![](https://substackcdn.com/image/fetch/$s_!kjgl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F263e577e-97a4-4915-80a7-7e4be742d42e_1600x884.png)](https://substackcdn.com/image/fetch/$s_!kjgl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F263e577e-97a4-4915-80a7-7e4be742d42e_1600x884.png)

The real pain transmits through allocation percentages: distributors on force majeure tell contracted customers they’ll receive 70% or 80% of normal volumes, with MRI (roughly 50,000 installed scanners, each requiring 1,500-2,000 liters) and aerospace at 100%, and lower-priority uses cut deeper. The installed base cannot switch to helium-free alternatives quickly; those volumes are locked in.

These four companies are not just pricing beneficiaries. They are an unelected allocation committee that decides which fabs produce chips and which ones don’t. Their allocation decisions are the actual transmission mechanism between Ras Laffan going dark and a Samsung fab in Pyeongtaek slowing down.

[![](https://substackcdn.com/image/fetch/$s_!FW0y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde94a67b-d780-4650-8519-d78794f2bb2d_1886x770.png)](https://substackcdn.com/image/fetch/$s_!FW0y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde94a67b-d780-4650-8519-d78794f2bb2d_1886x770.png)

## **What happened and how fast it moved**

Iranian drones hit Ras Laffan on March 2. QatarEnergy ceased all LNG and associated production. Force majeure declared March 4, all three helium plants offline. CEO Al-Kaabi told the Financial Times: no restart until complete cessation of hostilities, and even then “weeks to months,” which is physics, not hedging (LNG trains require cryogenic re-cooling, inspection after thermal cycling, gas requalification). For the full conflict timeline and damage assessment, see our three-part [Operation Epic Fury series](https://tscsw.substack.com/p/operation-epic-fury?r=203zi2). Brent at $116.50.

Helium spot reportedly doubled from pre-crisis levels of roughly $12/m³. But source pricing understates end-user impact: in prior shortages, delivered prices spiked 300-700%. The asymmetry is driven by logistics bottlenecks and panic buying. This matters less than it seems, because for semiconductor companies, helium cost is a rounding error on COGS. The price is noise. The signal is allocation volume.

[![](https://substackcdn.com/image/fetch/$s_!earH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80a32b21-6a5b-4df2-8898-8e06b63b84e8_1600x892.png)](https://substackcdn.com/image/fetch/$s_!earH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80a32b21-6a5b-4df2-8898-8e06b63b84e8_1600x892.png)

Two independent consultants triangulate the window. Kornbluth: minimum two-to-three month shutdown, four-to-six months to normalization. Garvey: even one month of disruption produces two-to-three months of logistics chain disruption. Both expect unwinding to outlast the shutdown by roughly 2x.

**Shortage 3.0 (2018-2020) is the precedent.** Also triggered by Qatar: the Saudi-led blockade severed Qatari helium from overland routes, cutting roughly 30% of supply, then compounded by simultaneous outages at LaBarge and Skikda, pushing the effective deficit to 40%. Distributors declared force majeure with tiered allocation: medical and aerospace at 100%, semiconductors at 90-95%, industrial uses cut 20-40%.

It took roughly two years from onset to full normalization because the logistics chain had been disrupted so thoroughly that unwinding it took as long as the disruption itself. The current crisis involves the same facility and a more severe trigger.

A diplomatic blockade is reversible with a phone call. Military strikes on energy infrastructure are not. And the demand conditions are incomparably tighter. During Shortage 3.0, DRAM prices were falling 40-50% from their mid-2018 peak, fabs were cutting utilization voluntarily, and a 5-10% helium allocation cut landed on an industry already producing below capacity. Today DRAM contract prices are up roughly 240% year over year. Quarter-on-quarter increases running 90-95%, the steepest sequential move in the modern memory industry.

[![](https://substackcdn.com/image/fetch/$s_!IYPq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30539085-cf29-4322-ac24-e1552f1fef02_1600x843.png)](https://substackcdn.com/image/fetch/$s_!IYPq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30539085-cf29-4322-ac24-e1552f1fef02_1600x843.png)

DRAM supply trailing demand by nearly 6%. Samsung and SK Hynix running finished inventory at three weeks against a normal floor of four-plus. SK Hynix having presold its entire 2026 output.

[![](https://substackcdn.com/image/fetch/$s_!fgGg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F387a6628-3348-4949-8a4a-37bb6a088e47_1884x1032.png)](https://substackcdn.com/image/fetch/$s_!fgGg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F387a6628-3348-4949-8a4a-37bb6a088e47_1884x1032.png)

There is no slack. There is no quiet quarter where a helium disruption can land softly. The same allocation severity produces categorically different downstream consequences when the market it hits is running at maximum utilization with zero slack.

[![](https://substackcdn.com/image/fetch/$s_!IyWi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44ed40dc-1ee4-4045-9e48-6288bc2353b8_1600x845.png)](https://substackcdn.com/image/fetch/$s_!IyWi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44ed40dc-1ee4-4045-9e48-6288bc2353b8_1600x845.png)

**Shortage 3.0 vs. Shortage 5.0: structured comparison**

[![](https://substackcdn.com/image/fetch/$s_!KJd-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd48d5b0-15fe-413c-902b-bcc5f0416ef7_1600x904.png)](https://substackcdn.com/image/fetch/$s_!KJd-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd48d5b0-15fe-413c-902b-bcc5f0416ef7_1600x904.png)

The other three shortages each lasted one to two years and resolved. Kornbluth’s “Shortage 5.0” framing reflects his view that the current crisis may be the worst. The row that determines everything downstream is reversibility. Engineering assessments do not care about ceasefire timelines.

## The semiconductor transmission mechanism

Now the part that moves capital. The narrative circulating contains genuine insight alongside meaningful exaggeration. Separating the two requires precision about what helium actually does inside a fab, what happens when supply tightens, and where the real vulnerability sits versus where the headlines put it.

Start with the number everyone gets wrong. The entire global helium market is roughly $4-6 billion in annual revenue. Samsung’s semiconductor division does north of $70 billion. Even if helium prices quadrupled, the COGS impact is a few basis points. The bears read that and say “Samsung will simply outbid everyone.” Also wrong. Most helium moves under long-term contracts, and during force majeure, allocation is determined by the distributor, not by the buyer’s willingness to pay. Samsung can write any check it wants for the 5-8% of volume that trades spot. For the 90%+ under contract, the check is irrelevant.

Where helium is genuinely irreplaceable (not a long list, but an absolute one): backside wafer cooling during dry etching (thermal conductivity nine times argon, six times nitrogen, nothing else maintains the temperature uniformity advanced etch profiles require), leak detection (helium’s atomic radius makes it the standard for vacuum integrity), and cryogenic cooling for superconducting systems and EUV infrastructure. Each advanced EUV system eats more than 10,000 liters annually. Hydrogen and nitrogen are being piloted in certain carrier and purge gas roles, with purity tradeoffs that make them useless as emergency substitutes. Net effect: helium shortage degrades fab throughput. It does not produce a hard shutdown unless inventories hit zero, which no major fab is currently facing.

[![](https://substackcdn.com/image/fetch/$s_!iNhM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f91971d-0c38-4838-b3f0-2681f6bd6cbe_1600x885.png)](https://substackcdn.com/image/fetch/$s_!iNhM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f91971d-0c38-4838-b3f0-2681f6bd6cbe_1600x885.png)

But the degradation math is nastier than it looks, and this is the part most coverage either misses or oversimplifies. When a fab conserves helium by reducing flow rates, it reduces cooling efficiency. Lower cooling efficiency means worse thermal uniformity. Worse uniformity means lower yield. Lower yield means more wafers consumed per good die, which means more helium consumed per good die. Conservation accelerates consumption of the resource being conserved. That is the kind of feedback loop that makes process engineers lose sleep. At modest supply reductions, they can optimize around it: adjusting flow patterns, extending cooling intervals, rebalancing chamber scheduling.

The throughput hit is disproportionately small relative to the supply cut. But there is a threshold, which varies by fab, by node, and by product mix, beyond which optimization stops working and process capability degrades. The relationship between helium supply and fab output is not linear. It has a flat region where things are manageable and then a sharp inflection where they are not. We do not have data to pinpoint exactly where that threshold sits for any specific fab (that information lives inside process engineering teams and is not published). What the physics tells us is that the inflection exists and that the distance between “manageable” and “severe” may be a narrower band of supply reduction than the headline numbers suggest.

One more distinction the market is treating carelessly: “semiconductor” is not one thing. An advanced logic fab at N2 with 20+ EUV layers consumes dramatically more helium per wafer start than a DRAM fab running 5-8 EUV layers. The triage discussion focuses on Korean memory because that is where the Qatar dependence data is public. But the per-wafer intensity and geographic exposure questions point in opposite directions for TSMC. Per wafer, logic consumes more.

[![](https://substackcdn.com/image/fetch/$s_!H5Rb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9038bdea-dd9f-4eef-9a02-82c1192926df_1600x904.png)](https://substackcdn.com/image/fetch/$s_!H5Rb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9038bdea-dd9f-4eef-9a02-82c1192926df_1600x904.png)

Geographically, Taiwan’s helium sourcing is opaque but likely draws more heavily from U.S. and Australian supply than from Qatar, given trade patterns and the absence of Taiwan from Qatar-dependent import data. If correct, TSMC’s physical vulnerability may be lower than Samsung’s despite higher per-wafer consumption. We cannot confirm this. TSMC does not disclose helium sourcing, and its public posture (”monitoring, no anticipated impact”) could reflect genuine supply security or standard IR procedure.

## The recycling math, or: why the crisis narrative might be built on the wrong number

This is where the analysis gets interesting, and where most commentary on the crisis is weakest.

The headline says semiconductors consume 21–24% of global helium. That number is real. It is also gross throughput, and gross throughput is the wrong number. Modern advanced fabs with dedicated recovery infrastructure recapture 80–95% of helium through closed-loop systems. Samsung and SK Hynix have both invested in recycling. Run the arithmetic: semiconductors consume roughly 1.3–1.4 BCF in gross throughput annually. At 90% recovery, net fresh demand is approximately 130–140 MCF. At 80%, about 260–280 MCF. The semiconductor industry’s actual fresh helium need, after recycling, is roughly 2–5% of the global market. Not 21–24%. The entire crisis narrative potentially rests on quoting the wrong number.

[![](https://substackcdn.com/image/fetch/$s_!y_WF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fc4d6a9-0bd9-409a-b7f3-41656fd76141_1600x897.png)](https://substackcdn.com/image/fetch/$s_!y_WF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fc4d6a9-0bd9-409a-b7f3-41656fd76141_1600x897.png)

But that 80-95% figure deserves more pressure than it is getting.

Recovery rates vary by process step: backside cooling helium in certain etch configurations is vented, not recaptured; leak detection helium is released by design. Not every fab has invested in closed-loop infrastructure. Leading-edge Korean and Taiwanese fabs almost certainly run at 85-95%.

Older fabs, rapidly expanding Chinese fabs on tight capex budgets, and smaller foundries may run at 50-70% or have no recovery at all. The blended global average is not publicly reported.

At 90% blended recovery, net fresh demand drops to roughly 140 MCF and remaining capacity covers it easily. At 75%, net fresh demand rises to roughly 350 MCF, manageable but with narrowing margins. At 60%, it hits roughly 560 MCF, approximately 10% of remaining capacity, competing directly with medical and aerospace. That is Shortage 3.0 allocation territory. We think the blended average sits in the 70-80% range, but we want to be direct: this is the single most important variable in the entire analysis, and we cannot measure it. If the true rate is 85%, the semiconductor vulnerability story largely collapses. If it is 60%, the tail case becomes the base case.

[![](https://substackcdn.com/image/fetch/$s_!zjrP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62140f46-e55f-466c-8e99-c2c7ff49c9bf_1600x899.png)](https://substackcdn.com/image/fetch/$s_!zjrP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62140f46-e55f-466c-8e99-c2c7ff49c9bf_1600x899.png)

What we can say: the binding constraint is not total helium supply. It is getting semiconductor-grade, process-qualified product to the right geography through a distribution oligopoly managing competing allocation claims. That is a fundamentally different problem, and a less catastrophic one, than “one-third of semiconductor helium vanished.”

## The China variable

South Korea gets the attention because its Qatar import dependence (64.7% per KITA) is publicly reported. But even that number deserves a caveat most coverage omits: Volza trade data for liquid helium imports specifically shows Qatar at only roughly 11% of South Korea’s liquid helium supply, ranking behind the U.S. and Russia. The likely reconciliation is that the 64.7% includes both gaseous and liquid helium, and Korea’s most critical form of supply (cryogenic liquid, which fabs actually consume) may be more diversified than the single headline figure implies. South Korea’s total helium consumption is approximately 13 million cubic meters annually (roughly 460 MCF), implying roughly 8.4 million cubic meters from Qatar across all forms. The vulnerability is real. It may also be less acute for the highest-grade liquid supply than the number everyone is quoting.

[![](https://substackcdn.com/image/fetch/$s_!wPI0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16e6fe1d-de67-4296-8cda-ce5ba4b9f3c2_1600x898.png)](https://substackcdn.com/image/fetch/$s_!wPI0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16e6fe1d-de67-4296-8cda-ce5ba4b9f3c2_1600x898.png)

China may matter more to the outcome and gets far less coverage. China imports roughly 95% of its helium. A substantial share comes from Qatar. SMIC, CXMT, and the entire Chinese domestic fab buildout are exposed to the same disruption. Here is why that matters for Korea: if Chinese buyers compete aggressively for non-Qatari helium, they bid against the same molecules Korean fabs need. Amur partially offsets for both countries, but Amur cannot serve both Chinese and Korean demand adequately if Qatar stays offline for months.

[![](https://substackcdn.com/image/fetch/$s_!Rrf9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F546e9f40-a317-4241-85ae-ca2da1191ed8_1600x646.png)](https://substackcdn.com/image/fetch/$s_!Rrf9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F546e9f40-a317-4241-85ae-ca2da1191ed8_1600x646.png)

The most dangerous version of the tail scenario is not that there is not enough helium globally. It is that Chinese and Korean buyers enter a bidding war for a shrinking pool of non-Qatari semiconductor-grade supply while the major Western distributors try to manage allocation across both markets simultaneously. That is not a supply problem. It is a geopolitical allocation problem wearing a commodity mask.

[![](https://substackcdn.com/image/fetch/$s_!7562!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3094bf4-82be-4733-b22b-4911332d476e_1600x843.png)](https://substackcdn.com/image/fetch/$s_!7562!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3094bf4-82be-4733-b22b-4911332d476e_1600x843.png)

## Inventories: the number that matters most, reported least reliably

Gasworld reports Korean chipmaker stockpiles for approximately six months. AJU Press puts Samsung and SK Hynix at two to three months individually. The six-month figure likely includes distributor, pipeline, and in-transit volumes. Two to three months is probably on-site fab storage. Conservative read: two to three months on-site with additional chain buffer. Resolve by May, probably fine. Persist into summer, probably not.

[![](https://substackcdn.com/image/fetch/$s_!Ij9P!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57e826d6-3842-4b99-aeaf-08a63655bdf6_1600x895.png)](https://substackcdn.com/image/fetch/$s_!Ij9P!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57e826d6-3842-4b99-aeaf-08a63655bdf6_1600x895.png)

SK Hynix told Reuters it has “long secured diverse supply chains and sufficient inventory.” GlobalWafers: “sufficient to support multiple years.” TSMC: monitoring, no anticipated impact. Read those statements with the same trust you extend to any corporate assurance made during a supply crisis with equity implications.

One partial exception: Lenovo has reportedly stockpiled component inventories to roughly 50% above normal levels and locked in long-term supply agreements, suggesting at least some downstream players positioned defensively before the crisis hit. That buys time. It does not change the margin math if memory pricing stays elevated for quarters rather than weeks.

## Allocation triage: where the math turns ugly

If helium becomes scarce enough to constrain production, fabs prioritize highest-margin products. That sounds rational. It is. It also means the downstream gets carved up in ways that are already visible.

HBM commands 4–5x the price premium of server DDR5 and already eats roughly 10% of global DRAM wafer capacity, rising to 13% by 2027. Here is the detail that makes the triage nastier than it looks on a slide: HBM requires three to four times more wafer starts per bit than standard DRAM. Every wafer a fab directs to HBM removes three to four wafers’ worth of consumer DDR5 it could have produced instead. SK Hynix has presold its entire 2026 output. Helium scarcity does not just reduce total output. It accelerates a cannibalization of consumer memory that was already underway before a single drone hit Ras Laffan.

Consumer DDR5, smartphone LPDDR, and automotive memory go to the back of the line. We have scoped this analysis to DRAM because that is where the Qatar dependence data, the inventory disclosures, and the pricing supercycle converge most acutely. NAND (Kioxia, Western Digital, and the Korean producers' flash divisions) faces the same helium inputs at lower per-wafer intensity, fewer EUV layers, and less public data on sourcing exposure. It is a related but distinct problem that deserves its own treatment.

[![](https://substackcdn.com/image/fetch/$s_!h0CB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5e55fa6-70f2-4e51-b264-bd761d0b5aea_1600x877.png)](https://substackcdn.com/image/fetch/$s_!h0CB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5e55fa6-70f2-4e51-b264-bd761d0b5aea_1600x877.png)

[![](https://substackcdn.com/image/fetch/$s_!mqAH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4dd679b2-8de0-4a42-870e-f72d1bfe9722_1886x1058.png)](https://substackcdn.com/image/fetch/$s_!mqAH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4dd679b2-8de0-4a42-870e-f72d1bfe9722_1886x1058.png)

There is a further constraint most coverage misses entirely. Semiconductor-grade helium is not just about meeting a purity spec on paper. A fab running Samsung’s advanced DRAM process has qualified specific helium from specific suppliers through extensive process-of-record testing. Switching suppliers, even to one producing equivalent purity, requires weeks to months of contamination profiling, tool-level baseline testing, and yield validation across multiple wafer lots. During Shortage 3.0, compressed emergency qualification still took four to eight weeks per new source. The real bottleneck is not “can we find 99.999% helium.” It is “can we find process-qualified helium from a validated supplier, at the volume we need, before our on-site inventory runs out.” Those are two completely different questions, and only the first one has an obvious answer.

[![](https://substackcdn.com/image/fetch/$s_!KMRK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff392c0e1-8daa-4417-9603-f626af8255e7_1600x866.png)](https://substackcdn.com/image/fetch/$s_!KMRK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff392c0e1-8daa-4417-9603-f626af8255e7_1600x866.png)

## The fabs may be fine. The downstream is where the pain lands.

At Shortage 3.0 allocation levels (90–95%), a 5–10% throughput reduction at Samsung memory implies $3.5–7 billion of gross volume loss. But in a supply-constrained memory market, volume loss and price gain happen simultaneously. During the 2021 semiconductor shortage, TSMC raised prices 10–20% while barely reducing utilization. If Samsung loses 5% of volume but DRAM ASPs rise 15–20% on tightened supply, net revenue is flat or positive. The fabs might actually make more money.

[![](https://substackcdn.com/image/fetch/$s_!0S9I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3276f66-055f-4007-b336-01c6b133cfdf_1600x805.png)](https://substackcdn.com/image/fetch/$s_!0S9I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3276f66-055f-4007-b336-01c6b133cfdf_1600x805.png)

The investable insight is not Samsung’s top line. It is Apple’s cost structure, Dell’s margin, and every mid-range phone OEM that just discovered a noble gas in Qatar determines whether they hit their BOM target.

The scale of cost transmission is already visible. Memory now accounts for more than half the materials cost of a traditional server, per HPE management on their March earnings call, with elevated pricing expected to persist well into 2027. For smartphones, the math is more striking: industry analysts estimate memory could reach 30–40% of bill-of-materials cost for mainstream handsets in 2026, up from a typical 10–15%. That is not a rounding error. That is a structural repricing of every $200–400 phone sold globally. One major sellside house has already cut its 2026 global smartphone shipment forecast to negative 11% year-on-year, with the decline concentrated in Chinese OEMs and developing markets where price elasticity bites hardest. Apple and Samsung gain share through supplier relationships and premium positioning. Everyone else bleeds units.

[![](https://substackcdn.com/image/fetch/$s_!TPwp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3764b2e6-79f3-454a-9ba1-c679133b7322_1600x773.png)](https://substackcdn.com/image/fetch/$s_!TPwp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3764b2e6-79f3-454a-9ba1-c679133b7322_1600x773.png)

The credit data makes the asymmetry concrete: Bloomberg Intelligence's sensitivity analysis shows Lenovo, operating on single-digit EBITDA margins, could breach Fitch's negative leverage guideline of 2.3x from a cost increase as small as 2% without price adjustment. Xiaomi's adjusted leverage crosses its 1.5x negative threshold at a 50%+ cost rise. These are not theoretical stress tests. They are the arithmetic of what happens when memory reaches 30-40% of handset BOM and the OEM cannot pass it through without killing demand.

This is not speculation. It is exactly what happened during the 2021 semiconductor shortage. AlixPartners estimated $210 billion in global automotive revenue losses and 7.7 million vehicles of lost production. And yet VW and Stellantis posted higher profitability, because they funneled scarce chip allocation to highest-margin models. The suppliers suffered. The OEMs adapted. The fabs thrived.

The analogy requires calibration. 2021 was a demand shock across the entire semiconductor industry; what we are describing is a potential constraint on a single input primarily affecting memory fabs in a specific geography. In 2021, Ford could not get MCUs at any price. In a helium scenario, Dell can still get DDR5, just at a higher ASP.

That is a margin story, not a production-halt story. The pattern holds, the magnitude is likely smaller, and it lands on an industry already absorbing the worst memory cost inflation in a decade.

[![](https://substackcdn.com/image/fetch/$s_!fE7o!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82a1fa93-bd9a-48e2-bcca-44ac0d14be7e_1600x897.png)](https://substackcdn.com/image/fetch/$s_!fE7o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82a1fa93-bd9a-48e2-bcca-44ac0d14be7e_1600x897.png)

## A competitive asymmetry the market has not priced

U.S. fabs sit on top of the world’s largest helium production base. Two-thirds of U.S. helium is consumed domestically. Intel’s fabs in Arizona and Ohio have structurally more secure helium access than Samsung in Pyeongtaek or TSMC in Tainan. In a prolonged disruption, this is a genuine input advantage in advanced logic and foundry.

Whether it matters depends entirely on whether Intel Foundry can execute. A company losing billions per quarter with unproven yields at 18A does not become competitive because it has better parking at the gas station. The advantage is real and compounds with every CHIPS Act fab near domestic supply. But it is a necessary condition for competitiveness, not a sufficient one.

[![](https://substackcdn.com/image/fetch/$s_!Xhn8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84aac0b3-b131-4b85-a96c-c48ed69c3cce_1600x876.png)](https://substackcdn.com/image/fetch/$s_!Xhn8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84aac0b3-b131-4b85-a96c-c48ed69c3cce_1600x876.png)

## The natural hedge nobody is talking about

Energy costs and helium scarcity are often presented as compounding risks. European gas prices surged as much as 67% in a single week following the Ras Laffan shutdown, a reminder that energy and helium move on the same trigger. But the two risks partially offset.

The scenario where helium scarcity bites hardest is one where AI capex continues at full pace, keeping fabs at full utilization and consuming every available molecule. But that is also the scenario where energy costs are least likely to kill the buildout, because hyperscaler AI spending is strategic, not discretionary. Conversely, $116 Brent triggering real demand destruction means memory demand softens and helium scarcity becomes less binding.

The nightmare for downstream consumers is helium scarcity without demand destruction: fabs produce less, prices soar, demand stays hot. The nightmare for fabs is demand destruction without scarcity: volumes fall, pricing power evaporates. These risks hedge each other more than they compound.

[![](https://substackcdn.com/image/fetch/$s_!sjUk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d194fce-4539-47c8-b661-b559b3edb45d_1600x701.png)](https://substackcdn.com/image/fetch/$s_!sjUk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d194fce-4539-47c8-b661-b559b3edb45d_1600x701.png)

**Who benefits, who suffers, and where to be skeptical**

**U.S. helium production: right thesis, wrong instrument.** LaBarge is the most critical helium facility on Earth: 1 BCF per year, expandable to 1.4 BCF, eight decades of reserves. But helium is a rounding error in ExxonMobil’s consolidated revenue. You cannot get meaningful equity exposure to U.S. helium through large-cap public markets. Blue Spruce’s $737M Dry Piney project is private.

**Industrial gas companies: informational value exceeds trade value.** Linde, Air Liquide, and Air Products see surcharge-driven margin expansion on specialty gas. Linde’s helium business generates roughly $1.0-1.5 billion annually (approximately 3-4.5% of $33 billion consolidated revenue, triangulated from its 24.5% share of a $4.1 billion global market per Verified Market Research). Meaningful for specialty gas margins, not transformative at the group level. Linde was near all-time highs before the conflict and has held firm. The market agrees: more narrative than material for these names. Their real value is informational: quarterly commentary on helium allocation and force majeure status, plus any disclosure of Beaumont cavern drawdown rates, is the most reliable public data on how the disruption is transmitting downstream.

**Semiconductor equipment makers are the second-derivative play nobody is watching.** Lam Research and Applied Materials have been developing helium-reduction chamber designs for years. Lam’s latest etch platforms claim 30-40% helium reduction per wafer. In a prolonged shortage, fabs with capital budget to upgrade or retrofit can meaningfully reduce dependency. That accelerates the equipment upgrade cycle. Not the primary thesis for either company, but if you’re looking for helium scarcity exposure that isn’t priced into a $5 billion commodity market, the pull-forward of tool upgrades is the angle.

[![](https://substackcdn.com/image/fetch/$s_!1-m-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe820d54f-9466-41a5-be37-b76e7f5964d8_1600x876.png)](https://substackcdn.com/image/fetch/$s_!1-m-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe820d54f-9466-41a5-be37-b76e7f5964d8_1600x876.png)

**Exploration-stage helium juniors: options, not assets.** Pulsar Helium (PLSR) has extraordinary concentrations (14.5%) and confirmed helium-3, though it’s worth noting that He-3 and He-4 (standard helium) serve entirely different markets with separate supply chains. He-3 is used in quantum computing dilution refrigerators and comes primarily from tritium decay in nuclear weapons programs, not natural gas. The Hormuz disruption affects He-4 (semiconductor helium) acutely and He-3 minimally. Pulsar’s He-3 presence is relevant to a quantum computing thesis, not to the semiconductor supply crisis at hand. Stock up ~334% since listing. Pre-revenue. Years from production. Renergen Phase 2 at 540 MCF would be genuinely meaningful at 9% of global supply, but that’s $1.16B of capex with production not before 2028-2029. These companies cannot fill a 2.6 BCF shortfall. Their near-term capacity is low single-digit percentages. Many geological claims come from their own promotional materials. Price them as deep out-of-the-money options.

**On the $200B Samsung/SK Hynix selloff.** Intellectual honesty demands a confession: that decline is overwhelmingly the broader war, and we covered precisely why in “Oil Isn’t The Trade.” Helium is one of perhaps fifteen concurrent supply chain risks hitting Korean equities simultaneously, and it is not the largest. If helium is your primary bear thesis for these names, you have mistaken a symptom for a disease.

[![](https://substackcdn.com/image/fetch/$s_!u76m!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F121a4988-eb86-4cb0-b91a-bdc97fb91827_1600x889.png)](https://substackcdn.com/image/fetch/$s_!u76m!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F121a4988-eb86-4cb0-b91a-bdc97fb91827_1600x889.png)

**Three scenarios**

An honest accounting: the blended global recycling rate is our estimate, not measured.

Beaumont’s actual fill level is not disclosed. China’s Qatar helium dependence by volume is not available in English-language sources. Every inventory estimate from Korean chipmakers reflects corporate messaging, not audited disclosure.

Our framework is built on the best available data, triangulated and stress-tested.

But several key variables are genuinely uncertain, and the reader should weight the scenarios accordingly. The probability framework follows the same conflict-duration logic we built in [Operation Epic Fury](https://tscsw.substack.com/p/operation-epic-fury?r=203zi2).

The key insight: helium’s restart is entirely derivative of LNG’s restart, which means conflict duration is the only variable that matters. Everything else is arithmetic you run after you pick a duration.

Three branches. First: conflict ends within weeks, say by early April. LNG restarts in April, helium normalizes by summer. We put roughly 25% on this because optimistic political timelines in Middle Eastern conflicts have a batting average that would get you sent to the minors. Second: conflict runs three to five months, the modal outcome when initial timelines slip. Korean fab inventories of two to three months on-site plus chain buffer cover this window with strain but not breakage. We put 50% here. Third: six months or more. Ras Laffan sustains meaningful damage requiring extended repair, or the conflict broadens. This is the tail that produces binding semiconductor constraints. We put 25% on it because physical damage has not been confirmed, but Al-Kaabi’s “onshore assessment is ongoing” leaves the door wider open than the market appreciates.

[![](https://substackcdn.com/image/fetch/$s_!Z-Z1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f4a0e42-05a2-4aae-985b-954635835e00_1600x815.png)](https://substackcdn.com/image/fetch/$s_!Z-Z1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f4a0e42-05a2-4aae-985b-954635835e00_1600x815.png)

**Benign resolution (~25%).** Conflict ends within weeks. LNG and helium restart by April. Normalization by summer. No allocation triage. Pre-crisis oversupply reasserts. Korean memory re-rates as war premium unwinds. Helium becomes a footnote.

**Base case (~50%).** Three-to-five month disruption. Spot helium stays elevated (2-3x pre-crisis) but contracted allocation holds above 90-95% for semiconductors. Beaumont and other storage assets provide a buffer that didn’t exist in prior shortages. Korean fabs draw inventories but avoid production triage.

[![](https://substackcdn.com/image/fetch/$s_!QWf3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f9ffb18-e428-4cb4-bd6e-7688b373b434_1600x645.png)](https://substackcdn.com/image/fetch/$s_!QWf3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f9ffb18-e428-4cb4-bd6e-7688b373b434_1600x645.png)

Conservation measures but no meaningful throughput reduction on existing capacity. Memory pricing accelerates on perceived supply risk, potentially benefiting fab revenue per unit even as helium tightens. The investable insight is not the fabs but the downstream OEMs paying more for less memory.

**Tail risk (~25%).** Six-month-plus disruption. Ras Laffan damage extends restart to 12+ months. Distributor force majeures cascade. Allocation falls to 85-90%, pushing fabs past the conservation knee where throughput degradation accelerates non-linearly. Production triage toward HBM at the expense of consumer and automotive memory. Samsung and SK Hynix revenue potentially protected by higher ASPs, making the equity impact ambiguous. Unambiguous losers: consumer electronics OEMs, auto manufacturers, any business model that assumes DDR5 and LPDDR availability at 2025 lead times. Multiple industry models project DRAM undersupply persisting through late 2027 even without a helium disruption. Layer it on, and the timeline to normalization extends into territory the memory industry has not experienced since the smartphone era began.

Chinese competition for remaining supply exacerbates the crunch. Intel and U.S. fabs gain competitive position from domestic helium access. Equipment vendors (Lam, AMAT) see accelerated upgrade cycles. Echoes Shortage 3.0’s two-year duration with materially worse starting conditions.

[![](https://substackcdn.com/image/fetch/$s_!S56L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff81bed7-eadb-4261-b1cd-fe44be2dd29c_1600x900.png)](https://substackcdn.com/image/fetch/$s_!S56L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff81bed7-eadb-4261-b1cd-fe44be2dd29c_1600x900.png)

**Five indicators and what they mean**

**1. Distributor force majeure on helium-specific contracts.** QatarEnergy’s force majeure covers LNG. If Linde, Air Liquide, or Iwatani issue allocation notices to semiconductor customers, the base case shifts toward the tail. This is the canary.

**2. Contracted allocation below 90%.** Spot is noise. The signal is volume cuts against long-term contracts. This data is private and emerges through earnings commentary, Gasworld reporting, and industry contacts. Genuine spot is only 5-8% of volume. The contract market is where shortage transmits.

**3. QatarEnergy restart timeline.** Independent engineering assessment confirming equipment damage requiring 6+ months shifts the tail to the base case.

**4. Government intervention.** South Korean or Chinese emergency procurement or strategic releases signal industry buffers are failing. This indicator is already in early motion: ruling party lawmaker Kim Young-bae briefed reporters last week that officials had raised the possibility of semiconductor production disruption if Middle Eastern materials cannot be sourced. South Korea’s industry ministry has identified at least 14 semiconductor supply chain inputs with high dependence on the Middle East. The question is whether this moves from monitoring to active intervention: emergency procurement contracts, strategic stockpile releases, or government-brokered supply agreements with non-Qatari producers. If Seoul or Beijing escalate to that level, it tells you the private sector’s buffers are insufficient.

**5. SK Hynix and Samsung Q1 earnings.** Listen for: “conservation measures,” “supply management,” “optimized gas utilization,” “selective maintenance scheduling.” Those are rationing by other names. Faster-than-expected inventory drawdown compresses the timeline to binding constraints.

[![](https://substackcdn.com/image/fetch/$s_!wpxP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06669e3f-12df-4d07-b7fa-94772abcedf2_1600x885.png)](https://substackcdn.com/image/fetch/$s_!wpxP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06669e3f-12df-4d07-b7fa-94772abcedf2_1600x885.png)

**What helium reveals**

The EU classified helium as a Critical Raw Material in 2023. Canada classifies it as critical. The United States does not. The USGS excluded it from the 2022 Critical Minerals List. The DOE’s 2023 list omits it. The strategic reserve that existed for nearly a century was sold off 20 months ago.

The AI supply chain runs from Wyoming geology through Qatari LNG plants through the Strait of Hormuz to Korean memory fabs to Nvidia’s Blackwell and Rubin architectures. Every link was assumed to be robust. One was not.

But helium is not the lesson. Helium is the example, and it is not even the only one from this conflict. Bromine, specifically high-purity hydrogen bromide used in polysilicon etching, is sourced 97.5% from Israel for Korean fabs. Two-thirds of global production comes from Israel and Jordan. Israel’s Dead Sea facilities are not directly disrupted by Hormuz, but the risk profile is structurally identical to helium: extreme geographic concentration, opaque pricing, non-trivial semiconductor qualification requirements, and a conflict with no clear end date.

South Korea’s industry ministry counts 14 semiconductor supply chain inputs with high Middle Eastern dependence. One conflict is stress-testing all of them simultaneously, and the market is analyzing each in isolation as though they are uncorrelated. The pattern is what matters. Neon from Ukraine. Palladium from Russia. Gallium and germanium from China. Cobalt from the DRC. Ultra-pure quartz from Spruce Pine.

[![](https://substackcdn.com/image/fetch/$s_!Db7N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd92f27a1-bd40-457b-9348-24afdadf5eca_1600x899.png)](https://substackcdn.com/image/fetch/$s_!Db7N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd92f27a1-bd40-457b-9348-24afdadf5eca_1600x899.png)

Each one sits in the same structural vulnerability: production concentrated in a handful of facilities, distribution controlled by a handful of companies, substitution impossible on any timeline that matters, and a market too small for price signals to provide early warning.

The semiconductor industry will probably navigate this helium disruption. It has navigated four previous ones. The question is whether an industry building $650 billion of infrastructure per year on the assumption of uninterrupted access to a dozen obscure commodity inputs has adequately priced the risk that any one of them disappears. The answer, based on the last two weeks, is obviously not.

One final thread worth pulling. Bloomberg Economics estimates the existing memory supercycle is already adding roughly 0.2 percentage points to consumer price inflation through device cost pass-through. Under a scenario where helium constraints compound the shortage, their own assessment is that this estimate “could prove conservative.” A noble gas that most people associate with party balloons may be contributing to the inflation print. Nobody in the CPI forecasting community is modeling that. Nobody in the helium community is thinking about CPI. The gap between those two worlds is where the next surprise lives.

Watch the five indicators. And start asking what breaks next.

[Share TSCS](https://tscsw.substack.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[Share](https://tscsw.substack.com/p/partys-over?utm_source=substack&utm_medium=email&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxNDAwMjQ1LCJwb3N0X2lkIjoxOTA4NTk0ODYsImlhdCI6MTc3NDIyNjI1MiwiZXhwIjoxNzc2ODE4MjUyLCJpc3MiOiJwdWItMjM1NDI0NCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.cEzQhJPd-REbcIhCkrFkXcoCImFEavpJEv5V_5LNiCs)

---

*TSCS Research. Not investment advice. Bloomberg terminal screenshots referenced throughout are available to subscribers.*

*Sources: USGS Mineral Commodity Summaries (2025, 2026); Bloomberg Economics (Global Insight, March 2026); UBS Memory Semis Monthly (March 2026); J.P. Morgan Hardware & Networking (March 2026); Bloomberg Intelligence (Micron Equity Research, March 2026); HPE Q1 FY2026 Earnings Call; TrendForce; Kornbluth Helium Consulting; Intelligas Consulting; TechCET Critical Materials Report; Gasworld; Sherwood News; CNBC; Tom’s Hardware; Korea Times; Seoul Economic Daily; AJU Press; Business Korea; ACS C&EN; Peninsula Qatar; Al Jazeera; Financial Times; IDTechEx; Linx-Consulting; ExxonMobil; QatarEnergy; BCG/SIA; Morningstar; Counterpoint Research; Bain & Company; SemiAnalysis; Verified Market Research; Grand View Research; Volza; AlixPartners; KITA; Reuters; Helium24 Group; South Korea Ministry of Trade, Industry and Energy; Bloomberg.*