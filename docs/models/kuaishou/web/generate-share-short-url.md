# Kuaishou Web Share Short URL API: pricing, parameters and code examples

`kuaishou/web/generate-share-short-url` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a shareable short URL for a specified Kuaishou video or photo post. Supply the target post identifier using the photo_id query parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/generate-share-short-url", "photo_id": "5193494945927590140"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/generate-share-short-url', {'photo_id': '5193494945927590140'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/generate-share-short-url", {
  "photo_id": "5193494945927590140"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/generate-share-short-url", sandbase.Params{
	"photo_id": "5193494945927590140",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/generate-share-short-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `photo_id` | string | yes | 作品ID/Photo ID  |

## Details

This API returns a Kuaishou short link for one video or photo post, along with the ready-made share message text. It needs the post's `photo_id` as input.

### Use cases

- Turn a known `photo_id` into a short `https://v.kuaishou.com/` link for use in chat messages or posts.
- Collect the ready-to-paste share text for a video, including its title text and play count.
- Store a short link next to each post in a content tracking sheet.
- Check that a `photo_id` resolves to a shareable post before you build a link list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/generate-share-short-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_id": "5193494945927590140"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_id` | string | Yes |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cache-scope": "nocache",
  "error_msg": null,
  "host-name": "public-bjmt-c34-kce-node1110.idchb1az4.hb1.kwaidc.com",
  "hostName": "public-bjmt-c34-kce-node1110.idchb1az4.hb1.kwaidc.com",
  "max-age": 0,
  "result": 1,
  "share": {
    "appIconUrl": "https://static.yximgs.com/udata/pkg/ks-share-sdk/cardlogonew.png",
    "appName": "as",
    "extParams": {
      "battleTemplateId": "",
      "expTag": "1_i/0_unknown0",
      "logExt": "{\"expTag\":\"1_i/0_unknown0\",\"trendingType\":\"\"}",
      "shareInfoWrap": "{\"shareTitleInfo\":{\"title\":\"分享一个作品给你\",\"subTitle\":\"推荐你看这个视频\"},\"shareId\":\"19166994…",
      "shareMethod": "token",
      "shareMode": "app",
      "styleKey": "",
      "templateGenerationType": "",
      "templateStyle": "",
      "tokenExtParams": "{}",
      "useMmuTitle": false
    },
    "kpn": "KUAISHOU",
    "shareChannel": "COPY_LINK",
    "shareMethod": "TOKEN",
    "shareMethodType": null,
    "shareMode": "APP",
    "shareObject": {
      "copyPopupWindowType": "DEFAULT",
      "copylinkFailedTips": "复制失败",
      "copylinkSuccessTips": "链接复制成功，快去分享给朋友吧",
      "kwaiToken": "X-2bp1gS…",
      "shareId": "19166994375513",
      "shareMessage": "https://v.kuaishou.com/KuPc5nPF 哥哥我会魔法一人就能变成两 \"李秀妍u \"为自己代言 该作品在快手被播放过157.6万次，点击链…",
      "shareObjectId": "5193494945927590140",
      "shareResourceType": "PHOTO_OTHER",
      "shortLink": "https://v.kuaishou.com/KuPc5nPF",
      "toastDisplayTimeMillis": 1000
    },
    "subBiz": "BROWSE_SLIDE_PHOTO"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `share.shareObject.shortLink` | The short URL for the post. It starts with `https://v.kuaishou.com/`. |
| `share.shareObject.shareMessage` | The full share text. It holds the short link, the post caption, the author name and a play count line, in Chinese. |
| `share.shareObject.shareObjectId` | The ID of the shared post. It matches the `photo_id` you sent. |
| `share.shareObject.kwaiToken` | A token string for the share. Kuaishou uses it for the copy-link share method. |
| `share.shareObject.shareId` | The ID of this share action. |
| `share.shareObject.shareResourceType / share.subBiz` | The type of the shared resource and the context it was shared from, for example `PHOTO_OTHER` and `BROWSE_SLIDE_PHOTO`. |
| `share.shareChannel / share.shareMethod / share.shareMode` | How the share is made. The sample shows `COPY_LINK`, `TOKEN` and `APP`. |
| `share.extParams.shareInfoWrap` | A JSON string with extra share details, such as the share title text and `shareType`. |
| `result` | A status code for the call. The sample returns `1`. |
| `error_msg` | An error message. It is `null` in the sample response. |

### Notes

- Send `photo_id` as a string. It is a long numeric ID, for example `5193494945927590140`.
- Read the link from `share.shareObject.shortLink`. `share.shareObject.shareMessage` already includes the same link.
- `share.extParams.shareInfoWrap` and `share.extParams.logExt` are JSON strings. Parse them again if you need their contents.
- To get post details for the same ID, call [Kuaishou Single Video Details](/apis/kuaishou/web/one-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.
- [Kuaishou Web Hot List (V2)](/apis/kuaishou/web/hot-list-v2): Returns current trending search rankings and hot topics on Kuaishou web.

---
Machine-readable: [`catalog/models/kuaishou/web/generate-share-short-url.json`](../../../../catalog/models/kuaishou/web/generate-share-short-url.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/generate-share-short-url
