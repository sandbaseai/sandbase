# Kalshi API: 4 endpoints with pricing and code examples

Call 4 Kalshi endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`kalshi/markets`](../models/kalshi/markets.md) | Get Kalshi Markets from Kalshi. Returns the official Kalshi API response unchanged. | $0.02 per call |
| [`kalshi/markets-by-ticker`](../models/kalshi/markets-by-ticker.md) | Get Market Price from Kalshi. Returns the official Kalshi API response unchanged. | $0.02 per call |
| [`kalshi/markets-orderbook`](../models/kalshi/markets-orderbook.md) | Get Kalshi Market OrderBook from Kalshi. Returns the official Kalshi API response unchanged. | $0.02 per call |
| [`kalshi/trades`](../models/kalshi/trades.md) | Get Kalshi Trades from Kalshi. Returns the official Kalshi API response unchanged. | $0.02 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kalshi/markets"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
