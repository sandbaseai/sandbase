# Kuaishou User Search (V2) API: pricing, parameters and code examples

`kuaishou/app/search-user-v2` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Searches for Kuaishou accounts matching a query term. Results can be filtered by gender and account relationship status, as well as sorted by follower count.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-user-v2", "keyword": "test"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-user-v2', {'keyword': 'test'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-user-v2", {
  "keyword": "test"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-user-v2", sandbase.Params{
	"keyword": "test",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-user-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | Pagination cursor, empty for first page, pass pcursor from previous response  |
| `fans_sort` | string |  | default / most_to_least / least_to_most one of: `default`, `most_to_least`, `least_to_most` |
| `user_gender` | string |  | all / male / female one of: `all`, `male`, `female` |
| `user_relation` | string |  | all / same_city / verified / live / following one of: `all`, `same_city`, `verified`, `live`, `following` |

## Details

Look up Kuaishou accounts using a search `keyword`. Narrow results by applying `user_gender`, `user_relation`, and `fans_sort` criteria.

### Use cases

- Find creator profiles matching target keywords on Kuaishou.
- Filter account search results by gender or verification status.
- Discover popular influencers by sorting profiles based on follower counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-user-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "<keyword>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | — |
| `pcursor` | string | No | Pagination cursor, empty for first page, pass pcursor from previous response |
| `fans_sort` | string | No | default / most_to_least / least_to_most |
| `user_gender` | string | No | all / male / female |
| `user_relation` | string | No | all / same_city / verified / live / following |

### Notes

- Leave `pcursor` empty for the first page, and pass the returned value from the prior call to request subsequent pages.
- The `fans_sort` parameter supports `default`, `most_to_least`, and `least_to_most`.
- Use `user_relation` to filter by `all`, `same_city`, `verified`, `live`, or `following`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-user-v2.json`](../../../../catalog/models/kuaishou/app/search-user-v2.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-user-v2
