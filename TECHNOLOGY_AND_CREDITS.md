# Technology and upstream credits

The following libraries are supported by imports or dependency declarations in the reviewed workspace. Listing an upstream project acknowledges its role as a dependency; it does not imply authorship of, or contributions to, that project.

## Main upstream repositories

| Project | Role in the workspace |
|---|---|
| [Telethon](https://github.com/LonamiWebs/Telethon) | Telegram client, ingestion, and automation |
| [solana-py](https://github.com/michaelhly/solana-py) | Solana RPC/client utilities in legacy scripts |
| [solders](https://github.com/kevinheavey/solders) | Solana primitives and execution-related types |
| [Coinbase Advanced Python SDK](https://github.com/coinbase/coinbase-advanced-py) | Optional authenticated adapter for the separate futures branch |
| [NumPy](https://github.com/numpy/numpy) | Numerical arrays and research calculations |
| [pandas](https://github.com/pandas-dev/pandas) | Tabular analysis and research workflows |
| [Matplotlib](https://github.com/matplotlib/matplotlib) | Research figures and equity plots |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | Statistical model and classification experiments |
| [aiohttp](https://github.com/aio-libs/aiohttp) | Asynchronous HTTP integrations |
| [HTTPX](https://github.com/encode/httpx) | Provider HTTP clients in the structured rebound package |
| [websockets](https://github.com/python-websockets/websockets) | WebSocket-based data ingestion |

Telethon's historical GitHub repository currently directs readers to [its Codeberg repository](https://codeberg.org/Lonami/Telethon). The GitHub link above reflects the historical dependency reference.

Other observed tools include Requests, SciPy, Joblib, orjson, ijson, PyArrow, python-dotenv, pytest, mypy, and Ruff. SQLite and several storage/serialization utilities come from Python's standard library.

## External services and documentation

| Service/reference | Relationship |
|---|---|
| Telegram | Message source and bot/user-client integration |
| [Solana](https://solana.com/docs) | Chain/RPC environment |
| [Jupiter](https://developers.jup.ag/) | Quote and swap integration work |
| [Birdeye](https://docs.birdeye.so/) | Token, price, OHLCV, liquidity, volume, and trade-data research |
| Coinbase | Historical liquid-market data and a separate futures execution/research adapter |
| DexScreener, GeckoTerminal, Raydium, SolanaTracker | Additional data/quote integrations or experiments in legacy scripts and research |
| [Pump public documentation](https://github.com/pump-fun/pump-public-docs) | Referenced for program/instruction discovery documentation |

Helius and Bitquery appear as optional interfaces in the rebound project. Their presence is not a claim of completed paid-provider integrations.

## Attribution boundaries

Project-specific work includes the workflows, integrations, data transformations, research harnesses, accounting, audit tools, and application organization described in this case study. Third-party libraries supply their own underlying capabilities.

The portfolio does not redistribute upstream source code. Exact origins of any borrowed implementation snippets would require a separate provenance review before source publication. Learning-resource links in private notes are not automatically represented as runtime dependencies or as the codebase's origin.
