*Opinions are my own and do not represent past, present, and/or future employers. All content is based on public information and independent research. This newsletter is not financial advice, and readers should always do their own research before investing in any security. I am invested in the semiconductor industry. As of the date of this publication, I currently hold a long position in Lumentum Holdings (LITE) and Coherent Corp. (COHR). Feel free to reach out at jasonschips@gmail.com.*

Subscribe for CPO (Consistently Profitable Opinions)

Subscribed

---

**I built a tool using Claude Code to automate DCF valuation.**

**[Check it out: dcfmodel.ai](http://www.dcfmodel.ai)**

---

This weekend, I was planning on writing about something, *anything*, unrelated to optics or CPO.

Unfortunately, I got pulled down another optical rabbit hole and after a 3.5 hour conversation with Claude Opus 4.6, here we are. I am yapping about CPO again, sorry.

We were unable to load this poll. Please refresh the page.

Anyways.

Something fundamental has changed in co-packaged optics over the past few weeks. We can all feel it. What was once a speculative technology timeline has crystallized into an urgent, near-term reality. CPO has gone from an “if” to a “when” to a “NOW” — and the investment implications are enormous. Today, I want to walk through why **scale-up** CPO specifically represents the most important secular growth opportunity in semiconductor infrastructure today, why the industry just crossed a critical inflection point, and how the economics of this transition favor certain companies far more than others.

## Why Scale-Up CPO TAM is Astronomically Large

Currently, GPUs in a scale-up domain (a single coherent “virtual chip”) are forced to be close together, a physical constraint imposed by copper, which means each virtual chip can only be so large.

NVLink can span roughly the length of a single rack before signal integrity degrades. NVIDIA packs 72 GPUs, 36 CPUs, and 18 NVSwitch chips into one rack with over 5,000 copper cables totaling 2 miles of wiring, all to maximize the number of GPUs that can see each other’s memory at full NVLink bandwidth without crossing the copper wall. Plus, tons of hot GPUs packed together requires lots of cooling.

Optics solve signal integrity, we know that. But it does something else as a byproduct: **optics decouples bandwidth from physical proximity.**

This is the key insight that makes scale-up CPO an absurd TAM. Once you replace copper with optics in the scale-up domain, the physical constraint that forces GPUs to be packed tightly together *disappears*. You no longer need all 72 GPUs crammed into a single rack. You can spread them out across two racks, four racks, an entire row, and still maintain the same NVLink-coherent memory domain. The “world size” for that virtual chip can expand arbitrarily.

This fundamentally **blurs the line between scale-up and scale-out**. You can scale up so much that it’s almost like scaling out?...

If your scale-up domain can span an entire datacenter hall, you need far less traditional scale-out networking. Scale-out doesn’t disappear but it becomes a much smaller fraction of total interconnect bandwidth. Scale-up CPO eats copper scale-up and optical scale-out all at once.

First of all, think about what this means for actual AI deployments. More GPUs can talk at full speed without the multi-hop latency scale-out required, very useful for training in particular. Second, think about what this means for TAM. In a CPO world where scale-up goes optical, the optical content per GPU multiplies by 5x, 10x, or more because every NVLink connection that was copper now becomes an optical link.

As Coherent CEO James Anderson put it on their most recent earnings call:

> “all of that network today, the networks within the racks, are electrical. And as those networks convert to optical over the coming years, the amount of optical content that we gain in the scale-up part of the network is just tremendous... we believe the scale-up CPO opportunity will dwarf the opportunity in scale-out. It will be orders of magnitude larger.”

## Scale-Out CPO is the Guinea Pig

I was very surprised at how early we got the first scale-out CPO orders as I thought we would at least have a generation or two with intermediate/bridge solutions such as NPO. Why is CPO coming so fast?

The answer is…

[![](https://substackcdn.com/image/fetch/$s_!Gxb-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb273c79-52cc-48c7-bef7-164a087cde1d_735x725.png)](https://substackcdn.com/image/fetch/$s_!Gxb-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb273c79-52cc-48c7-bef7-164a087cde1d_735x725.png)

Scale-out CPO acts as the guinea pig for the eventual scale-up endgame, serving two critical functions: **building the reliability database** and **readying the supply chain**.

CPO is a new technology with no track record at hyperscale deployment. Before NVIDIA can bet the scale-up fabric of a $500K+ Rubin Ultra rack on co-packaged optics, they need real-world reliability data across millions of device-hours. They need to understand failure modes, degradation curves, thermal cycling effects, and mean time between failures — not from lab testing, but from production deployments at scale. Scale-out CPO provides the perfect testing ground: it’s a large enough deployment to generate statistically meaningful reliability data, but it’s at the network edge where a failure is less catastrophic than inside the scale-up domain.

Simultaneously, NVIDIA is using scale-out CPO orders to force the supply chain into readiness. This is classic NVIDIA playbook — the same thing they did with CoWoS advanced packaging and HBM memory. By placing large purchase orders years ahead of volume scale-up deployment, they ensure that laser suppliers, SiPho foundries, optical engine assemblers, and test equipment vendors are investing in capacity, qualifying processes, and solving yield problems *before* the scale-up ramp hits. When scale-up CPO demand arrives in 2027-2028, the supply chain will already be running at production maturity rather than scrambling through early yield learning.

This is why Lumentum’s recent scale-out CPO orders are so significant as a leading indicator. On their February earnings call, Lumentum CEO Michael Hurlston disclosed that the company

> “secured an additional multi-$100 million purchase order for ultra-high-power lasers that support optical scale-out applications,”

with shipments expected in 2027. This follows earlier orders and confirms that scale-out CPO is entering production volumes. The supply chain is being primed.

## From “If” to “When” to “Now”

Three converging data points mark the inflection where CPO shifted from speculative to inevitable to imminent.

**First, Lumentum’s scale-out CPO orders are now in production ramp.** Hurlston confirmed on the February call that the company expects

> “material shipment inflection of UHP chips in the second half of this calendar year,” with the additional multi-hundred-million-dollar order clicking in during the first half of 2027. CPO is no longer a design-in exercise — it’s a production program with purchase orders and delivery schedules.

**Second, Coherent’s language on scale-up CPO has shifted dramatically.** Anderson told investors that Coherent recently “secured an exceptionally large purchase order from a market-leading AI data center customer for a CPO solution” and that there are

> “very active, deep engagements” on scale-up CPO across multiple customers. Most tellingly, when asked if scale-up was years away, he responded: “I wouldn’t call it years out, I think it’s sooner than that based on the plans that we’re seeing from our customers.”

This is a company that has direct line of sight into NVIDIA’s roadmap telling you that scale-up is coming faster than consensus expects.

**Third, the supply chain data supports aggressive timelines.** NVIDIA is rumored to be asking Lumentum for 50 million laser capacity by 2027 — roughly double what the current trajectory implies. Lumentum itself confirmed it expects “first scale-up CPO shipments replacing longer copper connections” by late calendar 2027.

The ratio of scale-up to scale-out CPO content per rack (648 vs. 144 optical engines, or roughly 4.5:1 in the Rubin Ultra architecture) underscores the point: scale-up is already the dominant source of CPO demand in the first generation, and this ratio will only increase as future architectures expand the scale-up domain to larger GPU counts while scale-out becomes more secondary.

## LITE vs TSEM for CPO Exposure

Both Lumentum and Tower Semiconductor make stuff that go in CPO, but the economics of their participation are quite different. Let me run through the math.

#### Lumentum

Lumentum’s CPO value chain starts with ultra-high-power (UHP) CW lasers and extends into External Light Source (ELS) modules. Each ELS module contains 8 UHP lasers operating at different wavelengths, packaged together as a pluggable light source that couples into the SiPho optical engine.

The content math per ELS module works as follows. For standalone laser chip shipments, Lumentum captures approximately $260 per ELS equivalent (8 lasers at roughly $32-35 each). For full ELS modules — which Lumentum is now actively pursuing as a higher-value product — the ASP is approximately $600-700 per module. If we assume a blended mix where roughly 25% of Lumentum’s CPO shipments are full ELS modules and 75% are laser chips, the average content per ELS module equivalent is approximately **$350**.

What’s remarkable about this is the value capture relative to the traditional transceiver market. In the pluggable transceiver world, Lumentum sells EML or CW laser chips at $5-15 per device into a transceiver module selling for $100-300. Lumentum captures maybe 5-10% of the transceiver BOM. In CPO, with ELS modules, Lumentum captures 40-60% of the optical BOM per link. The technology difficulty premium — 400mW UHP lasers with subsea-grade reliability — is what enables this pricing power.

#### Tower Semiconductor

Tower’s CPO value chain is as the monopoly silicon photonics foundry. They fabricate the SiPho die — the photonic integrated circuit containing waveguides, modulators, multiplexers, and photodetectors — that sits at the heart of every CPO optical engine.

The content math per ELS module requires understanding how SiPho die map to the system architecture. Each ELS module feeds one SiPho transmit engine (the laser light enters the SiPho die which modulates it). On the receive side, there’s a corresponding SiPho die with demux and photodetectors. Under a disaggregated architecture (separate TX and RX die), each ELS maps to 2 SiPho die. Under a consolidated architecture (TX+RX integrated), it’s 1 larger die per ELS.

Tower runs 200mm SiPho wafers at approximately $7,000 ASP (reflecting their monopoly pricing power in a supply-constrained market). A 200mm wafer has roughly 31,000 mm² of usable area. For a disaggregated TX die at ~50 mm², you get approximately 250 good die per wafer at mature yields, putting the cost per die at roughly $28. Two die per ELS (TX + RX) = $56 of Tower content per ELS module. For a consolidated TX+RX die at ~80 mm², you get approximately 160 good die per wafer, putting the cost at roughly $44 per die — so $44 of Tower content per ELS module in this scenario. Averaging across both architectures gives approximately **$50** of Tower content per ELS module.

#### Comparison

Lumentum captures approximately $350 per ELS module equivalent. Tower captures approximately $50. That’s a 7:1 ratio of value capture per unit of CPO deployment.

And yet, as of writing, Lumentum’s market cap is only approximately 3x Tower’s. This means that in terms of pure CPO torque, Lumentum offers roughly 2.3x better exposure than Tower.

## The VCSEL CPO Call Option at Coherent

Coherent loves to push VCSEL because they’re the best at it. Unfortunately VCSEL faces reliability issues at higher lane speeds which means VCSEL 1.6T transceivers (which uses 200G) are mostly not viable. However, for CPO, it is possible to use a 100G per lane VCSEL approach with massive parallelism.

The VCSEL CPO architecture has genuine advantages over SiPho, the consensus/incumbent solution, at ultra-short reach. VCSELs consume roughly 1 pJ/bit versus 5-10+ pJ/bit for SiPho-based solutions. They’re dramatically cheaper to manufacture and wafer-test. They don’t require the complex coupling alignment that SiPho demands. And they don’t need an external laser source at all as the VCSEL *is* the transmitter. For massively parallel connections at distances under 5 meters like chip-to-chip or intra-tray the brute-force simplicity of VCSEL CPO is compelling: you sacrifice per-lane data rate (100G vs. 200G+ for SiPho) but compensate with sheer lane count at a fraction of the power and cost per bit.

Coherent confirmed on their latest earnings call that 200G VCSEL-based 1.6T transceivers will begin ramping in the second half of calendar 2026, and they have “engagements across multiple customers for both indium phosphide and 200 gig VCSEL-based solutions for CPO and MPO applications.”

The VCSEL CPO thesis at Coherent is a genuine call option on an alternative architecture that could coexist alongside SiPho CPO — capturing the ultra-short-reach, power-constrained tier of the market while SiPho handles everything from rack-scale upward. If it materializes, it’s incremental TAM for Coherent at high margins with technology barriers that are difficult for others to replicate. It’s not the base case for the CPO transition, but it’s not nothing either.