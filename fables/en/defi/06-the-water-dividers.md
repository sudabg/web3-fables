---
title: "The Water Dividers"
title_cn: "分水渠"
concept: "0xSplits Revenue Sharing"
concept_cn: "0xSplits 收入拆分协议"
category: "defi"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/分析0xsplits---收入拆分协议.md"
tags: [defi, revenue-sharing, splits, royalty, collaboration]
---

# The Water Dividers

> *The hardest part is not earning money, but dividing it fairly.*

## The Story

East of Yunzhou City ran a canal fed by three sources: a mountain spring, a rain channel, and an underground aquifer. The three source owners agreed: canal revenue (irrigation fees, boat tolls) would be distributed according to each source's contribution—spring fifty percent, rain channel thirty percent, underground aquifer twenty percent.

It sounded simple, but execution was a nightmare.

---

**Old Method: Manual Division**

Initially, the canal's terminus had a water-dividing gate. Gatekeeper Zhao manually calculated each source's share daily, wrote three silver drafts, and sent them out.

If total revenue was one hundred taels, Zhao would open his ledger, calculate one hundred × fifty percent = fifty taels for the spring owner, thirty for the rain channel owner, twenty for the aquifer owner. Then write three drafts and send them separately.

If only two sources contributed today? Say it didn't rain, and the rain channel contributed nothing. Zhao still had to go through the entire process: calculate, write drafts, send—though the rain channel owner received zero.

More troublesome: when a new source joined. Suppose a fourth source—a reservoir—wanted to connect to the canal. Zhao had to: recalculate percentages, rebuild the dividing gate, update the ledger, notify all parties. The entire process took three days.

And if someone questioned: "Zhao, is my fifty taels correct?" Zhao could only flip to a certain page and point: "See, I wrote it down." But this proved he hadn't miscalculated, nor that he hadn't secretly altered numbers.

---

**New Method: Automatic Water Dividers**

One day, a young engineer designed an "automatic water division system."

The system's core was a "division contract"—carved on a bronze plate, hung in the public temple by the canal, readable by anyone. The contract was extremely simple:

**"All water entering the canal, and the revenue it generates, shall be automatically distributed as follows: spring fifty percent, rain channel thirty percent, underground aquifer twenty percent."**

The contract was accompanied by an "automatic water divider" device: when revenue reached the canal terminus, the device automatically channeled it according to contract-specified proportions into the three source owners' accounts. No Zhao needed, no ledger, no silver drafts.

More surprisingly: this device was "immutable." Once the contract on the bronze plate was carved, no one could unilaterally modify the percentages. If all three source owners agreed to change percentages, they had to cast a new bronze plate together and replace the old one.

This meant: Zhao's "trust problem" was completely solved. No one needed to trust Zhao not to miscalculate—because Zhao had been removed from the entire process.

---

**New Problems Emerge**

The automatic water division system operated for half a year before a new requirement emerged.

The spring owner was a family with five brothers who needed to split the spring's fifty percent share equally among themselves. Under the old method, Zhao manually divided again. But the automatic system did not support "nested distribution"—it could only distribute according to the first-layer contract, not automatically handle second layers.

The young engineer upgraded the system: "sub-contracts" were allowed.

Now, the water division system became two layers:
- Layer one: Total canal revenue → distributed to three sources according to main contract
- Layer two: Spring's share → distributed to five brothers according to sub-contract
- Layer two could continue: Eldest brother's share → distributed to his wife and children according to grandchild-contract

Each layer's contract was an independent bronze plate with its own automatic water divider. Revenue flowed like water, layer by layer, until reaching final recipients.

Moreover, any layer's contract could be "forked"—if the third brother decided to go independent, he could extract his share from the family sub-contract and create his own independent sub-contract, no longer participating in family distribution. This process required no consent from the other four brothers, nor Zhao's approval.

---

**Unexpected Applications of Automatic Water Division**

The automatic water division system was originally designed for canals, but people quickly discovered broader applications:

- **Music workshop royalties**: A composition jointly created by lyricist, composer, and performer. They created a three-way division contract: lyrics thirty percent, composition forty percent, performance thirty percent. Whenever someone paid to listen, revenue automatically distributed according to these proportions.
- **Inn partnerships**: An inn jointly funded by ten partners. They created a ten-way division contract, distributing profits according to investment shares. Anyone could sell their share to others anytime—simply changing their address in the division contract to the new owner's.
- **Charitable donations**: A charity project created a two-way division contract: ninety percent to beneficiaries, ten percent to platform operations. Donors could see the contract content and confirm their money would not be intercepted.

In these scenarios, the automatic water division system's core value was not "calculation"—calculation itself was simple—but "trust." Participating parties did not need to trust any intermediary; they only needed to trust that publicly visible bronze plate.

---

Years later, Yunzhou City's water division system had connected thousands of revenue streams. Some had only two layers of distribution; others had over a dozen. Some contracts were permanently immutable; others automatically adjusted proportions quarterly based on performance.

Zhao did not lose his job. He transformed into a "contract consultant"—helping people design the most suitable division structures. After all, the automatic water division system could perfectly execute any contract, but it could not decide for people "what a fair contract looks like."

Zhao often said: "Machines solved the 'how to divide' problem. But the 'how much to divide' problem will always require humans to answer."

---

## What This Fable Is About

This fable illustrates **0xSplits**—an on-chain revenue splitting protocol that allows creators, collaborators, team members, and others to automatically distribute earnings according to preset proportions. Its core values are: trustlessness, immutability, and composability.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Canal and three sources | Multi-party collaborative revenue | Any scenario requiring fixed-proportion revenue distribution |
| Zhao's manual division | Traditional off-chain revenue distribution | Relies on third parties (platforms, accountants) for manual calculation and transfer; has trust costs and delays |
| Bronze plate division contract | 0xSplits smart contract | On-chain immutable distribution rules; code is law |
| Automatic water divider | Automatic splitting logic | When revenue arrives, the contract automatically distributes according to preset proportions to each recipient |
| Immutable contract | Immutability | Once deployed, distribution proportions cannot be unilaterally modified; prevents mid-stream changes |
| Nested sub-contracts | Splits composability | A Split's recipient can be another Split's address, forming multi-layer distribution structures |
| Third brother going independent | Share transferability | Anyone can extract or transfer their share in a Split to someone else |
| Music workshop royalties | Royalties / copyright distribution | NFT creators, musicians can set permanent royalties; secondary market trading revenue automatically distributes |
| Inn partnerships | Investment / partnership revenue distribution | Investors, team members automatically share profits according to agreed proportions |
| Charitable donations | Transparent fund flows | Donors can verify fund destinations, ensuring no misappropriation |

### Why This Story?

Revenue splitting looks simple but is actually extremely complex in practice. Off-chain solutions either rely on trusted third parties or have high execution costs and low transparency.

The "water dividers" metaphor for 0xSplits offers several intuitive advantages:
1. **Liquidity**: Revenue flows like water; distribution is a natural physical process
2. **Composability**: Sub-contract nesting corresponds to Splits' recursive structure
3. **Trust replacement**: The bronze plate replaces Zhao, solving the "who watches the watchers" problem

### Further Reading

- wiki-web3: Analysis of 0xSplits — Revenue Splitting Protocol
- [0xSplits Official Docs](https://docs.0xsplits.xyz/)
- [Mirror: Splits for Creators](https://mirror.xyz/)
