# TradingView API: 4 endpoints with pricing and code examples

Call 4 TradingView endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`tradingview/chart`](../models/tradingview/chart.md) | Get recent OHLC bar data for a forex pair at the specified interval. | $0.03 per call |
| [`tradingview/quote`](../models/tradingview/quote.md) | Get a comprehensive real-time forex quote including current price, OHLC, bid/ask spread, volume, change, technical summary, key… | $0.03 per call |
| [`tradingview/scan-forex`](../models/tradingview/scan-forex.md) | Scan multiple forex pairs at once, returning price, change, bid/ask, volume, and key technical indicators for each pair. Useful for… | $0.03 per call |
| [`tradingview/technicals`](../models/tradingview/technicals.md) | Get detailed technical analysis for a forex pair including all oscillators (RSI, MACD, CCI, ADX, Stochastic, etc.), moving averages… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tradingview/chart"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
