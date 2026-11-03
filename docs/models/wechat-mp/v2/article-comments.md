# WeChat MP Article Comments API: pricing, parameters and code examples

`wechat-mp/v2/article-comments` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get the comments on a WeChat official account article from its URL: comment text, likes, time and commenter region, with cursor pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/article-comments", "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/article-comments', {'url': 'https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/article-comments", {
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/article-comments", sandbase.Params{
	"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/article-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=full raw comment objects; False=simplified comment view. default `true` |
| `url` | string | yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…`). E.g. `https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw`  |
| `buffer` |  |  | Optional, default empty. Pagination cursor; leave empty for the first page, pass `buffer` from the previous response for the next page. default `""` |

## Details

This API returns the comments on a WeChat official account article. It needs the article URL in the form `https://mp.weixin.qq.com/s/...`. Each comment has its text, like count, post time and the commenter's region.

### Use cases

- Read how an audience reacts to a published article by sorting comments by `like_num`.
- Collect reader feedback on a sponsored post for a campaign report.
- Track comment volume on a competitor's article by comparing `total_count` over time.
- Group commenters by province to see where an article's readers are located.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/article-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw", "raw": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…`). E.g. `https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw` |
| `buffer` | string | No | Optional, default empty. Pagination cursor; leave empty for the first page, pass `buffer` from the previous response for the next page. |
| `raw` | boolean | No | Optional, default True. True=full raw comment objects; False=simplified comment view. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "appmsgid": "2247780992",
  "buffer": "GBQwAA==",
  "comment_id": "3884868893382230017",
  "comments": [
    {
      "bucket": "elected_comment",
      "content": "所谓的软件优化要是真能提升性能的话，老黄他敢卖只有一组128流处理器的游戏卡",
      "content_id": "6255846262940111556",
      "create_time": 1741148719,
      "identity_name": "oHQDtwFlc10nT5noCRuBWtzFyAB0",
      "ip_wording": {
        "city_id": "",
        "city_name": "",
        "country_id": "156",
        "country_name": "中国",
        "province_id": "",
        "province_name": "浙江"
      },
      "is_elected": 1,
      "is_top": 0,
      "like_num": 87,
      "nick_name": "舟",
      "replies": [],
      "reply_total": 0
    }
  ],
  "continue_flag": true,
  "debug_id": "274abfa0",
  "debug_info": "gAAAAABq6ZFFk646JNd6c3Vwdh3W_qwzeiLr3aAaqboZqF8AYBu47-DtHajMf37OrgyKbEHqYOGu4dTf…",
  "elected_total": 21,
  "has_more": true,
  "total_count": 26
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[].content` | Text of the comment. It can include WeChat emoji codes such as `[奸笑]`. |
| `comments[].like_num` | Number of likes on the comment. |
| `comments[].create_time` | Time the comment was posted, as a Unix timestamp in seconds. |
| `comments[].nick_name / comments[].identity_name` | Display name of the commenter and an opaque identifier string for the commenter. |
| `comments[].ip_wording.province_name / comments[].ip_wording.country_name` | Province and country shown for the commenter. The city fields can be empty strings. |
| `comments[].content_id` | ID of the comment. Use it to tell comments apart. |
| `comments[].reply_total / comments[].replies` | Number of replies to the comment and the list of replies returned with it. Both can be empty or zero. |
| `comments[].is_top / comments[].is_elected` | Flags set to `1` or `0`. `is_top` marks a pinned comment and `is_elected` marks a featured comment. |
| `total_count / elected_total` | Total comment count for the article and the count of featured comments. |
| `has_more / buffer` | `has_more` shows whether more pages exist. `buffer` is the cursor to request the next page. |

### Notes

- Set `buffer` to empty for the first page. For the next page, send the `buffer` value from the previous response with the same `url`.
- Stop paging when `has_more` is `false`.
- `raw` defaults to `true`, which returns full comment objects. The sample response used `raw` set to `false`.
- To get replies to a single comment, call [WeChat MP Comment Replies](/apis/wechat-mp/v2/comment-replies).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat MP Account Articles](/apis/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [WeChat MP Article Detail](/apis/wechat-mp/v2/article-detail): Get a WeChat official account (MP) article from its URL: title, author, account, publish time, cover, full text and HTML content, and album info.
- [WeChat MP Article Stats](/apis/wechat-mp/v2/article-stats): Get the engagement metrics of a WeChat official account article from its URL: reads, likes, "wow" count, shares, favorites and comments.

---
Machine-readable: [`catalog/models/wechat-mp/v2/article-comments.json`](../../../../catalog/models/wechat-mp/v2/article-comments.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/article-comments
