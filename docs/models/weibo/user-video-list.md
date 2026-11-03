# Weibo User Video List API: pricing, parameters and code examples

`weibo/user-video-list` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get a Weibo user's video waterfall feed by UID, with an optional cursor from a prior response. Use it to browse videos published by a known account or continue through its video feed.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/user-video-list", "uid": "2803301701"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/user-video-list', {'uid': '2803301701'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/user-video-list", {
  "uid": "2803301701"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/user-video-list", sandbase.Params{
	"uid": "2803301701",
})
```

Same call via the path form: `POST /v1/api/weibo/user-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Weibo User ID (UID).  |
| `cursor` | string |  | Pagination cursor returned by the previous response.  |

## Details

Returns a page of videos posted by a Weibo account, taken from its video feed. It needs the account's `uid`, and it accepts an optional `cursor` to fetch the next page.

### Use cases

- Build a list of the latest videos from a news or brand account on Weibo.
- Compare likes, comments and reposts across an account's recent videos.
- Collect video cover images and durations to build a media gallery for one account.
- Page back through an account's video history with `next_cursor`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/user-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "2803301701"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Weibo User ID (UID). |
| `cursor` | string | No | Pagination cursor returned by the previous response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "list": [
      {
        "analysis_extra": "",
        "annotations": [
          []
        ],
        "attitudes_count": 206,
        "attitudes_status": 0,
        "can_edit": false,
        "cardid": "star_1624",
        "comment_manage_info": {
          "approval_comment_type": 0,
          "comment_anon_type": 0,
          "comment_permission_type": -1,
          "comment_sort_type": 0
        },
        "comments_count": 81,
        "content_auth": 0,
        "created_at": "Tue Nov 03 14:21:45 +0800 2026",
        "favorited": false,
        "id": 5361173809858197
      }
    ],
    "next_cursor": "5360540163509216"
  },
  "ok": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.list[]` | One video post from the account's feed. |
| `data.list[].mblogid / data.list[].idstr` | Post identifiers. `mblogid` is a short code such as `RpFpqFmzb`. `idstr` is the numeric post ID as a string. |
| `data.list[].created_at` | Publish time of the post as text, for example `Tue Nov 03 14:21:45 +0800 2026`. |
| `data.list[].attitudes_count / data.list[].comments_count / data.list[].reposts_count` | Counts of likes, comments and reposts on the post. |
| `data.list[].page_info.content2` | Caption text of the video post, including hashtags. |
| `data.list[].page_info.media_info.duration` | Video length. The values seen are whole numbers such as `48`. |
| `data.list[].page_info.media_info.author_name` | Display name of the account that posted the video. |
| `data.list[].page_info.media_info.big_pic_info.pic_big.url` | Cover image URL of the video in the largest size. `pic_middle` and `pic_small` hold smaller versions, each with `width` and `height`. |
| `data.list[].page_info.media_info.ext_info.video_orientation` | Orientation of the video, for example `vertical`. |
| `data.next_cursor` | Cursor string for the next page of videos. |

### Notes

- Send `next_cursor` from `data.next_cursor` as `cursor`, with the same `uid`, to get the next page.
- `uid` is the numeric Weibo user ID. The example uses `2803301701`. `page_info.author_id` in each item shows the owner's UID.
- For full details of a single video, call [Weibo Video Detail](/apis/weibo/app/video-detail). For the account's profile, call [Weibo User Profile Information](/apis/weibo/app/user-info).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/weibo/user-video-list.json`](../../../catalog/models/weibo/user-video-list.json) · Store page: https://www.sandbase.ai/model/weibo/user-video-list
