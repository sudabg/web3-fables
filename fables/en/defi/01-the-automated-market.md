---
title: "The Automated Market"
title_cn: "自动市集"
concept: "Uniswap V2 AMM"
concept_cn: "Uniswap V2 自动做市商"
category: "defi"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/uniswap-v2-之书.md"
tags: [defi, amm, uniswap, liquidity, xy-k]
---

# The Automated Market

> *A marketplace with no shopkeeper, run by a balance scale that never tips.*

## The Story

Yunzhou City had two great products: silk from the east and tea from the west. Merchants had always traded between them, but there was a persistent problem: who decided how many pounds of tea one bolt of silk was worth?

Traditionally, this was the job of the "market brokers"—specialized middlemen who observed supply and demand daily and quoted a price both sides would accept. But brokers had a fatal flaw: they lied. When silk was oversupplied, they told tea merchants "silk is cheap" while telling silk merchants "silk is scarce," pocketing the spread.

The new magistrate of Yunzhou abolished the broker system. He built an "Automated Market" in the city center. There were no shopkeepers, no price quoters—only a giant balance scale, with silk on the left tray and tea on the right.

The market's operating rules were carved in stone and never changed:

**"The amount of silk on the left tray multiplied by the amount of tea on the right tray equals a fixed constant."**

This constant was set when the market was built—based on the initial amounts of silk and tea deposited. If one hundred bolts of silk and one thousand pounds of tea were initially deposited, the constant was 100,000.

---

On the first day of operation, a silk merchant arrived with ten bolts of silk to exchange for tea. He placed the silk on the left tray—now there were one hundred ten bolts. According to the rule, the right tray had to adjust so that 110 × right = 100,000. So the tea had to become 100,000 ÷ 110 ≈ 909 pounds.

The right tray had held one thousand pounds; now it held nine hundred nine—a reduction of ninety-one pounds. Those ninety-one pounds were what the silk merchant received for his ten bolts.

The merchant was satisfied. He did not need to haggle with a broker; the rules were public, the outcome deterministic. He deposited ten bolts of silk and took ninety-one pounds of tea, all without anyone's permission.

But there was a subtlety: the ninety-one pounds were not calculated at a fixed exchange rate of "ten bolts equals ninety-one pounds." If he had brought only one bolt, the left tray would have one hundred one bolts, and the right would become 100,000 ÷ 101 ≈ 990 pounds—he would receive only ten pounds of tea. If he brought fifty bolts, the left tray would have one hundred fifty, and the right would become 100,000 ÷ 150 ≈ 667 pounds—he would receive three hundred thirty-three pounds of tea, but at the cost of fifty bolts.

The more he exchanged, the less tea each bolt was worth. This is "price impact"—large trades significantly shift the balance of the scale.

---

Another important participant was the "pool depositor." Depositors did not trade; they simply deposited equal values of silk and tea into both trays simultaneously. In return, they received a token called a "pool receipt"—representing their share of the market.

Whenever a trade occurred, the trader paid a tiny "slippage fee" (say, 0.3%). This fee did not go into anyone's pocket; it stayed directly on the scale—slightly increasing the total amounts on both sides.

This meant that while depositors' percentage shares remained the same, the absolute quantities they represented slowly grew. They earned money without doing anything.

A clever merchant discovered this. He calculated that if the Automated Market's trading volume was high enough, the accumulated slippage fees would exceed "impermanent loss" (the relative loss caused by price fluctuations). He invested his entire fortune into the pool and became one of the largest depositors.

Three years later, he was one of the wealthiest men in Yunzhou City. He had never made a single trade; his wealth came from the accumulated drip of countless traders.

---

But the Automated Market had its vulnerabilities.

One year, a pest infestation destroyed mulberry trees in the east, and silk production plummeted. Silk prices soared in external markets, but the Automated Market's scale reacted slowly—it continued operating at its original ratio until someone traded massive amounts of tea for silk, nearly emptying the left tray.

When only one bolt of silk remained on the left tray, one thousand pounds of tea remained on the right. At this point, if someone wanted to trade one bolt for tea, how much would they receive? 100,000 ÷ (1+1) = 50,000 pounds. But this would nearly empty the market's tea supply.

The bigger problem: when one side's assets were nearly exhausted, the market lost its purpose—no one could trade there anymore. This is called "liquidity exhaustion."

The magistrate later made two improvements: first, encourage more depositors to participate, making the scale's base large enough that individual trades would not significantly impact the ratio. Second, introduce a "price oracle"—when external market prices diverged significantly from the scale's ratio, arbitrage opportunities would attract traders to restore balance.

---

Years later, the Automated Market had evolved from a city facility into standard infrastructure across the entire empire. Markets across the land were interconnected, forming a vast trading network. No brokers, no shopkeepers—just the simple formula carved in stone:

**Left × Right = Constant**

A traveling mathematician stood before the Automated Market for a long time and finally said something that was carved on the back of the stone: "This is not a market. This is mathematics ruling commerce."

---

## What This Fable Is About

This fable illustrates the **Uniswap V2 Automated Market Maker (AMM)**. Uniswap V2 uses the constant product formula `x × y = k` to determine trade prices, where `x` and `y` are the quantities of the two tokens in the liquidity pool, and `k` is a constant.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Automated Market | Uniswap V2 Pair | A liquidity pool of two tokens with no order book and no market maker |
| Balance scale | Constant product formula `x × y = k` | The trade automatically adjusts prices so that the product of the two token quantities remains constant |
| Silk merchant exchanging tea | Swap transaction | User deposits one token into the pool and withdraws the other. The pool automatically adjusts prices according to `x × y = k` |
| More exchanged, less per unit | Price impact / Slippage | Large trades relative to pool depth cause significant price deviation from market average |
| Pool depositor | Liquidity Provider (LP) | Deposits both tokens simultaneously into the pool and receives LP tokens as share certificates |
| Slippage fee | Trading fee (0.3%) | Automatically reinvested into the pool, increasing `k`. LPs earn proportional to their share |
| Pool receipt | LP Token (ERC-20) | A transferable token representing a share of liquidity |
| Impermanent loss | Impermanent Loss | When external market prices change, the LP's portfolio is worth less than simply holding the assets because the AMM's rebalancing mechanism "buys high and sells low" |
| Pest disaster causing imbalance | External price deviation from pool price | Arbitrageurs trade against the pool until its price aligns with external markets |
| Liquidity exhaustion | Single-sided asset depletion | If one side of the pool is drained, trading halts. Sufficient liquidity and incentives are needed to maintain two-sided balances |

### Why This Story?

The AMM is one of DeFi's core innovations, but its mechanics are deeply counterintuitive for newcomers—"Where does the price come from if there are no buyers and sellers?"

The "balance scale" metaphor makes `x × y = k` viscerally intuitive:
- Add to one side, the other must decrease proportionally
- The more you add, the less favorable the exchange rate becomes
- The total value (`k`) slowly grows from fees

The pool depositor also maps to the LP's role—they bear the risk of impermanent loss in exchange for fee revenue. And the "abolition of brokers" metaphorizes the AMM's core value: removing middlemen and replacing them with immutable mathematical rules.

### Further Reading

- wiki-web3: Uniswap V2 Book
- [Uniswap V2 Whitepaper](https://uniswap.org/whitepaper.pdf)
- [Uniswap V2 Core Concepts](https://docs.uniswap.org/contracts/v2/overview)
- [Impermanent Loss Explained](https://medium.com/auditless/impermanent-loss-and-why-it-matters-2ce4e4ef5a2e)
