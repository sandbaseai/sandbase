# WeChat MP Article Comments API: pricing, parameters and code examples

`wechat-mp/article-comment` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get top-level comments for a WeChat Official Account article by URL, with an optional buffer cursor for pagination. Use it to review reader discussion or continue through comment pages for a known article.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/article-comment", "articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/article-comment', {'articleUrl': 'http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/article-comment", {
  "articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/article-comment", sandbase.Params{
	"articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/article-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `buffer` | string |  | Comment pagination buffer returned by the previous response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.  |
| `articleUrl` | string | yes | WeChat Official Account article URL used to fetch top-level article comments.  |

## Details

Returns top-level reader comments for a WeChat Official Account article. It needs the article URL (`articleUrl`) and accepts an optional `buffer` cursor to fetch the next page.

### Use cases

- Read what readers say about a known Official Account article.
- Collect comment text and like counts to compare which comments got the most reactions.
- Group commenters by `province_name` to see where an article's audience is located.
- Page through a long comment section by passing back the returned `buffer`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/article-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `articleUrl` | string | Yes | WeChat Official Account article URL used to fetch top-level article comments. |
| `buffer` | string | No | Comment pagination buffer returned by the previous response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "buffer": "GAUgADAA",
  "continue_flag": false,
  "data": [
    {
      "content": "和互联网+ 一个道理吧。AI+ 为万物 添智赋能",
      "content_id": "4715966089207481774",
      "country_id": "156",
      "country_name": "中国",
      "create_time": "2026-10-29 13:37:12",
      "create_time_stamp": 1793252232,
      "id": 46,
      "is_top": 0,
      "like_num": 21,
      "logo_url": "https://wx.qlogo.cn/mmopen/PiajxSqBRaEJnoBQlkHSTXYoYYQqgVzUPcS4b8jCSMaGtZa8cmukU…",
      "multi_info": {
        "emojis": [],
        "pictures": [],
        "voices": []
      },
      "new_reply_list": []
    }
  ],
  "total": 5
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].content` | Text of the comment. |
| `data[].nick_name` | Display name of the commenter. |
| `data[].like_num` | Number of likes on the comment. |
| `data[].create_time / data[].create_time_stamp` | Comment time as a formatted string and as a Unix timestamp in seconds. |
| `data[].province_name / data[].country_name` | Location label shown for the commenter, such as a province and country. |
| `data[].reply_total_cnt` | Total number of replies to the comment. The sample comments show `0`. |
| `data[].is_top` | Top flag for the comment. All sample comments show `0`. |
| `data[].content_id` | ID string for the comment. |
| `buffer` | Cursor string to send as `buffer` in the next request. |
| `continue_flag / total` | `continue_flag` shows whether more pages follow. `total` is the count reported with the response. |

### Notes

- Leave `buffer` empty on the first call. For later pages, send the `buffer` from the previous response in an `application/x-www-form-urlencoded` form body.
- In the sample response, `continue_flag` is `false`, which means no further page was reported.
- Use the full article URL, including the `__biz`, `mid`, `idx` and `sn` query values.
- For replies under a comment, see [WeChat MP Comment Replies](/apis/wechat-mp/v2/comment-replies).

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/article-comment.json`](../../../catalog/models/wechat-mp/article-comment.json) · Store page: https://www.sandbase.ai/model/wechat-mp/article-comment
