# Instagram Shortcode to Media ID API: pricing, parameters and code examples

`instagram/v1/shortcode-to-media-id` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Convert an Instagram post shortcode (from instagram.com/p/<shortcode>/) into the numeric media ID required by the Instagram post, comments and likes APIs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/shortcode-to-media-id", "shortcode": "DYurEPdgKQ4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/shortcode-to-media-id', {'shortcode': 'DYurEPdgKQ4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/shortcode-to-media-id", {
  "shortcode": "DYurEPdgKQ4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/shortcode-to-media-id", sandbase.Params{
	"shortcode": "DYurEPdgKQ4",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/shortcode-to-media-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shortcode` | string | yes | Post shortcode  |

## Details

Convert the shortcode in an Instagram post or reel link (`instagram.com/p/<shortcode>/` or `/reel/<shortcode>/`) into the numeric media ID that the comments, likers and post-detail APIs require.

### Use cases

- Turn post links collected from search, bios or spreadsheets into media IDs before fetching comments or likers.
- Deduplicate posts that arrive as both links and numeric IDs.
- Recover the post creation time from the media ID (see Notes).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/shortcode-to-media-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shortcode": "DRhvwVLAHAG"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shortcode` | string | Yes | Post shortcode |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "media_id": "3774507992167247878",
  "shortcode": "DRhvwVLAHAG",
  "status": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `media_id` | Numeric media ID as a string. Keep it as a string: it exceeds the 53-bit integer range of JavaScript. |
| `shortcode` | The shortcode you sent. |
| `status` | `true` when the conversion succeeded. |

### Notes

- An Instagram media ID and its shortcode are the same number in two encodings. The shortcode is the media ID written in base 64 with the alphabet `A-Z a-z 0-9 - _` (A = 0, _ = 63), so `DRhvwVLAHAG` and `3774507992167247878` name the same post. The media ID itself is a 64-bit snowflake: the top 41 bits are milliseconds since Instagram's epoch (2011-08-24 21:07:01.721 UTC), followed by 13 bits of shard ID and 10 bits of sequence, so `media_id >> 23` plus 1314220021721 gives the post's creation time in Unix milliseconds. Media IDs longer than 19 digits, with a `_<user_id>` suffix, are the same ID with the owner appended: drop the suffix before converting.
- v1, v2 and v3 return the same ID for the same shortcode; they differ only in upstream channel and price. v1 is the cheapest.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Get cities by country](/apis/instagram/v1/cities): Get cities/regions list of specified country.
- [Get posts by hashtag](/apis/instagram/v1/hashtag-posts): Get posts under specific hashtag.
- [Get location info](/apis/instagram/v1/location-info): Get detailed information of specified location.

---
Machine-readable: [`catalog/models/instagram/v1/shortcode-to-media-id.json`](../../../../catalog/models/instagram/v1/shortcode-to-media-id.json) · Store page: https://www.sandbase.ai/model/instagram/v1/shortcode-to-media-id
