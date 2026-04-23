---
title: "The Messenger and the Auction House"
title_cn: "信使与拍卖行"
concept: "Front-running Attack"
concept_cn: "抢跑攻击"
category: "security"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/solodit-检查清单解读-4抢跑攻击.md"
tags: [security, front-running, sandwich-attack, mempool, mev]
---

# The Messenger and the Auction House

> *In a city where all messages pass through a public square, the fastest reader always wins.*

## The Story

In Yunzhou City, all commercial messages were posted on a public bulletin board before delivery. Messengers would read the board, pick up letters, and deliver them in order of postage fee—whoever paid the most got their letter delivered first.

This system was transparent, but it created a shadow economy of "message brokers" who operated in the alleyways behind the bulletin board.

---

**The Sandwich Thief**

A sandwich thief did not write letters. He only read other people's messages.

When a merchant named Xu wrote a letter to the marketplace saying, "I wish to buy ten bolts of silk for one hundred taels," the letter was posted on the bulletin board. The sandwich thief read it.

He immediately did three things:
1. Sent a first letter: "Buy all cheap silk at the marketplace." (Paid express postage to arrive before Xu's letter.)
2. Waited for Xu's letter to be delivered, forcing Xu to buy at the now-inflated price.
3. Sent a second letter: "Sell all the silk I just bought." (Paid express postage to arrive immediately after Xu's letter.)

The result: the thief bought low, sold high, and pocketed the difference. Xu had done nothing wrong—he simply bought silk at the market price—but the "market price" had been artificially inflated by the thief.

This is called a "sandwich attack"—the attacker wraps the victim's transaction between two of their own, like bread around meat.

---

**The Arbitrage Hawk**

The arbitrage hawk watched two marketplaces simultaneously: the East Market and the West Market.

East Market sold silk for one hundred taels per bolt; West Market sold it for one hundred and five. Normally, such price differences would be naturally arbitraged away by merchants buying low and selling high.

But the hawk was faster than ordinary merchants. He did not need his own silk inventory. He simply:
1. Borrowed money from the "Lightning Money House" (same-transaction loan, must be repaid within the hour).
2. Bought silk at the East Market with borrowed funds.
3. Immediately sold it at the West Market.
4. Repaid the loan and its fee.
5. Kept the profit.

All within five minutes. By the time ordinary merchants finished their calculations, the hawk had already pocketed the money.

---

**The Scavenger**

The scavenger did not seek profit. He sought certainty.

The money house's rule was: when collateral value fell below a threshold, anyone could execute liquidation, acquiring the collateral at a discount. But liquidation required precise timing—too early, and the threshold had not been reached; too late, and someone else might execute first.

The scavenger's job was to monitor all collateral in all money houses. The instant a threshold was triggered, he sent a liquidation letter with the highest postage fee, ensuring his letter was delivered first.

The scavenger's income was modest—only a few percentage points of discount per liquidation—but he was risk-free. As long as he was fast enough, he never lost.

---

## What This Fable Is About

This fable illustrates **front-running attacks** in blockchain systems—where attackers exploit the public visibility of pending transactions (the mempool) to insert their own transactions ahead of victims', profiting from price slippage, arbitrage, or liquidation rewards.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Public bulletin board | Mempool | Pending transactions are publicly visible before being included in a block |
| Postage fee determines delivery order | Gas Price / Priority Fee | Miners/validators prioritize transactions with higher gas prices |
| Sandwich thief | Sandwich Attacker | Inserts buy order before victim's swap and sell order after, profiting from price slippage |
| Arbitrage hawk | Arbitrage Searcher | Exploits price differences between DEXes, typically using flash loans |
| Lightning Money House | Flash Loan | Same-transaction, zero-collateral loan that must be repaid atomically |
| Scavenger | Liquidation Bot | Monitors collateral prices and submits liquidation transactions immediately when thresholds are triggered |
| Alleyway chaos | MEV negative externalities | MEV extraction leads to worse prices for ordinary users, higher slippage, and network congestion |
| Private delivery station (Feiluo) | Flashbots / MEV-Boost | Private mempool and sealed-bundled auction system to mitigate open gas-price wars |

### Why This Story?

MEV is one of the darkest and most complex topics in blockchain. It is not a single technical problem but an incentive-structure problem: when transaction order can be influenced, influencing order itself becomes a profit source.

The "messengers in the alley" metaphor makes the MEV ecosystem tangible: sandwich thieves, arbitrage hawks, and scavengers are the three typical MEV strategies. The story also shows how Flashbots' private mempool—represented by Feiluo's private delivery station—changes the information flow to reduce harmful MEV.

### Further Reading

- wiki-web3: Mempool Monitoring and Front-running
- [Flashbots: MEV Overview](https://docs.flashbots.net/)
- [MEV-Boost: PBS for Ethereum](https://boost.flashbots.net/)
- [Ethereum.org: MEV](https://ethereum.org/en/developers/docs/mev/)
