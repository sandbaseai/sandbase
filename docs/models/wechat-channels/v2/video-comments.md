# WeChat Channels Video Comments API: pricing, parameters and code examples

`wechat-channels/v2/video-comments` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns first-level comments or nested replies for a WeChat Channels video, including like counts and IP regions, using the video object ID.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/video-comments", "object_id": "14941130915890399732"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/video-comments', {'object_id': '14941130915890399732'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/video-comments", {
  "object_id": "14941130915890399732"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/video-comments", sandbase.Params{
	"object_id": "14941130915890399732",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure.  |
| `object_id` | string | yes | Video objectId (numeric), e.g. `14941130915890399732`. From the video `id` of `fetch_user_videos` / `fetch_video_detail`.  |
| `comment_id` |  |  | Optional. To expand the replies of a comment, pass its `comment_id` (numeric); leave empty for the first-level page.  |
| `last_buffer` |  |  | Optional pagination cursor (base64). **Leave empty for the first page**; when `down_continue` is truthy, pass the previous page's `last_buffer`.  |

## Details

Returns a page of first-level comments for a WeChat Channels video, or the nested replies under one comment. It needs the numeric video `object_id`. Each comment includes the text, author nickname, like count and IP region.

### Use cases

- Show the most liked viewer comments for a specific Channels video.
- Count comments by `ipRegionInfo.regionText` to see which regions a video's audience comes from.
- Expand the replies under one comment by passing its `comment_id`.
- Track a video's comment, like, favorite and forward totals over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"object_id": "14941130915890399732"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `object_id` | string | Yes | Video objectId (numeric), e.g. `14941130915890399732`. From the video `id` of `fetch_user_videos` / `fetch_video_detail`. |
| `comment_id` | string | No | Optional. To expand the replies of a comment, pass its `comment_id` (numeric); leave empty for the first-level page. |
| `last_buffer` | string | No | Optional pagination cursor (base64). **Leave empty for the first page**; when `down_continue` is truthy, pass the previous page's `last_buffer`. |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified parsed structure. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "baseResponse": {
    "errMsg": {
      "pbRequestMsgInfo": null,
      "string": ""
    },
    "pbRequestMsgInfo": null,
    "ret": 0
  },
  "commentInfo": [
    {
      "advertisementInfo": null,
      "authorContact": {
        "additionalFlag": 0,
        "archievementInfo": null,
        "authInfo": null,
        "bindInfo": [],
        "clubInfo": null,
        "coverEntranceFlag": 0,
        "coverImgUrl": "",
        "coverUrl": ""
      },
      "authorReactionInfo": null,
      "blacklistFlag": 0,
      "chatroomMemberNickname": "",
      "clientId": "",
      "commentId": 14941155874161101301,
      "commentType": 0,
      "content": "一粥一饭暖人心，一草一木皆风景，无论所得还是所不得，都不如内心的安然自得。山不解释自己的高度，海不炫耀自己的深度。你也不必证明给谁看，时间会让一切水落石出。",
      "contentInfo": null,
      "contentType": 0,
      "continueFlag": 0
    }
  ],
  "countInfo": {
    "bulletcommentCount": 0,
    "commentCount": 97,
    "favCount": 13502,
    "forwardCount": 100002,
    "likeCount": 9158,
    "pbRequestMsgInfo": null,
    "readCount": 0,
    "versionData": {
      "dataVersion": 1793676409,
      "overwrite": false,
      "pbRequestMsgInfo": null
    }
  },
  "debug_id": "e6696f48",
  "debug_info": "gAAAAABq6ZEqX5QkY9hHkUSohd-feyYNc1yc4wJNKVCSrgXzNZvl88qqSZveAo1nAtIE7jC8VCWJC1cs…",
  "descComment": {
    "advertisementInfo": null,
    "authorContact": {
      "additionalFlag": 0,
      "archievementInfo": null,
      "authInfo": null,
      "bindInfo": [],
      "clubInfo": null,
      "coverEntranceFlag": 0,
      "coverImgUrl": "",
      "coverUrl": "",
      "extFlag": 0,
      "extInfo": {
        "birthDay": 0,
        "birthMonth": 0,
        "birthYear": 0,
        "city": "",
        "country": "",
        "pbRequestMsgInfo": null,
        "province": "",
        "sex": 1
      },
      "fansCount": 0,
      "feedCount": 0
    },
    "authorReactionInfo": null,
    "blacklistFlag": 0,
    "chatroomMemberNickname": "",
    "clientId": "",
    "commentId": 14941155874161101301,
    "commentType": 0,
    "content": "一粥一饭暖人心，一草一木皆风景，无论所得还是所不得，都不如内心的安然自得。山不解释自己的高度，海不炫耀自己的深度。你也不必证明给谁看，时间会让一切水落石出。",
    "contentInfo": null,
    "contentType": 0,
    "continueFlag": 0
  },
  "descComments": [],
  "downContinueFlag": 1,
  "emojiDescComments": [],
  "halfSheetInfo": null,
  "lastBuffer": "CqsCCP///////////wEY9ZP06LHD6azPARj8k5DOyqeNz88BGLq08NmDmO2szwEY5JS4l7rd6qzPARi1…",
  "last_buffer": "CqsCCP///////////wEY9ZP06LHD6azPARj8k5DOyqeNz88BGLq08NmDmO2szwEY5JS4l7rd6qzPARi1…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `commentInfo[].commentId` | ID of the comment. Pass it as `comment_id` to load the replies under that comment. |
| `commentInfo[].content` | Text of the comment. |
| `commentInfo[].nickname / commentInfo[].headUrl` | Display name and avatar URL of the commenter. |
| `commentInfo[].likeCount` | Number of likes on the comment. |
| `commentInfo[].createtime` | Time the comment was posted, as a Unix timestamp in seconds. |
| `commentInfo[].ipRegionInfo.regionText` | Region shown for the commenter's IP, for example `Henan`. |
| `commentInfo[].expandCommentCount / commentInfo[].levelTwoComment[]` | Reply data for the comment. `levelTwoComment` holds nested replies when they are returned. |
| `countInfo.commentCount / countInfo.likeCount / countInfo.favCount / countInfo.forwardCount` | Totals for the whole video: comments, likes, favorites and forwards. |
| `downContinueFlag` | Shows whether more comments can be loaded. A value of `1` means another page exists. |
| `lastBuffer` | Cursor for the next page. Pass it as `last_buffer` in the next request. |

### Notes

- Get `object_id` from the video `id` returned by [WeChat Channels User Videos](/apis/wechat-channels/v2/user-videos) or [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail).
- Leave `last_buffer` empty for the first page. When `downContinueFlag` is `1`, send the previous response's `lastBuffer` value as `last_buffer`.
- To read replies, send the `commentId` of a first-level comment as `comment_id` together with the same `object_id`.
- The response includes both `lastBuffer` and `last_buffer` with the same cursor value. `descComment` repeats the first comment with extra author profile fields.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Collection Videos](/apis/wechat-channels/v2/collection-videos): Returns videos contained within a WeChat Channels collection using a collection ID.

---
Machine-readable: [`catalog/models/wechat-channels/v2/video-comments.json`](../../../../catalog/models/wechat-channels/v2/video-comments.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/video-comments
