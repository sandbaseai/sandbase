# Bilibili Comment Replies API: pricing, parameters and code examples

`bilibili/web/comment-reply` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns replies to a specific comment on a Bilibili video by video ID and comment ID. Supports pagination to browse threaded discussion replies.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/comment-reply", "bv_id": "BV1dFad6aEz9", "rpid": "237108091664"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/comment-reply', {'bv_id': 'BV1dFad6aEz9', 'rpid': '237108091664'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/comment-reply", {
  "bv_id": "BV1dFad6aEz9",
  "rpid": "237108091664"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/comment-reply", sandbase.Params{
	"bv_id": "BV1dFad6aEz9",
	"rpid": "237108091664",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/comment-reply` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pn` | integer |  | Page number  |
| `rpid` | string | yes | Reply id  |
| `bv_id` | string | yes | Video id  |

## Details

Fetch threaded replies for a specific comment using `bv_id` and `rpid`. Browse through conversation pages by specifying `pn`.

### Use cases

- Inspect user conversations beneath specific video comments.
- Analyze engagement and reaction metrics on comment threads.
- Build moderation or archiving tools for video discussion replies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/comment-reply" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bv_id": "BV1dFad6aEz9", "rpid": "237108091664"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `rpid` | string | Yes | Reply id |
| `bv_id` | string | Yes | Video id |
| `pn` | integer | No | Page number |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "replies": [
      {
        "count": 0,
        "ctime": 1723373731,
        "dynamic_id_str": "0",
        "like": 18,
        "rcount": 0,
        "type": 1,
        "member": {
          "rank": "10000",
          "uname": "喜欢孤独的滋味"
        },
        "reply_control": {
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

- Identify the target video using `bv_id`.
- Provide the parent comment identifier via `rpid`.
- Use `pn` to page through nested reply results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/comment-reply.json`](../../../../catalog/models/bilibili/web/comment-reply.json) · Store page: https://www.sandbase.ai/model/bilibili/web/comment-reply
