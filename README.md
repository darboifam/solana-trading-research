# Solana Trading Systems & Quantitative Research

A personal engineering and research project started in **January 2025**, spanning Telegram automation, Solana execution tooling, market-data collection, paper trading, and quantitative strategy evaluation.

The project grew from small wallet and message-handling scripts into several connected research and trading systems. Its main engineering challenge became making historical results reflect what a bot could actually observe and execute at the time.

**This repository is a public project case study. The implementation, strategy rules, model artifacts, datasets, credentials, and operational logs remain private.**

## Project scope

| Area | Work represented |
|---|---|
| Telegram automation | Message ingestion, token-reference extraction, original-call/update matching, deduplication, and source comparison |
| Solana execution | Wallet/RPC utilities, quote and swap experiments, token-account handling, position tracking, concurrency, and trade-event logging |
| Data engineering | Resumable historical downloads, timestamp normalization, compact compressed datasets, liquidity/volume collection, and SQLite observation stores |
| Strategy research | Event-driven simulations, entry/exit studies, chronological selection, model experiments, regime analysis, and portfolio comparisons |
| Execution realism | Candle availability, observation/fill delays, fees, liquidity constraints, missing exits, and backtest/simulation reconciliation |
| Structured applications | A point-in-time collector and spot paper-trading package, an established-token rebound scanner, and a separate Coinbase futures branch |
| Quality and operations | Typed domain models, provider adapters, risk gates, deterministic tests, health checks, retry/rate-limit handling, and reproducible reports |

## Engineering highlights

- Built workflows that connect unstructured messages to timestamped token histories.
- Developed collection and conversion tools for large, compressed market-data archives.
- Separated signal generation, execution assumptions, accounting, and risk controls in newer systems.
- Investigated the difference between candle timestamps and the time data became observable.
- Reconciled historical simulations against recorded forward-simulation events.
- Evaluated strategies with chronological splits, frozen configurations, stress tests, and explicit rejection criteria.
- Documented failed hypotheses and validation limitations alongside promising historical results.

## Explore the project

- [Development history](PROJECT_HISTORY.md)
- [Workstreams and scope](PROJECT_SCOPE.md)
- [System architecture](ARCHITECTURE.md)
- [Research methods and engineering lessons](RESEARCH_ENGINEERING.md)
- [Technology and upstream credits](TECHNOLOGY_AND_CREDITS.md)

## Status and evidence

This is an evolving project with multiple generations of software. Legacy trading integrations, paper-only spot collection, isolated live-execution scaffolding, and the separate futures implementation have different completion levels.

The portfolio documents implemented modules and saved research findings. It does not present every research branch as deployed or validated. Historical profitability, a passing causality check, and reliable forward performance are separate claims; several studies explicitly rejected their candidates.

Development dates are reconstructed from surviving artifacts and dated research reports. This repository begins with a retrospective project account; it does not claim a continuous Git commit history dating to 2025.

Third-party libraries and services are credited separately from project-specific work. No third-party source code is redistributed here.
