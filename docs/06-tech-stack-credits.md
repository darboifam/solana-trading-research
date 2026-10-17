# Technology stack and external credits

The project is an independent integration and research effort. **Using a dependency does not mean authoring or contributing to that dependency's upstream repository.** These links are attribution and technical context, not forks of a private trading system.

## Languages and core libraries

| Project / service | Role | Upstream reference |
| --- | --- | --- |
| Python | Main implementation and research language | https://www.python.org/ |
| Telethon | Telegram event integration | https://github.com/LonamiWebs/Telethon (archived GitHub mirror; upstream project moved to Codeberg) |
| solana-py | Solana Python RPC interactions | https://github.com/michaelhly/solana-py |
| solders | Solana transaction structures and keypair/public-key types | https://github.com/kevinheavey/solders |
| NumPy | Array and numeric analysis | https://github.com/numpy/numpy |
| pandas | Research datasets and time-indexed analysis | https://github.com/pandas-dev/pandas |
| Matplotlib | Historical performance and diagnostic charts | https://github.com/matplotlib/matplotlib |
| scikit-learn | Predictive evaluation and metrics in exploratory research | https://github.com/scikit-learn/scikit-learn |
| LightGBM | Experimental historical downside-risk classifier | https://github.com/lightgbm-org/LightGBM |

## APIs and services

| Service | Where it fit |
| --- | --- |
| Telegram | Signal ingestion, notifications, remote operational controls. |
| Solana RPC | Chain state, token balances, transaction submission/confirmation. |
| Birdeye | Price, liquidity, token and historical market-data access. |
| GeckoTerminal | Price/pool/market-data enrichment in multiple iterations. |
| SolanaTracker | Swap-routing/execution integration in later versions. |
| Jupiter | Swap exploration and routing in earlier prototype iterations. |
| DexScreener | Token/pool discovery and reference links. |
| CoinGecko | SOL/USD reference data in some iterations. |

**Important distinction:** A number of other projects were evaluated or suggested over the life of this work, but they are intentionally **not** listed as incorporated unless project records support their use. No upstream code has been copied into this public documentation repository.

## Acknowledgment standards

- State how a library was used, rather than claiming to have built its underlying functionality.
- Link to upstream maintained repositories/docs; comply with third-party licenses if code is ever redistributed.
- Do not embed access tokens, wallet keys or request URLs carrying credentials in issues, docs, screenshots, examples or commits.
- The documentation repository does not imply affiliation with vendors or Telegram channels.

[Return to overview](../README.md)
