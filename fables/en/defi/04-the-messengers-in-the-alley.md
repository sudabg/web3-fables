---
title: "The Messengers in the Alley"
title_cn: "暗巷中的信使"
concept: "MEV and Flashbots"
concept_cn: "MEV 与 Flashbots"
category: "defi"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/mempool-监听与抢先交易实战从原理到-flashbots-套利脚本uniswap-v3-sepolia-测试网.md"
tags: [defi, mev, flashbots, sandwich-attack, priority-fee, block-builder]
---

# The Messengers in the Alley

> *In a system where everyone can read the mail, the fastest reader writes the rules.*

## The Story

Yunzhou City's postal system had a peculiar design: all letters were hung on a public bulletin board at the city gate before delivery. Couriers decided pickup order based on postage fees—whoever paid the highest fee got their letter picked up and delivered first.

The design's intention was transparency. But soon, a special class of "messengers" formed a secret society in the city's alleyways.

---

**The Sandwich Thief**

The sandwich thief did not write letters; he only read others' mail.

When merchant Xu Zhen wrote a letter to the marketplace: "I wish to buy ten bolts of silk for one hundred taels of silver," the letter was posted on the bulletin board. The sandwich thief read it.

He immediately did three things:
1. Sent a first letter: "Buy all cheap silk at the marketplace." (Paid express postage to ensure delivery before Xu Zhen's letter.)
2. Waited for Xu Zhen's letter to be delivered, forcing Xu to buy at the inflated price.
3. Sent a second letter: "Sell all the silk I just bought." (Paid express postage to ensure delivery immediately after Xu Zhen's letter.)

Result: the thief bought low, sold high, and pocketed the spread. Xu Zhen had done nothing wrong—he simply bought silk at market price—but the "market price" had been artificially inflated by the thief.

This is a "sandwich attack"—inserting two transactions around the victim's transaction, like bread around meat.

---

**The Arbitrage Hawk**

The arbitrage hawk simultaneously watched two marketplaces: East Market and West Market.

East Market sold silk for one hundred taels per bolt; West Market for one hundred five. Normally, such price differences would be naturally arbitraged away by merchants buying low and selling high.

But the hawk was far faster than ordinary merchants. He did not need his own silk inventory. He simply:
1. Borrowed from the "Lightning Money House" (same-transaction loan, must be repaid within the hour).
2. Bought silk at East Market with borrowed funds.
3. Immediately sold it at West Market.
4. Repaid the loan and its fee.
5. Kept the profit.

All within five minutes. By the time ordinary merchants finished their calculations, the hawk had already pocketed the money.

---

**The Scavenger**

The scavenger did not seek profit; he sought certainty.

The money house's rule was: when collateral value fell below a threshold, anyone could execute liquidation, acquiring collateral at a discount. But liquidation required precise timing—too early, and the threshold had not been reached; too late, and someone else might execute first.

The scavenger's job was to monitor all collateral in all money houses. The instant a threshold was triggered, he sent a liquidation letter with the highest postage fee, ensuring his letter was delivered first.

The scavenger's income was modest—only a few percentage points of discount per liquidation—but he was risk-free. As long as he was fast enough, he never lost.

---

**Order in the Alley**

The activities of these three messenger classes threw Yunzhou City's postal system into chaos. Ordinary merchants discovered that no matter what they bid, their letters were always slower than the sandwich thieves. The market was no longer driven by supply and demand, but by "who could pay higher postage fees."

Worse, the alleyway messengers began attacking each other. Two sandwich thieves targeting the same letter would competitively raise postage until profits were eaten by fees. Arbitrage hawks found East-West price spreads narrowing—too many were arbitraging, and opportunities vanished in seconds.

An old courier named Feiluo could no longer stand it. He did one thing: built a "private delivery station" outside the city.

The private station's rule was: messengers no longer posted letters on the public bulletin board; they handed letters directly to Feiluo. Feiluo did not read letter contents; he only sorted them by the messenger's bid, then packaged the sorted letters and delivered them to the city gate courier in one batch.

This offered two benefits:
1. Letter "contents" were no longer public—sandwich thieves could no longer read others' mail.
2. Messengers no longer needed to compete on the bulletin board; they conducted "sealed auctions" at Feiluo's station, where the highest bidder went first, but no one knew others' bids.

Feiluo's private station quickly became the mainstream. Sandwich thieves were unemployed—they could no longer read others' mail. Arbitrage hawks still existed, but they could only exploit publicly available market information, not mempool transparency. Scavengers could continue working, but competition became more orderly.

Feiluo took a tiny fee from each transaction as his compensation. He invented no new technology; he only changed how information flowed.

---

## What This Fable Is About

This fable illustrates **MEV (Maximal Extractable Value)** and **Flashbots**—solutions that mitigate the harmful effects of MEV extraction. MEV refers to the additional value that block producers (or searchers) can extract by controlling transaction ordering, including front-running, back-running, sandwich attacks, and liquidation arbitrage.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Public bulletin board | Mempool | Pending transactions are publicly visible before being included in a block; anyone can read them |
| Postage determines order | Gas Price / Priority Fee | Miners/validators prioritize transactions with higher gas prices |
| Sandwich thief | Sandwich attacker | Wraps a victim's large swap between buy and sell transactions, exploiting price slippage |
| Arbitrage hawk | Arbitrage searcher | Exploits price differences between DEXes, typically using flash loans |
| Lightning Money House | Flash loan | Uncollateralized loan borrowed and repaid within a single atomic transaction. Provided by Aave, dYdX, etc. |
| Scavenger | Liquidation bot | Monitors collateral prices and submits liquidation transactions immediately when conditions are triggered, earning liquidation rewards |
| Alley chaos | Negative externalities of MEV | MEV extraction causes ordinary users to face worse prices, higher slippage, and network congestion |
| Feiluo's private station | Flashbots / MEV-Boost / private mempool | Reduces open gas-price auction wars through private transaction pools (e.g., Flashbots Protect) or PBS (Proposer-Builder Separation) |
| Sealed auction | MEV-Boost auction mechanism | Searchers submit sealed transaction bundles to block builders, who select the most profitable combination |
| Feiluo's cut | Builder profit | Builders extract value from MEV and share it with validators |

### Why This Story?

MEV is one of the darkest and most complex topics in blockchain. It is not a single technical problem but an incentive-structure problem—when transaction order can be influenced, influencing order itself becomes a profit source.

The "messengers in the alley" metaphor makes the MEV ecosystem tangible: sandwich thieves, arbitrage hawks, and scavengers are the three typical MEV strategies. The story also shows how Flashbots' private mempool and PBS—represented by Feiluo's private delivery station—change information flow to protect ordinary users.

### Further Reading

- wiki-web3: Mempool Monitoring and Front-running with Flashbots
- [Flashbots: MEV Overview](https://docs.flashbots.net/)
- [MEV-Boost: PBS for Ethereum](https://boost.flashbots.net/)
- [Ethereum.org: MEV](https://ethereum.org/en/developers/docs/mev/)
- [EigenPhi: MEV Dashboard](https://eigenphi.io/)
