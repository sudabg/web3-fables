---
title: "The Deep Well and the Shallow Pond"
title_cn: "深井与浅池"
concept: "Uniswap V3 Concentrated Liquidity"
concept_cn: "Uniswap V3 集中流动性"
category: "defi"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/uniswap-v3-开发指南-23799.md"
tags: [defi, uniswap, concentrated-liquidity, tick, range, lp]
---

# The Deep Well and the Shallow Pond

> *It is not about having more water, but about having water in the right places.*

## The Story

Yunzhou City's Automated Market (Uniswap V2) operated well, but depositors gradually discovered a frustrating fact: most of their funds were "idle" most of the time.

In V2's Automated Market, depositors had to deposit equal values of both assets into both sides of the scale. These funds were distributed across the entire price range—from near zero to infinity. This meant that wherever the market price was, only a tiny fraction of funds was actually participating in trades. The vast majority lay at the extremes of the price range, like hibernating bears, doing nothing.

A mathematician named Chen Shen calculated a startling number: in V2 markets, approximately only 0.5% of funds at any given price point were actually "working." The remaining 99.5% sat in the pool but contributed nothing to trading—they simply waited for extreme prices that might never come.

"This is wasteful," Chen Shen said. "If I know the reasonable price range for silk and tea is one bolt for eighty to one hundred twenty pounds of tea, why should my money be distributed from zero to infinity?"

---

Chen Shen designed a new market: the "Range Market."

In the Range Market, depositors were no longer forced to distribute funds across the entire price axis. They could specify a range: "I will only provide liquidity within the eighty to one hundred twenty pounds of tea per bolt of silk range."

This was like a depositor renting a booth at a specific location in the market, rather than being evenly distributed across the entire square. When the market price was within their rented range, their funds participated in trading and earned fees. When the market price moved outside their range, their funds automatically "exited"—becoming entirely single-asset, no longer participating in trading or earning fees.

This design brought several dramatic changes:

**First, capital efficiency increased tenfold.**

In V2 markets, ten thousand taels of capital might generate only ten taels of daily fees. In Range Markets, if depositors concentrated funds in the most active price range near the current price, the same capital could generate hundreds of taels daily—because their funds were no longer diluted across never-touched price ranges.

**Second, booth location became strategy.**

In V2 markets, all depositors were identical—you deposited a certain amount, and earned proportionally. In Range Markets, different booth locations meant different risks and returns.

Conservative depositors chose a wide range (say, fifty to two hundred), so market prices rarely moved outside their range. But their capital utilization was low, because only a small portion of funds in a wide range worked near the current price.

Aggressive depositors chose a narrow range (say, ninety-five to one hundred five), compressing all funds into the most active price point. Their capital utilization was extremely high, fee income potentially dozens of times that of conservatives. But risk was equally high—if market prices fluctuated even slightly and moved outside their range, all their funds became single-asset and stopped earning.

**Third, the market developed a "depth map."**

V2 markets were like uniformly deep swimming pools—wherever you jumped in, the depth was the same. V3 Range Markets were like irregular deep wells—some locations were bottomless, others were shallow puddles.

Traders loved deep wells: where depth was great, large trades had minimal price impact. In shallow puddles, even small trades caused huge price jumps.

Clever depositors observed the market's depth map and injected funds into "shallow puddles"—because competition was less there, fees were shared among fewer people. But this also meant they were taking risks: shallow puddles were shallow precisely because those price ranges were not favored by the market.

---

One year after the Range Market launched, an unexpected phenomenon emerged: overall market liquidity had not increased, but fund distribution became extremely uneven.

Near price one hundred—the historically most active price—well depth was twenty times that of V2-era levels. Traders enjoyed minimal slippage here. But near price two hundred—a rarely touched extreme—puddles nearly dried up. If someone suddenly needed to make a large trade at that price, they might find there was simply insufficient liquidity to support it.

Chen Shen's explanation was: "This is not a bug; it is a feature. V2 used uniform distribution to hide true supply and demand. V3 exposes true supply and demand. Capital naturally flows to the most profitable places; this is the market's choice."

But critics said: "Liquidity exhaustion in extreme situations is a safety hazard. When markets panic and everyone wants to flee, there is not enough water in shallow puddles to cushion the shock."

This debate remains unresolved.

---

## What This Fable Is About

This fable illustrates **Uniswap V3's Concentrated Liquidity** mechanism. V3's biggest innovation is allowing liquidity providers (LPs) to customize price ranges, concentrating funds in the price ranges they believe are most active, thereby dramatically improving capital efficiency.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| V2 Automated Market | Uniswap V2 AMM | Liquidity uniformly distributed across [0, ∞) price range; low capital utilization |
| 99.5% idle funds | V2 capital efficiency problem | At any actual price point, only a tiny fraction of V2 pool funds actively participate |
| Range Market | Uniswap V3 Concentrated Liquidity | LPs can specify price range [lower, upper]; liquidity only provided within that range |
| Booth location | Tick Range / Position | V3 divides the price axis into discrete ticks; each position occupies a tick range |
| Wide range fifty to two hundred | Conservative LP strategy | Choosing wider ranges reduces impermanent loss risk but also lowers capital efficiency |
| Narrow range ninety-five to one hundred five | Aggressive LP strategy | Highly concentrated capital maximizes fee income, but risk of price moving out of range and impermanent loss are extremely high |
| Out of range | Out of Range | When price exceeds a position's range, all liquidity becomes single-asset, no longer earning fees |
| Depth map | Liquidity Distribution | V3 allows observing liquidity depth at different price ranges. Mainstream ranges are extremely deep; extreme ranges are extremely shallow |
| Less competition in shallow puddles | Non-uniform distribution arbitrage space | In liquidity-thin ranges, small capital can earn higher fee proportions, but faces greater impermanent loss |
| Extreme liquidity exhaustion | Tail risk | V3 concentrates liquidity near current prices; extreme market conditions may create liquidity vacuums, amplifying price volatility |

### Why This Story?

Uniswap V3 is one of DeFi's most sophisticated designs, but also one of the hardest to intuitively understand. The concept of "concentrating liquidity from infinite ranges to finite ranges" is deeply counterintuitive for many beginners.

The "deep well and shallow pond" metaphor offers several intuitive advantages:
1. **Spatial sense**: Abstract price ranges are concretized as "booth locations," letting readers understand that "location choice itself is a strategy"
2. **Risk-return**: Narrow range = deep well = high return high risk; wide range = shallow pond = low return low risk
3. **Systemic impact**: V3 "authenticates" liquidity distribution, exposing market structure—this is not a bug but market efficiency improvement, though it brings new tail risks

### Further Reading

- [wiki-web3: Uniswap V3 Development Guide](../../wiki-web3/concepts/uniswap-v3-开发指南-23799.md)
- [Uniswap V3 Whitepaper](https://uniswap.org/whitepaper-v3.pdf)
- [Uniswap V3 Core Concepts](https://docs.uniswap.org/concepts/protocol/concentrated-liquidity)
- [Charged Particles: V3 LP Strategies](https://medium.com/auditless/uniswap-v3-lp-strategies-8c50f0878e26)
