# Xiaohongshu (RED) PGY Note Detail API: pricing, parameters and code examples

`xiaohongshu/pgy/note-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns detailed information for a specific Pugongying (PGY) note on Xiaohongshu (RED). Look up content and metadata using a note identifier.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/note-detail", "note_id": "6a20edfa0000000021020951"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/note-detail', {'note_id': '6a20edfa0000000021020951'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/note-detail", {
  "note_id": "6a20edfa0000000021020951"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/note-detail", sandbase.Params{
	"note_id": "6a20edfa0000000021020951",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/note-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `note_id` | string | yes | Note ID, e.g. "6a20edfa0000000021020951"  |

## Details

Returns details for one Xiaohongshu (RED) note listed on the Pugongying (PGY) platform. It needs a `note_id` and returns the note text, images, engagement counts and a profile block for the author.

### Use cases

- Pull the read, like, favorite, comment and share counts of a sponsored note to check how it performed.
- Read the author's `fansNum`, `picturePrice` and `videoPrice` next to a note to review a creator before a campaign.
- Download the note's image URLs and text to archive a campaign post.
- Match a note to its author's content tags and location to sort creators by niche and city.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/note-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id": "6a20edfa0000000021020951"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `note_id` | string | Yes | Note ID, e.g. "6a20edfa0000000021020951" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "agentName": null,
    "atUserList": null,
    "cmtNum": 16,
    "compClickData": null,
    "content": "憨豆先生表情：盯梢三分钟然后默默点头……\n和我站在湖滨in77这家冰淇淋店前一模一样\n\t\n店员说：每天现做，卖不完当晚报废\n我：嗯？\n店员又说：绝不隔夜\n我：🙂…",
    "contentItemList": null,
    "createTime": "2026-06-04 11:16",
    "favNum": 20,
    "featureTags": null,
    "followCnt": 0,
    "goodCaseCollect": false,
    "headPhoto": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31hpod1vijs705n36hcv4k5g5f8fn40g…"
  },
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title / data.content` | Title and body text of the note. The body can contain line breaks and emoji. |
| `data.readNum / data.impNum` | Read count and impression count of the note. |
| `data.likeNum / data.favNum / data.cmtNum / data.shareNum` | Like, favorite, comment and share counts of the note. |
| `data.createTime / data.time.createTime` | Publish time. `createTime` is a text date such as `2026-06-04 11:16`. The `time` object holds the same moment and the update times as millisecond timestamps. |
| `data.imagesList[].url / data.imagesList[].original` | Image link at 1080 px width and the original image link. `width` and `height` sit beside them. |
| `data.imagesList[].imageExtraInfo.livePhotoVideoFileId` | File ID of the video clip when an image is a live photo. It is `null` for normal images. |
| `data.noteLink` | Link to the note on xiaohongshu.com, with the `xsec_token` and `xsec_source` query values included. |
| `data.userInfo.nickName / data.userInfo.userId` | Display name and user ID of the note's author. |
| `data.userInfo.fansNum / data.userInfo.location` | Follower count and the listed location of the author. |
| `data.userInfo.picturePrice / data.userInfo.videoPrice` | Listed prices for an image note and a video note from this author. |
| `data.userInfo.contentTags[].taxonomy1Tag / data.userInfo.contentTags[].taxonomy2Tags` | Top-level content category and its sub-categories for the author, such as food and city travel. |

### Notes

- `note_id` is a 24-character hex string. It also appears in `data.noteId` and in the `data.noteLink` path.
- `data.userInfo.userId` is the author's ID. Pass it to [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail) for the full creator profile.
- For featured comments on the same note, call [Xiaohongshu PGY note featured comments](/apis/xiaohongshu/pgy/note-comments).
- `data.videoInfo` is `null` for this image note, and several other fields can also be `null`.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/apis/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/apis/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/note-detail.json`](../../../../catalog/models/xiaohongshu/pgy/note-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/note-detail
