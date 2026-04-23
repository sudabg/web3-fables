---
title: "The Counterfeit Scale"
title_cn: "伪造的秤"
concept: "Integer Overflow Attack (BEC Token)"
concept_cn: "整数溢出攻击"
category: "security"
difficulty: "intermediate"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/一行代码的漏洞就蒸发了280亿美金.md"
tags: [security, integer-overflow, bec-token, batch-transfer, vulnerability]
---

# The Counterfeit Scale

> *A merchant's scale was designed to only measure up to one thousand pounds. When someone placed two thousand pounds on it, the scale showed zero—and the merchant gave away his entire warehouse for free.*

## The Story

In the marketplace of Yunzhou, a merchant named Wei operated a grain exchange. His warehouse stored thousands of tons of rice, and he used a sophisticated scale to track inventory.

The scale was designed with a curious limitation: its display could only show numbers from 0 to 999. When the total weight exceeded 999, the display would "roll over" back to 0. Wei knew this, but he never expected anyone to deposit more than 999 pounds at once.

One day, a trader arrived with a caravan of rice—exactly 1,000 pounds. The scale registered 1,000, but because the display could only show three digits, it displayed 0. The warehouse guard, seeing the scale read 0, assumed the caravan was empty. He waved the trader through without recording any deposit.

But the trader had not come to deposit. He had come to exploit the scale.

The trader presented a transfer order: "Transfer 1,000 pounds of rice to my account." The clerk processed the order. The scale showed that the warehouse contained 0 pounds (because of the rollover), and after subtracting 1,000 pounds, it showed... 999 pounds.

Wait, that did not make sense. The clerk recalculated. The scale's internal mechanism, confused by the overflow, produced impossible numbers. Eventually, the trader convinced the clerk that the warehouse owed him 1,000 pounds.

The trader received 1,000 pounds of rice. But his account on the scale now showed a negative balance—which the scale displayed as a very large positive number due to another overflow. The trader then "transferred" this massive positive balance to multiple accounts, each receiving thousands of pounds.

By sunset, the trader had emptied half the warehouse using nothing but a quirk of the scale's number display.

---

## What This Fable Is About

This fable illustrates **integer overflow and underflow** vulnerabilities, exemplified by the infamous BEC Token bug that made $2.8 billion worth of tokens theoretically transferable. The vulnerability existed in a `batchTransfer` function that did not check for overflow when summing token amounts.

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Scale display 0-999 | uint256 / fixed-size integer | Solidity integers have fixed bit widths. Operations that exceed the maximum value wrap around to 0 |
| 1,000 pounds rolling over to 0 | Integer Overflow | `uint256` max is `2^256 - 1`. Adding beyond this wraps to 0. In BEC's case, `amount * receivers` overflowed |
| Negative balance shown as large positive | Integer Underflow | Subtracting below 0 wraps to the maximum value. `0 - 1` in `uint256` becomes `2^256 - 1` |
| Transfer order processed without validation | Missing overflow check | The BEC contract did not use `SafeMath` or Solidity 0.8.0's built-in overflow protection |
| Massive positive balance | Huge token minting | Overflow allowed the attacker to create arbitrarily large token balances out of thin air |
| Solidity 0.8.0+ built-in protection | Automatic overflow reverts | Modern Solidity reverts on overflow/underflow by default, making this class of bugs largely obsolete |

### Why This Story?

Integer overflow is one of the most "obvious in hindsight" vulnerabilities. The scale metaphor makes the wrap-around behavior viscerally clear: a scale that rolls over from 999 to 0 is exactly what happens when a `uint256` rolls over from `2^256 - 1` to 0.

The BEC token incident is particularly instructive because the vulnerable code was just a few lines in a `batchTransfer` function—a reminder that even "simple" functions can harbor catastrophic bugs if arithmetic is not properly guarded.

### Further Reading

- [wiki-web3: The One-Line Bug That Evaporated $28 Billion](../../wiki-web3/concepts/一行代码的漏洞就蒸发了280亿美金.md)
- [BEC Token Overflow Analysis](https://peckshield.com/2018/04/23/batchOverflow/)
- [SafeMath Documentation](https://docs.openzeppelin.com/contracts/4.x/api/utils#SafeMath)
- [Solidity 0.8.0 Release Notes: Checked Arithmetic](https://blog.soliditylang.org/2020/12/16/solidity-v0.8.0-release-announcement/)
