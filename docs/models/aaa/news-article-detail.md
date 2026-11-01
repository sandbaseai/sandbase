# AAA News Article Detail

`aaa/news-article-detail` · api · AAA

Returns the full content of a specific news article identified by its URL slug. The slug is obtainable from get_news_articles results.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/news-article-detail", "slug": "national-gas-average-drops-nearly-20-cents-in-one-week"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/news-article-detail', {'slug': 'national-gas-average-drops-nearly-20-cents-in-one-week'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/news-article-detail", {
  "slug": "national-gas-average-drops-nearly-20-cents-in-one-week"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/news-article-detail", sandbase.Params{
	"slug": "national-gas-average-drops-nearly-20-cents-in-one-week",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/news-article-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | Article URL slug (e.g. national-gas-average-drops-nearly-20-cents-in-one-week). Obtainable from get_news_articles results.  |

## Details

Returns the full content of a specific news article identified by its URL slug. The slug is obtainable from get_news_articles results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/news-article-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "national-gas-average-drops-nearly-20-cents-in-one-week"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Article URL slug (e.g. national-gas-average-drops-nearly-20-cents-in-one-week). Obtainable from get_news_articles results. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/aaa/news-article-detail.json`](../../../catalog/models/aaa/news-article-detail.json) · Store page: https://www.sandbase.ai/model/aaa/news-article-detail
