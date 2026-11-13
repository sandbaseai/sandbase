# Finviz Stock News Sentiment API: pricing, parameters and code examples

`finviz/news-sentiment` · data API · Finviz · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** async

Get recent news headlines for a US ticker from Finviz with source, time and a sentiment score for each headline.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "finviz/news-sentiment", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('finviz/news-sentiment', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("finviz/news-sentiment", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "finviz/news-sentiment", sandbase.Params{
	"ticker": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/finviz/news-sentiment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | Stock ticker symbol (e.g. AAPL, TSLA, MSFT). Case-insensitive.  |

## Details

Get recent news headlines for a US ticker from Finviz with source, time and a sentiment score for each headline.

---
Machine-readable: [`catalog/models/finviz/news-sentiment.json`](../../../catalog/models/finviz/news-sentiment.json) · Store page: https://www.sandbase.ai/model/finviz/news-sentiment
