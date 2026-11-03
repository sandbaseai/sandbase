# Zhihu Pin Detail API: pricing, parameters and code examples

`zhihu/web/pin-detail` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves the full content and details of a single Zhihu pin using its unique pin identifier. Returns parsed text blocks, links, and formatting metadata.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/pin-detail", "pin_id": "2050290260991534603"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/pin-detail', {'pin_id': '2050290260991534603'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/pin-detail", {
  "pin_id": "2050290260991534603"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/pin-detail", sandbase.Params{
	"pin_id": "2050290260991534603",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/pin-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pin_id` | string | yes | Pin ID  |

## Details

Returns the full record of one Zhihu pin: its text and image blocks, author profile, engagement counts and a sample of users who liked it. It needs one input, the `pin_id` of the pin.

### Use cases

- Archive the text and image links of a Zhihu pin before it is edited or deleted.
- Track likes, favorites and comments on a pin to compare how a post performs.
- Pull the author profile attached to a pin to see who posted it and how many followers they have.
- Extract the image URLs and sizes from a pin to build a gallery or run image analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/pin-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"pin_id": "2050290260991534603"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `pin_id` | string | Yes | Pin ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ab_config": {
    "md_interact_unify": "1"
  },
  "admin_closed_comment": false,
  "author": {
    "avatar_url": "https://picx.zhimg.com/v2-84d915f37f2c56232c42566f0bef233d_720w.jpg?source=8a6f5…",
    "badge_v2": {
      "detail_badges": [],
      "icon": "",
      "merged_badges": [],
      "night_icon": "",
      "title": "我与我周旋久，宁作我~"
    },
    "exposed_medal": {
      "avatar_url": "https://picx.zhimg.com/v2-7565d834d652a9960da0cedd8d7952ee_720w.jpg?source=8a6f5…",
      "description": "被 100 个人关注",
      "medal_avatar_frame": "",
      "medal_id": "972477022068568064",
      "medal_name": "备受瞩目",
      "mini_avatar_url": "https://pica.zhimg.com/v2-7565d834d652a9960da0cedd8d7952ee_720w.jpg?source=8a6f5…"
    },
    "follower_count": 143,
    "gender": 0,
    "headline": "我与我周旋久，宁作我~",
    "id": "c72367b43730a490687966ceb87e9305",
    "is_advertiser": false,
    "is_blocked": false,
    "is_blocking": false,
    "is_followed": false,
    "is_following": false
  },
  "can_top": false,
  "comment_count": 13,
  "comment_permission": "all",
  "comments": [],
  "content": [
    {
      "content": "普通人学AI，建议死磕这10个油管博主 | <p>① Andrej Karpathy｜AI界传奇人物</p><p>主要分享：大模型原理、GPT训练过程、神经网络…",
      "fold_type": "raw",
      "own_text": "普通人学AI，建议死磕这10个油管博主 | <p>① Andrej Karpathy｜AI界传奇人物</p><p>主要分享：大模型原理、GPT训练过程、神经网络…",
      "text_link_type": "internal",
      "title": "",
      "type": "text"
    }
  ],
  "content_html": "<div>普通人学AI，建议死磕这10个油管博主 | <p>① Andrej Karpathy｜AI界传奇人物</p><p>主要分享：大模型原理、GPT训练过程…",
  "created": 1781607393,
  "creation_disclaimer": "",
  "current_user_is_navigator": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `content[]` | List of content blocks in the pin. Each block has a `type` such as `text` or `image`. |
| `content[].own_text` | Text of a `text` block. It can contain inline HTML tags such as `<p>`. |
| `content[].url / content[].original_url / content[].watermark_url` | Links to an `image` block in its standard, original and watermarked versions. `width` and `height` give the image size. |
| `content_html` | The pin body as one HTML string. |
| `created` | Creation time of the pin as a Unix timestamp in seconds. |
| `like_count / comment_count / favorite_count / repin_count` | Counts of likes, comments, favorites and reposts for the pin. |
| `author.name / author.url_token / author.headline / author.follower_count` | Display name, URL token, headline and follower count of the pin author. |
| `likers[]` | Sample of users who liked the pin. Each entry has the same profile fields as `author`. |
| `reaction.statistics.up_vote_count` | Number of upvotes on the pin. Other counters such as `share_count` and `down_vote_count` sit in the same object. |
| `pin_type / state / is_deleted` | Type of the pin, its current state, and whether it is deleted. |

### Notes

- `pin_id` is a numeric string such as `2050290260991534603`. The same value comes back in the `id` field.
- To read the discussion under a pin, call [Zhihu Pin Comments](/apis/zhihu/web/pin-comments). The `comments` list in this response was empty.
- To list pins from one author, call [Zhihu User Pins](/apis/zhihu/web/user-pins), then pass a returned pin ID here.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/pin-detail.json`](../../../../catalog/models/zhihu/web/pin-detail.json) · Store page: https://www.sandbase.ai/model/zhihu/web/pin-detail
