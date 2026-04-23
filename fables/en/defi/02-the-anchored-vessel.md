---
title: "The Anchored Vessel"
title_cn: "锚定之舟"
concept: "Modern Stablecoin Design (FX 2.0)"
concept_cn: "现代稳定币设计"
category: "defi"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/现代稳定币-fx-20-是如何构建的.md"
tags: [defi, stablecoin, fx-20, peg, collateral, algorithmic]
---

# The Anchored Vessel

> *A ship that does not dock at the pier, but anchors itself to the seabed with a chain. The shorter the chain, the steadier the ship—but when the waves grow too high, the chain may snap.*

## The Story

The merchants of Silver Sea Kingdom faced a chronic problem in cross-border trade: exchange rate volatility. Today, one bolt of silk was worth one hundred taels of silver; tomorrow, it might be one hundred twenty due to a war in a neighboring kingdom, and eighty the day after. This uncertainty made long-term contracts nearly impossible.

The Royal Advisor proposed issuing an "anchor coin"—a token whose value was permanently fixed at one hundred pounds of rice. Regardless of silver price fluctuations, one anchor coin would always be redeemable for one hundred pounds of rice. Merchants could use anchor coins to enter long-term contracts without worrying about silver price changes.

But the question was: who guarantees the anchor?

---

**First Generation: Full Collateral**

The Advisor's first scheme was simple: for every anchor coin issued, the Royal Treasury would hold one hundred pounds of actual rice. Anyone could redeem an anchor coin at the Treasury for one hundred pounds of rice at any time.

This was called the "full collateral" model. The anchor coin's credibility came entirely from the real rice in the Treasury. As long as the Treasury was not empty, the anchor coin was rock-solid.

But full collateral had a fatal cost: millions of pounds of rice in the Treasury sat idle most of the time, generating no returns. This rice could have been lent to farmers for planting or to merchants for trade—but now it was "locked up," solely to support the anchor coin's credibility.

The Treasury officials calculated: to issue one million anchor coins, the Treasury had to lock up one million pounds of rice, losing opportunity costs of approximately one hundred thousand taels of silver annually. Who would bear this cost? Either taxpayers subsidized it, or anchor coin users paid high fees.

---

**Second Generation: Partial Collateral**

Second-generation designers came up with a clever idea: you don't need full collateral, just "enough" collateral.

The approach: the Treasury would hold only fifty pounds of rice to back each anchor coin. If all coin holders came to redeem simultaneously, the Treasury would not have enough—but this was practically impossible. Under normal circumstances, only a small fraction of people would redeem, and fifty pounds was more than sufficient.

The remaining fifty pounds could be invested, lent, and generate yield. A portion of the investment returns would subsidize anchor coin holders, giving them not just stability but also income.

But partial collateral contained an implicit bet: it gambled that "not everyone will redeem at the same time." Once market panic struck and everyone rushed to the Treasury simultaneously, fifty pounds per coin would be exhausted instantly. The remaining holders would find their anchor coins had become worthless paper.

This is called "depegging"—the anchor coin's value falling below its promised one hundred pounds of rice.

---

**Third Generation: Algorithmic Adjustment**

Third-generation designers went further. They said: "Since full collateral is too expensive and partial collateral too dangerous, let's eliminate collateral entirely."

They designed an "algorithmic anchor vessel." This vessel had no Treasury, no reserves—only a set of automatic adjustment rules:

- When the anchor coin's market price exceeded one hundred pounds of rice, the system automatically minted new anchor coins and sold them into the market, pushing the price back down. The proceeds from issuance were retained by the system.
- When the market price fell below one hundred pounds of rice, the system used retained proceeds to buy back and burn anchor coins, pulling the price back up.

In theory, this system could self-balance. No collateral was needed; pure algorithms maintained the price.

But real-world waves proved far more complex than theory. One year, rumors spread: "Silver Sea Kingdom is going to war." Anchor coin holders panicked and sold, driving the price from one hundred to fifty pounds. According to the rules, the system should have initiated buybacks—but the retained proceeds were nowhere near enough to buy back all the anchor coins being dumped.

The algorithmic anchor vessel sank. With no collateral to support it, it was like a ship without ballast—one strong wind could capsize it.

---

**Fourth Generation: Hybrid Anchor**

Fourth-generation designers learned from the failures of the first three generations. They designed a "hybrid anchor" system:

- **Core layer**: Every anchor coin was backed by solid over-collateralization (e.g., one hundred twenty pounds of rice backing one hundred anchor coins). This was the safety floor.
- **Buffer layer**: A portion of collateral could be deployed in low-risk yield protocols, with returns distributed to holders. This was efficiency enhancement.
- **Adjustment layer**: When market prices deviated slightly, algorithms automatically fine-tuned supply; when deviations became severe, the system triggered emergency collateral liquidation to ensure core-layer solvency.

More critically, fourth-generation anchor vessel collateral was not single rice, but a diversified portfolio: rice, silk, tea, even government bonds of other nations. This way, even if one asset collapsed, the overall collateral ratio remained safe.

---

Years later, the Silver Sea Kingdom's anchor coin had become the most stable currency on the continent. No one knew whether it was fully collateralized, partially collateralized, or algorithmically adjusted—because the fourth-generation design had merged all three into one.

An old captain stood at the harbor watching anchor coin merchant vessels come and go. He said to his apprentice: "Do you know what's most impressive about the anchor coin? It's not that it doesn't depreciate—it's that when it truly faces a storm, you don't even feel the rocking. Because that vessel was designed assuming the worst sea conditions from the very beginning."

---

## What This Fable Is About

This fable illustrates the **evolution of stablecoin design**, from full collateral (USDC), over-collateralization (DAI), algorithmic stablecoins (UST), to hybrid designs (like FX 2.0). The core challenge of stablecoins is balancing the "stablecoin impossible triangle": **stability, capital efficiency, and decentralization**.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Anchor coin | Stablecoin | A cryptocurrency pegged to a fiat currency (usually USD) or other asset |
| Full collateral | Fiat-backed stablecoin (USDC, USDT) | Each stablecoin backed 1:1 by fiat or short-term Treasuries. Safest, but capital inefficient |
| Partial collateral | Fractional reserve model | Historically used by traditional banks; also tried by some algorithmic stablecoins |
| Algorithmic adjustment | Pure algorithmic stablecoin (UST, AMPL) | No collateral; supply adjusted by smart contracts to maintain price. Highest capital efficiency, but weakest resilience |
| UST collapse | Death Spiral | Market panic selling drives price below peg; system lacks sufficient reserves to buy back supply; confidence collapses, triggering further selling |
| Hybrid anchor | Hybrid stablecoin / FX 2.0 | Combines over-collateralization, yield generation, and algorithmic adjustment in a multi-layer safety design |
| Diversified collateral | Multi-asset collateral (DAI, FX 2.0) | Using multiple crypto assets as collateral reduces risk of single-asset crashes |
| Over-collateralization | Over-collateralization | E.g., DAI requires 150%+ collateral ratio—100 DAI issued requires at least $150 of ETH locked |
| Emergency liquidation | Liquidation Mechanism | When collateral value falls below required ratio, the system automatically auctions collateral to protect solvency |

### Why This Story?

Stablecoins are the foundation of DeFi, but the 2022 UST/Luna collapse wiped out hundreds of billions of dollars, proving the fragility of algorithmic stablecoins under extreme stress.

The "anchored vessel" metaphor maps the evolution through generations of failure and fourth-generation fusion, offering several advantages:
1. **Historical clarity**: From full collateral to algorithmic adjustment to hybrid design, mirroring the real development of stablecoins
2. **The impossible triangle**: Safety (strong chain), capital efficiency (light ship), decentralization (no captain)—three incompatible goals
3. **Death spiral visualization**: The algorithmic vessel's sinking is concretely depicted as "a strong wind capsizing a ship without ballast"

### Further Reading

- wiki-web3: How Modern Stablecoin FX 2.0 Is Built
- [MakerDAO: How DAI Works](https://docs.makerdao.com/)
- [Terra/Luna Collapse Analysis](https://academy.binance.com/en/articles/the-history-of-the-terra-luna-collapse)
- [FX 2.0 Stablecoin Design](https://fxprotocol.gitbook.io/fx-protocol)
