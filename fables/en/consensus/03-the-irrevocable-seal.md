---
title: "The Irrevocable Seal"
title_cn: "不可撤销的印章"
concept: "Block Finality"
concept_cn: "区块最终性"
category: "consensus"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/权益证明-pos-共识机制.md"
tags: [consensus, finality, checkpoint, epoch, reorg, probabilistic]
---

# The Irrevocable Seal

> *Stamping a document is only the beginning. Only when the ink seeps into the paper fibers does it truly take effect.*

## The Story

Yunzhou City's document system had a tradition after stamping: waiting.

---

**Instant Seal vs. Final Seal**

Under the old system, documents took effect immediately after stamping. But there was a problem: if the seal was later discovered to be forged, or if the stamper was proven unauthorized, what happened to already-executed documents?

The answer: withdrawal. But withdrawing already-executed documents was extremely difficult—for example, completed transactions, transferred property—how to reverse?

The new system introduced two types of seals:

**Instant Seal**: After stamping, the document could immediately be referenced and read. But it had a hidden property—it could be "replaced." If subsequent checks discovered problems, the instant seal could be replaced by a corrected document.

**Final Seal**: After a document received enough seals (confirmations from different officials), and enough time had passed, it became "irrevocable." Once the final seal was applied, the document was permanently effective; no power could modify or withdraw it.

---

**From Instant to Final**

The process from instant seal to final seal was:

1. The first official stamped (proposal). The document entered "instant" status.
2. Over the following period, other officials reviewed the document; if they agreed, they stamped their confirmation.
3. When the number of confirmation seals reached the threshold (say, two-thirds of total officials), the document entered "final" status.

The key was the "period" in step two. During this period, it was possible for two contradictory documents to both receive partial official confirmations. For example:

- Document A received 40% of officials' confirmation.
- Document B (contradicting A) received 35% of officials' confirmation.

If the system stopped now, neither A nor B reached the two-thirds threshold, so neither would finally take effect. Officials would continue confirming until one reached the threshold.

But what if a malicious official group simultaneously confirmed both A and B (double confirmation), trying to confuse the system?

The answer: double-confirming officials would be discovered and punished—their confirmation qualifications would be revoked, and all their previous confirmations would become invalid. Thus, the system would eventually converge to a single final document.

---

**Probability vs. Determinism**

Yunzhou City's old ledger (based on computational competition) had a different finality model:

Under the old system, after a document was stamped, it was "likely" correct, but not "absolutely" correct. Theoretically, if someone controlled over half the computational power, they could rewrite history—replacing already-stamped documents. But as documents were covered by more and more subsequent documents, the cost of rewriting grew exponentially.

Under the new system (based on staking consensus), finality was deterministic: once a document received enough official confirmations and reached final status, it was absolutely unchangeable. No probability estimation was needed; no assumption that "no one controls over half the power" was required.

In numbers:
- Old system: A transaction was "almost impossible" to roll back after six blocks. But "almost impossible" is not "absolutely impossible."
- New system: A transaction reached final status after about twelve minutes (two epochs). Once final, absolutely irreversible.

---

**The Ghost of Rollback**

Even under the new system, before the final seal was applied, "rollback" could still occur.

If an official's node had a software bug, or network partitioning caused him to see a different world from other officials, he might confirm an "erroneous" document. In such cases, the system would briefly fork—two versions of the ledger coexisting temporarily.

But this fork was temporary. When the network recovered and officials resynchronized, they would select the "heavier" version to continue according to rules, discarding the other. Documents confirmed during the fork that were ultimately not selected would become invalid.

This is why "instant seal" does not equal "final seal." After the instant seal is applied but before the final seal, everything is still variable.

---

Years later, Yunzhou City's merchants formed a habit: small transactions trusted instant seals; large transactions waited for final seals. An old accountant said: "Instant seals let you run faster; final seals let you sleep more soundly. Smart traders know when to seek speed and when to seek stability."

---

## What This Fable Is About

This fable illustrates **Block Finality**—the property that transactions, once confirmed, cannot be rolled back. PoW (like Bitcoin) provides "probabilistic finality," while PoS (like Ethereum) provides "deterministic finality" through Casper FFG.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Instant seal | Block inclusion / block confirmation | Transaction is packaged into a block; can be referenced but not yet final |
| Final seal | Finalized block | Through Casper FFG and other finality gadgets, blocks confirmed by enough validators are irreversible |
| Official confirmation | Validator attestation | Validators vote to confirm block validity |
| Two-thirds threshold | Supermajority | In Ethereum PoS, 2/3 of validators must vote to confirm for a block to reach finality |
| Double confirmation | Double vote / slashable behavior | Validators voting for two contradictory blocks are slashed |
| Punish, revoke qualification | Slashing | Double-voting validators are punished; their votes become invalid |
| Converge to single document | Consensus finality | The system guarantees eventual convergence to a single, consistent final state |
| Old system probabilistic finality | PoW probabilistic finality | Bitcoin, etc. More blocks covering a transaction exponentially reduce rollback probability, but theoretically never reach 100% |
| New system deterministic finality | PoS deterministic finality | Ethereum PoS. After two epochs (~12.8 minutes), blocks are absolutely irreversible |
| Six blocks later | Bitcoin 6 confirmations | In Bitcoin, six block confirmations are considered "sufficiently secure" (~1 hour) |
| Twelve minutes later | Ethereum PoS finality | In Ethereum PoS, transactions finalize after ~12.8 minutes (2 epochs) |
| Fork and rollback | Reorg / fork | Before finality is reached, temporary forks may occur; shorter chains are abandoned |
| Network partition | Network partition | Network splits cause some validators to see different states, potentially creating forks |
| Small trust instant seal | Daily use accepting confirmation | Ordinary transfers are considered valid after being packaged into blocks |
| Large wait for final seal | Large transactions waiting for finality | Exchange deposits, cross-chain bridges typically wait for multiple confirmations or finality |

### Why This Story?

Finality is the core guarantee of blockchain security, but the difference between "probabilistic finality" and "deterministic finality" is vague for many users.

The "instant seal vs. final seal" metaphor for finality offers several intuitive advantages:
1. **Two-phase confirmation**: Instant seal (confirmation) → final seal (finalization) = two stages of transactions
2. **Probability vs. determinism**: Old system "almost impossible" to roll back vs. new system "absolutely impossible"
3. **Temporary nature of forks**: Officials seeing different worlds = temporary forks caused by network partitioning
4. **Practical application**: Small seeks speed, large seeks stability = different scenarios' different finality needs

### Further Reading

- [wiki-web3: Proof of Stake Consensus Mechanism](../../wiki-web3/concepts/权益证明-pos-共识机制.md)
- [Ethereum Finality](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/#finality)
- [Casper FFG Paper](https://arxiv.org/abs/1710.09437)
- [Probabilistic vs Deterministic Finality](https://medium.com/mechanism-labs/finality-in-blockchain-consensus-7d963b5f9d5e)
- [Bitcoin Confirmations](https://en.bitcoin.it/wiki/Confirmation)
