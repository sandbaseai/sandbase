# Twitter Search Timeline API: pricing, parameters and code examples

`twitter/search` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search X (Twitter) by keyword across top, latest, media, people, or list result modes with cursor pagination. Use it to find public conversations, accounts, media, or lists related to a topic.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/search", "keyword": "iphone"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/search', {'keyword': 'iphone'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/search", {
  "keyword": "iphone"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/search", sandbase.Params{
	"keyword": "iphone",
})
```

Same call via the path form: `POST /v1/api/twitter/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor returned by the previous response.  |
| `keyword` | string | yes | Search keyword.  |
| `searchType` | string |  | Search result type. one of: `TOP`, `LATEST`, `MEDIA`, `PEOPLE`, `LISTS` |

## Details

Search X (Twitter) by keyword across top, latest, media, people, or list result modes with cursor pagination. Use it to find public conversations, accounts, media, or lists related to a topic.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "iphone"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `searchType` | string | No | Search result type. |
| `cursor` | string | No | Pagination cursor returned by the previous response. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/twitter/search.json`](../../../catalog/models/twitter/search.json) · Store page: https://www.sandbase.ai/model/twitter/search
