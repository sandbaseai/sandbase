# Bilibili Video Comments (Web) API: pricing, parameters and code examples

`bilibili/web/video-comments` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comment threads and reply metadata for a specific Bilibili video. Query by video ID with optional page numbering.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/video-comments", "bv_id": "BV13eam6MEmV", "pn": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/video-comments', {'bv_id': 'BV13eam6MEmV', 'pn': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/video-comments", {
  "bv_id": "BV13eam6MEmV",
  "pn": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/video-comments", sandbase.Params{
	"bv_id": "BV13eam6MEmV",
	"pn": 1,
})
```

Same call via the path form: `POST /v1/api/bilibili/web/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pn` | integer |  | Page number default `1` |
| `bv_id` | string | yes | Video id  |

## Details

Retrieve user comments and replies for a specific Bilibili video using `bv_id`. You can paginate through comment threads using the `pn` parameter.

### Use cases

- Analyze viewer feedback and engagement on a video.
- Monitor top comments and user interactions on specific content.
- Collect discussion data across multiple video comment pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bv_id": "BV1M1421t7hT"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bv_id` | string | Yes | Video id |
| `pn` | integer | No | Page number |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "replies": [
      {
        "count": 47,
        "ctime": 1723373621,
        "dynamic_id_str": "0",
        "like": 2301,
        "rcount": 34,
        "type": 1,
        "member": {
          "rank": "10000",
          "uname": "笑chu腹肌"
        },
        "reply_control": {
          "sub_reply_entry_text": "共34条回复",
          "sub_reply_title_text": "相关回复共34条",
          "time_desc": "786天前发布"
        },
        "up_action": {
          "like": false
        }
      }
    ]
  }
}
```

### Notes

- Specify the target video using its identifier in `bv_id`.
- Use `pn` to paginate through comment results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-comments.json`](../../../../catalog/models/bilibili/web/video-comments.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-comments
