---
title: "The One-Day Loan"
title_cn: "一日借款"
concept: "Flash Loan"
concept_cn: "闪电贷"
category: "other"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/闪电贷详解.md"
tags: [flash-loan, uncollateralized, atomic, arbitrage, liquidation, attack-vector]
---

# The One-Day Loan

> *Borrow ten thousand taels, use for one day, zero interest, but must be repaid before sunset.*

## The Story

Yunzhou City's money house launched an unprecedented service: the one-day loan.

The rules were extremely simple:
1. You could borrow any amount from the money house—one hundred taels, ten thousand taels, even one million taels.
2. No collateral required.
3. No credit check.
4. Interest was extremely low—almost negligible.
5. But there was one absolute condition: **you must repay principal plus interest before sunset that day. If you cannot repay, the loan automatically cancels, as if nothing ever happened.**

---

**Uses of One-Day Loans**

**Arbitrage**:
A merchant discovered East Market sold rice for one tael per pound, West Market for one tael and five cents. But he had no capital.

He borrowed a one-day loan: ten thousand taels.
Used ten thousand taels to buy rice at East Market, immediately sold at West Market for ten thousand five hundred taels.
Repaid ten thousand taels principal and ten taels interest; net profit four hundred ninety taels.

The entire process took only two hours.

**Liquidation**:
The money house's rule was: when collateral value fell below threshold, anyone could execute liquidation, acquiring collateral at a discount.

Liquidators had no ready funds. They borrowed a one-day loan: ten thousand taels.
Used ten thousand taels to repay a certain borrower on the verge of liquidation, acquiring collateral worth eleven thousand taels at a discount.
Immediately sold the collateral on the market for ten thousand eight hundred taels.
Repaid ten thousand taels principal and ten taels interest; net profit seven hundred ninety taels.

**Refinancing**:
Someone's loan at the original money house had a very high interest rate. Another money house could offer a lower rate, but the original loan had to be repaid first to release collateral.

They borrowed a one-day loan to repay the original loan, release collateral, then use the collateral to obtain a low-rate loan at the new money house, repaying the one-day loan.

---

**Dark Side of One-Day Loans**

One-day loans were not only arbitrage tools but also attack weapons.

**Price manipulation**:
An attacker borrowed a one-day loan: one million taels. Used this money to massively buy something in a small market, driving the price up tenfold. Then in another derivatives market, he shorted that same thing. When the one-day loan was repaid and his buying disappeared, prices crashed, and his short position profited.

**Governance attack**:
An attacker borrowed a one-day loan, temporarily obtaining massive funds, using this money to purchase an organization's voting power, passing a malicious proposal to transfer the organization's treasury to himself, then repaying the loan. The entire process was completed within one day.

**Protocol vulnerability exploitation**:
An attacker discovered a logical vulnerability in a protocol, but exploiting it required large amounts of funds. He borrowed a one-day loan to trigger the vulnerability, stole funds, then repaid the loan.

---

**Money House Risks**

You might ask: why is the money house willing to provide this service? What if the borrower cannot repay?

The answer: the money house is not afraid of borrowers failing to repay.

Because one-day loans have an "atomicity" guarantee: borrowing, using, and repayment must be completed in a single indivisible operation. If any step fails—such as the borrower not earning enough to repay—the entire operation automatically rolls back.

This means: the money house either recovers principal plus interest before sunset, or treats the loan as never having happened. The money house never loses money.

The real risk bearers are the rest of the protocol—the markets triggered by one-day loans, the contracts attacked. They have no automatic rollback protection.

---

Years later, one-day loans became a double-edged sword in Yunzhou City's financial system. An old money house manager said: "One-day loans themselves are neutral—they are just a tool. Used well, they make markets more efficient. Used badly, they make attackers stronger. The real problem is not one-day loans, but those unprepared protocols."

---

## What This Fable Is About

This fable illustrates **Flash Loans**—uncollateralized, uncredit-checked loans in DeFi where borrowing and repayment must occur within the same atomic transaction. If final repayment fails, the entire transaction rolls back, and the lender bears no risk.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| One-day loan | Flash Loan | Loan borrowed and repaid within a single atomic transaction |
| Any amount | No borrowing limit | Can borrow all pool liquidity (limited by pool size) |
| No collateral | Uncollateralized | No assets need to be locked as collateral |
| Extremely low interest | 0.09% fee (Aave) | Flash loan fees are typically extremely low to encourage use |
| Repay before sunset | Repay within same transaction | Borrowing and repayment must be completed within a single atomic operation |
| Cannot repay means cancel | Atomicity / transaction rollback | If final repayment fails, entire transaction reverts; state rolls back to pre-borrowing |
| Money house does not lose | Protocol zero risk | Flash loan providers (e.g., Aave) either receive repayment + fee or transaction rolls back |
| Arbitrage | Arbitrage | Exploiting price differences between markets; most common flash loan use |
| Liquidation | Liquidation | Using flash loan funds to execute liquidation, earning liquidation rewards |
| Refinancing | Collateral swap / refinancing | Using flash loans to switch collateral or reduce borrowing rates |
| Price manipulation | Price oracle manipulation | Using flash loan funds to temporarily manipulate prices in one market, profiting in another |
| Governance attack | Flash loan governance attack | Borrowing funds to temporarily acquire voting power, passing malicious proposals |
| Protocol vulnerability exploitation | Flash loan attack | Using flash loans to amplify attack scale, e.g., Cream Finance, Elephant Money, etc. |
| Atomicity guarantee | Transaction atomicity | EVM guarantees operations within a single transaction either all succeed or all roll back |

### Why This Story?

Flash loans are one of DeFi's most unique financial innovations—a mechanism impossible in traditional finance. They are simultaneously the most powerful arbitrage tools and the most common attack vectors.

The "one-day loan" metaphor for flash loans offers several intuitive advantages:
1. **Zero-risk lending**: Not repaid by sunset means never happened = atomic rollback
2. **Miracle of no collateral**: No credit needed = complete reliance on automated code execution
3. **Double-edged sword**: Arbitrage tool = attack weapon = flash loan's neutrality and necessity of protocol defense
4. **Protocol risk**: Attacked contracts have no rollback protection = essence of flash loan attacks

### Further Reading

- [wiki-web3: Flash Loans Explained](../../wiki-web3/concepts/闪电贷详解.md)
- [Aave Flash Loans](https://docs.aave.com/developers/guides/flash-loans)
- [Flash Loan Attacks: Analysis](https://insights.glassnode.com/defi-flash-loan-attacks/)
- [The Biggest Flash Loan Attacks in DeFi History](https://rekt.news/leaderboard/)
- [How to Protect Against Flash Loan Attacks](https://blog.openzeppelin.com/defending-against-flash-loan-attacks/)
