# Douyin Work Hot Comment Word Cloud API: pricing, parameters and code examples

`douyin/billboard/hot-comment-word-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns word cloud analysis data and keyword weights extracted from comments on a Douyin video. Input a target video identifier to analyze audience feedback topics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-comment-word-list", "aweme_id": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-comment-word-list', {'aweme_id': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-comment-word-list", {
  "aweme_id": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-comment-word-list", sandbase.Params{
	"aweme_id": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-comment-word-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Work id  |

## Details

Returns a list of keywords taken from the comments on one Douyin video, each with a weight. It needs one input, the video's `aweme_id`.

### Use cases

- Find the most repeated words in a video's comments to see what viewers talk about.
- Build a word cloud image for a report on one Douyin video.
- Compare the top comment words of several videos to see how audience reactions differ.
- Spot calls to action or repeated phrases in comments, such as requests for replies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-comment-word-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7372484719365098803"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Work id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "related_comment": null,
      "value": 46,
      "word_seg": "宝宝"
    }
  ],
  "extra": {
    "now": 1793691108000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code` | Status code of the response. `0` appears in a normal response. |
| `data[]` | One entry per keyword found in the comments. |
| `data[].word_seg` | The keyword text, taken from the comments. |
| `data[].value` | The weight of the keyword. A higher number means the word counts for more in the word cloud. |
| `data[].related_comment` | Comments linked to the keyword. It is `null` in the sample response. |
| `extra.now` | A 13-digit number that looks like a timestamp in milliseconds. It is likely the time of the response. |
| `message` | Text message from the response. It is an empty string in the sample. |

### Notes

- Pass the video ID as `aweme_id`, for example `7372484719365098803`. Send it as a string.
- The request has no pagination parameters. The sample response returns all keywords in one `data` list.
- Use `data[].value` to size words in a word cloud or to sort keywords.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-comment-word-list.json`](../../../../catalog/models/douyin/billboard/hot-comment-word-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-comment-word-list
