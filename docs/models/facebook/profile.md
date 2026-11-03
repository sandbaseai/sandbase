# Facebook Profile API: pricing, parameters and code examples

`facebook/profile` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch a Facebook page's public profile (likes, followers, category, about) by URL or handle.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/profile"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/profile', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/profile", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/profile", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/facebook/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Full Facebook page URL.  |
| `handle` | string |  | Facebook page handle/username.  |

## Details

Returns the public profile of a Facebook page, including its name, category, like and follower counts, contact details and ad status. It needs either a full page `url` or a page `handle`.

### Use cases

- Compare the `likes` and `followers` counts of competing brand pages.
- Check whether a brand is running ads on Facebook before you pull its ads.
- Collect the website and phone number listed on a business page for a lead list.
- Resolve a page URL to its numeric `id` and `adLibraryPageId` for use in other lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/nike"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | No | Facebook page handle/username. |
| `url` | string | No | Full Facebook page URL. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "about": "",
    "adLibraryPageId": "15087023444",
    "adStatus": "This Page is currently running ads.",
    "avatarUrl": "https://scontent-ord5-1.xx.fbcdn.net/v/t39.30808-1/284964043_10159903868513445_7…",
    "category": "Sportswear Store",
    "coverPhotoUrl": "https://scontent-ord5-2.xx.fbcdn.net/v/t39.30808-6/285211224_10159903868008445_5…",
    "createdUtc": 1211328000,
    "followers": 39000000,
    "id": "100044541544829",
    "likes": 39488396,
    "name": "Nike",
    "pageActive": false
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name` | Display name of the page. |
| `data.id` | Numeric ID of the page. |
| `data.category` | Category label of the page, for example `Sportswear Store`. |
| `data.likes / data.followers` | Number of likes and number of followers the page has. |
| `data.talkingAboutCount` | Count of people talking about the page, as reported on the page. |
| `data.adStatus` | Text that says whether the page is currently running ads. |
| `data.adLibraryPageId` | ID of the page in the Facebook ad library. Use it to look up the page's ads. |
| `data.createdUtc` | Page creation time as a Unix timestamp in seconds (UTC). |
| `data.website / data.phone` | Website and phone number listed on the page. |
| `data.avatarUrl / data.coverPhotoUrl` | Image URLs for the page's profile picture and cover photo. |

### Notes

- Send either `url` or `handle`. The example request uses `url`.
- Check `found` first. A lookup that finds no page returns `found: false`.
- `about` can be an empty string when the page has no description.
- To get a page's ads, call [Facebook Company Ads](/apis/facebook/company-ads). For recent posts, call [Facebook Get Profile Posts](/apis/facebook/profile-posts).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/profile.json`](../../../catalog/models/facebook/profile.json) · Store page: https://www.sandbase.ai/model/facebook/profile
