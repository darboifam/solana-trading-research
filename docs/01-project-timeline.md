# Development history | January 2025 onward

This timeline summarizes known project milestones. Dates below reflect contemporaneous notes where available; they are **not** backdated Git commits. Periods not well documented are deliberately not assigned invented accomplishments.

## January 2025: Initial prototype

- Began with a Telegram automation workflow for incoming Solana token-call messages.
- Built token contract-address extraction and forwarding/notification experiments.
- Explored early Solana Python libraries, basic swap/order workflows and automated sell logic.
- Key technical questions: event handling, token identity, wallet interaction and operational reliability.

## Spring 2025: Integrations and remote operation

- Iterated on Solana trading-bot prototypes and early automated-trading workflows.
- Deployed/testing the bot on a virtual private server in April 2025 (private server details excluded).
- Improved handling of asynchronous Telegram events and market-data requests.

## May to June 2025: Signal filtering and simulation

- Built market-data-dependent screening using concepts such as liquidity, market cap, age, volume and time of day.
- Added simulated trade outcomes and logging to analyze selected candidates rather than judging channels by promotional performance updates.
- Compared profit-taking, stop-loss, slippage and fee assumptions.

## July to August 2025: Full bot operations

- Expanded Telegram source monitoring and experimented with simultaneous source confirmation for the same token.
- Integrated providers such as Birdeye, GeckoTerminal and SolanaTracker; investigated Jupiter and fallback routing in earlier versions.
- Added position monitoring, duplicate protection, Telegram controls, wallet/balance checks, persistent trade state and trade-history/PnL reporting.
- Debugged execution, stale/missing data, failed route lookups and dust/leftover-token behavior.

## 2026: Quantitative data research

- Gathered and aligned Telegram call archives with sampled token prices, token liquidity and available metadata.
- Compared separate source populations (VIP, DSB and CTO) and 1-second versus 15-second recordings when present.
- Iterated through event-driven backtests and one-global-position replay, including explicit execution delays and missing-data policies.
- Focused on distinguishing attractive historical peaks from outcomes a causal, executable strategy could capture.

## September 2026: Broad historical strategy sweeps

- Evaluated momentum/breakout, confirmation, fixed holding and risk-management approaches.
- Tested different friction levels, chronology, position concurrency, caps and adverse missing-fill behavior.
- Reassessed initial apparently positive results under stricter assumptions and later datasets.

## October 2026: Cross-dataset audits and predictive-risk direction

- Large-scale screens covered asymmetric exits, trailing strategies, partial profit-taking, market-cap/lifecycle adaptation, volatility patterns, regime gating and resting-take-profit hypotheticals.
- Corrected a trailing-exit simulator boundary error: the previously apparent universal profitability **disappeared** after correction. The invalid results were discarded.
- Examined Telegram update-based exits, price-peak decay, price-resolution effects, data coverage and independent retests.
- Investigated whether pre-entry features could predict severe losses. An exploratory LightGBM-based screen showed modest risk discrimination, but **not profitable universal strategies**.
- Independently checked the **+63-second Birdeye one-minute liquidity embargo** and kept it as a permanent causality requirement.

## What this timeline does not claim

- Not an uninterrupted public GitHub commit history since January 2025.
- Not verified profitability, verified executable fills or a strategy in profitable production.
- Not open-source authorship of third-party SDKs, APIs or frameworks.

[Return to overview](../README.md)
