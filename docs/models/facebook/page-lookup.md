# Facebook Page Lookup

`facebook/page-lookup` · api · Facebook

Look up Facebook Pages and profiles by name with Facebook's own quick search. A name lookup that returns basic identity fields only: name, URL, profile image, Facebook id, and verified status. Matches can include personal profiles as well as Pages. For full Page details (category, followers, phone, website), use facebook.search_pages.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00975**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/page-lookup", "query": "NASA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/page-lookup', {'query': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/page-lookup", {
  "query": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/page-lookup", sandbase.Params{
	"query": "NASA",
})
```

Same call via the path form: `POST /v1/api/facebook/page-lookup` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of matches to return (1-7, default 7). Facebook's quick search answers a name with at most 7 matches. default `7`; range 1–7 |
| `query` | string | yes | Name to look up, as you would type it into Facebook's search box (e.g. NASA or plumber chicago).  |

## Details

Look up Facebook Pages and profiles by name with Facebook's own quick search. A name lookup that returns basic identity fields only: name, URL, profile image, Facebook id, and verified status. Matches can include personal profiles as well as Pages. For full Page details (category, followers, phone, website), use facebook.search_pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/page-lookup" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 5, "query": "NASA"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Name to look up, as you would type it into Facebook's search box (e.g. NASA or plumber chicago). |
| `limit` | integer | No | Maximum number of matches to return (1-7, default 7). Facebook's quick search answers a name with at most 7 matches. |

### Pricing

Billed at the actual cost of each call, usually $0.00975 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/page-lookup.json`](../../../catalog/models/facebook/page-lookup.json) · Store page: https://www.sandbase.ai/model/facebook/page-lookup
