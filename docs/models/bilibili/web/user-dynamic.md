# Bilibili User Dynamics API: pricing, parameters and code examples

`bilibili/web/user-dynamic` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves dynamic feed posts and timeline updates for a specified Bilibili user by UID, with optional offset-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-dynamic", "offset": "", "uid": "178360345"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-dynamic', {'offset': '', 'uid': '178360345'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-dynamic", {
  "offset": "",
  "uid": "178360345"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-dynamic", sandbase.Params{
	"offset": "",
	"uid": "178360345",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-dynamic` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |
| `offset` | string |  | offset default `""` |

## Details

List a Bilibili user's dynamics (动态) feed: video uploads, text and image posts, reposts and articles, newest first, with author, publish time and like, comment and forward counts.

### Use cases

- Monitor a creator's new uploads and posts.
- Collect a user's activity for analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-dynamic" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "178360345"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |
| `offset` | string | No | offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "has_more": false,
    "offset": "",
    "items": [
      {
        "id_str": "1252966819274162197",
        "type": "DYNAMIC_TYPE_AV",
        "modules": {
          "module_author": {
            "name": "Azulsolitan",
            "mid": 178360345,
            "pub_ts": "1790567471"
          },
          "module_dynamic": {
            "major": {
              "archive": {
                "bvid": "BV1RMaq65EAH",
                "title": "ATM10sky通关纪念",
                "duration_text": "06:50",
                "jump_url": "//www.bilibili.com/video/BV1RMaq65EAH",
                "stat": {
                  "danmaku": "0",
                  "play": "36",
                  "vt": ""
                }
              }
            }
          },
          "module_stat": {
            "comment": {
              "count": 0
            },
            "forward": {
              "count": 0
            },
            "like": {
              "count": 0
            }
          }
        }
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].type` | Kind of dynamic, e.g. `DYNAMIC_TYPE_AV` (video), `DYNAMIC_TYPE_DRAW` (images), `DYNAMIC_TYPE_FORWARD` (repost). |
| `items[].modules.module_author` | Author `name`, `mid` and `pub_ts` (Unix seconds). |
| `items[].modules.module_dynamic.major` | The content; for videos `archive` with `bvid`, `title`, `duration_text`, play and danmaku counts. |
| `items[].modules.module_stat` | Comment, forward and like counts. |
| `data.has_more / offset` | Pass `offset` back to get the next page. |

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/user-dynamic.json`](../../../../catalog/models/bilibili/web/user-dynamic.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-dynamic
