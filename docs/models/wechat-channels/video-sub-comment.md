# WeChat Channels Video Sub Comments API: pricing, parameters and code examples

`wechat-channels/video-sub-comment` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get replies under a first-level WeChat Channels video comment using the video and root-comment IDs. Use it to continue a threaded comment discussion with buffer pagination.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/video-sub-comment", "objectId": "15042116979764234697", "rootCommentId": "15042242325261781458"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/video-sub-comment', {'objectId': '15042116979764234697', 'rootCommentId': '15042242325261781458'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/video-sub-comment", {
  "objectId": "15042116979764234697",
  "rootCommentId": "15042242325261781458"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/video-sub-comment", sandbase.Params{
	"objectId": "15042116979764234697",
	"rootCommentId": "15042242325261781458",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/video-sub-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `objectId` | string | yes | WeChat Channels video object id used to fetch second-level comment replies.  |
| `last_buffer` | string |  | Pagination buffer for WeChat Channels second-level comment replies. Use the first-level comment's last_buffer for the first reply page when present. For this POST endpoint, send it in an…  |
| `rootCommentId` | string | yes | Root first-level comment id returned by the WeChat Channels video comments endpoint.  |

## Details

Returns the second-level replies under one first-level comment on a WeChat Channels video. It needs the video `objectId` and the `rootCommentId` of the parent comment. Each reply includes its text, author, like count, and a `last_buffer` for the next page.

### Use cases

- Read the full reply thread under a popular comment to see how viewers respond to it.
- Collect reply text and like counts to measure sentiment on a single comment.
- Group repliers by `ip_region_info.region_text` to see where a discussion comes from.
- Page through a long thread and store every reply with its `comment_id` and `createtime`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/video-sub-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"objectId": "15042116979764234697", "rootCommentId": "15042242325261781458"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `objectId` | string | Yes | WeChat Channels video object id used to fetch second-level comment replies. |
| `rootCommentId` | string | Yes | Root first-level comment id returned by the WeChat Channels video comments endpoint. |
| `last_buffer` | string | No | Pagination buffer for WeChat Channels second-level comment replies. Use the first-level comment's last_buffer for the first reply page when present. For this POST endpoint, send it in an application/x-www-form-urlencoded |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comment_info": [
    {
      "author_contact": {
        "bind_info": [],
        "head_url": "https://wx.qlogo.cn/mmhead/ver_1/1NUh9hyHm9axx8pDKTAKwPMbz8lHSqNpOXtgU5sfLXN8qIp…",
        "menu": [],
        "nickname": "刘明顺",
        "reference_info": [],
        "username": "v5_020b0a16610401000000000099da18de46a5c9000000b1afa7d8728e3dd43ef4317a780e33c2a…"
      },
      "comment_id": "15045764170299677659",
      "content": "666",
      "content_type": 0,
      "createtime": "1793594857",
      "dislike_count": 0,
      "display_flag": 0,
      "expand_comment_count": 0,
      "ext_flag": 32,
      "head_url": "https://wx.qlogo.cn/mmhead/ver_1/1NUh9hyHm9axx8pDKTAKwPMbz8lHSqNpOXtgU5sfLXN8qIp…",
      "interaction_label_list": [],
      "ip_region_info": {
        "region_text": "贵州"
      }
    }
  ],
  "down_continue_flag": 1,
  "last_buffer": "CJGSoKCZp9Lm0AE4yP6/mvTwvAY=",
  "req_p": "192.168.1.129:2020"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comment_info[].comment_id` | ID of the reply comment. |
| `comment_info[].content` | Text of the reply. |
| `comment_info[].nickname / comment_info[].head_url` | Display name and avatar URL of the person who wrote the reply. |
| `comment_info[].createtime` | Time the reply was posted, as a string. The values look like Unix timestamps in seconds. |
| `comment_info[].like_count / comment_info[].dislike_count` | Number of likes and dislikes on the reply. |
| `comment_info[].ip_region_info.region_text` | Region label shown with the reply, for example a Chinese province name. |
| `comment_info[].reply_comment_id / comment_info[].reply_content` | ID and text of the comment this reply belongs to. `reply_comment_id` matches the `rootCommentId` you sent. |
| `comment_info[].expand_comment_count` | Count of further replies that can be expanded under this reply. |
| `down_continue_flag` | Value `1` in this response, which goes with a `last_buffer` for another page. Treat it as a continue flag. |
| `last_buffer` | Pagination buffer. Send it as `last_buffer` in the next request to get the next page of replies. |

### Notes

- Get `rootCommentId` from the first-level comment list in [WeChat Channels Video Comments](/apis/wechat-channels/v2/video-comments) or [WeChat Channels Video Comments](/apis/wechat-channels/video-comment).
- For the first reply page, you can pass the first-level comment's `last_buffer` when it is present. For later pages, pass the `last_buffer` from the previous response.
- Send `last_buffer` in an `application/x-www-form-urlencoded` form body on this POST endpoint.
- `comment_id` values are long numeric strings. Keep them as strings.

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/video-sub-comment.json`](../../../catalog/models/wechat-channels/video-sub-comment.json) · Store page: https://www.sandbase.ai/model/wechat-channels/video-sub-comment
