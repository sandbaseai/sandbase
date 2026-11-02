# TikTok Tag Posts API: pricing, parameters and code examples

`tiktok/web/tag-post` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of TikTok videos associated with a specific tag or challenge ID. Supports pagination using cursor and count parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/tag-post", "challengeID": "7551"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/tag-post', {'challengeID': '7551'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/tag-post", {
  "challengeID": "7551"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/tag-post", sandbase.Params{
	"challengeID": "7551",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/tag-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page default `30` |
| `cursor` | integer |  | Page cursor default `0` |
| `challengeID` | string | yes | Tag ID  |

## Details

Retrieve videos tied to a specific hashtag challenge by supplying `challengeID`. Supports pagination via `cursor` and `count`.

### Use cases

- Retrieve video content grouped under a specific TikTok hashtag challenge.
- Analyze trending videos associated with a targeted tag ID.
- Collect paginated video feeds for hashtag performance research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/tag-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"challengeID": "7551"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `challengeID` | string | Yes | Tag ID |
| `count` | integer | No | Number per page |
| `cursor` | integer | No | Page cursor |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "itemList": [
    {
      "video": {
        "bitrateInfo": [
          {
            "CodecType": "h264",
            "GearName": "normal_720_0",
            "QualityType": 10
          }
        ]
      }
    }
  ]
}
```

### Notes

- Specify the target hashtag identifier using `challengeID`.
- Manage pagination via `cursor` and configure batch size with `count`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/tag-post.json`](../../../../catalog/models/tiktok/web/tag-post.json) · Store page: https://www.sandbase.ai/model/tiktok/web/tag-post
