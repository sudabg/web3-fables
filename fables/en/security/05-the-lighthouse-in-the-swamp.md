---
title: "The Lighthouse in the Swamp"
title_cn: "沼泽中的灯塔"
concept: "Honeypot Contract"
concept_cn: "蜜罐合约"
category: "security"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/一个蜜罐合约的解析.md"
tags: [security, honeypot, scam, trap, bait]
---

# The Lighthouse in the Swamp

> *A beacon that promises safe passage but lures ships into the mud.*

## The Story

In the marshlands outside Yunzhou City, travelers spoke of a mysterious lighthouse. It appeared only at night, casting a warm golden light across the treacherous swamp. Those who followed the light claimed it led to a hidden treasure.

The lighthouse was real. The treasure was not.

The structure was built by a clever trickster named Hu. He constructed the lighthouse from reflective mirrors and oil lamps—nothing magical, just carefully angled optics that made the light visible from miles away. Beneath the lighthouse, he dug a deep pit lined with mud and stakes.

Travelers who approached the lighthouse found a path clearly marked by lanterns. The path led directly to the pit. The first few steps were solid ground, luring the traveler forward. Then the ground softened. By the time the traveler realized they were sinking, the mud had already reached their knees.

The more they struggled, the deeper they sank.

Some travelers escaped by abandoning their packs and crawling back along the solid ground. But most clung to their belongings—and were swallowed whole.

The trickster watched from the treeline, collecting the abandoned packs of those who escaped and the bodies of those who did not.

---

## What This Fable Is About

This fable illustrates a **honeypot contract**—a malicious smart contract designed to lure users into depositing funds with the promise of profit, while containing hidden code that prevents withdrawal or steals deposited assets.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Lighthouse | Honeypot Contract | A contract that appears to offer arbitrage or profit opportunity |
| Golden light | Seemingly profitable function | The contract's code appears to allow extracting value |
| Marked path | Publicly visible vulnerability | The "bug" is intentionally visible to attract attackers |
| Solid ground first | Partial functionality | Some functions work as expected to build trust |
| Sinking mud | Hidden withdrawal lock | The code contains hidden conditions that prevent withdrawal |
| Struggling sinks deeper | Attempting withdrawal triggers more losses | Some honeypots drain additional funds when withdrawal is attempted |
| Abandoning packs to escape | Cutting losses | Recognizing the trap and abandoning deposited funds |
| Trickster collecting packs | Attacker harvesting funds | The contract creator collects all trapped deposits |

### Why This Story?

Honeypots exploit the greed and overconfidence of would-be attackers. The lighthouse metaphor captures the seductive nature of these traps: they offer something too good to be true, and the path to ruin is paved with initial signs of legitimacy.

### Further Reading

- wiki-web3: Analysis of a Honeypot Contract
- [HoneyPot Detector Tools](https://honeypot.is/)
- [Solidity Honeypot Techniques](https://medium.com/coinmonks/honeypots-in-solidity-5c5b96e9d5f3)
