---
title: "The Weighted Democracy"
title_cn: "砝码民主"
concept: "Token Voting Governance"
concept_cn: "代币投票治理"
category: "governance"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/代币投票治理.md"
tags: [governance, dao, token-voting, quadratic-voting, delegation, plutocracy]
---

# The Weighted Democracy

> *One person, one vote is the ideal. One coin, one vote is the reality. The problem with reality: the more money you have, the heavier your voice.*

## The Story

After abolishing the guild master's dictatorship, Yunzhou City's merchant guild tried a "one person, one vote" democratic system. Every member, regardless of contribution size, had one vote.

This system quickly exposed problems.

---

**The Dilemma of One Person, One Vote**

The guild had two major merchants, each contributing one hundred thousand taels, accounting for 80% of total guild funds. There were also two hundred small merchants, each contributing a few hundred taels, totaling only 20%.

In a vote on "whether to increase membership fees," two hundred small merchants passed the "massively increase fees" proposal with a 200:2 overwhelming majority. The two major merchants' opposition was ineffective.

Result: the two major merchants exited the guild, taking 80% of funds. The guild instantly fell into financial crisis.

The vice president reflected: "One person, one vote protected the small but drove away the big. Without the big, the small have nothing to gain."

---

**Introduction of Weighted Voting**

The guild introduced a "weight voting" system: voting weight was proportional to contribution. You contributed how much silver, you had how much weight.

Under the new system, the two major merchants held 80% of weight; two hundred small merchants held 20%. Any major decision was dominated by the major merchants' opinions.

This system solved the "big players leaving" problem but brought new problems:

- Small merchants' opinions were almost ignored. Even if two hundred small merchants unanimously opposed, as long as the two major merchants favored it, the proposal passed.
- The guild became an organization where "two major merchants called the shots"; democracy existed in name only.
- Worse, external capital could buy weight to manipulate guild decisions.

---

**Square Weight Experiment**

A mathematician named Dela proposed a compromise: "square weights."

The rule: voting weight was not proportional to contribution, but proportional to the square root of contribution.

Example:
- Someone contributing 100 taels had weight = √100 = 10
- Someone contributing 10,000 taels had weight = √10,000 = 100

Note: contribution differed by 100 times, but weight only differed by 10 times. Those who contributed more still had advantages, but advantages were "compressed."

Under this system:
- Two major merchants (each contributing 100,000 taels) total weight = 2 × √100,000 ≈ 632
- Two hundred small merchants (averaging 100 taels) total weight = 200 × √100 = 2,000

Small merchants' total weight actually exceeded major merchants! This meant small merchants, if united, could counterbalance major merchants. But major merchants were still much stronger than any single small merchant—their individual influence remained significant.

---

**Delegation System**

But square weights had a practical problem: not every small merchant had time and knowledge to study every proposal. Often, they did not even know what they voted for.

The guild introduced a "delegation" system: small merchants could delegate their weight to a representative they trusted. The representative voted with pooled weight. Small merchants could withdraw delegation anytime and vote themselves.

This system made professional governance possible. Some people who made studying proposals their profession emerged—they were called "governance experts." Small merchants delegated weight to governance experts; experts voted with professional knowledge. In return, governance experts received compensation from the guild's governance rewards.

---

**External Attacks**

The weighted voting system's greatest enemy came from outside.

One year, an external consortium wanted to control the guild. They had no long-term intention of operating the guild—they only wanted to pass one malicious proposal through a single vote to empty the guild's treasury.

Under the old system, this required purchasing over 50% of weight—extremely costly.

But the external consortium discovered a vulnerability: they could borrow large amounts of weight, vote, transfer funds, then return the borrowed weight. The entire process could be completed within one day.

This was called a "flash weight attack." The guild nearly went bankrupt.

Afterward, the guild added a rule to voting: "Voting weight must be locked for a period (e.g., three days) before the vote; it cannot be borrowed or transferred during the voting period."

This simple modification completely eliminated the possibility of flash weight attacks.

---

Years later, Yunzhou City's weighted democracy continued to evolve. Some said it was not fair enough; others said it was the most realistic option. An old merchant summarized: "There is no perfect voting system. One person, one vote drives away capital; one coin, one vote becomes oligarchy. Square weights are a compromise, but they at least give 'united majorities' a chance to counter 'wealthy minorities.'"

---

## What This Fable Is About

This fable illustrates **token voting governance**—the most common decision-making mechanism in DeFi protocols and DAOs. It explores the evolution from "one person, one vote" to "one coin, one vote" to "quadratic voting," and practical issues like delegation and flash loan attacks.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| One person, one vote | Traditional democracy | Each address gets one vote; coin holdings not considered |
| Big merchants driven away | Capital flight risk | If large holders' interests cannot be protected, they exit the protocol, causing liquidity drain |
| Weight voting | Token-weighted voting | Voting weight proportional to coin holdings. Most common DAO governance mechanism |
| Oligarchy | Plutocracy | Wealthy holders control decisions; small holders lose influence |
| External capital buying weight | Governance token acquisition | Attackers purchase large amounts of governance tokens to pass malicious proposals |
| Square weights | Quadratic voting | Voting weight = √balance. Balances large holders' influence and small holders' collective power |
| Delegation | Vote delegation | Token holders delegate voting power to representatives (e.g., Compound's Governance Bravo) |
| Governance experts | Governance contributors / delegates | Professional governance participants who study proposals and vote on behalf of delegators |
| Flash weight attack | Flash loan governance attack | Attackers borrow funds to temporarily acquire voting power, pass malicious proposals |
| Weight lock before voting | Voting delay / vote locking | Requires voting power to be held before proposal creation; prevents flash loan attacks |
| Three-day lock | Common timelock parameters | E.g., Compound's voting delay is 1 block, but many protocols have extended to several days |

### Why This Story?

Token voting is the core of DAO governance but also one of the most criticized mechanisms—Vitalik Buterin and others have pointed out that "one coin, one vote" is essentially plutocracy.

The "weighted democracy" metaphor for token voting offers several intuitive advantages:
1. **Intuitive inequality**: Weight heaviness = voting weight; readers immediately understand "money = voice"
2. **Quadratic voting visualization**: Square root compression = giving majorities a chance to counter wealthy minorities
3. **Flash loan attack concretization**: Borrowing weight to vote then returning = flash loan governance attack

### Further Reading

- wiki-web3: Token Voting Governance
- [Vitalik: Moving Beyond Coin Voting Governance](https://vitalik.ca/general/2021/08/16/voting3.html)
- [Quadratic Voting: How Mechanism Design Can Radicalize Democracy](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2003531)
- [Beanstalk Flash Loan Governance Attack](https://rekt.news/beanstalk-rekt/)
- [Compound Governance](https://compound.finance/governance)
