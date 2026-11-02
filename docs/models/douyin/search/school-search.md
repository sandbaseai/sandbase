# Douyin School Search API: pricing, parameters and code examples

`douyin/search/school-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns school information search results from Douyin matching search queries. Filter schools by entering a specific school name or city query via the keyword parameter.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/school-search", "keyword": "北京"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/school-search', {'keyword': '北京'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/school-search", {
  "keyword": "北京"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/school-search", sandbase.Params{
	"keyword": "北京",
})
```

Same call via the path form: `POST /v1/api/douyin/search/school-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search keyword, e.g., school name "Peking University" or city "Beijing" default `"北京"` |

## Details

Search for schools on Douyin using the optional `keyword` parameter to query by school name or location.

### Use cases

- Search for school names on Douyin.
- Look up educational institutions by city or location keyword.
- Populate school selection fields in search workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/school-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search keyword, e.g., school name "Peking University" or city "Beijing" |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "schools": [
    {
      "name": "北京四中"
    }
  ]
}
```

### Notes

- Pass a school name or city name in `keyword` to narrow results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Challenge Search](/model/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/model/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/model/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/school-search.json`](../../../../catalog/models/douyin/search/school-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/school-search
