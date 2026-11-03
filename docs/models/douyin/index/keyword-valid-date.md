# Douyin Index Keyword Valid Dates API: pricing, parameters and code examples

`douyin/index/keyword-valid-date` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the valid date ranges available for specified search terms in the Douyin Index. Queries accept a comma-separated list of keywords to identify data availability periods.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/keyword-valid-date", "keyword_list": "人工智能"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/keyword-valid-date', {'keyword_list': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/keyword-valid-date", {
  "keyword_list": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/keyword-valid-date", sandbase.Params{
	"keyword_list": "人工智能",
})
```

Same call via the path form: `POST /v1/api/douyin/index/keyword-valid-date` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword_list` | string | yes | Keyword list, comma separated  |

## Details

Use this endpoint to inspect the available Douyin Index date ranges for search terms provided via `keyword_list`.

### Use cases

- Check historical data availability before querying keyword index metrics.
- Verify valid date boundaries for multiple tracking keywords in batch.
- Align analytics date pickers with active Douyin Index time windows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/keyword-valid-date" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword_list": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword_list` | string | Yes | Keyword list, comma separated |

### Notes

- Accepts multiple terms supplied as a comma-separated string in `keyword_list`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/keyword-valid-date.json`](../../../../catalog/models/douyin/index/keyword-valid-date.json) · Store page: https://www.sandbase.ai/model/douyin/index/keyword-valid-date
