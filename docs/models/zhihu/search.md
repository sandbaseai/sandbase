# Zhihu Keyword Search API: pricing, parameters and code examples

`zhihu/search` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.027778 per call · **Modes:** sync

Search Zhihu by keyword with optional result-type, sort, time-interval, topic-display, and offset controls. Use it to find relevant answers, articles, or videos.

## Pricing

- **$0.027778 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/search", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/search', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/search", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/search", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/zhihu/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sorting criteria. one of: `upvoted_count`, `created_time` |
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `keyword` | string | yes | Search keywords.  |
| `vertical` | string |  | Result type filter. one of: `answer`, `article`, `zvideo` |
| `timeInterval` | string |  | Publish time interval filter. one of: `a_day`, `a_week`, `a_month`, `three_months`, `half_a_year`, `a_year` |
| `showAllTopics` | string |  | Whether to show all topics. one of: `FALSE`, `TRUE`; default `"FALSE"` |

## Details

Search Zhihu by keyword with optional result-type, sort, time-interval, topic-display, and offset controls. Use it to find relevant answers, articles, or videos.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keywords. |
| `offset` | integer | No | Start offset, begins with 0. |
| `showAllTopics` | string | No | Whether to show all topics. |
| `vertical` | string | No | Result type filter. |
| `sort` | string | No | Sorting criteria. |
| `timeInterval` | string | No | Publish time interval filter. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/zhihu/search.json`](../../../catalog/models/zhihu/search.json) · Store page: https://www.sandbase.ai/model/zhihu/search
