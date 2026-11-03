# Kuaishou App Share Link API: pricing, parameters and code examples

`kuaishou/app/generate-share-link` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Generates a shareable URL for Kuaishou application content using a specified object identifier. Returns share link details for the target item.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/generate-share-link", "shareObjectId": "3xg5wjqdtekbb3u"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/generate-share-link', {'shareObjectId': '3xg5wjqdtekbb3u'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/generate-share-link", {
  "shareObjectId": "3xg5wjqdtekbb3u"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/generate-share-link", sandbase.Params{
	"shareObjectId": "3xg5wjqdtekbb3u",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/generate-share-link` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shareObjectId` | string | yes | 作品ID/Photo ID  |

## Details

This API returns a Kuaishou share link for one work. You send the work ID as `shareObjectId`, and it returns a short link, a share message with a copy-ready caption, and share metadata.

### Use cases

- Turn a Kuaishou work ID into a `https://v.kuaishou.com/...` short link to post in chats or on other platforms.
- Build a share caption for a video from the ready-made `shareMessage` text.
- Store the short link next to a work ID in a content tracking sheet.
- Check which share type and resource type Kuaishou assigns to a given work.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/generate-share-link" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shareObjectId": "3xg5wjqdtekbb3u"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shareObjectId` | string | Yes |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cache-scope": "nocache",
  "debug_id": "c1b8d08e",
  "debug_info": "gAAAAABq6Y7dAVOq-kfXfhMBrCWnwIAjc-dL-69vD4Ur_tjq-1uHCNQygWN0-jpkN1RJuR-tJhcrEiga…",
  "error_msg": null,
  "host-name": "public-bjx-c34-kce-node9.idchb1az1.hb1.kwaidc.com",
  "hostName": "public-bjx-c34-kce-node9.idchb1az1.hb1.kwaidc.com",
  "max-age": 0,
  "result": 1,
  "share": {
    "appIconUrl": "https://static.yximgs.com/udata/pkg/ks-share-sdk/cardlogonew.png",
    "appName": "as",
    "extParams": {
      "battleTemplateId": "",
      "expTag": "1_i/0_unknown0",
      "logExt": "{\"expTag\":\"1_i/0_unknown0\",\"trendingType\":\"\"}",
      "shareInfoWrap": "{\"shareTitleInfo\":{\"title\":\"分享一个作品给你\",\"subTitle\":\"推荐你看这个视频\"},\"shareId\":\"19167006…",
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
      "copylinkFailedTips": "Copy failed",
      "copylinkSuccessTips": "Copied successfully, go share it with friends",
      "kwaiToken": "X8XgJpxj…",
      "shareId": "19167006876328",
      "shareMessage": "https://v.kuaishou.com/KcrZIFsI 被好的风景收买，剩下的全是好心情”\"手机摄影 \"水下摄影 \"治愈系 This work has …",
      "shareObjectId": "3xg5wjqdtekbb3u",
      "shareResourceType": "PHOTO_OTHER",
      "shortLink": "https://v.kuaishou.com/KcrZIFsI",
      "toastDisplayTimeMillis": 1000
    },
    "subBiz": "BROWSE_SLIDE_PHOTO"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `share.shareObject.shortLink` | Short URL for the work, on the `v.kuaishou.com` domain. |
| `share.shareObject.shareMessage` | Full share text. It holds the short link, the work caption with hashtags, and a play count line. |
| `share.shareObject.shareObjectId` | The work ID you sent in the request. |
| `share.shareObject.kwaiToken` | Token string tied to this share. Kuaishou uses it for the token share method. |
| `share.shareObject.shareId` | ID of this share action. |
| `share.shareObject.shareResourceType` | Type of the shared resource, for example `PHOTO_OTHER`. |
| `share.shareChannel / share.shareMethod / share.shareMode` | How the share is made. The sample shows `COPY_LINK`, `TOKEN` and `APP`. |
| `share.shareObject.copylinkSuccessTips / share.shareObject.copylinkFailedTips` | Text the app shows after a copy succeeds or fails. |
| `share.extParams.shareInfoWrap` | JSON string with extra share details, such as the share title and subtitle text. Parse it before you read it. |
| `result` | Status code of the call. The sample returns `1`. |

### Notes

- Use the work ID from a video response as `shareObjectId`. The ID in the example looks like `3xg5wjqdtekbb3u`.
- Call [Kuaishou Video Details (V1)](/apis/kuaishou/app/one-video) to check the work before you build its share link.
- Use [Kuaishou Web Share Short URL](/apis/kuaishou/web/generate-share-short-url) if you need a share link from the web side.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.
- [Kuaishou Hot Board Detail](/apis/kuaishou/app/hot-board-detail): Returns trending topics and search keywords from Kuaishou hot boards based on the specified board identifier and board type.

---
Machine-readable: [`catalog/models/kuaishou/app/generate-share-link.json`](../../../../catalog/models/kuaishou/app/generate-share-link.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/generate-share-link
