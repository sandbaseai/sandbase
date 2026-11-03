# Facebook Page Search API: pricing, parameters and code examples

`facebook/search-pages` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.123 per call · **Modes:** sync

Search Facebook Pages by keyword, optionally narrowed to a location, and get structured page profiles (name, category, followers, contact details).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.123**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/search-pages", "query": "nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/search-pages', {'query': 'nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/search-pages", {
  "query": "nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/search-pages", sandbase.Params{
	"query": "nike",
})
```

Same call via the path form: `POST /v1/api/facebook/search-pages` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-10, default 10). You are billed per result returned, so a lower limit costs less. range 1–10 |
| `query` | string | yes | Keyword to search Facebook Pages for (e.g. 'coffee roasters').  |
| `location` | string |  | Optional free-text location to narrow the search: a city, province, or country (e.g. 'Berlin').  |

## Details

Returns a list of public Facebook Pages that match a keyword, with each page's name, category, follower count, website and phone. It needs a `query` and accepts an optional `location` and `limit`.

### Use cases

- Find the official and regional Pages that a brand runs, such as sub-brand Pages for one company.
- Build a list of local businesses in a category and city, with their websites and phone numbers.
- Check which Pages of a brand are currently running ads.
- Compare follower counts across competing Pages in the same category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/search-pages" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "nike"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search Facebook Pages for (e.g. 'coffee roasters'). |
| `limit` | integer | No | Maximum number of results to return (1-10, default 10). You are billed per result returned, so a lower limit costs less. |
| `location` | string | No | Optional free-text location to narrow the search: a city, province, or country (e.g. 'Berlin'). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "about": "Sport Style Innovation\nwww.nike.com/sportswear",
        "adLibraryPageId": "20825389113",
        "adStatus": "This Page is currently running ads.",
        "categories": [
          "Page"
        ],
        "category": "Product/service",
        "coverPhotoUrl": "https://scontent-lax3-2.xx.fbcdn.net/v/t39.30808-6/351512729_2609225615905264_37…",
        "createdUtc": 1218153600,
        "followers": 15452600,
        "id": "100064933082327",
        "image": "https://scontent-lax3-2.xx.fbcdn.net/v/t39.30808-1/352238800_1378999996006774_42…",
        "likes": 0,
        "owner": "NIKE, Inc."
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].title` | Display name of the Page. |
| `data.items[].id` | Numeric ID of the Page. |
| `data.items[].pageAlias / data.items[].url` | The Page's URL slug and its full Facebook URL. |
| `data.items[].category / data.items[].categories` | Main category of the Page, and the full list of category labels. |
| `data.items[].followers / data.items[].likes` | Follower count and like count. `likes` can be `0` even when the Page has many followers, so use `followers` for audience size. |
| `data.items[].website / data.items[].phone` | Contact details listed on the Page. Either can be an empty string. |
| `data.items[].about` | Text from the Page's about section. It can be empty. |
| `data.items[].owner` | Name of the business that owns the Page. |
| `data.items[].adStatus / data.items[].adLibraryPageId` | Text saying whether the Page is currently running ads, and the Page ID used in the Facebook Ad Library. |
| `data.items[].createdUtc` | Page creation time as a Unix timestamp in seconds. |

### Notes

- Set `limit` between 1 and 10. The default is 10, and you pay per result returned.
- Use `location` with a city, province or country, such as `Berlin`, to narrow the results.
- Pass `adLibraryPageId` to [Facebook Company Ads](/apis/facebook/company-ads) to see a Page's ads, or call [Facebook Page Contact Info](/apis/facebook/page-contact) for more contact details.
- Use [Facebook Profile Posts](/apis/facebook/profile-posts) with the Page `url` to read its posts.

### Pricing

Billed at the actual cost of each call, about $0.123 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/search-pages.json`](../../../catalog/models/facebook/search-pages.json) · Store page: https://www.sandbase.ai/model/facebook/search-pages
