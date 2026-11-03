# Facebook Page Lookup API: pricing, parameters and code examples

`facebook/page-lookup` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00975 per call · **Modes:** sync

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

This API looks up Facebook Pages and profiles by name and returns up to 7 matches. It needs one input, `query`, the name you would type into Facebook's search box. Each match has only basic identity fields.

### Use cases

- Find the Facebook URL and `id` of a brand or organization from its name.
- Check whether a Page that matches a name is verified before you use it in a workflow.
- Collect profile images for a list of names to show next to search results.
- Resolve a name to an `id` or `url`, then pass it to another Facebook API for deeper data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/page-lookup" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 5, "query": "NASA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Name to look up, as you would type it into Facebook's search box (e.g. NASA or plumber chicago). |
| `limit` | integer | No | Maximum number of matches to return (1-7, default 7). Facebook's quick search answers a name with at most 7 matches. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "id": "100044561550831",
        "image": "https://scontent-mia5-2.xx.fbcdn.net/v/t39.30808-1/243095782_416661036495945_384…",
        "isVerified": true,
        "name": "NASA - National Aeronautics and Space Administration",
        "url": "https://www.facebook.com/NASA"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the lookup returned at least one match. A lookup with no matches returns `found: false`. |
| `data.items[]` | One match for the name. The list holds at most `limit` entries, and never more than 7. |
| `data.items[].name` | Display name of the Page or profile, for example `NASA - National Aeronautics and Space Administration`. |
| `data.items[].url` | Public Facebook URL of the match, for example `https://www.facebook.com/NASA`. |
| `data.items[].id` | Facebook id of the match, returned as a string of digits. |
| `data.items[].isVerified` | `true` when the match shows as verified on Facebook. |
| `data.items[].image` | URL of the small profile image for the match. The sample URLs point to 120x120 images. |

### Notes

- Matches can be personal profiles as well as Pages, so check `name` and `url` before you use a result.
- Set `limit` between 1 and 7. The default is 7, and there is no pagination.
- This API does not return category, followers, phone or website. Use [Facebook Page Search](/apis/facebook/search-pages) for full Page details.
- To get the id from a known URL, use [Facebook Profile ID](/apis/facebook/profile-id).

### Pricing

Billed at the actual cost of each call, about $0.00975 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/page-lookup.json`](../../../catalog/models/facebook/page-lookup.json) · Store page: https://www.sandbase.ai/model/facebook/page-lookup
