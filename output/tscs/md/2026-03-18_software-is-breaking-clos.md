The average software loan bids at 86 cents. The median bids at 95. If you stopped at the average, you would think the sector is sick. If you stopped at the median, you would think it is fine. Both are wrong, and the 8.5-point gap between them is the single most important number in credit markets right now.

I pulled 227 active software term loans from the Bloomberg Terminal. Every institutional-scale credit that matters for CLO and BDC portfolios, the near-complete universe. 72 instruments bid above 95: Oracle, SS&C, business as usual. 34 bid below 80. Fifteen of those below 50. SonicWall at 30 cents. The distribution is not a bell curve. It is two peaks with a valley in the middle, and the valley is where capital goes to die.

[![](https://substackcdn.com/image/fetch/$s_!1k5H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fd5864e-f61d-418e-b17e-0ea6dafd640e_2112x1183.png)](https://substackcdn.com/image/fetch/$s_!1k5H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fd5864e-f61d-418e-b17e-0ea6dafd640e_2112x1183.png)

But the traded credits are not the scary part. 66 of the 227 instruments have no observable bid at all. No dealer making a market. No Bloomberg composite. 29% of the software loan universe is operating in the dark, and the composition is not random: 81% of PIK-TERM instruments and 83% of unitranches have no price. These are the credits held by BDCs marking to model, paying cash dividends on phantom income, with no secondary trade to confirm or contradict the marks. Names you would recognise (Zendesk, Hyland, Alteryx, Squarespace, CoreWeave), billions in outstanding debt, and no market-based price.

In [Don't Short SaaS](https://open.substack.com/pub/tscsw/p/dont-short-saas?r=203zi2&utm_campaign=post&utm_medium=web) I argued that the "AI kills SaaS" narrative was wrong, that the real divide was between a Fortress Zone of entrenched platforms with 97%+ gross retention and a Dead Zone of commoditised tools already losing altitude. In [Private Credit Is Eating Itself](https://open.substack.com/pub/tscsw/p/dont-short-saas?r=203zi2&utm_campaign=post&utm_medium=web) I mapped the mechanism: a self-reinforcing cycle where markdowns in one portfolio mechanically propagate to every other portfolio holding the same credit, amplified by CLO overcollateralisation tests and BDC dividend obligations. In [Private Credit Is Lying to You](https://open.substack.com/pub/tscsw/p/private-credit-is-lying-to-you?r=203zi2&utm_campaign=post&utm_medium=web) I showed where the illusion is most acute: PIK instruments paying phantom income, unitranches with no secondary market, and managers marking to model because no observable trade exists to mark against.

This piece does what the first two promised. It opens the Bloomberg Terminal and shows you the wiring diagram: the CUSIP-level proof that 37 CLO managers hold positions across the same 15 distressed credits simultaneously, the maturity cliff that forces 48 instruments into a binary refinance-or-restructure outcome by 2028, the 28-point price cliff between B-minus and CCC+ that turns a single-notch downgrade into a portfolio event, the EU CLO contagion channel I did not expect to find, and the 126-percentage-point NAV gap between the best and worst BDC manager.

Every chart and table is built from Bloomberg Terminal data. The computed average bid matches the Bloomberg-reported average exactly. This is, to my knowledge, the most comprehensive public analysis of the software leveraged loan market. The dataset, the overlap network, the positioning framework, and the instrument-level evidence are below.

**Subscribe to TSCS to read the full analysis. Paid subscribers get access to the complete 227-loan dataset, the CLO holder overlap map, the BDC quality spectrum, and the positioning framework I am using to build into Fortress Zone names ahead of Q1 earnings. If you manage capital with software credit exposure, this is the piece your risk committee will wish they had read in March.**

Subscribed

## **The Number That Captures Everything**

Split the 161 software term loans with an observable bid into two piles. Pile one: 72 instruments, 45% of the universe, bidding above 95 cents. Oracle at 99.75. SS&C at 99.63. Business as usual, coupon clipping, nothing to see. Pile two: 34 instruments bidding below 80. Fifteen of those below 50. Optiv at 41 (pre its mid-March Amend & Extend, which extended maturities to 2028/2029 with near-unanimous creditor support, expect this to re-rate). SonicWall at 30. Redstone at 40.

Not “under pressure.” Not “experiencing headwinds.” Zeros with a pulse, and in Optiv’s case, the maturity cliff forced exactly the binary outcome Section 3 predicts: restructure or refinance. There was no third option.

And in the middle? Almost nothing. 23 names between 90 and 95, 32 between 80 and 90, and 34 below 80. The tails dominate: the top and bottom buckets together hold 106 of 161 instruments, two-thirds of the observable universe, while the entire 80-to-95 zone holds the remaining third. The distribution is bimodal, not bell-shaped. The valley between the peaks is shallower than a pure binary sort would imply, but the weight sits at the extremes, and the middle is thin enough that migration in either direction moves the aggregate numbers fast.

The arithmetic mean across the whole universe is 86.46. The median is 95.00. If you stopped at the average, you would think software credit is sick. If you stopped at the median, you would think it is fine. Both are wrong. The average is being dragged down by a small number of names carrying hundreds of millions in outstanding debt across overlapping CLO and BDC portfolios, each one a marking event that cascades through every structure holding the same CUSIP. The median is being held up by a performing core that does not need the distressed tail to recover, but cannot fully insulate itself from the contagion mechanics I mapped in Part 2.

That 8.5-point gap between the mean and the median is the K-shape expressed as a single statistic. Not a sector-wide default wave. Not a healthy market with a few problem children. A bifurcation so clean you could teach a graduate seminar with it, except the tuition is funded by LP capital and the case study is still being written.

Meanwhile, 66 of the 227 instruments in the universe have no observable bid at all. We will get to those. They are worse.

[![](https://substackcdn.com/image/fetch/$s_!fKC2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F456f0be4-8d42-42d0-baba-77d2d030b5b8_1405x705.png)](https://substackcdn.com/image/fetch/$s_!fKC2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F456f0be4-8d42-42d0-baba-77d2d030b5b8_1405x705.png)

[![](https://substackcdn.com/image/fetch/$s_!BmsA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f066b14-0357-45a5-840c-393b9dd66857_1405x573.png)](https://substackcdn.com/image/fetch/$s_!BmsA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f066b14-0357-45a5-840c-393b9dd66857_1405x573.png)

[![](https://substackcdn.com/image/fetch/$s_!Pn-q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d069e18-475b-4419-a497-8fed37118757_1405x552.png)](https://substackcdn.com/image/fetch/$s_!Pn-q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d069e18-475b-4419-a497-8fed37118757_1405x552.png)

## **Section 1: The Universe**

The dataset is 227 active USD-denominated software term loans captured via Bloomberg SRCH (Fixed Income), filtered by BICS classification (Application Software, Infrastructure Software) with amount outstanding of $500 million or above. This is not a sample. It is the near-complete universe of institutional software leveraged loans that matter for CLO and BDC portfolios.

Of those 227, 161 have observable bid prices. The remaining 66 are dark: no dealer making a market, or trading so infrequently that Bloomberg does not display a composite bid.

PIK-TERM and unitranche structures are heavily overrepresented in the dark universe: 81% of PIK-TERM instruments and 83% of unitranches have no observable bid, far above the no-bid rate for standard syndicated terms. Together they account for roughly half the 66 no-bid instruments, but the overrepresentation within their own structure types is what matters analytically. These are the instruments where the “illusion of valuation” from Part 2 is most acute.

A few landmarks. At the top, Oracle bids at 99.75 with a 125 bps spread. At the bottom, BYJU’s Alpha sits at 5.63, effectively a zero-recovery credit. X.AI trades at 103.25 (above par) with a 725 bps spread, the widest spread in the entire universe on an above-par instrument. The market will pay a premium for software exposure when the name carries sufficient conviction, even at an eye-watering spread. That is the Fortress Zone thesis expressed in credit. It proves the market can discriminate. It is choosing not to for the rest of the sector, because the plumbing does not reward discrimination.

Average spread across the universe: 417 basis points. Average tranche size: $1.55 billion. Average amount outstanding: $1.76 billion. These are institutional-scale credits sitting inside the largest CLO and BDC portfolios in the world.

## **Section 2: The K-Shape in Credit**

The bid distribution tells the story more precisely than any summary statistic.

The bid distribution from the open tells you the shape. This section tells you why the shape is dangerous.

[![](https://substackcdn.com/image/fetch/$s_!zB3N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda82e13c-bc76-45b1-ba60-7b90d2670bcc_1405x456.png)](https://substackcdn.com/image/fetch/$s_!zB3N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda82e13c-bc76-45b1-ba60-7b90d2670bcc_1405x456.png)

The Fortress Zone names (Oracle, SS&C, Gen Digital, Clearwater Analytics, all bidding 99+) coexist in the same index, the same CLO pools, and often the same manager portfolios as the Dead Zone names (Optiv at 41, SonicWall at 30, Redstone at 40).

[![](https://substackcdn.com/image/fetch/$s_!5r5w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e24b33c-5fe4-41af-bf81-59ee9b00c6b1_1405x782.png)](https://substackcdn.com/image/fetch/$s_!5r5w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e24b33c-5fe4-41af-bf81-59ee9b00c6b1_1405x782.png)

Here is why that coexistence matters mechanically. When a CLO manager holds both in the same portfolio, the Barracuda markdown hits the portfolio’s weighted average bid, pressures the OC test, and can force the manager to sell, not the distressed name nobody wants, but the performing credit with actual liquidity. The full mechanics of that transmission are in Section 5. The point here is simpler: the performing half does not need the distressed half to recover. The distressed half needs the performing half to not get dragged down with it. That asymmetry is the entire risk.

## **Section 3: The Maturity Cliff**

210 of 227 instruments have identifiable maturity dates. The concentration is stark.

2028 is the cliff. 48 instruments mature that year, more than any other, and 14 are already trading below 80. These borrowers need to refinance into a market where the average software loan bids at 86 cents and 31% of distressed volume in the LSTA index is software. Every failed refinancing becomes a new data point that reprices the entire sector lower.

2027 is the early warning. 12 instruments, 3 distressed, with names like Symplr (bid 70.25, maturing December 2027) and Planview (bid 77.13, maturing December 2027) approaching their refinancing windows already weakened. If Symplr cannot refinance its $1.2 billion term loan at or near par by mid-2027, that is not a Symplr problem. It is a data point that reprices every B-minus software credit maturing within 18 months.

[![](https://substackcdn.com/image/fetch/$s_!gKdC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faefef2d5-8444-459e-9762-3d88fd995fcb_1405x791.png)](https://substackcdn.com/image/fetch/$s_!gKdC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faefef2d5-8444-459e-9762-3d88fd995fcb_1405x791.png)

2031 and 2032 show 75 instruments with near-zero distress, predominantly post-refinancing vintages with longer runways, many originated in the 2024-2025 window when direct lenders were competing aggressively for deal flow. They have time. The 2027-2028 cohort does not.

The maturity wall interacts with the reflexive loop in a specific way. Each approaching maturity forces a binary outcome: refinance at or near par, or restructure. There is no “extend and pretend” option for a $1.5 billion syndicated term loan maturing in 18 months when the secondary bid is 70 cents. The sponsor injects equity, the lenders take a haircut, or the company files. Each outcome generates a new observable price that feeds back into the marking cycle for every other credit in the same rating bucket.

This is not a 2028 event. It is a 2026-2027 refinancing anxiety event that prices in 18 months early.

## **Section 4: The Quality Cliff**

The rating matrix reveals something the averages conceal: the deterioration from investment-grade-adjacent to deep distress is not gradual. It is a cliff.

Software loans rated BB or above average a bid of 93.8. B-rated loans average 90.1. The step down is 3.7 points. Manageable. Expected. The normal credit risk gradient.

Then you hit CCC+. Average bid: 61.06. The drop from B-minus (88.93) to CCC+ is 28 points.

[![](https://substackcdn.com/image/fetch/$s_!M7PY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F903d458b-3dcb-4fe5-abd0-2f7f851a1aa8_1405x787.png)](https://substackcdn.com/image/fetch/$s_!M7PY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F903d458b-3dcb-4fe5-abd0-2f7f851a1aa8_1405x787.png)

That is not a gradient. That is a regime change. It means that the difference between a B-minus credit and a CCC+ credit is the difference between a portfolio that passes its OC test and one that does not. The ratings agencies, specifically Moody’s and S&P, control the boundary, and a single-notch downgrade from B3/B-minus to Caa1/CCC+ mechanically reclassifies a loan from the “performing bucket” into the “CCC bucket” that most CLO indentures cap at 7.5% of the portfolio.

[![](https://substackcdn.com/image/fetch/$s_!hrLr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd389d25d-a802-4fdf-9c42-80ee5a4e7731_1405x710.png)](https://substackcdn.com/image/fetch/$s_!hrLr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd389d25d-a802-4fdf-9c42-80ee5a4e7731_1405x710.png)

The concentration of observable instruments is heaviest at B-minus (55 instruments) and B (32 instruments). These are the credits on the edge. A deterioration in any one of the fundamental drivers (revenue growth deceleration, covenant amendment, sponsor equity call missed) that triggers a one-notch downgrade does not just impair that credit. It pushes the CLO’s CCC concentration closer to the cap, which haircuts the excess in the OC test, which diverts cash from equity, which pressures the manager to trade.

11 of 55 B-minus credits already bid below 80. That is a 20% distress rate within a rating category that is supposed to be performing. The market is front-running downgrades that the agencies have not yet issued.

## **Section 5: The Synchronous Marking Proof**

This is the section that either confirms or breaks the core mechanism from Part 2. The claim was specific: overlapping CLO and BDC holdings of the same distressed software credits create synchronous marking pressure, where a markdown in one portfolio mechanically propagates to every other portfolio holding the same CUSIP.

To test this, I pulled Bloomberg HDS (Holdings) data for 15 distressed software loan CUSIPs, identified every institutional holder, and mapped the overlap. The results are more concentrated than I expected.

[![](https://substackcdn.com/image/fetch/$s_!UH6e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2342531-d651-433e-b887-50936437c48f_1405x765.png)](https://substackcdn.com/image/fetch/$s_!UH6e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2342531-d651-433e-b887-50936437c48f_1405x765.png)

**37 CLO managers hold positions in four or more of these 15 distressed credits simultaneously.** The three most connected, Sound Point Capital, BlueMountain CLO, and Palmer Square Capital, each hold positions across 10 of the 15 names. Sound Point and BlueMountain overlap on 9 of their 10, meaning a markdown on any single credit in either portfolio generates correlated mark-to-market losses across both.

[![](https://substackcdn.com/image/fetch/$s_!MtZr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02292df5-94c0-4556-becc-0a7bc3d3324a_1405x783.png)](https://substackcdn.com/image/fetch/$s_!MtZr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02292df5-94c0-4556-becc-0a7bc3d3324a_1405x783.png)

I want to be precise about what this does and does not prove. It proves that the *structural conditions* for synchronous marking exist: the same managers hold the same distressed credits, so a price decline in one is arithmetically a price decline in all portfolios holding it. It does not prove that managers are marking simultaneously (they mark on their own quarterly cycles), nor does it prove forced selling (discretionary trading is manager-specific). What it proves is the *channel* through which correlated losses propagate. The wiring diagram, not the current flowing through it.

But the wiring diagram is damning enough.

I want to be clear about what is missing: I have not identified a confirmed OC test breach leading to forced liquidation in a software-heavy CLO tranche. That would be the smoking gun. What I have is the loaded weapon, the structural conditions that make synchronous marking pressure not just possible but arithmetically inevitable once the trigger fires. The Q1 reporting cycle, specifically the CLO trustee reports due in May and June, is when we find out whether the current is flowing through the wiring or just waiting.

Take the 15 credits and look at the holder concentration:

**Cornerstone OnDemand (CSOD):** 23 multi-credit managers holding 49.8% of outstanding. Bid: 76.56. This is the name from Part 2 whose $5.2 billion LBO is buckling under the same AI substitution pressure that killed Pluralsight. Nearly half the outstanding debt is held by managers who also hold at least three other distressed software credits. A markdown here cascades across 23 portfolios.

**Qlik (QLIK):** 22 multi-credit managers, 36.5% held. Bid: 76.19. Blackstone Liquid Credit holds 3.81%, Madison Park Funding 3.75%, AGL CLO 2.88%. The top 10 holders alone control over 25% of the outstanding. When Blackstone marks this down, every other holder’s risk committee notices.

**Barracuda Networks (CUDA):** 15 multi-credit managers, 41.6% held. Bid: 57.81. Palmer Square holds 7.73%, Shenkman 6.25%, Golub 5.85%. Three managers hold nearly 20% between them. This is not a diversified holder base. This is a concentrated bet by a handful of CLO platforms.

**AQA Acquisition (SMABEA):** The most concentrated of all. 85.95% of the tracked outstanding is held by the top holders in the Bloomberg HDS data. Golub Capital CLO alone holds 16.87%. Madison Park Funding holds 16.02%. Apidos CLO holds 9.03%. Three managers control 42% of the outstanding. If Golub marks this down, it is not a Golub problem. It is a problem for every structure where Golub’s marking establishes the observable price.

**Skillsoft (SKIL):** Prudential Financial holds 15.12%. Madison Park 8.01%. Silver Point 6.83%. Bain Capital 6.48%. The top four holders control 36% of the outstanding on a credit bidding at 48 cents with a distressed exit from a prior restructuring already in the rearview mirror. This is the name where Pluralsight’s debt-for-equity template is most directly applicable. The lenders may end up owning the company. Again.

The overlap network has a specific topology. It is not random. The most connected managers (Sound Point, BlueMountain, Palmer Square, Carlyle, CBAM, BlackRock, Blackstone Liquid Credit, Trinitas) are disproportionately CLO platforms that buy across the entire syndicated loan market. They do not concentrate into software by choice. They concentrate into software because software is 16% of the leveraged loan index, and any diversified CLO portfolio will mechanically hold a large software book.

**This is the key insight: the overlap is structural, not discretionary.** These managers did not take a collective bet on software. They built diversified portfolios that, because of the sector’s outsized share of the loan market, ended up being correlated across the exact names now under stress. Diversification became correlation, not because of bad risk management, but because the index itself is concentrated.

[![](https://substackcdn.com/image/fetch/$s_!iqNg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5472fd5-ffb9-44a6-9312-005e1bb32371_1405x795.png)](https://substackcdn.com/image/fetch/$s_!iqNg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5472fd5-ffb9-44a6-9312-005e1bb32371_1405x795.png)

[![](https://substackcdn.com/image/fetch/$s_!O6VO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2ba6324-6149-4605-80d9-ac71ecb726d3_1405x345.png)](https://substackcdn.com/image/fetch/$s_!O6VO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2ba6324-6149-4605-80d9-ac71ecb726d3_1405x345.png)

The synchronous marking pressure operates through three channels:

**Channel 1: Observable price contagion.** When any one of the 37 overlapping managers sells a distressed credit in the secondary market, that trade establishes an observable bid that Bloomberg captures. Every other holder of the same CUSIP now has a market price that their auditors and risk committees can reference. The manager may prefer to hold, but the observable bid constrains how generously they can mark. If Palmer Square sells CUDA at 57, Golub cannot mark CUDA at 75 without explaining the discrepancy.

**Channel 2: CLO OC test arithmetic.** When a credit gets downgraded to CCC, it enters the haircut bucket. If the CLO already has 7% CCC exposure (against a 7.5% cap), one more downgrade pushes the excess into the OC numerator at market value rather than par. A credit that was counted at 100 is now counted at 57. The OC test deteriorates by the difference, which can breach the junior trigger and divert cash from equity. Across 37 managers holding 4+ of the same credits, a single downgrade wave ripples through dozens of OC tests simultaneously.

**Channel 3: Risk committee contagion.** When TCPC reported an 81% average write-down on six technology-adjacent credits (detailed in Part 2), risk committees across the BDC and CLO complex initiated reviews of their own software-heavy books. This is not mechanical. It is behavioural. But it is no less real. Conservative marking begets conservative marking, because no risk officer wants to be the one who missed the write-down that their peer already took.

## **Section 6: The BDC Quality Spectrum**

The BDC universe data reveals a 126-percentage-point spread between the best and worst managers, and the spread itself is the market pricing the reflexive loop in real time.

Main Street Capital trades at a 68% *premium* to NAV. Prospect Capital trades at a 58% *discount*. That gap is not noise. It is the public equity market doing exactly what the credit market cannot: differentiating between managers based on portfolio quality, vintage risk, and the credibility of reported NAV.

The spectrum sorts into three tiers.

**Tier 1: Premium to NAV (5 names).** Main Street Capital (+68%), Capital Southwest (+32%), Hercules Capital (+21%), Sixth Street (+9%), Trinity Capital (+9%). These are the managers the market trusts. Average ROE: 13.8%. Average dividend yield: 10.2%. They earn their premiums through consistent return generation and conservative underwriting. Main Street at 1.68x book with 17% ROE is the market’s statement that this manager’s marks are real.

**Tier 2: Moderate discount (15 names, discount 3-28%).** This is the broad middle: ARCC, GBDC, BXSL, OBDC, KBDC, GSBD, and others. Discounts range from 3% (Gladstone Investment) to 28% (Bain Capital Specialty). The market believes these managers are competent but is applying a sector-wide discount for software exposure, rate sensitivity, and the general cloud of uncertainty over private credit. ARCC at a 7% discount with 1.2% non-accruals and $13.3 billion market cap is the cleanest large-cap expression of private credit quality. BXSL at 8% discount with Blackstone’s origination platform behind it is the closest thing to a “safe” software-exposed BDC.

**Tier 3: Severe discount (6 names, discount 31-58%).** NMFC (31%), OCSL (31%), FSK (52%), CION (51%), TCPC (49%), PSEC (58%). These are the names where the market is telling you the NAV is not real. FSK at 0.48x book with 0.2% ROE and 19% dividend yield is the market pricing in a dividend cut that has not yet been announced (though the distribution has already been reduced roughly 31% from its peak). TCPC at 0.51x book with negative 12.9% ROE is the KBRA-downgraded wreckage from Part 2, where six credits accounted for two-thirds of the quarterly NAV decline, destroying roughly 12.7% of total book value in a single quarter.

[![](https://substackcdn.com/image/fetch/$s_!beQT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9981926c-7871-4a77-bfce-e099121e6e75_1405x723.png)](https://substackcdn.com/image/fetch/$s_!beQT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9981926c-7871-4a77-bfce-e099121e6e75_1405x723.png)

[![](https://substackcdn.com/image/fetch/$s_!16R9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e96da21-42b7-498f-8a1d-ac2e3112927c_1405x616.png)](https://substackcdn.com/image/fetch/$s_!16R9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e96da21-42b7-498f-8a1d-ac2e3112927c_1405x616.png)

**The dividend yield inversion tells you everything.** The five BDCs trading at premiums average 10.2% dividend yield. The six trading at severe discounts average 17.5%. In any other income asset class, a higher yield means higher return. In BDCs, it means the market is pricing a cut that management has not yet conceded. PSEC at 20.5% yield, FSK at 19.0%, TCPC at 18.8%: these are not income opportunities. They are countdown timers.

[![](https://substackcdn.com/image/fetch/$s_!6vhj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2eb7a95-d402-456f-b84c-627316630160_1405x450.png)](https://substackcdn.com/image/fetch/$s_!6vhj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2eb7a95-d402-456f-b84c-627316630160_1405x450.png)

The BDC data also reveals something about the carry breakeven from Part 2. At current prices, the Tier 3 BDCs are already trading at levels that imply 30-50% permanent NAV impairment. If you buy FSK at 48 cents on book, you are betting that at least 48% of the NAV is real and that the remaining portfolio generates enough carry to offset further markdowns. The carry breakeven math from Part 2 (net yield of 6.5%, breakeven at 28% cumulative defaults with 30-cent recoveries) applies to the portfolio, not the stock price. The stock price has already priced in a scenario worse than the base case. The question for FSK, TCPC, and PSEC is not “will the carry hold?” It is “how much of the reported NAV is fiction?”

I do not have the answer to that question yet. The BDC-by-BDC software concentration data that would let me test it directly requires Schedule of Investments sector breakdowns that are not in the Bloomberg DES Ratios tab. I will pull this from the most recent 10-Qs and publish the scatter plot in a follow-up. The directional claim, that the Tier 3 discounts correlate with software exposure and vintage risk, is well-supported by what I can observe (TCPC’s six write-downs were all technology-adjacent, 2021-vintage credits). The precise correlation awaits the data.

## **Section 7: The EU Contagion Channel**

Technology accounts for 12% of EU CLO collateral, roughly €29.6 billion across €247 billion in total holdings as of Q4 2025. Not dominant. Not ignorable. The pricing divergence is what matters: as of February 2026, software loans within EU CLO collateral are priced at approximately 90 versus 96 for non-software. That 6-point gap did not exist 18 months ago. It opened in October 2025 and accelerated into 2026. The same credits appear in both markets via cross-border syndication, so the reflexive loop does not stop at the Atlantic.

[![](https://substackcdn.com/image/fetch/$s_!I3RL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb86203db-147c-42fe-8e5a-7acb65cd8651_1405x771.png)](https://substackcdn.com/image/fetch/$s_!I3RL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb86203db-147c-42fe-8e5a-7acb65cd8651_1405x771.png)

[![](https://substackcdn.com/image/fetch/$s_!289C!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F814e0b48-7d28-435c-97de-00060dad8bed_1405x629.png)](https://substackcdn.com/image/fetch/$s_!289C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F814e0b48-7d28-435c-97de-00060dad8bed_1405x629.png)

The fundamental exposure appears less severe than the market reaction. A Bloomberg Intelligence analyst decomposing the EU data into actual impairment versus headline exposure arrived at fairly low implied loss rates. The plumbing is transmitting stress cross-border. The fundamentals, for the Fortress Zone names, do not justify the transmission. I do not have the cross-border CUSIP overlap data to map this channel with the same precision as Section 5, so I am flagging it as a monitoring signal rather than a confirmed transmission mechanism. If the gap widens past 8 points or EU CLO managers begin reporting software-specific OC test pressure, it gets promoted to a full section in the next update.

[![](https://substackcdn.com/image/fetch/$s_!qPMV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d414870-3a75-4d14-96c1-7d62bfc68a16_1405x789.png)](https://substackcdn.com/image/fetch/$s_!qPMV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d414870-3a75-4d14-96c1-7d62bfc68a16_1405x789.png)

## **Section 8: The Opacity Layer**

I want to spend a moment on the 66 instruments with no observable bid, because this is where the analytical consensus is weakest and the risk is highest.

Of the 227 instruments in the universe, 66 have no bid displayed on Bloomberg. That is 29% of the market operating in the dark.

The composition of the dark universe is not random, though the concentration pattern is subtler than a headline number suggests. PIK-TERM and unitranche structures together account for roughly half the 66 no-bid instruments, not an outright majority, but their no-bid rates within their own structure types are extreme:

17 of 21 PIK-TERM instruments have no bid (81%). 15 of 18 unitranche structures have no bid (83%).

A necessary distinction before we go further. Some of these instruments have no bid because something is wrong. Others have no bid because nothing is traded. A $3 billion unitranche held by a single direct lender was never syndicated, has no secondary market, and will never show a Bloomberg composite bid. That is the product working as designed, not evidence of mismarking. The concern is not illiquidity per se. The concern is illiquidity combined with observable credit deterioration: revenue deceleration, covenant amendments, missed sponsor equity calls, the kind of fundamental signals that, in the syndicated market, would already be reflected in a lower bid. In the unitranche and PIK universe, those signals exist but have no price to attach to. The manager marks to model. The model marks to assumptions. The assumptions have not been stress-tested by a market that does not exist.

[![](https://substackcdn.com/image/fetch/$s_!_dtd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92380887-3d90-4ac8-87f7-a19a4baee6c0_1403x789.png)](https://substackcdn.com/image/fetch/$s_!_dtd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92380887-3d90-4ac8-87f7-a19a4baee6c0_1403x789.png)

PIK loans, as I detailed in Part 2, are the instruments where the borrower has stopped paying cash interest and is instead accruing additional debt as payment. The BDC is legally required (under Subchapter M of the IRS code) to distribute 90% of taxable income, which includes PIK interest, meaning the BDC pays cash dividends on phantom income funded from sources other than the borrower. The cash register says “empty.” The distribution cheque clears anyway.

The unitranche structures are the domain of direct lenders, typically held by a single fund or small club, with no secondary market and no price discovery mechanism beyond the manager’s own quarterly mark. When Blue Owl or Golub holds a $1 billion unitranche and marks it at 98 cents, there is no observable trade to confirm or contradict that mark. The auditor can stress-test the assumptions. The auditor cannot point to a secondary bid.

This is not an accusation of fraud. It is a structural observation about the limits of fair-value accounting in illiquid markets. The 29% of the universe with no bid is where the “illusion of valuation” from Part 2 is most acute. If even a fraction of these no-bid instruments are materially overmarked, the next round of 10-Q filings will reveal write-downs that are currently invisible.

The names are worth listing. Zendesk (PIK-TERM, $2.87 billion outstanding, no bid). Hyland Software ($3.25 billion unitranche, no bid). Alteryx ($1.8 billion PIK-TERM, no bid). Squarespace ($2.1 billion term, no bid). CoreWeave ($2.5 billion term, no bid). Diligent Corp ($552 million PIK-TERM, no bid). These are not obscure micro-cap credits. These are household names in technology, held across the largest private credit portfolios, with billions in outstanding debt and no market-based price.

**The market knows what the traded credits are worth. It does not know what the untraded credits are worth. The 66 instruments in the dark are the known unknown of this cycle.**

[![](https://substackcdn.com/image/fetch/$s_!_Xk1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0312b095-60ca-48cc-a177-255c0966db74_1403x786.png)](https://substackcdn.com/image/fetch/$s_!_Xk1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0312b095-60ca-48cc-a177-255c0966db74_1403x786.png)

## **Section 9: The Spread-Price Convexity**

One analytical dimension that deserves explicit discussion: the relationship between loan spread and bid price is not linear. It is convex, and the convexity is the mathematical expression of the reflexive loop.

[![](https://substackcdn.com/image/fetch/$s_!lRMG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cb1ea4b-c4a5-4779-b810-901506efc5c2_1405x795.png)](https://substackcdn.com/image/fetch/$s_!lRMG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1cb1ea4b-c4a5-4779-b810-901506efc5c2_1405x795.png)

At the performing end, Oracle trades at 99.75 with a 125 bps spread. SS&C at 99.63 with 200 bps. Gen Digital at 99.25 with 175 bps. The relationship between spread and price is gentle: a 75 bps increase in spread corresponds to roughly 0.5 points of price discount. Normal credit risk pricing.

At the distressed end, the relationship inverts and steepens. Barracuda Networks: 450 bps spread, 57.81 bid. Ivanti: 475 bps, 67.59. Cast & Crew: 375 bps, 40.38. Optiv: 525 bps, 41.13 (pre mid-March A&E; expect re-rating as the extended maturity reprices the refinancing probability). The per-basis-point price impact is an order of magnitude larger in the distressed zone.

This convexity is not just a statistical artefact. It is the reflexive loop expressed as a price function. In the performing zone, a spread widening reflects credit risk incrementally. In the distressed zone, a spread widening reflects something qualitatively different: the market’s assessment that the borrower may not be able to refinance, that the sponsor may not inject equity, that the loan may need to be restructured. The price is no longer discounting the coupon stream. It is discounting a probability-weighted recovery scenario.

[![](https://substackcdn.com/image/fetch/$s_!oJO3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F104569e0-43f4-43ad-ba5d-d7b6d038b0f5_1405x627.png)](https://substackcdn.com/image/fetch/$s_!oJO3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F104569e0-43f4-43ad-ba5d-d7b6d038b0f5_1405x627.png)

The convexity means that lumping them into a single “software loan” category and computing an average is like averaging the temperature in a room where half is on fire and half is air-conditioned. The average is meaningless. The distribution is everything.

And the convexity has a reflexive property: as a credit migrates from the performing zone into the distressed zone, the price impact per unit of fundamental deterioration accelerates. A B-minus credit that gets downgraded to CCC+ does not lose 3 points. It loses 28. That non-linearity is why the reflexive loop runs faster once it starts: each downgrade triggers a price collapse that is disproportionate to the fundamental change, which triggers further selling, which drives further price collapse.

## **Section 10: The Fundamental Bridge**

The credit data above tells you what the plumbing is doing. This section tells you whether the plumbing is right.

A correction first. In Part 2, I cited “Fortress Zone NRR of 120-130%” as a distinguishing characteristic. That was imprecise. CrowdStrike is the only Fortress Zone name that discloses a clean NRR figure: 115%, improving sequentially, with 97% gross retention. ServiceNow, Veeva, and Guidewire do not publish NRR. Their expansion dynamics strongly imply figures above 115%, but I am not going to fabricate a number to fill a gap in the framework. The correction matters. The conclusion does not change. Here is why.

The divergence is cleaner when you stop trying to force it through a single metric and let the full picture speak. But it is also less binary than Parts 1 and 2 implied, and I want to be honest about that.

Start with gross retention, because that is where the moat either exists or does not. Guidewire is the extreme case: Jeff Cooper disclosed this quarter that over five years, zero InsuranceSuite customers above $1M ARR have voluntarily left. Not low churn. Zero churn. CrowdStrike sits at 97%. ServiceNow at 98%. When your gross retention is 97-99%, your NRR has a floor. Your revenue growth has a floor. Your pricing power has a floor. Everything downstream is a question of degree, not survival.

At the other end, Five9 implies gross retention below 95%. HubSpot sits in the high 80s. When your gross retention is in the high 80s, no amount of upsell fixes the leaking bucket. You are running to stand still, and AI substitution only accelerates the leak.

[![](https://substackcdn.com/image/fetch/$s_!5X_w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97801d00-a403-45bd-8345-2613fce6dc15_1403x788.png)](https://substackcdn.com/image/fetch/$s_!5X_w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97801d00-a403-45bd-8345-2613fce6dc15_1403x788.png)

Revenue growth maps onto this. CrowdStrike 23% ARR, ServiceNow 20-21% subscription, Guidewire 22% ARR, Veeva 16%. Call that cluster roughly 20% average. Against that: Five9 at 8%, Freshworks at 14-15%. Clear Dead Zone.

A handful of names do not sort cleanly. HubSpot at 16-18% revenue growth with gross retention in the high 80s, Freshworks at 14-15%, Datadog somewhere in between. I am not going to force them into a framework the data does not support. They deserve their own analysis, and I will publish it separately. For now, the sorting that is clean: Fortress Zone (97%+ gross retention, 20%+ growth, expanding margins): CrowdStrike, ServiceNow, Guidewire, Veeva. Dead Zone (sub-95% gross retention, sub-10% growth, or AI substitution already visible in the pipeline): Five9, Pluralsight, the LBO casualties from the CUSIP data above.

[![](https://substackcdn.com/image/fetch/$s_!hIcD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa046860e-b5d5-4cc1-a517-680b8e84b96f_1405x631.png)](https://substackcdn.com/image/fetch/$s_!hIcD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa046860e-b5d5-4cc1-a517-680b8e84b96f_1405x631.png)

Operating margins complete the picture for the names where the sorting is clean. Veeva at 45% non-GAAP. ServiceNow above 30%. CrowdStrike expanding toward 25%+ FCF margins. The Fortress Zone prints cash. The Dead Zone spends it defending market position against AI substitution that has not yet shown up in the retention data but is already showing up in the narrative.

[![](https://substackcdn.com/image/fetch/$s_!eajH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5156665-97cf-414e-9463-900e94a235db_1403x788.png)](https://substackcdn.com/image/fetch/$s_!eajH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5156665-97cf-414e-9463-900e94a235db_1403x788.png)

And that is the critical timing caveat. Every figure above reflects customer behaviour through Q4 2025. NRR is a trailing 12-month metric. The crisis entered the numerator approximately yesterday. That makes Q1 2026 earnings the single most important data point for the entire three-part thesis. If Fortress Zone retention holds through the panic, the ‘AI kills software’ narrative breaks against the data. If it compresses, I will tell you that too. The Fortress Zone entered this crisis pulling away on every measurable dimension. The Dead Zone entered it already losing altitude. Q1 earnings will tell us whether the grey zone collapses into the Dead Zone or holds.

[![](https://substackcdn.com/image/fetch/$s_!eWTZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0867a884-091f-4803-8a90-fec1ff42baaf_1406x786.png)](https://substackcdn.com/image/fetch/$s_!eWTZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0867a884-091f-4803-8a90-fec1ff42baaf_1406x786.png)

## **Section 11: What the Data Confirms and What It Revises**

I built a deliberately contrarian framework across three pieces. Sections 1 through 10 deliver the confirmations. I am not going to re-summarise evidence you just read. What matters here is what the data forced me to change.

**Revision 1: The opacity risk is larger than I initially framed.**

In Part 2, I focused on PIK as a borrower-level income illusion. The data reveals a market-structure dimension I underweighted: 29% of the software loan universe has no observable bid. The no-bid instruments are overwhelmingly PIK and unitranche, precisely the structures held by direct lenders and BDCs that mark to model rather than mark to market. The next wave of write-downs will not come from the credits already trading at 45 cents. Those losses are recognised. It will come from the credits currently marked at 98 on manager books because no secondary trade has forced a re-evaluation.

This adds a fifth signal to the monitoring framework from Part 2. In addition to BIZD price action, BCRED redemption composition, bank behaviour, and the Proskauer default index:

**Signal 5: PIK and unitranche marking in Q1 10-Q filings (May-June 2026).** If three or more BDCs report material write-downs on PIK or unitranche instruments that were previously marked near par, the opacity layer is cracking. That is the TCPC dynamic (81% average write-down on credits marked near par the prior quarter) repeating across the broader market.

[![](https://substackcdn.com/image/fetch/$s_!Y30_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0c59c65-9c94-4640-9903-ef0b3be28672_1403x789.png)](https://substackcdn.com/image/fetch/$s_!Y30_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0c59c65-9c94-4640-9903-ef0b3be28672_1403x789.png)

**Revision 2: The carry breakeven is an upper bound, not a central estimate.**

Part 2’s carry breakeven assumed a stable performing book. The data shows that 20% of B-minus credits, the largest rating bucket, already bid below 80. If the distressed tail continues to grow, the carry on the performing 80% has to absorb not just losses on existing distressed credits but the migration of currently-performing credits into distress. The static breakeven underestimates this migration risk. I do not have the data for a dynamic simulation, but the Part 2 breakeven (net yield of 6.5%, breakeven at 28% cumulative defaults with 30-cent recoveries) should be treated as the ceiling on the cushion, not the midpoint.

[![](https://substackcdn.com/image/fetch/$s_!s6EI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9aff801-dd9e-440f-89a2-4a027050fbd9_1405x781.png)](https://substackcdn.com/image/fetch/$s_!s6EI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9aff801-dd9e-440f-89a2-4a027050fbd9_1405x781.png)

[![](https://substackcdn.com/image/fetch/$s_!wYOA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5297c54a-c398-4477-a3e0-7273e5f08d47_1405x722.png)](https://substackcdn.com/image/fetch/$s_!wYOA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5297c54a-c398-4477-a3e0-7273e5f08d47_1405x722.png)

[![](https://substackcdn.com/image/fetch/$s_!cT7D!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb76c8ffc-cb13-4136-a88a-eabdc2b80724_1405x638.png)](https://substackcdn.com/image/fetch/$s_!cT7D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb76c8ffc-cb13-4136-a88a-eabdc2b80724_1405x638.png)

## **Positioning Implications**

The data does not change the positioning framework from Part 2. It sharpens it.

**For the Fortress Zone equity thesis:** The loan-level data confirms that the performing core of the software market is intact (72 instruments above 95, including the names most closely associated with Fortress Zone fundamentals). The retention data, while messier than a clean NRR comparison would suggest, shows the Fortress Zone entering the crisis from a position of strength across every measurable dimension. The selloff in Fortress Zone equities remains predominantly narrative-driven, not flow-driven, because the direct mechanical channel from credit liquidation to equity selling is zero (as I sized in Part 2).

I am building positions in ServiceNow, CrowdStrike, and Veeva at current levels. But I am not full-sized, and I will not be until Q1 earnings confirm what the trailing data implies. The setup is the best I have seen in Fortress Zone names since the 2022 rate shock. The confirmation has not arrived yet.

Sizing before confirmation is not conviction. It is impatience. The analysis above maps the structural conditions for the reflexive loop but does not confirm that the loop has fired. The allocation reflects that distinction.

[![](https://substackcdn.com/image/fetch/$s_!Ukqz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8787975-01d9-4cdc-aa15-722213674e2e_1403x672.png)](https://substackcdn.com/image/fetch/$s_!Ukqz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8787975-01d9-4cdc-aa15-722213674e2e_1403x672.png)

I would rather leave 10% of upside on the table by waiting for April than eat a 25% drawdown because retention compressed and I was already full.

**For the private credit thesis:** ARCC at a 7% discount with the lowest non-accrual rate in the sector and $5.5 billion in borrowing capacity remains the cleanest expression. The BDC quality spectrum data confirms that the market is already differentiating between managers. The opportunity is in Tier 2 names that get dragged toward Tier 3 discounts by sector contagion despite holding Tier 1 quality portfolios. Golub (GBDC) at a 15% discount, having already cut the dividend and partially reset expectations, is the name to watch. The cut itself may have been the clearing event.

**For risk management:** The opacity layer revision adds urgency to the Q1 10-Q monitoring cycle. If the PIK/unitranche markdowns materialise broadly, the adverse scenario from Part 2 moves from minority probability toward base case. The framework is simple: build toward full Fortress Zone equity exposure as Q1 retention data confirms, scale back hard if Signal 5 fires alongside any of the original four signals. If you need a number, I am at roughly 60% of target allocation today. April earnings get me to 80 or back to 40. Not 100. Not yet.

## **What Comes Next**

This piece delivers the instrument-level evidence I promised. One deliverable remains outstanding: BDC NAV discount versus software concentration (scatter plot, pending 10-Q Schedule of Investments data). It will be published as an update within two weeks.

The confirmation window opens in late April. ServiceNow reports Q1 around April 22-29, the first Fortress Zone read on enterprise retention through the SaaSpocalypse. CrowdStrike, Veeva, and Guidewire follow in late May and early June, each reporting quarters that end April 30. By mid-June, we will have the data to confirm or break the thesis. If the Fortress Zone names deliver retention stability or improvement through the SaaSpocalypse, the narrative breaks against the data. If they do not, I will tell you that too.

[![](https://substackcdn.com/image/fetch/$s_!_d05!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68877230-2454-4bec-b6a9-84f0a44decfb_1405x788.png)](https://substackcdn.com/image/fetch/$s_!_d05!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68877230-2454-4bec-b6a9-84f0a44decfb_1405x788.png)

The dataset underlying this piece is the most comprehensive public analysis I am aware of on the software leveraged loan market. Every number is from Bloomberg. Every chart is sourced. The data is yours. Use it.

---

*Source: Bloomberg Terminal (SRCH Fixed Income, DES Ratios, HDS, FA); Bloomberg Intelligence (BI CLOE, BI CLON, BI STRTE, Reto Bachmann); Capital IQ Pro (earnings transcripts, retention metrics). All loan data transcribed directly from terminal screenshots and validated. Computed average bid (86.46) matches Bloomberg-reported average. EU CLO chart values are approximate reads from published BI charts; text-based metrics are exact as reported. Retention figures sourced from Q4 2025/FQ4 2026 earnings transcripts and reflect trailing 12-month metrics pre-dating the February 2026 selloff. This analysis is for informational purposes only and does not constitute investment advice. The author holds positions in Fortress Zone names discussed in the accompanying piece.*