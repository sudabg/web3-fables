---
title: "The Seven Gates"
title_cn: "七道门"
concept: "Common Solidity Security Vulnerabilities"
concept_cn: "Solidity 常见安全漏洞概述"
category: "security"
difficulty: "beginner"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/solidity智能合约常见安全漏洞概述.md"
tags: [security, solidity, vulnerabilities, checklist, audit]
---

# The Seven Gates

> *A fortress with seven gates. Each gate guards against a different kind of intruder. Leaving any one unguarded is leaving the fortress unguarded.*

## The Story

In the ancient kingdom of Yunzhou, the imperial treasury was protected by seven gates. Each gate was designed by a different master engineer, and each guarded against a specific type of threat.

**The First Gate: Overflow**
This gate used a counting mechanism that could only count up to a certain number. When the count exceeded the limit, it wrapped around to zero. An attacker discovered that by deliberately triggering the overflow, he could reset the treasury's balance to zero—making it appear as though nothing had ever been deposited.

**The Second Gate: Access Control**
This gate was supposed to check whether the person entering had the proper credentials. But due to a design oversight, the credential checker could be bypassed by simply not presenting any credentials at all. Anyone could walk through.

**The Third Gate: Randomness**
This gate relied on "random" patterns to determine who could pass. But the randomness was generated from predictable sources—like the current time of day. An attacker who monitored the patterns could predict exactly when the gate would open.

**The Fourth Gate: Delegate**
This gate allowed trusted messengers to pass through on behalf of others. But the gate did not verify whether the messenger was truly authorized. A clever intruder disguised himself as a messenger and walked right in.

**The Fifth Gate: Denial of Service**
This gate could be jammed from the outside. By flooding the entrance with thousands of fake requests, an attacker could prevent legitimate users from ever reaching the treasury.

**The Sixth Gate: Front-Running**
This gate processed requests in the order they were received. But a fast courier could see requests in transit, place his own request ahead of them, and profit from the advance knowledge.

**The Seventh Gate: Logic**
This was the most subtle gate. Its lock had a logical flaw: under a very specific combination of conditions, the "locked" and "unlocked" states could be simultaneously true. An attacker who studied the gate long enough found that combination and simply walked through.

The treasury fell not because any single gate was weak, but because the defenders assumed that seven gates meant seven layers of safety. They did not realize that a determined attacker needs only find *one* open gate.

---

## What This Fable Is About

This fable provides an overview of the **most common categories of vulnerabilities in Solidity smart contracts**: integer overflow/underflow, access control failures, weak randomness, delegate call vulnerabilities, denial of service, front-running, and logical errors.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| First Gate: Overflow | Integer Overflow/Underflow | Arithmetic operations that exceed type limits wrap around. In Solidity <0.8.0, this can be exploited to manipulate balances |
| Second Gate: Access Control | Missing Access Control | Functions that should be restricted (like `selfdestruct` or privileged operations) lack proper `require(msg.sender == owner)` checks |
| Third Gate: Randomness | Weak Randomness Sources | Using `block.timestamp`, `blockhash`, or `keccak256` on predictable values as randomness sources can be manipulated by miners or observers |
| Fourth Gate: Delegate | Delegate Call Vulnerabilities | Improper use of `delegatecall` can allow attackers to execute arbitrary code in the context of the vulnerable contract |
| Fifth Gate: Denial of Service | DoS via Gas Limits / Reverts | External calls that revert can block contract functionality. Unbounded loops can hit block gas limits |
| Sixth Gate: Front-Running | Transaction Ordering Attacks | Mempool visibility allows attackers to see pending transactions and insert their own with higher gas prices to execute first |
| Seventh Gate: Logic | Business Logic Flaws | Complex state machines with edge cases where contradictory states coexist, allowing unintended execution paths |
| Seven gates | Defense in Depth | Security requires guarding against *all* attack vectors, not just the obvious ones |

### Why This Story?

Smart contract security is not about finding "the one bug"—it is about systematically checking every possible attack surface. The Seven Gates metaphor makes this concrete: a treasury with six perfect gates and one broken gate is still a breached treasury.

### Further Reading

- wiki-web3: Common Solidity Security Vulnerabilities Overview
- [SWC Registry](https://swcregistry.io/)
- [ConsenSys Smart Contract Best Practices](https://github.com/Consensys/smart-contract-best-practices)
- [Solodit Checklist](https://solodit.xyz/checklist)
