# Xiaohongshu Pugongying Note Details API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/note-id-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Xiaohongshu Pugongying details for a known note ID. Use it to review an individual note during creator or campaign research.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/note-id-detail", "noteId": "6abccf9c000000000a02609a"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/note-id-detail', {'noteId': '6abccf9c000000000a02609a'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/note-id-detail", {
  "noteId": "6abccf9c000000000a02609a"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/note-id-detail", sandbase.Params{
	"noteId": "6abccf9c000000000a02609a",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/note-id-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `noteId` | string | yes | Note's unique ID.  |

## Details

Returns details for one Xiaohongshu note listed on the Pugongying (PGY) platform. The response covers the note text, engagement counts, images or video, the linked brand, and a summary of the creator who posted it. It needs one input, `noteId`.

### Use cases

- Check likes, saves, comments and shares of a sponsored note after a campaign post goes live.
- Read the creator's follower count and listed video and image prices next to the note they published.
- Find which brand a note was reported for using `reportBrandName` and `reportBrandUserId`.
- Download the note's image URLs or video URL for content review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/note-id-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"noteId": "6abccf9c000000000a02609a"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `noteId` | string | Yes | Note's unique ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "agentName": null,
  "atUserList": null,
  "cmtNum": 7311,
  "compClickData": {
    "commentTag": null,
    "content": "较高",
    "engage": "-",
    "hover": "正常：0-2%，较高：2%-10%，极高：10%+",
    "noteBottom": "-",
    "noteComment": "-"
  },
  "content": "晚上好啊宝宝们，最近换季加上熬夜，皮肤真的状况百出。今天收工赶紧来分享我的“回春”神器2.0版，就是百雀羚灵玉面霜！\n淡淡花香超治愈，走的是中式养肤路线，由内养…",
  "contentItemList": null,
  "createTime": "2026-10-08 11:09",
  "favNum": 25405,
  "featureTags": null,
  "followCnt": 10935,
  "goodCaseCollect": false,
  "headPhoto": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo32206nlg5n2004a17jb2vl5roop6fpu0…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title / content` | Title and body text of the note. Long body text may contain hashtags such as `#百雀羚灵玉面霜[话题]#`. |
| `likeNum / favNum / cmtNum / shareNum` | Counts of likes, saves (favorites), comments and shares on the note. |
| `readNum / impNum` | Read count and impression count for the note. |
| `compClickData.content / compClickData.hover` | A rating label for the note (here `较高`) and the hover text that explains the bands: normal 0-2%, higher 2%-10%, very high 10%+. |
| `reportBrandName / reportBrandUserId` | Name and user ID of the brand reported for this note. |
| `time.createTime / time.updateTime` | Timestamps in milliseconds since the Unix epoch. `createTime` at the top level is the same moment as a formatted string. |
| `userInfo.nickName / userInfo.userId / userInfo.fansNum` | Name, user ID and follower count of the creator who posted the note. |
| `userInfo.videoPrice / userInfo.picturePrice` | Prices listed for this creator for video notes and image notes. |
| `imagesList[].url` | Image URL for each image in the note, with `width` and `height` in pixels. |
| `videoInfo.videoUrl / videoInfo.meta.duration` | Direct URL of the video file and its metadata. The URL carries a `sign` and `t` query parameter. |

### Notes

- `noteId` is a 24-character hex string, like `6abccf9c000000000a02609a`. It also appears in `noteLink`.
- `noteLink` is a full note URL that includes an `xsec_token`.
- To find note IDs for a creator, call [Xiaohongshu Pugongying Creator Note List](/apis/xiaohongshu/pgy-v2/data-v2-notes-detail).
- For the creator's own profile, use `userInfo.userId` with [Xiaohongshu Pugongying Creator Profile](/apis/xiaohongshu/pgy-v2/blogger-user-id).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/note-id-detail.json`](../../../../catalog/models/xiaohongshu/pgy-v2/note-id-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/note-id-detail
