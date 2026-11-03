# Douyin Item Report Comments API: pricing, parameters and code examples

`douyin/xingtu-v2/item-report-comments` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call · **Modes:** sync

Get Item Report Comments on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.003 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/item-report-comments", "item_id": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/item-report-comments', {'item_id': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/item-report-comments", {
  "item_id": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/item-report-comments", sandbase.Params{
	"item_id": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/item-report-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video (item) ID  |

## Details

Returns a list of comments for one Douyin video, taken from its Xingtu item report. Each comment has its ID, text, like count and reply count. The only input is the video `item_id`.

### Use cases

- Read what viewers say under a sponsored video to judge audience reaction.
- Sort comments by `like_count` to find the most liked comments on a video.
- Export comment text for sentiment or keyword analysis of a campaign video.
- Check how many replies a comment drew to spot threads that started a discussion.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/item-report-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7372484719365098803"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video (item) ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "comments": [
    {
      "comment_count": "30",
      "comment_id": "7372955079207256882",
      "comment_text": "不仅赞还评论你也尽量[比心]",
      "like_count": "97"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_resp.status_code / base_resp.status_message` | Status of the request. A `status_code` of `0` with an empty `status_message` means the call worked. |
| `comments[]` | List of comments on the video. Each entry is one comment. |
| `comments[].comment_id` | ID of the comment, returned as a string. |
| `comments[].comment_text` | Text of the comment. It can contain platform emoji codes such as `[比心]`. |
| `comments[].like_count` | Number of likes the comment received, returned as a string. |
| `comments[].comment_count` | Number of replies to the comment, returned as a string. |

### Notes

- `item_id` is the Douyin video ID, for example `7372484719365098803`.
- Numeric values such as `like_count` and `comment_count` come back as strings, so convert them before sorting.
- For other report views of the same video, call [Douyin Item Report Detail](/apis/douyin/xingtu-v2/item-report-detail) or [Douyin Item Report Interaction Analysis](/apis/douyin/xingtu-v2/item-report-th-analysis).

### Pricing

$0.003 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/item-report-comments.json`](../../../../catalog/models/douyin/xingtu-v2/item-report-comments.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/item-report-comments
