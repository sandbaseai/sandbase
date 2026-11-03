# WeChat MP Comment Replies API: pricing, parameters and code examples

`wechat-mp/v2/comment-replies` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns second-level replies under a specific WeChat MP article comment using the article url and comment identifiers. Supports pagination offset and raw output formats.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/comment-replies", "url": "http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/comment-replies', {'url': 'http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/comment-replies", {
  "url": "http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/comment-replies", sandbase.Params{
	"url": "http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=full raw reply objects; False=simplified replies.  |
| `url` | string | yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…`). E.g. `http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd`  |
| `offset` | integer |  | Optional, default 0 (>=0). Reply pagination offset; 0 for the first page, pass `next_offset` from the previous response when `has_more=true`. Ignored when `all_pages=true`. range 0– |
| `comment_id` |  |  | 文章的评论 id（可选，**性能捷径**）：不传时上游要先抓并解析整篇文章 HTML 才能拿到它，约占本接口耗时的一半；已有该值时传进来可显著加快。取自 /fetch_article_detail 或 /fetch_article_detail_h5 响应的 `$.data.content.comment_id`/Article comment id (optional, performance shortcut): when…  |
| `content_id` |  |  | Optional (numeric). `content_id` of the target first-level comment, from `$.data.comments[N].content_id` of the `fetch_article_comments` response; **defaults to the first comment that has replies when omitted**. E.g.…  |

## Details

Returns the second-level replies under one comment on a WeChat MP article. It needs the article `url`, and you can pass `content_id` to pick the parent comment. Each reply includes its text, author name, like count and post time.

### Use cases

- Read the full reply thread under a top-ranked comment on a WeChat MP article.
- Collect reader reactions and reply like counts to see which replies get the most support.
- Check whether the article's own account replied in a thread, using the account identity fields.
- Export replies in pages to store or analyze discussion around one article.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…`). E.g. `http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd` |
| `comment_id` | string | No | 文章的评论 id（可选，**性能捷径**）：不传时上游要先抓并解析整篇文章 HTML 才能拿到它，约占本接口耗时的一半；已有该值时传进来可显著加快。取自 /fetch_article_detail 或 /fetch_article_detail_h5 响应的 `$.data.content.comment_id`/Article comment id (optional, performance shortcut): when omit |
| `content_id` | string | No | Optional (numeric). `content_id` of the target first-level comment, from `$.data.comments[N].content_id` of the `fetch_article_comments` response; **defaults to the first comment that has replies when omitted**. E.g. `12 |
| `offset` | integer | No | Optional, default 0 (>=0). Reply pagination offset; 0 for the first page, pass `next_offset` from the previous response when `has_more=true`. Ignored when `all_pages=true`. |
| `raw` | boolean | No | Optional, default True. True=full raw reply objects; False=simplified replies. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "content_id": "12109128638545265979",
  "count": 10,
  "debug_id": "0d41cab3",
  "debug_info": "gAAAAABq6ZFm9cqo_BaXAx6tA_99hUS5k-sFZNfmp4SXBeT9jRLMb-sPphtjS_Hpdix7smKz4HPQeF97…",
  "has_more": true,
  "next_offset": 10,
  "offset": 0,
  "parent_nick": "静思",
  "replies": [
    {
      "author_like_status": 0,
      "bizattr_servicetype": 1,
      "can_share": true,
      "content": "[破涕为笑][破涕为笑][破涕为笑]",
      "create_time": 1756807415,
      "from_ai": false,
      "identity_name": "gh_d679208ae987",
      "identity_type": 1,
      "is_from": 2,
      "is_from_friend": 0,
      "is_reward": 0,
      "logo_url": "https://wx.qlogo.cn/mmhead/SQd7RF5caa1fc1EKVsgLwgCxw9KicpM9h1ibJaqjvAl30sx8EFvkw…"
    }
  ],
  "reply_total": 14
}
```

### Response fields

| Field | Meaning |
|---|---|
| `content_id` | ID of the parent first-level comment these replies belong to. |
| `reply_total` | Total number of replies under that comment. |
| `has_more / next_offset` | `has_more` is `true` when more replies remain. Pass `next_offset` as `offset` to get the next page. |
| `count / offset` | Number of replies returned in this page and the offset this page started from. |
| `parent_nick` | Nickname of the author of the parent comment. |
| `replies[].content` | Text of the reply. Emoji appear as bracket codes such as `[破涕为笑]`. |
| `replies[].nick_name` | Display name of the reply author. |
| `replies[].create_time` | Time the reply was posted, as a Unix timestamp in seconds. |
| `replies[].reply_like_num` | Number of likes on the reply. |
| `replies[].reply_id` | Sequence ID of the reply within the thread. |
| `replies[].ip_wording.province_name` | Province shown for the reply author. Some replies, such as ones from the article's account, do not include `ip_wording`. |

### Notes

- Get `content_id` from the `comments[].content_id` field of [WeChat MP Article Comments](/apis/wechat-mp/v2/article-comments). If you omit it, the API uses the first comment that has replies.
- Get `comment_id` from the article detail response at `data.content.comment_id`, for example from [WeChat MP Article Detail (H5, Recommended)](/apis/wechat-mp/v2/article-detail-h5). Passing it skips the article page lookup and speeds up the call.
- To page through replies, start with `offset` at `0`. While `has_more` is `true`, send `next_offset` as the next `offset`.
- Set `raw` to `false` to get simplified reply objects instead of the full raw ones shown here.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat MP Account Articles](/apis/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [WeChat MP Account Profile](/apis/wechat-mp/v2/account-profile): Retrieves the profile details of an official WeChat account, including name, avatar, signature, and verification entity type using its official account ID.
- [WeChat MP Article Ads](/apis/wechat-mp/v2/article-ad): Returns embedded ad slot information for a specified WeChat MP article URL.

---
Machine-readable: [`catalog/models/wechat-mp/v2/comment-replies.json`](../../../../catalog/models/wechat-mp/v2/comment-replies.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/comment-replies
