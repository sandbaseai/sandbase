# TikTok User Playlists API: pricing, parameters and code examples

`tiktok/web/user-play-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the public playlists or mixes associated with a TikTok user using their secure user ID. Includes playlist metadata, video counts, and creator details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-play-list", "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-play-list', {'secUid': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-play-list", {
  "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-play-list", sandbase.Params{
	"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-play-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page default `30` |
| `cursor` | integer |  | Page cursor default `0` |
| `secUid` | string | yes | User secUid  |

## Details

Retrieve playlist collections for a specified TikTok account using the `secUid` parameter. Supports pagination controls through `cursor` and `count`.

### Use cases

- Inspect playlists curated by a target TikTok creator.
- Analyze video collection counts across profile mixes.
- Display organized video series on creator dashboard tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-play-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | User secUid |
| `count` | integer | No | Number per page |
| `cursor` | integer | No | Page cursor |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "playList": [
    {
      "id": "7681171537575824159",
      "mixName": "Songs Of The Summer 2026",
      "name": "Songs Of The Summer 2026",
      "videoCount": 3,
      "creator": {
        "id": "107955",
        "nickname": "<user>",
        "privateAccount": true,
        "verified": false
      }
    }
  ]
}
```

### Notes

- Paginate results using `cursor` and adjust the batch size with `count`.
- Requires the target account's `secUid`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-play-list.json`](../../../../catalog/models/tiktok/web/user-play-list.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-play-list
