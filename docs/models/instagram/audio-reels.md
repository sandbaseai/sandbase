# Instagram Reels by Audio API: pricing, parameters and code examples

`instagram/audio-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

List Instagram reels that use a given audio track by audio id.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/audio-reels", "audioId": "1392969992841787"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/audio-reels', {'audioId': '1392969992841787'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/audio-reels", {
  "audioId": "1392969992841787"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/audio-reels", sandbase.Params{
	"audioId": "1392969992841787",
})
```

Same call via the path form: `POST /v1/api/instagram/audio-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor returned by a previous response.  |
| `audioId` | string | yes | Audio identifier from the Instagram audio page URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `reshares`, and it is served only by a source that returns every one…  |

## Details

Returns a page of Instagram reels that use a given audio track. Each reel includes the creator, caption, engagement counts, and location data when present. The only required input is `audioId`.

### Use cases

- Track how many creators use a song and which reels get the most plays.
- Find creators who post with a specific sound to plan outreach.
- Compare `likes`, `comments`, and `reshares` across reels that share one audio track.
- Collect reels tagged with a place by reading the location fields.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/audio-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"audioId": "1392969992841787"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `audioId` | string | Yes | Audio identifier from the Instagram audio page URL. |
| `cursor` | string | No | Pagination cursor returned by a previous response. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `reshares`, and it is served only by a source that returns every one o |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "hasMore": true,
    "nextCursor": "cur_5wMl39Ie9zJrkNOUjs_d3A",
    "reels": [
      {
        "avatarUrl": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/795554226_18091598798677…",
        "caption": "SOMEONE GET IN THE BOAT\n\n#crowdsurf #moshpit #grunge #rockmusic #concerts",
        "code": "DeFBkTapVop",
        "comments": 77,
        "createdUtc": 1791130067,
        "displayName": "Dexter and The Moonrocks",
        "durationSeconds": 29.882,
        "handle": "the_moonrocks",
        "hashtags": [
          "#crowdsurf"
        ],
        "id": "4000610736784366121",
        "image": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/836512536_18093524156677…",
        "likes": 16593
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.reels[].code` | Short code of the reel. It is the identifier used in Instagram post URLs. |
| `data.reels[].id` | Numeric ID of the reel as a string. |
| `data.reels[].handle / data.reels[].displayName` | Username and display name of the account that posted the reel. |
| `data.reels[].caption` | Caption text of the reel. |
| `data.reels[].plays / data.reels[].likes / data.reels[].comments / data.reels[].reshares` | Engagement counts for the reel: plays, likes, comments, and reshares. |
| `data.reels[].createdUtc` | Time the reel was posted, as a Unix timestamp in seconds. |
| `data.reels[].durationSeconds` | Length of the reel in seconds. |
| `data.reels[].hashtags / data.reels[].mentions` | Hashtags and @handles found in the caption, as lists of strings. |
| `data.reels[].locationName / data.reels[].locationLat / data.reels[].locationLng` | Place tagged on the reel with its coordinates. These are `null` when no location is tagged. |
| `data.hasMore / data.nextCursor` | Whether more reels exist, and the cursor that fetches the next page. |

### Notes

- Take `audioId` from the Instagram audio page URL.
- To get the next page, send `data.nextCursor` as `cursor` along with the same `audioId`. Stop when `hasMore` is `false`.
- Pass `requireFields` with names such as `reshares` or `taggedUsers` when you need those fields on every reel. The call may then cost more.
- To read one reel in full, pass its `code` to [Instagram Post Details](/apis/instagram/post-detail).

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/audio-reels.json`](../../../catalog/models/instagram/audio-reels.json) · Store page: https://www.sandbase.ai/model/instagram/audio-reels
