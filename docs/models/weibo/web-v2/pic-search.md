# Weibo Picture Search API: pricing, parameters and code examples

`weibo/web-v2/pic-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns picture content and associated post details matching a search query on Weibo. Results include image URLs, post text, and user profile information.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/pic-search", "page": 1, "query": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/pic-search', {'page': 1, 'query': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/pic-search", {
  "page": 1,
  "query": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/pic-search", sandbase.Params{
	"page": 1,
	"query": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/pic-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (default 1) default `1` |
| `query` | string | yes | Search keyword (required)  |

## Details

Returns Weibo posts that contain pictures and match a search keyword. Each result has an image URL, the post text, and basic details about the user who posted it. It needs one input, `query`, and takes an optional `page`.

### Use cases

- Collect images that Weibo users post about a brand or product name.
- Pull post text next to each picture to review how a topic is discussed with images.
- Build a list of accounts that post pictures about a keyword using `user.name` and `user.profile_url`.
- Check whether a picture comes from an original post or a repost with `is_forward`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/pic-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required) |
| `page` | integer | No | Page number (default 1) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "claim_auth": [],
  "claim_auth_white": true,
  "is_end": 0,
  "noResultMsg": "抱歉，未找到相关结果。",
  "pic_list": [
    {
      "created_at": "Tue Nov 03 15:42:14 +0800 2026",
      "forward_id": 0,
      "is_forward": false,
      "mid": "5361194065202409",
      "original_pic": "//wx1.sinaimg.cn/large/66fd066bly1iip1qt0l0sj20hw0aadhh.jpg",
      "sub_name": "宝玉xp",
      "sub_text": "OpenAI 的下一代大模型可能要来了，正好接上...",
      "text": "OpenAI 的下一代大模型可能要来了，正好接上 Altman 11 月 2 日在阿布扎比说的“下一个 GPT 很快发布”。\n\n不过目前只是猜测，没有正式发布。…",
      "url": "//wx1.sinaimg.cn/thumb180/66fd066bly1iip1qt0l0sj20hw0aadhh.jpg",
      "user": {
        "name": "宝玉xp",
        "profile_image_url": "//tva3.sinaimg.cn/crop.0.0.180.180.50/66fd066bjw1e8qgp5bmzyj2050050aa8.jpg?KID=i…",
        "profile_url": "//weibo.com/dotey"
      }
    }
  ],
  "risk_control": {
    "aitabHidden": 0,
    "cateList": [],
    "navControl": [],
    "overall": 0
  },
  "suda_pre": "seqid:179369198652802043194|type:0|t:0|pos:1-0|q:OpenAI|ext:",
  "total_number": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `pic_list[]` | One picture result per item. Each item holds the image links, the post text and the poster. |
| `pic_list[].original_pic` | Link to the large version of the image. It starts with `//`, so add `https:` to use it. |
| `pic_list[].url` | Link to a small thumbnail (`thumb180`) of the same image. |
| `pic_list[].text` | Text of the post. Long posts end with an ellipsis. |
| `pic_list[].sub_text` | Shorter preview of the post text. |
| `pic_list[].mid` | ID of the post as a string of digits. |
| `pic_list[].created_at` | Time the post was created, for example `Tue Nov 03 15:42:14 +0800 2026`. |
| `pic_list[].is_forward / pic_list[].forward_id` | `is_forward` is `true` when the post is a repost. `forward_id` holds an ID for a repost and is `0` when the post is not a repost. |
| `pic_list[].user.name / pic_list[].user.profile_url` | Display name of the poster and a link to their Weibo profile. `sub_name` repeats the name at the item level. |
| `pic_list[].user.profile_image_url` | Link to the poster's avatar image. |
| `is_end` | Paging flag. The value `0` is shown in this response, which had results. |

### Notes

- `pic_list[].mid` is the post ID. Pass it to [Weibo Post Detail](/apis/weibo/web-v2/post-detail) to get the full post.
- Image and profile links start with `//`. Add `https:` before you open them.
- Set `page` to get later result pages. It defaults to 1.
- `total_number` returned `0` even though `pic_list` had items, so count the items in `pic_list` instead.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/pic-search.json`](../../../../catalog/models/weibo/web-v2/pic-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/pic-search
