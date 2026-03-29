*Opinions are my own and do not represent past, present, and/or future employers. All content is based on public information and independent research. This newsletter is not financial advice, and readers should always do their own research before investing in any security. I am invested in the semiconductor industry. As of the date of this publication, I may hold long positions in the securities discussed in this article.*

subscribe

Subscribed

Lumentum. A $25b market cap Nasdaq-listed AI infrastructure company that according to their 10-K is a “leading provider of optical and photonic products” whose products “are essential to a range of cloud, artificial intelligence and machine learning (“AI/ML”), telecommunications, consumer, and industrial end-market applications.”

This stock has performed remarkably, up almost 4x since the year began. It’s got so much momentum **its name even rhymes with it** (Lumentum? Momentum?). If you’re a skeptic of AI, you would probably see this stock as a hallmark of the AI bubble, propped up by nothing but speculation.

[![](https://substackcdn.com/image/fetch/$s_!PguK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6de4c0e5-0156-47bf-906a-2b390925bb73_1029x688.png)](https://substackcdn.com/image/fetch/$s_!PguK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6de4c0e5-0156-47bf-906a-2b390925bb73_1029x688.png)

So why has LITE been performing so well? Beyond the memetic narrative of optics being the next big bottleneck in AI (see this [viral tweet by Vikram Sekar](https://x.com/vikramskr/status/1992537949708431638)), Lumentum is actually a fascinating company with **many business lines all hitting inflection points**. Several credible investors are long for different reasons, sometimes with completely unrelated theses. That’s why Lumentum has truly been enjoyable to research.

Between now and the end of Q1, I’ll publish a piece every few weeks or so forecasting one part of this business and explaining in depth the industry dynamics behind my assumptions. By the end of these posts, I’ll have published a fully finished revenue build, 3 statement model, EPS analysis, and DCF valuation, culminating in a 50-80 page deep dive.

---

Thanks for reading! Subscribe for free to receive new posts and support my work.

Subscribed

### Why Do We Need Optics?

If you want to communicate data through a datacenter, you have two choices, copper or light (a.k.a. optics). Copper is great for close range communications, like between chips in a rack (scale up), but falters when more distance is added.

Copper is like shouting to a friend across a dinner table. It’s easy, cheap, and effective. But shouting the same message to a friend standing three football fields away and you’re going to lose your voice, they aren’t going to hear you, and you’ll burn a lot of energy trying. In physics terms, this is called “attenuation” or signal loss. As we push more data through copper wires at higher speeds, the electrons generate heat (resistance) and the signal dies out after just a few meters. To compensate, you have to make the cables thicker and heavier, until you’re basically trying to wire a data center with garden hoses.

Modern AI models are massive and to run these models, we have to stitch together 10,000, 20,000, or even 100,000 GPUs into a single, giant supercomputer known as a coherent supercluster. These chips need to “talk” with each other constantly, sharing data back and forth at blistering speeds.

Since you can’t fit 100,000 GPUs in a single server rack, you have to spread them out across a warehouse-sized hall. Suddenly, your data needs to travel 50, 100, or 500 meters to get from GPU A to GPU Z. This is known as scale out (versus scale up), and copper physically cannot do this at the speeds AI demands (800 Gigabits or 1.6 Terabits per second).

This is where light shines (get it?). Unlike electrons, photons don’t have mass and they don’t experience resistance. They can zip down a strand of glass thinner than a human hair for kilometers without generating heat or losing the signal.

Lumentum is one of the purest ways to gain exposure to optics. However, they operate what I see as 4 distinct businesses, each of which I will cover separately.

* First, they assemble **Transceiver Modules**, the pluggable “on-ramps” that translate electrical signals into light so data can escape the server rack. These are full systems that include many parts like a light source (also made by Lumentum), photodiode, modulator, digital signal processor (DSP), etc.
* Second are the **Laser Components**, the light source inside those transceivers that actually generate the beam.
* Third is **Systems**, a burgeoning high-margin monopoly where Lumentum sells entire complex hardware units, like the Optical Circuit Switches (OCS) or Co-Packaged Optics (CPO).
* And finally, there is the **Non-AI** business consisting of legacy telecom and industrial lasers.

[![](https://substackcdn.com/image/fetch/$s_!XRAP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff42ab3e0-74bd-4271-a6df-be55f07f87eb_1024x559.png)](https://substackcdn.com/image/fetch/$s_!XRAP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff42ab3e0-74bd-4271-a6df-be55f07f87eb_1024x559.png)

### Transceiver Modules

Today’s topic is Lumentum’s most straightforward business line: the sale of fully assembled optical transceiver modules enabled by their acquisition of Cloud Light.

Optical transceiver modules are fundamentally a manufacturing operation: taking complex optical chips (lasers, detectors, DSPs), packaging them into a standardized metal casing, and selling the finished unit to hyperscalers.

Because this business relies on assembly rather than pure IP invention, it has historically operated with lower margins. The primary barrier to entry is not inventing the underlying physics, but rather scaling the assembly line efficiently. Consequently, this market trends toward commoditization over time. Aggressive manufacturers, particularly Chinese firms like **Innolight** and **Eoptolink**, excel at this dynamic, ramping up volume, optimizing yields, and consistently driving down prices. As a result, the Average Selling Price (ASP) for any specific transceiver module generation typically declines each year.

However, the industry counteracts this pricing pressure through a cycle of “Generational Resets.”

Every few years, data center speeds double: moving from 400G to 800G, and now to 1.6T. When a new generation launches, the price doesn’t simply double as well; it often increases by **more than 2x**. This premium exists because jumping from 400G to 800G involves far more than just adding data lanes. It requires solving exponential challenges in signal integrity, thermal management, and precision manufacturing. Early in a cycle, manufacturing yields are low and few players can build the units reliably. This scarcity allows companies like Lumentum to command significant pricing power. Over time, as these engineering hurdles are cleared and competitors enter the market, volumes ramp up. Soon enough, the module returns to commodity status until the next generation arrives, after which older generations ramp down as obsolescence takes hold.

Credits to Irrational Analysis for the following image taken at this year’s OCP conference showing the volume lifecycle in action for the 400G, 800G, 1.6T, and 3.2T generations. Please check out his work and go support him if you haven’t already.

[![](https://substackcdn.com/image/fetch/$s_!TMt9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22a3f8d9-38b1-4409-86c7-1fdd042f8e20_1024x599.png)](https://substackcdn.com/image/fetch/$s_!TMt9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22a3f8d9-38b1-4409-86c7-1fdd042f8e20_1024x599.png)

Lumentum acquired Cloud Light for $750 million in late 2023 with a singular goal: to capture the hyperscale data center market that had previously eluded them. Before this deal, Lumentum was primarily a component supplier, selling the laser chips to the transceiver makers. Cloud Light gave them the capability to build the entire box themselves, specifically targeting the high-speed (800G and 1.6T) modules that cloud giants like Google and Nvidia were demanding. This vertical integration allows them to capture more margin dollars per unit, as they now own both the “engine” (laser) and the “car” (module).

However, Lumentum has adopted a disciplined, almost contrarian strategy for this business. Management has stated they intend to cap transceiver revenue at roughly **$1 billion annually**. This is a deliberate move to preserve profitability. The optical module market is notoriously cutthroat, with Chinese competitors often driving gross margins down to the low 20% range. By self-imposing a cap, Lumentum signals they will only chase “premium” sockets—high-speed, complex modules where their vertical integration provides a distinct advantage—and walk away from low-margin commodity volume. That said, they have explicitly noted they *could* ramp capacity to $2–4 billion if margin profiles improve, leaving the door open for upside if the market tightens.

Several tailwinds support this premium strategy, most notably the shift toward **bidirectional (BiDi) modules**. These are specialized transceivers that transmit and receive data simultaneously over a single fiber strand, doubling capacity without laying new cable. BiDi modules are critical for architectures like Google’s **Optical Circuit Switch (OCS)** fabric, which requires high port density and complex optics that commodity manufacturers struggle to produce at yield. This complexity creates a “moat” around the socket, protecting Lumentum’s margins from the inevitable price erosion that plagues standard transceivers.

[![](https://substackcdn.com/image/fetch/$s_!iVh2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa01ce9d6-0545-4af9-adbd-ec85d0586afe_1497x733.png)](https://substackcdn.com/image/fetch/$s_!iVh2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa01ce9d6-0545-4af9-adbd-ec85d0586afe_1497x733.png)

Based on these dynamics and management’s strategic discipline, here is how we are forecasting the transceiver segment:

We forecast 400G shipments declining rapidly, effectively treating it as a legacy tail. Lumentum is prioritizing profitability over volume, meaning they will actively exit this commoditized socket rather than fight a price war they don’t need to win.

For the 800G generation, we model shipments peaking in 2027 and 2028. This aligns with the standard industry product lifecycle (as seen in LightCounting data from OCP), where 800G serves as the high-volume workhorse for inference clusters before the next speed transition takes over.

Looking further out, we see 1.6T and 3.2T ramping significantly in the late 2020s, with 1.6T volumes substantially higher than 3.2T as the ecosystem matures. However, we are modeling declining ASPs across the board. This reflects the reality of the “physics tax” eventually being solved by aggressive competitors like Innolight and Eoptolink, who will inevitably storm the field and compress pricing.

Despite this pricing pressure, we forecast Gross Margins slowly climbing to the low 40s. This margin expansion is purely a function of mix shift: as Lumentum sheds the lower-margin, commoditized modules and focuses on the complex, high-speed sockets (like custom BiDi or early 1.6T), the overall profitability profile improves.

Finally, on the top line, our model stays disciplined. We keep total transceiver revenues around $1 billion in 2026, respecting management’s explicit commentary about capping revenue to preserve margins. However, as the AI total addressable market expands and Lumentum scales its high-end capacity, we model revenue ramping to $3.5 billion by 2030, consistent with management’s long-term upside commentary.

### Up Next

In the next post, we will continue our revenue build and our journey across Lumentum’s various business segments, tackling Laser Components, then Systems, and lastly non-AI.