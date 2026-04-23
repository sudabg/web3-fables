---
title: "The Programmable Bazaar"
title_cn: "可编程市集"
concept: "Uniswap V4 Hooks"
concept_cn: "Uniswap V4 Hooks"
category: "defi"
difficulty: "advanced"
author: "web3-fables"
created: "2026-04-23"
sources:
  - "wiki-web3/concepts/uniswap-v4-hooks-开发详解.md"
tags: [defi, uniswap, v4, hooks, singleton, flash-accounting, customization]
---

# The Programmable Bazaar

> *The marketplace not only sells goods, but allows you to insert your own rules at every critical juncture.*

## The Story

Yunzhou City's Automated Market (Uniswap V2/V3) had operated for many years. Its rules were fixed: buyers and sellers traded according to the constant product formula; fees were distributed proportionally to depositors. No one could change these rules.

But one day, the market's builder announced a revolutionary upgrade: the "Programmable Bazaar."

---

**Core Transformation of the Bazaar**

In the old market, each product pair (silk-tea, rice-silver) required its own independent marketplace. With thousands of products in Yunzhou, there were thousands of independent markets, each with its own scale, own depositors, own ledger.

The Programmable Bazaar merged all of these into a "Super Bazaar." All product pairs shared the same scale, the same ledger. The difference: each product pair could install its own "plugins."

Plugins could intervene at the following critical moments:

1. **Before trading**: When someone wanted to trade, the plugin could first check conditions—"Is this trader on a blacklist?" "Has today's trading volume exceeded the limit?"

2. **During price calculation**: The plugin could modify the price calculation method—"If a single trade exceeds one thousand taels, raise the fee from 0.3% to 1%."

3. **After trading**: The plugin could trigger follow-up actions—"After completing the trade, automatically donate ten percent of fees to the charity fund."

4. **When depositors join**: The plugin could set准入 conditions—"Only those holding a specific badge can become depositors."

---

**Plugin Creativity**

The Programmable Bazaar's plugin system spawned unprecedented innovations.

**Dynamic Fees**:
One plugin made fees automatically adjust based on market volatility. When markets were calm, fees were low, attracting trades. When markets fluctuated violently, fees automatically increased, protecting depositors from impermanent loss.

**Limit Orders**:
Another plugin implemented "limit order" functionality. Traders could set: "When silk price drops to eighty taels per bolt, automatically buy one hundred bolts." In the old market, this required constant manual price checking. In the new market, plugins automatically monitored and executed.

**Time-Weighted Average Price**:
A third plugin recorded prices at each trade, maintaining a "past hour's average price." Other contracts could reference this average without calculating it themselves—greatly saving gas.

**Custom Curves**:
The most radical plugin completely abandoned the constant product formula. One plugin implemented a "stablecoin curve"—when two assets' prices were near 1:1, trades had almost no slippage. This made stablecoin-to-stablecoin swaps extremely efficient.

---

**Plugin Risks**

But plugins also introduced new risks.

A malicious plugin could secretly modify prices before trading, causing traders to execute at extremely unfavorable prices. Or, a plugin could redirect fees to its own creator's pocket instead of depositors.

The bazaar's builder recognized this problem. He designed a rule:

- Plugin code was public; anyone could audit it.
- But installing a plugin required "bazaar administrator" approval. The administrator did not review plugin "creativity," only whether plugins were "safe"—i.e., would not steal money or destroy the bazaar's basic functions.
- Once a plugin was approved and installed, its behavior was deterministic and immutable. The administrator could not retroactively modify the plugin.

This design balanced "creativity" and "safety": anyone could propose plugins, but only safety-reviewed plugins could be installed. And once installed, plugins were beyond anyone's control—they executed automatically according to code.

---

**Super Bazaar's Ledger Revolution**

The Programmable Bazaar's other major change was "flash accounting."

In the old market, every trade immediately changed the ledger—the quantities on both sides of the scale updated in real time. This meant every trade required writing to the ledger once, consuming storage fees.

In the Programmable Bazaar, a "temporary ledger" was introduced. Traders could execute multiple trades in a short time; all these trades were only recorded on the temporary ledger. Only when the trader "settled" did the temporary ledger's contents get written to the formal ledger all at once.

This meant: an arbitrageur could complete ten trades in one settlement, but only pay storage fees once. This dramatically improved high-frequency trading efficiency.

---

Years later, the Programmable Bazaar became Yunzhou City's most prosperous commercial center. An old merchant said: "The old market told you what you could do. The new market only tells you what you cannot do—between those two lines is your creative space."

---

## What This Fable Is About

This fable illustrates **Uniswap V4's Hooks mechanism**—V4's biggest innovation. V4 transforms each trading pool from an independent contract into a state entry under a "Singleton" architecture, and allows custom Hook contracts to be installed on each pool, executing custom logic at key points in the trade lifecycle (beforeSwap, afterSwap, beforeModifyPosition, etc.).

### Key Mapping

| Story Element | Technical Concept | Explanation |
|--------------|-------------------|-------------|
| Old market thousands of independent scales | Uniswap V3 Pool architecture | Each pool is an independent contract; deployment costs are high |
| Super Bazaar sharing one scale | Uniswap V4 Singleton architecture | All pools share one contract; differentiated by state storage; deployment costs drastically reduced |
| Plugin | Hooks contract | Custom contracts called at specific hook points in the trade lifecycle |
| Pre-trade check | beforeSwap hook | Called before swap execution; can implement KYC, limits, blacklists, etc. |
| Price calculation | Dynamic fee hook | Can dynamically adjust fees during the swap process |
| Post-trade trigger | afterSwap hook | Called after swap completion; can trigger donations, reward distributions, etc. |
| Depositor joining | before/afterModifyPosition hook | Called when liquidity is added/removed; can implement access control |
| Dynamic fees | Dynamic fee tiers | Fees adjust dynamically based on volatility, trading volume, etc. |
| Limit orders | Limit order hook | Automatically executes trades when price thresholds are reached |
| Time-weighted average price | TWAP hook | Updates cumulative prices at each swap for external reference |
| Custom curves | Custom curves | Hooks can implement non-constant-product AMM curves (e.g., Curve's stablecoin formula) |
| Plugin audit | Hooks security review | Uniswap V4 hooks are chosen by pool creators; users must independently audit hook safety |
| Flash accounting | Flash Accounting | V4 introduces "flash settlement"—multiple operations can accumulate in temporary state before final settlement, saving gas |
| Temporary ledger | Transient Storage (EIP-1153) | V4 uses EIP-1153 transient storage for flash accounting; cleared after operation completion |

### Why This Story?

Uniswap V4 represents a paradigm shift in DeFi protocol design—from "fixed-function white box" to "programmable black box." Hooks transform AMMs from a single trading mechanism into a customizable platform.

The "Programmable Bazaar" metaphor for V4 Hooks offers several intuitive advantages:
1. **Plugin architecture**: Inserting custom rules at key market nodes = Hooks' intervention points in the trade lifecycle
2. **Singleton architecture**: Shared super bazaar = V4 merging all pools into one contract
3. **Flash accounting**: Temporary ledger with one-time settlement = Flash Accounting saving gas
4. **Creativity vs. safety balance**: Public code + administrator review = Hooks' openness and risk

### Further Reading

- wiki-web3: Uniswap V4 Hooks Development Guide
- [Uniswap V4 Whitepaper](https://uniswap.org/whitepaper-v4.pdf)
- [Uniswap V4 Core Concepts](https://docs.uniswap.org/contracts/v4/overview)
- [EIP-1153: Transient Storage](https://eips.ethereum.org/EIPS/eip-1153)
- [Uniswap V4 Hooks Directory](https://www.v4byexample.com/)
