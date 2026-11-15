# Eastmoney API: 11 endpoints with pricing and code examples

Call 11 Eastmoney endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`eastmoney/community-posts`](../models/eastmoney/community-posts.md) | Get stock community discussion posts from EastMoney's Guba forum related to the stock screening topic (znxg). Returns posts with title,… | $0.03 per call |
| [`eastmoney/filter-conditions`](../models/eastmoney/filter-conditions.md) | Get the full hierarchical tree of filter conditions available for stock or fund screening. Returns all categories (范围, 基本面, 行情技术面, 消息面,… | $0.03 per call |
| [`eastmoney/filter-conditions-fundamentals`](../models/eastmoney/filter-conditions-fundamentals.md) | Get filter conditions related to fundamentals: valuation (PE, PB), per-share metrics (EPS, BPS), profitability (ROE, net profit), revenue… | $0.03 per call |
| [`eastmoney/filter-conditions-news`](../models/eastmoney/filter-conditions-news.md) | Get filter conditions related to news and events: major announcements (限售解禁, 定向增发, 资产重组), institutional attention (调研, 评级, 持股比例), and… | $0.03 per call |
| [`eastmoney/filter-conditions-popularity`](../models/eastmoney/filter-conditions-popularity.md) | Get filter conditions related to popularity ranking (股吧人气排名, 粉丝占比) and limit-up (涨停) status including 首板, 连板, and consecutive limit-up days. | $0.03 per call |
| [`eastmoney/filter-conditions-range`](../models/eastmoney/filter-conditions-range.md) | Get filter conditions related to listing scope and range: market type (沪市/深市/创业板/科创板/北交所), listing time, concepts, and index membership. | $0.03 per call |
| [`eastmoney/filter-conditions-technical`](../models/eastmoney/filter-conditions-technical.md) | Get filter conditions related to technical analysis and K-line patterns: MACD (golden/death cross, divergence), KDJ, moving averages,… | $0.03 per call |
| [`eastmoney/hot-conditions`](../models/eastmoney/hot-conditions.md) | Get curated hot screening conditions that are currently trending on EastMoney's stock screener. Each condition includes a title, full… | $0.03 per call |
| [`eastmoney/real-time-hot-queries`](../models/eastmoney/real-time-hot-queries.md) | Get real-time hot search query recommendations from the platform. Recommendations are popular screening queries users can try. Also… | $0.03 per call |
| [`eastmoney/screen-stocks`](../models/eastmoney/screen-stocks.md) | Search for stocks using natural language or filter conditions on EastMoney's AI stock screener. Accepts Chinese or symbolic queries like… | $0.03 per call |
| [`eastmoney/stock-detail`](../models/eastmoney/stock-detail.md) | Get details for a specific stock by searching its code through the AI stock screener. Returns the stock's market data including latest… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "eastmoney/community-posts"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
