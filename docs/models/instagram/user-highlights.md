# Instagram User Highlights API: pricing, parameters and code examples

`instagram/user-highlights` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List an Instagram account's story highlight reels by handle.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/user-highlights", "handle": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/user-highlights', {'handle': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/user-highlights", {
  "handle": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/user-highlights", sandbase.Params{
	"handle": "nasa",
})
```

Same call via the path form: `POST /v1/api/instagram/user-highlights` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Instagram username without the leading @.  |
| `userId` | string |  | Instagram numeric user id (optional, faster than handle).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `mediaCount`, and it is served only by a source that returns every…  |

## Details

This API returns the story highlight reels of an Instagram account. It needs the account's `handle`, and it also accepts a numeric `userId`. Each highlight comes back with its id, title, owner and avatar image.

### Use cases

- Show the titles of an account's highlight reels in a brand monitoring dashboard.
- Collect highlight ids for a list of accounts, then fetch the stories inside each one.
- Check whether a creator or brand keeps highlights such as product or campaign collections.
- Map a handle to its numeric `userId` and avatar URL in the same call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/user-highlights" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Instagram username without the leading @. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `mediaCount`, and it is served only by a source that returns every one |
| `userId` | string | No | Instagram numeric user id (optional, faster than handle). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "highlights": [
      {
        "avatarUrl": "https://scontent-iad6-1.cdninstagram.com/v/t51.2885-19/29090066_159271188110124_…",
        "coverUrl": "",
        "createdUtc": null,
        "id": "18195781759377100",
        "mediaCount": null,
        "ownerHandle": "nasa",
        "title": "Roman",
        "userId": "528817151"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the account was found. A lookup that finds nothing returns `false`. |
| `data.highlights[]` | One entry per highlight reel on the account. |
| `data.highlights[].id` | Identifier of the highlight reel. Use it to look up the reel's contents. |
| `data.highlights[].title` | Name of the highlight as shown on the profile, for example `Artemis III`. |
| `data.highlights[].ownerHandle` | Instagram handle of the account that owns the highlight. |
| `data.highlights[].userId` | Numeric Instagram id of the owning account. |
| `data.highlights[].avatarUrl` | URL of the owner's profile picture, not of the highlight cover. |
| `data.highlights[].coverUrl` | URL of the highlight cover image. It can be an empty string. |
| `data.highlights[].createdUtc / data.highlights[].mediaCount` | Creation time and number of items in the highlight. Both can be `null` in the default response. |

### Notes

- Pass `userId` along with `handle` for a faster lookup. The `userId` appears in each highlight, so you can reuse it on later calls.
- `createdUtc` and `mediaCount` can be `null`. Add them to `requireFields` to get a source that returns them. This can raise the price of the call.
- Pass a highlight `id` to [Instagram Highlight Detail](/apis/instagram/highlight-detail) to get the contents of one reel.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/user-highlights.json`](../../../catalog/models/instagram/user-highlights.json) · Store page: https://www.sandbase.ai/model/instagram/user-highlights
