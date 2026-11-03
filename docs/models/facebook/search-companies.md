# Facebook Company Search API: pricing, parameters and code examples

`facebook/search-companies` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Search the Meta Ad Library for advertisers by keyword and get matching pages: page ID, category, verification, follower counts, and linked Instagram.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/search-companies", "query": "nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/search-companies', {'query': 'nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/search-companies", {
  "query": "nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/search-companies", sandbase.Params{
	"query": "nike",
})
```

Same call via the path form: `POST /v1/api/facebook/search-companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Keyword to search advertiser pages for (e.g. "nike").  |

## Details

This API searches the Meta Ad Library for advertiser pages that match a keyword. It returns a list of matching pages with page ID, category, verification status, like count, and linked Instagram account. It needs one input, `query`.

### Use cases

- Find the official Facebook page ID of a brand before you pull its ads.
- Compare follower and like counts across a brand's regional or product pages, such as Nike, Nike Football and Nike Run Club.
- Check whether a page is verified and has a linked Instagram account before you add it to a monitoring list.
- Build a list of advertiser pages that match a keyword for competitor research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/search-companies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "nike"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search advertiser pages for (e.g. "nike"). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "companies": [
      {
        "category": "Sportswear Store",
        "country": "",
        "entityType": "PERSON_PROFILE",
        "igFollowers": 290838453,
        "igUsername": "nike",
        "igVerified": true,
        "imageUrl": "https://scontent-iad3-1.xx.fbcdn.net/v/t39.30808-1/284964043_10159903868513445_7…",
        "likes": 39489880,
        "name": "Nike",
        "pageAlias": "nike",
        "pageDeleted": false,
        "pageId": "15087023444"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.companies[].pageId` | Facebook page ID as a string. Use it to look up the page's ads or other page data. |
| `data.companies[].name / data.companies[].pageAlias` | Display name of the page and its URL alias, such as `Nike` and `nike`. |
| `data.companies[].category` | Page category, such as `Sportswear Store`. |
| `data.companies[].verification` | Verification status of the page. The sample shows `BLUE_VERIFIED`. |
| `data.companies[].likes` | Number of likes on the Facebook page. |
| `data.companies[].igUsername` | Username of the linked Instagram account. |
| `data.companies[].igFollowers / data.companies[].igVerified` | Follower count of the linked Instagram account, and whether that account is verified. |
| `data.companies[].pageDeleted` | `true` if the page has been deleted, `false` if not. |
| `data.companies[].imageUrl` | URL of the page's profile image. |
| `found` | `true` when the search returned matching pages. |

### Notes

- Pass any brand or advertiser keyword in `query`. The request has no pagination parameter.
- Take `pageId` from a result and pass it to [Facebook Company Ads](/apis/facebook/company-ads) to see that advertiser's ads.
- To search regular Facebook pages instead of advertisers, use [Facebook Page Search](/apis/facebook/search-pages).
- Some fields can be empty. In the sample, `country` is an empty string for every result.

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/search-companies.json`](../../../catalog/models/facebook/search-companies.json) · Store page: https://www.sandbase.ai/model/facebook/search-companies
