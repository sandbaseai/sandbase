# Kuaishou User Search API: pricing, parameters and code examples

`kuaishou/search-user` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Search public Kuaishou user accounts by keyword with page-number pagination. Use it to discover relevant creators or accounts before requesting profile and published-video data.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/search-user", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/search-user', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/search-user", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/search-user", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/kuaishou/search-user` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for results, starting from 1. default `1` |
| `keyword` | string | yes | The search keyword to find users.  |

## Details

Search public Kuaishou user accounts by keyword with page-number pagination. Use it to discover relevant creators or accounts before requesting profile and published-video data.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/search-user" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The search keyword to find users. |
| `page` | integer | No | Page number for results, starting from 1. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/kuaishou/search-user.json`](../../../catalog/models/kuaishou/search-user.json) · Store page: https://www.sandbase.ai/model/kuaishou/search-user
