---
title: "The Weather Vane Deception"
title_cn: "风向旗的骗局"
concept: "Oracle Manipulation"
concept_cn: "预言机操纵"
category: "security"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/solodit-检查清单解读-4预言机操纵.md"
tags: [security, oracle, manipulation, price-feed, flash-loan]
---

# The Weather Vane Deception

> *He who controls the weather vane controls the wind—or at least, what everyone believes about the wind.*

## The Story

In Yunzhou City, the farmers relied on a great weather vane to determine when to plant and harvest. The vane was connected to a complex system of gears and pulleys that measured wind direction, temperature, and humidity. Based on these readings, the city council issued planting recommendations.

The system worked well for years. Then a drought came.

A wealthy landowner named Qian realized something: the weather vane did not actually measure the weather. It measured what the *majority of local weather stations* reported. And Qian owned three of the five stations.

Qian's plan was simple:
1. Manipulate his three stations to report extreme conditions.
2. The weather vane, taking the majority reading, would declare a false storm approaching.
3. The city council would issue an emergency harvest order.
4. Farmers would rush to sell their crops at depressed prices.
5. Qian would buy low, then restore the true readings.
6. Prices would recover. Qian would sell high.

The execution was flawless. The weather vane showed a storm. The council panicked. The market crashed. Qian bought an entire season's harvest for a fraction of its value.

Then he "fixed" his weather stations. The vane returned to normal. Prices soared. Qian sold everything and tripled his wealth.

No one could prove manipulation. The weather vane had done exactly what it was designed to do: report the majority. The flaw was not in the vane but in the assumption that the majority could not be bought.

---

## What This Fable Is About

This fable illustrates **oracle manipulation**—attacks on price oracle systems where an attacker controls or manipulates the data sources that a smart contract relies on for price information, enabling them to profit from the resulting price discrepancies.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Weather vane | Price Oracle | A system that provides external price data to smart contracts |
| Five weather stations | Multiple data sources | Decentralized oracles use multiple sources to determine consensus |
| Qian owns three stations | Majority control | If an attacker controls >50% of data sources, they can manipulate the consensus |
| False storm report | Manipulated price feed | The oracle reports an artificial price based on corrupted sources |
| Emergency harvest | Liquidation / forced selling | DeFi protocols may trigger liquidations or other automated responses based on oracle prices |
| Market crash | Price collapse | Users sell at manipulated low prices |
| Buy low, sell high | Oracle manipulation arbitrage | Attacker profits from the artificial price movement |
| Assumption of honest majority | Oracle trust model | The security of many oracle systems depends on the assumption that most sources are honest |

### Why This Story?

Oracle manipulation is one of the most devastating and high-value attack vectors in DeFi. The weather vane metaphor makes the attack visceral: the vane itself is not broken; the trust model underlying it is.

### Further Reading

- [wiki-web3: Oracle Manipulation Checklist](../../wiki-web3/concepts/solodit-检查清单解读-4预言机操纵.md)
- [Chainlink: Oracle Security](https://chain.link/education/blockchain-oracles)
- [DeFi Oracle Exploits: A Timeline](https://rekt.news/oracle-manipulation/)
