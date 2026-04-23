---
title: "The Ledger After the Avalanche"
title_cn: "雪崩后的账本"
concept: "Data Availability"
concept_cn: "数据可用性"
category: "infrastructure"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/数据可用性比你想象的更重要.md"
tags: [infrastructure, data-availability, da, rollup, sampling]
---

# The Ledger After the Avalanche

> *When the mountain falls, what matters is not who wrote the ledger, but whether anyone can still read it.*

## The Story

In the mountains above Yunzhou City, monks kept the imperial ledger. Every transaction in the empire was recorded in their great books. The monks were trusted; their books were the source of truth.

One winter, an avalanche destroyed the monastery. The monks survived, but the books were buried under tons of snow and rock.

The empire faced a crisis. No one doubted that the monks had recorded the transactions honestly. But the records were inaccessible. Merchants could not verify their balances. Tax collectors could not assess dues. The economy ground to a halt.

A young engineer proposed a new system. Instead of keeping the ledger in one monastery, every town would keep a copy. Not the entire ledger—no town had space for that—but every town would keep enough fragments that, collectively, the entire ledger could be reconstructed.

The system worked through random sampling. If a merchant wanted to verify a transaction, he would ask ten random towns for fragments. If all ten provided consistent fragments, the merchant could be confident the full ledger existed somewhere. If even one town failed to provide its fragment, the alarm would sound: the ledger was incomplete.

This system was not as efficient as the monastery. Verification took longer. But when the next avalanche came—this time a flood that destroyed three towns—the empire kept running. The lost fragments were recovered from other towns. The ledger endured.

---

## What This Fable Is About

This fable illustrates **Data Availability (DA)**—the guarantee that block data has been published and is available for anyone to download and verify. DA is critical for rollups and light clients.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Monastery ledger | Centralized block storage | A single source of truth for all transaction data |
| Avalanche | Node failure / censorship | A catastrophic event that makes data inaccessible |
| Towns keeping fragments | Distributed data availability | Data is erasure-coded and distributed across many nodes |
| Random sampling | Data Availability Sampling (DAS) | Light clients randomly sample data chunks to verify availability without downloading everything |
| Ten consistent fragments | Sampling confidence | The probability of detecting data unavailability increases exponentially with each sample |
| One town failing | Unavailability detection | If any sampled chunk is missing, the data is provably unavailable |
| Lost fragments recovered | Erasure coding | Using Reed-Solomon coding, the full data can be reconstructed from a subset of fragments |

### Why This Story?

Data availability is often overlooked but is the foundation of rollup security. The avalanche metaphor makes it visceral: trust is not enough; accessibility is what matters.

### Further Reading

- wiki-web3: Data Availability Is More Important Than You Think
- [Ethereum.org: Data Availability](https://ethereum.org/en/developers/docs/data-availability/)
- [Celestia: What is Data Availability?](https://celestia.org/learn/data-availability/)
