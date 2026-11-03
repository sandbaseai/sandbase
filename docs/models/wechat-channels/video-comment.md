# WeChat Channels Video Comments API: pricing, parameters and code examples

`wechat-channels/video-comment` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get first-level comments for a WeChat Channels video by object ID with continuation-buffer pagination. Use it to review audience discussion on known video content.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/video-comment", "objectId": "15042116979764234697"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/video-comment', {'objectId': '15042116979764234697'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/video-comment", {
  "objectId": "15042116979764234697"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/video-comment", sandbase.Params{
	"objectId": "15042116979764234697",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/video-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `objectId` | string | yes | WeChat Channels video object id used to fetch first-level comments. If you only have the exportId returned by a video search result, first call the Export Id Conversion (V1) endpoint at…  |
| `last_buffer` | string |  | Pagination buffer returned by the previous first-level WeChat Channels comment response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.  |
| `objectNonceId` | string |  | Optional WeChat Channels object nonce id.  |

## Details

Returns one page of first-level comments for a WeChat Channels video. Each comment includes the text, author, like count, reply count and IP region. The request needs the video `objectId`. `objectNonceId` and `last_buffer` are optional.

### Use cases

- Read what viewers say about a specific WeChat Channels video.
- Rank comments by `like_count` to find the most supported opinions.
- Group commenters by `ip_region_info.region_text` to see where a discussion comes from.
- Export comment text for sentiment or topic analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/video-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"objectId": "15042116979764234697", "objectNonceId": "13454967799950666727_0_0_4_32_0_45d03c48-d38a-11f1-8fe5-9b7987977b23"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `objectId` | string | Yes | WeChat Channels video object id used to fetch first-level comments. If you only have the exportId returned by a video search result, first call the Export Id Conversion (V1) endpoint at /api/weixin-channels/convert-expor |
| `last_buffer` | string | No | Pagination buffer returned by the previous first-level WeChat Channels comment response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body. |
| `objectNonceId` | string | No | Optional WeChat Channels object nonce id. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comment_info": [
    {
      "author_contact": {
        "bind_info": [],
        "ext_info": {
          "sex": 2
        },
        "head_url": "https://wx.qlogo.cn/finderhead/Q3auHgzwzM43y0x0AvRudFaN6YZ0vXX6Xkc4GEiaS0SKcjnWD…",
        "menu": [],
        "nickname": "招财姐爱生话",
        "reference_info": [],
        "username": "v2_060000231003b20faec8c4e48b1dcbd6cc02ed3db0778a03150e48f267d8f64d121737888919@…"
      },
      "comment_id": "15042242325261781458",
      "content": "能实现的",
      "content_type": 0,
      "continue_flag": 1,
      "createtime": "1793175020",
      "dislike_count": 0,
      "display_flag": 8,
      "expand_comment_count": 12,
      "ext_flag": 32,
      "head_url": "https://wx.qlogo.cn/finderhead/Q3auHgzwzM43y0x0AvRudFaN6YZ0vXX6Xkc4GEiaS0SKcjnWD…",
      "interaction_label_list": []
    }
  ],
  "down_continue_flag": 1,
  "last_buffer": "CsIBCKq55KH3qIPm0AEY0pPMtKn2seDQARiUsoCNruO34NABGJWQuOrcvLng0AEY/5X0/IautODQARjP…",
  "req_p": "2020"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comment_info[].comment_id` | ID of the comment. Use it to identify a single comment. |
| `comment_info[].content` | Text of the comment. |
| `comment_info[].createtime` | Time the comment was posted. The value is a string of digits that looks like a Unix timestamp in seconds. |
| `comment_info[].like_count / dislike_count` | Number of likes and dislikes on the comment. |
| `comment_info[].expand_comment_count` | Number of replies under the comment. Replies are not included in this response, and `level_two_comment` was empty. |
| `comment_info[].nickname / username` | Display name and internal user ID of the comment author. The `username` value ends in `@finder`. |
| `comment_info[].author_contact.head_url` | URL of the author's avatar image. |
| `comment_info[].ip_region_info.region_text` | Region label shown for the commenter, for example `广东`. |
| `comment_info[].reply_comment_id / reply_content` | Set when the comment replies to another comment. Top-level comments show `0` and an empty string. |
| `last_buffer` | Pagination token for the next page of comments. |
| `down_continue_flag` | Flag for more comments. The value was `1` in this response, which suggests more pages exist. |

### Notes

- For the first page, leave `last_buffer` empty. For the next page, send the top-level `last_buffer` value from the response in an `application/x-www-form-urlencoded` form body.
- If you only have an `exportId` from a video search result, convert it first with [WeChat Channels Export Id Conversion](/apis/wechat-channels/convert-export-id). You can find videos with [WeChat Channels Video Search](/apis/wechat-channels/search-video).
- To read the replies under a comment, call [WeChat Channels Video Sub Comments](/apis/wechat-channels/video-sub-comment).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/video-comment.json`](../../../catalog/models/wechat-channels/video-comment.json) · Store page: https://www.sandbase.ai/model/wechat-channels/video-comment
