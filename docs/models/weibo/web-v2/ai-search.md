# Weibo AI Search API: pricing, parameters and code examples

`weibo/web-v2/ai-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/ai-search", "query": "#人工智能#"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/ai-search', {'query': '#人工智能#'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/ai-search", {
  "query": "#人工智能#"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/ai-search", sandbase.Params{
	"query": "#人工智能#",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/ai-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword (required, recommend using topic format #TopicName#)  |

## Details

Returns the result of a Weibo AI search for one keyword or topic. The response holds an AI-written answer in `msg`, a block of multimodal post cards in `card_multimodal`, and links to the source posts. It needs one input, `query`.

### Use cases

- Pull the AI summary text for a Weibo topic such as `#人工智能#` to see how Weibo describes it.
- List the image and video posts that Weibo ranks highest for a topic, with the author name and media URL.
- Rank candidate posts for a topic by `hit_score_final` to pick the ones to review first.
- Collect the post IDs behind an AI answer so you can fetch full post details or comments.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/ai-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "#人工智能#"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required, recommend using topic format #TopicName#) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ab_suffix": "default",
  "abtest_info": {
    "chat_entrance": 1
  },
  "analysis_time": 1793666810,
  "basemodel": "实验组82",
  "business_context": "long_tail_query",
  "card_multimodal": {
    "data": [
      {
        "click_num": 0,
        "click_rate": 0,
        "cur_mid": "5361060795386149",
        "doc_score": 7754,
        "focus_point": {
          "height": 0.6923247,
          "left": 0.07478951,
          "top": 0.2864349,
          "width": 0.9230996
        },
        "h": 2304,
        "hit_score_final": 90.378128,
        "hit_score_new": 90.722656,
        "id": "emphasis-tag-0",
        "img": "http://wx3.sinaimg.cn/middle/5854ac96ly1iiomfq4rcej21c01s0hdu.jpg",
        "img_pid": "5854ac96ly1iiomfq4rcej21c01s0hdu",
        "scheme": "sinaweibo://multimedia?mix_mid=5361060795386149&from=search&content_show=1&mix_i…"
      }
    ],
    "type": "mediablock"
  },
  "chat_status_stage": 4,
  "comment_info": {},
  "content_tail": "",
  "cot": 1,
  "current_model": "deepseek-v4-flash",
  "current_time": 1793691982153
}
```

### Response fields

| Field | Meaning |
|---|---|
| `msg` | The AI-generated answer text, in the format named by `msg_format` (here `markdown`). It can begin with a `<think>` reasoning section. |
| `display_query` | The query string that Weibo searched, such as `#人工智能#`. |
| `card_multimodal.data[].cur_mid` | The ID of the post that the card shows. |
| `card_multimodal.data[].type / card_multimodal.data[].vtype` | The card media type. The sample shows `p` for a picture card and `v` for a video card. `vtype` is a numeric subtype, `0` for the picture card and `3` for the video cards. |
| `card_multimodal.data[].hit_score_final / card_multimodal.data[].hit_score_new / card_multimodal.data[].doc_score` | Relevance scores for the card. Higher values mean a stronger match in the sample ordering, and `doc_score` falls from the first card to the last. |
| `card_multimodal.data[].user_name / card_multimodal.data[].user_avatar` | The display name and avatar image URL of the post author. |
| `card_multimodal.data[].img / card_multimodal.data[].video_url` | The cover image URL and, for video cards, the video page URL. `video_url` is an empty string for picture cards. |
| `card_multimodal.data[].w / card_multimodal.data[].h` | Width and height of the card image. The response does not state the unit. |
| `link_list` | Links in the `sinaweibo://detail?mblogid=` form that point to the posts used for the answer. |
| `current_model` | The name of the model that wrote the answer. |

### Notes

- Set `query` in topic format, for example `#人工智能#`. The endpoint takes no pagination parameters.
- Post IDs appear in `cur_mid` and in `link_list` after `mblogid=`. Pass them to [Weibo Post Detail](/apis/weibo/web-v2/post-detail) or [Weibo Post Comments](/apis/weibo/web-v2/post-comments).
- `scheme` holds an app deep link that starts with `sinaweibo://`. It opens in the Weibo app, not in a browser.
- For related questions and recommended bloggers on the same keyword, call [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo All Groups Information](/apis/weibo/web-v2/all-groups): Retrieves complete group information on the Weibo platform.

---
Machine-readable: [`catalog/models/weibo/web-v2/ai-search.json`](../../../../catalog/models/weibo/web-v2/ai-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/ai-search
