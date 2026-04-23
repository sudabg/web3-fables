---
title: "The Brand of the Faithless"
title_cn: "失信者的烙印"
concept: "Slashing Mechanism"
concept_cn: "Slashing 惩罚机制"
category: "consensus"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/权益证明-pos-共识机制.md"
tags: [consensus, pos, slashing, validator, penalty, byzantine]
---

# The Brand of the Faithless

> *Trust is bought with money; betrayal is repaid with money.*

## The Story

Yunzhou City's stakers' roulette operated well, but the sages soon discovered a problem: if the cost of a keeper's misbehavior was only "losing future earnings," then in certain situations misbehavior remained profitable.

For example, a keeper simultaneously participated in a competing ledger system in another city. If he disrupted consensus here, causing Yunzhou City's ledger chaos, he could earn huge returns from the other side. Even if he lost his security deposit here, the other side's earnings might exceed the loss.

This was called "external incentive conflict"—the gains from misbehavior might exceed the losses from punishment.

---

**Introduction of the Branding System**

To solve this problem, the sages introduced the "branding system."

The core of the branding system: misbehavior not only cost money but also left permanent marks.

Specific rules:

1. **Light brand**: If a keeper went offline briefly due to network failure or operational error, and failed to confirm blocks in time. A small portion of his security deposit would be deducted as punishment, but no brand was left.

2. **Medium brand**: If a keeper was discovered voting twice in the same round—such as simultaneously supporting two conflicting blocks. This was "double voting." A larger portion of his security deposit would be deducted, and a "yellow brand" would be left. The yellow brand did not permanently ban participation, but reduced the keeper's weight for a period.

3. **Heavy brand**: If a keeper was discovered doing "surround voting"—a more complex attack where contradictory votes were cast at different times to disrupt consensus. Nearly all of his security deposit would be confiscated (up to the entire stake), and a "red brand" would be left. The red brand meant he could almost never participate in ledger keeping again.

Most critically: brands were public, permanent, and irreversible. Anyone could query whether a keeper had brands, and what type and reason.

---

**Deterrence of Brands**

The branding system completely changed the incentive structure of the stakers' roulette.

Under the old system, a keeper considered: "If I misbehave, how much security deposit will I lose?"

Under the new system, he had to consider: "If I misbehave, I will lose my security deposit and be permanently marked as faithless. Even if I have gains in another city, my reputation here is ruined."

For professional ledger institutions, reputation was everything. A branded institution, even if it changed names or security deposits, could still have its brand history traced. Clients would not delegate funds to an institution with red brand history.

A sage said: "Monetary punishment solves the 'economic incentive' problem. Brands solve the 'identity and reputation' problem. Combined, they make the system truly unbreakable."

---

**False Accidents and Appeals**

The branding system also had its dark side.

One keeper's node went offline for three days due to a data center fire. According to rules, he was deducted part of his security deposit for "continuous inactivity." He appealed: "This was force majeure, not my fault."

The appeal committee reviewed and determined the fire was indeed force majeure, refunding his security deposit. But the brand record still carried an annotation: "Once offline for three days due to force majeure." This annotation did not affect his weight, but anyone querying his history could see it.

The keeper was dissatisfied: "Since you determined I was not at fault, why not delete this record?"

The committee answered: "We cannot delete records, because records are carved in stone. But we can add annotations explaining the truth. History cannot be changed, but history can be interpreted."

---

## What This Fable Is About

This fable illustrates **Slashing**—the economic punishment for misbehaving validators in PoS consensus. Slashing not only confiscates funds but also reduces validators' effective balance, affects their reputation, and leaves permanent records on-chain.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| External incentive conflict | External attack motivation | Attackers may earn more from off-chain than they lose from staking (e.g., shorting, competitor bribery) |
| Light brand | Inactivity Leak / offline penalty | Validators not participating in consensus for extended periods slowly bleed effective balance but do not receive slashable records |
| Medium brand | Slashing: Double Vote | Voting for two different blocks in the same slot. 1 ETH immediate slash; remaining portion gradually slashed over 36 days |
| Heavy brand | Slashing: Surround Vote | Surround voting (more complex double signing). More severe punishment; may slash entire effective balance |
| Yellow / red brand | Punishment levels | Different severity slashable behaviors correspond to different slashing proportions |
| Public and permanent brands | Slashing record immutability | Slashing events are permanently recorded on-chain; anyone can query |
| Professional institution reputation | Validator reputation risk | For institutional validators, being slashed severely damages commercial credibility |
| Appeals and annotations | Force majeure and rule rigidity | On-chain rules execute automatically; cannot be rolled back for "non-malicious" reasons. But off-chain explanations are possible |
| Carved in stone | Blockchain immutability | Once confirmed on-chain, facts cannot be deleted; only information can be supplemented |

### Why This Story?

Slashing is the core pillar of PoS security, but many people only understand "losing money," not the dimensions of "reputation" and "permanence."

The "brand" metaphor for Slashing offers several intuitive advantages:
1. **Economic + reputation punishment**: Money loss + permanent mark = complete deterrence system
2. **Public shame**: Brands publicly queryable = transparent on-chain slashing records
3. **Rule rigidity**: Force majeure still leaves records = blockchain's automatic execution and non-appealability

### Further Reading

- [wiki-web3: Proof of Stake Consensus Mechanism](../../wiki-web3/concepts/权益证明-pos-共识机制.md)
- [Ethereum Slashing Specifications](https://github.com/ethereum/consensus-specs/blob/dev/specs/phase0/beacon-chain.md#slashing)
- [Slashing Risks for Validators](https://lighthouse-book.sigmaprime.io/slashing-protection.html)
- [Penalties and Rewards in Ethereum PoS](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/)
