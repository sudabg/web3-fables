---
title: "The Cooling Chamber"
title_cn: "冷却室"
concept: "Timelock Governance"
concept_cn: "时间锁与治理"
category: "governance"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/时间锁与治理.md"
tags: [governance, timelock, dao, proposal, delay, emergency]
---

# The Cooling Chamber

> *Decisions made in passion often need to sit in an ice room for a while.*

## The Story

Yunzhou City's merchant guild used to make decisions simply: the guild master convened everyone for a meeting, discussed, voted, decided on the spot, and executed immediately.

This method was fast, but it caused several serious accidents.

---

**First Accident: Passionate Decision**

One year, rumors suddenly spread that all spice ships from the Eastern Sea had sunk. The guild held an emergency meeting and, in panic, voted to "immediately sell all spice inventory at current prices."

The decision was executed immediately. The guild sold all inventory at low prices. Three days later, the news was proven false—the spice ships had not sunk at all. Market spice prices instantly doubled. The guild lost half a year's profit due to panic selling.

Post-mortem, the vice president said: "If we had waited three more days for confirmation before deciding, we wouldn't have lost."

The master sighed: "But the atmosphere in the meeting room at the time left no room for calm thought."

---

**Second Accident: Malicious Raid**

Another year, an outsider merchant joined the guild. At an ordinary meeting, he suddenly proposed a motion: "Amend guild bylaws to allow the guild master alone to decide transactions over ten thousand taels."

The motion itself was absurd—it amounted to giving the guild's financial power to one person. But the outsider had bribed over a dozen small members in advance, who suddenly voted collectively in favor. Most members had not reacted before the vote was over.

Under the old rules, the motion took effect immediately. The guild nearly fell under one person's control. Fortunately, several old members took overnight action to block execution before the bylaws took effect—but this should never have happened.

---

**Birth of the Cooling Chamber**

After these accidents, the guild introduced the "cooling chamber" system.

The rules were:

1. Any major decision (involving amounts over one thousand taels, or amending bylaws), after passing the vote, would not take effect immediately.

2. The decision would be sent to the "cooling chamber"—a public, transparent waiting area. In the cooling chamber, the decision's content was visible to all; anyone could review, discuss, and raise objections.

3. The cooling period was fixed at seven days. During these seven days, if anyone discovered problems with the decision, they could initiate an "emergency veto." If more than one-third of members supported the veto, the decision would be canceled.

4. After seven days, if not vetoed, the decision automatically took effect.

---

**Effects of the Cooling Chamber**

After introducing the cooling chamber, the guild's decision quality significantly improved.

- Passionate decisions were filtered: seven days was enough for market emotions to settle and for rumors to be proven false or true.
- Raid attacks were blocked: even if malicious motions passed, the seven-day cooling period gave other members enough time to organize opposition.
- Errors were discovered in time: several times during the cooling period, hidden vulnerabilities were discovered in motions—seemingly harmless clauses that actually allowed massive power abuse. These vulnerabilities were discovered and fixed during the cooling period.

But the cooling chamber also had costs: some truly urgent decisions were forced to wait seven days. One year, floods came; the guild needed emergency appropriations to repair dikes. But under the rules, the appropriation decision had to wait seven days. The dikes breached during the wait.

The guild later made adjustments: establishing an "emergency channel"—with agreement from over two-thirds of members, certain emergency decisions could skip the cooling chamber. But emergency channel use was permanently recorded and subject to post-hoc review.

---

Years later, the cooling chamber system was adopted by all major organizations in Yunzhou City. An old member said: "The cooling chamber is not delay; it is giving reason a chance. Most catastrophic decisions are made in moments of hot blood. The cooling chamber gives hot blood time to cool."

---

## What This Fable Is About

This fable illustrates **Timelock governance mechanisms**—common safety measures in DeFi protocols. Major governance decisions (like modifying protocol parameters, upgrading contracts, transferring funds) must wait for a period (e.g., 2-7 days) after voting before execution, giving users time to react and exit.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| On-the-spot decision and execution | Governance without timelock | Voting takes effect immediately; extremely high risk |
| Panic selling | Emotional governance attack | Decisions made during market panic are often wrong |
| Malicious raid | Governance flash loan attack / 51% voting raid | Attackers temporarily acquire massive voting power to pass malicious proposals |
| Cooling chamber | Timelock contract | After voting passes, proposals enter a waiting queue with delayed execution |
| Seven-day cooling period | Delay parameter | Common values are 2-7 days, sufficient for users to detect anomalies and exit |
| Emergency veto | Opposition / cancellation mechanism | Users can withdraw funds or initiate opposition during the delay period |
| Hidden vulnerabilities discovered | Community audit window | The delay period gives the community time to review proposal code and impact |
| Emergency channel | Multi-sig / emergency pause | In extreme cases, trusted multi-sigs can skip timelock to execute emergency actions |
| Permanent record | On-chain transparency | All operations are recorded on-chain; post-hoc auditability |
| Flood dike repair | Timelock vulnerability | True emergencies may miss optimal handling timing due to timelock |

### Why This Story?

Timelock is DeFi governance's last line of defense, but many protocols omit it (or set extremely short delays) due to inconvenience. The 2022 Beanstalk attack (governance flash loan) was a bloody lesson—attackers acquired voting power, passed proposals, and executed them in a single transaction, stealing $180 million.

The "cooling chamber" metaphor for timelock offers several intuitive advantages:
1. **Emotional filtering**: Hot blood cooling = preventing panic and FOMO-driven decisions
2. **Defense against raids**: Seven-day wait = giving community time to organize opposition
3. **Tradeoffs of emergency channels**: Skipping the cooling chamber = double-edged sword of multi-sig/emergency power

### Further Reading

- [wiki-web3: Timelock and Governance](../../wiki-web3/concepts/时间锁与治理.md)
- [OpenZeppelin: Timelock Controller](https://docs.openzeppelin.com/contracts/4.x/governance#timelock)
- [Beanstalk Governance Attack Analysis](https://rekt.news/beanstalk-rekt/)
- [DeFi Governance Best Practices](https://medium.com/@aave/governance-best-practices-9d3e7d1e0b1c)
