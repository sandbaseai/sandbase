# WeChat MP Account Historical Articles API: pricing, parameters and code examples

`wechat-mp/account-history-articles` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.042857 per call · **Modes:** sync

Get historical posts for a WeChat Official Account by username, with cursor pagination and article, video, audio, or image content tabs. Use it to browse an account's publishing history.

## Pricing

- **$0.042857 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/account-history-articles", "username": "worldofai"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/account-history-articles', {'username': 'worldofai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/account-history-articles", {
  "username": "worldofai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/account-history-articles", sandbase.Params{
	"username": "worldofai",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/account-history-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | string |  | Base64 pagination cursor. Leave empty for the first page; pass next_offset from the previous response for the next page. Send it in the URL-encoded form body.  |
| `username` | string | yes | WeChat Official Account username with the gh_ prefix.  |
| `itemShowType` | string |  | Content tab. Defaults to ARTICLE. one of: `ARTICLE`, `VIDEO`, `AUDIO`, `IMAGE`; default `"ARTICLE"` |

## Details

This API returns a page of historical posts for a WeChat Official Account. It needs the account `username` with the `gh_` prefix, and it can switch between article, video, audio, and image tabs.

### Use cases

- Build a full archive of an account's posts by paging through its history with `next_offset`.
- Track how often an account publishes by comparing post timestamps across pages.
- Collect `contentUrl` links for every post, then fetch each full article in a separate call.
- Pull the video, audio, or image tab of an account to see what non-article content it posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/account-history-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "worldofai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | WeChat Official Account username with the gh_ prefix. |
| `itemShowType` | string | No | Content tab. Defaults to ARTICLE. |
| `offset` | string | No | Base64 pagination cursor. Leave empty for the first page; pass next_offset from the previous response for the next page. Send it in the URL-encoded form body. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "articles": [
    {
      "appMsg": {
        "baseInfo": {
          "appMsgId": 2649696034,
          "bigPic": 1,
          "createTime": 1793154388,
          "hasExpanded": false,
          "pbRequestMsgInfo": null,
          "type": 9,
          "updateTime": 1793154570
        },
        "detailInfo": [
          {
            "appEditJumpUrl": "",
            "audioDuRation": 0,
            "audioId": 0,
            "audioPlayUrl": "",
            "authorDesc": "",
            "canModifyByWxa": 0,
            "contentUrl": "http://mp.weixin.qq.com/s?__biz=MzAwNzIyMTQ2MA==&mid=2649696034&idx=1&sn=2203411…",
            "coverImgUrl": "https://mmbiz.qpic.cn/mmbiz_jpg/S2BrhvkmwcSnn5GwicDRpBibOkHNl5SNQ1Xo6esOD9rKLsy1…"
          }
        ],
        "pbRequestMsgInfo": null
      },
      "baseInfo": {
        "dateTime": 1793154388,
        "funcFlag": 0,
        "msgId": 2649696034,
        "msgType": 49,
        "pbRequestMsgInfo": null,
        "status": 0,
        "uniqueId": "0_2649696034",
        "virtualMsgType": 0
      },
      "featuredExposed": false,
      "image": null,
      "pbRequestMsgInfo": null,
      "text": null,
      "video": null,
      "voice": null
    }
  ],
  "biz_username": "gh_143f18f53985",
  "count": 10,
  "debug_id": "156b29b7",
  "debug_info": "gAAAAABq6ZEvNfOgypF0CI3yuVWk_rDBalQ8ohv9bnSmqtFfVjZe9UAiAtm1-wfsBigfM4AGhumDL3tR…",
  "is_end": 0,
  "next_offset": "WABgAGiB9pr5jsOSqWk=",
  "pages": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `articles[]` | One post in the account history. Each item holds `appMsg` for article content and `baseInfo` for message-level info. The `image`, `text`, `video`, and `voice` keys are `null` for article posts. |
| `articles[].appMsg.detailInfo[].contentUrl` | Link to the article page on mp.weixin.qq.com. The URL carries the `mid`, `idx`, and `sn` values. |
| `articles[].appMsg.detailInfo[].coverImgUrl` | Link to the cover image of the article. |
| `articles[].appMsg.baseInfo.appMsgId / articles[].baseInfo.msgId` | Numeric ID of the post. Both values match in the sample response. |
| `articles[].appMsg.baseInfo.createTime / articles[].appMsg.baseInfo.updateTime` | When the article was created and last updated. Values look like Unix timestamps in seconds. |
| `articles[].baseInfo.dateTime` | Time of the post as a Unix-style timestamp in seconds. |
| `articles[].baseInfo.uniqueId` | String ID for the post, built from two numbers joined by an underscore, such as `0_2649696034`. |
| `biz_username` | The `gh_` username of the account that the posts belong to. |
| `count` | Number of posts in this page of results. |
| `is_end` | Flag for the end of the history. `0` means more pages remain. |
| `next_offset` | Cursor for the next page. Send it as `offset` in the next request. |

### Notes

- For the first page, leave `offset` empty. For each next page, pass the `next_offset` value from the previous response as `offset`.
- Set `itemShowType` to `ARTICLE`, `VIDEO`, `AUDIO`, or `IMAGE` to pick the content tab. It defaults to `ARTICLE`.
- Keep paging until `is_end` is not `0`.
- To read the full text of a post, pass its `contentUrl` to [WeChat MP Article Detail](/apis/wechat-mp/article-detail). For account details, use [WeChat MP Account Basic Info](/apis/wechat-mp/account-basic-info).

### Pricing

$0.042857 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/account-history-articles.json`](../../../catalog/models/wechat-mp/account-history-articles.json) · Store page: https://www.sandbase.ai/model/wechat-mp/account-history-articles
