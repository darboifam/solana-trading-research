# Development history

The project began in January 2025. This chronology summarizes surviving files and dated reports reviewed in October 2026. Early phases use approximate periods inferred from file modification dates, which can change when files are copied or edited. Later research phases have explicit dates inside reports. Historical market-data coverage is not a development date.

| Period | Development focus | What changed |
|---|---|---|
| January–February 2025 | Wallet and Telegram foundations | Wallet utilities, forwarding, bot messages, combined scripts, authentication helpers, and token-address parsing established the initial workflow. The earliest surviving project-file modification dates are January 24–25. |
| March–June 2025 | Trading state and signal analysis | Trading scripts expanded alongside simulation, trade-history handling, scraping, call/update matching, and descriptive token analysis. |
| July–September 2025 | Execution experiments and historical data | Quote/swap utilities, token-account probes, several bot revisions, market-metric logging, historical price collection, and source comparisons broadened the system. |
| October–December 2025 | Backtesting and optimization | Entry-feature experiments, large exit-policy searches, checkpointed optimization, slippage comparisons, and equity reporting made research a substantial workstream. |
| January–June 2026 | Data reliability and further collection | Feed immutability and live-versus-later-historical probes investigated data availability. Additional source ingestion and historical research utilities expanded coverage. |
| July 2026 | Structured packages and causal research | Work included a point-in-time collector, spot paper trading, an established-token rebound scanner, SOL strategy-family studies, a separate Coinbase futures branch, and source-level causal evaluations. |
| August 2026 | Liquidity, robustness, and portfolio audits | Live-liquidity settlement research, pre-entry/order-flow collection, nested walk-forward studies, sizing experiments, diversification, and larger overfit/causality audits examined feasibility. |
| September–October 2026 | Archive expansion and continued validation | Further source archiving, recent-window evaluation, metadata reconciliation, and an October research report continued the cycle of collecting, testing, and rejecting or retaining hypotheses. |

## How the project evolved

The early objective was operational: read a message, identify a token, and connect it to a trading workflow. As data accumulated, the project shifted toward comparing signal sources and measuring outcomes.

Backtesting introduced another set of problems: unavailable historical observations, revised candles, sparse exits, overlapping positions, execution costs, and repeated use of the same historical windows. Later work made these assumptions explicit and added independent reconstruction, frozen experiments, and adverse-condition tests.

The newer packages represent a move toward maintainable boundaries: external data providers, persistent state, strategy decisions, paper execution, risk controls, and reporting. The older scripts remain part of the development history rather than evidence that every component belongs to a single finished application.

## History limitations

This account covers artifacts that survived in the reviewed workspace. It cannot recover deleted work, unsaved experiments, previous remote repositories, or conversations stored elsewhere. The public documentation intentionally summarizes the development journey without distributing the implementation archive.
