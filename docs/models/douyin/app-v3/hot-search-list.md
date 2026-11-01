# Douyin Hot Search List

`douyin/app-v3/hot-search-list` · api · Douyin

Get the Douyin hot search list and other boards (seeding, entertainment, social and challenge lists): trending words with heat values and video counts.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/hot-search-list", "board_sub_type": "", "board_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/hot-search-list', {'board_sub_type': '', 'board_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/hot-search-list", {
  "board_sub_type": "",
  "board_type": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/hot-search-list", sandbase.Params{
	"board_sub_type": "",
	"board_type": "0",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/hot-search-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `board_type` | string |  | - 0: Hot search list (default) default `"0"` |
| `board_sub_type` | string |  | - Empty string: Hot search list (default) default `""` |

## Details

Fetch the current Douyin hot search board, or switch to the seeding, entertainment, social or challenge lists with `board_type`.

### Use cases

- Track trending topics on Douyin in real time.
- Find hot challenges for content planning.
- Alert when a brand or product starts trending.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/hot-search-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `board_type` | string | No | - 0: Hot search list (default) |
| `board_sub_type` | string | No | - Empty string: Hot search list (default) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "active_time": "2026-10-06 16:57:19",
    "word_list": [
      {
        "position": 13,
        "word": "跑步真的伤膝盖吗",
        "hot_value": 9039299,
        "sentence_id": "2682767",
        "event_time": 1791245696,
        "video_count": 1,
        "label": 16
      }
    ]
  }
}
```

### Notes

- `board_type` selects the list; `"0"` is the main hot search list.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Video Statistics (Batch)](/model/douyin/app-v3/multi-video-statistics): Get play, like, share and download counts for up to 50 Douyin videos in one request by passing comma-separated video IDs.
- [Douyin User Videos](/model/douyin/app-v3/user-post-videos): Get the videos on a Douyin user's profile with descriptions, publish time and play, like, comment and share counts.
- [Get Douyin brand hot search list data](/model/douyin/app-v3/brand-hot-search-list): Get Douyin brand hot search category data.

---
Machine-readable: [`catalog/models/douyin/app-v3/hot-search-list.json`](../../../../catalog/models/douyin/app-v3/hot-search-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/hot-search-list
