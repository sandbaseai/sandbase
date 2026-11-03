# Facebook Page Contact Info API: pricing, parameters and code examples

`facebook/page-contact` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Look up a Facebook Page's public contact details (email, phone, website, and address) by page URL or ID.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/page-contact", "page": "https://www.facebook.com/joesstonecrab"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/page-contact', {'page': 'https://www.facebook.com/joesstonecrab'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/page-contact", {
  "page": "https://www.facebook.com/joesstonecrab"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/page-contact", sandbase.Params{
	"page": "https://www.facebook.com/joesstonecrab",
})
```

Same call via the path form: `POST /v1/api/facebook/page-contact` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string | yes | Facebook Page URL or page ID to look up (e.g. https://www.facebook.com/nasa).  |
| `language` | string |  | Locale code for the returned data (e.g. en-US). default `"en-US"` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `createdUtc` or `adStatus`, and it is served only by a source that…  |

## Details

This API returns the public contact details of a Facebook Page, including email, phone, website, and address. It also returns basic page facts such as category, follower count, and ad status. You send a Page URL or a page ID in `page`.

### Use cases

- Build a lead list of local businesses with their email, phone, and website.
- Check that a restaurant's listed address and phone number match your own records.
- Find the Instagram or other linked profiles a business lists on its Page.
- Check whether a Page is currently running ads before you look at its ad activity.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/page-contact" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page": "https://www.facebook.com/joesstonecrab"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | string | Yes | Facebook Page URL or page ID to look up (e.g. https://www.facebook.com/nasa). |
| `language` | string | No | Locale code for the returned data (e.g. en-US). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `createdUtc` or `adStatus`, and it is served only by a source that ret |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "about": "For more than 100 years, no visit to Miami has been complete without stopping he…",
        "adLibraryPageId": "404077308008",
        "adStatus": "This Page isn't currently running ads.",
        "address": "11 Washington Ave, Miami Beach, FL, United States, 33139",
        "category": "Seafood Restaurant",
        "coverPhotoUrl": "https://scontent-msp1-1.xx.fbcdn.net/v/t39.30808-6/626797260_1324209616413613_36…",
        "createdUtc": 1268006400,
        "email": "marketing@joesstonecrab.com",
        "followers": 44732,
        "id": "100064737608769",
        "image": "https://scontent-msp1-1.xx.fbcdn.net/v/t39.30808-1/626760115_1324209663080275_79…",
        "links": [
          "https://www.instagram.com/joesstonecrab"
        ]
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].email / phone / website` | Public contact details the Page lists. A Page that does not list one of these may omit it. |
| `data.items[].address` | Street address of the business as one text string. |
| `data.items[].title` | Display name of the Page. |
| `data.items[].category` | Business category of the Page, such as `Seafood Restaurant`. |
| `data.items[].followers` | Number of followers the Page has. |
| `data.items[].createdUtc` | Page creation time as a Unix timestamp in seconds. |
| `data.items[].adStatus` | Text that says whether the Page is currently running ads. |
| `data.items[].adLibraryPageId` | ID of the Page in the Facebook Ad Library. |
| `data.items[].id` | Numeric Facebook ID of the Page. |
| `data.items[].links` | List of other profile URLs the Page links to, such as Instagram. |

### Notes

- Set `page` to a full Page URL such as `https://www.facebook.com/joesstonecrab` or to a numeric page ID.
- The Page is returned as the single entry in `data.items`. When nothing matches, the response has `found: false`.
- Use `requireFields` with `adStatus`, `createdUtc`, or `followers` to make sure the answering source returns those fields. This can change the price of the call.
- To search for Pages by name first, use [Facebook Page Search](/apis/facebook/search-pages).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/page-contact.json`](../../../catalog/models/facebook/page-contact.json) · Store page: https://www.sandbase.ai/model/facebook/page-contact
