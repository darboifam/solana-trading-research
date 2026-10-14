# Workstreams and scope

## Telegram and signal ingestion

Early scripts handled forwarding, bot/user sessions, token-reference extraction, and message monitoring. Later collectors archived historical messages and linked original calls to updates using explicit identifiers, token references, and timing.

Research compared several signal populations rather than assuming all sources behaved alike. Work included overlap analysis, time-to-outcome studies, drawdown/rebound patterns, holding-time distributions, and recent-period comparisons. Raw messages, source identities, and access credentials remain private.

## Trading and execution tooling

The workspace contains multiple generations of trading scripts plus targeted quote, swap, wallet, and token-account utilities. Later versions added richer trade-event logging, execution-state handling, and strategy runtime integration.

This work supports a discussion of asynchronous integration, failure handling, concurrency, and reconciliation. It does not establish production uptime or verified live profitability.

## Market-data engineering

Collectors and converters manage token metadata, prices, candles, liquidity, volume, trade-tape features, and selected wallet-derived features. Tools address pagination, bounded requests, resuming interrupted downloads, interval merging, timestamp normalization, and compact compressed outputs.

Newer research stores observations in SQLite. Historical archives and exports also use JSON/gzip, CSV, and Parquet. These formats belong to different generations and purposes; they are not all persistence backends for one application.

## Quantitative research

Experiments cover entry timing, exit policies, momentum, reversion, liquidity regimes, participation, volatility, source health, and portfolio combinations. Some use interpretable rules; others evaluate statistical models or classifiers.

Research tools include chronological splits, expanding walk-forward selection, frozen manifests, integrity checks, parameter perturbations, timing/cost stresses, bootstrap/resampling methods, negative controls, and component ablations. These methods differ across studies and are not claimed for every historical script.

## Structured Solana applications

One package combines independent on-chain discovery, optional Telegram ingestion, two-way quote observations, SQLite storage, and spot paper trading. It also hosts broader SOL research and a separate Coinbase futures branch.

A second package focuses on established-token rebound research: historical discovery, supply/peak handling, typed state transitions, quote validation, paper fills, risk limits, and event-driven backtesting. Its automated Solana live-submission path is explicitly deferred in its documentation. Optional Helius and Bitquery boundaries are scaffolding rather than completed provider integrations.

## Quality and reproducibility

The structured projects include deterministic tests. The rebound package also configures linting and static type checks. Research outputs preserve configuration, data provenance, accounting assumptions, and limitations in reports.

The public case study describes these practices without publishing test implementations, operational configuration, private strategy parameters, trained models, or reproducible trading datasets.
