# Bilibili User Collection Folder Videos API: pricing, parameters and code examples

`bilibili/web/user-collection-videos` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns video data stored within a specified collection folder on Bilibili. Supports pagination to browse through items in the folder.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-collection-videos", "folder_id": "1756059545"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-collection-videos', {'folder_id': '1756059545'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-collection-videos", {
  "folder_id": "1756059545"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-collection-videos", sandbase.Params{
	"folder_id": "1756059545",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-collection-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pn` | integer |  | Page number  |
| `folder_id` | string | yes | collection folder id  |

## Details

Returns the videos saved in one Bilibili collection folder, plus summary details about the folder and its owner. It needs a `folder_id`, and you can pass `pn` to request other pages.

### Use cases

- List every video a user has saved in a themed collection folder, such as the art folder in the example.
- Rank the videos in a folder by `cnt_info.play` or `cnt_info.collect` to find the most watched items.
- Check when each video was added to a folder by reading `fav_time`.
- Page through a large folder with `pn` and `has_more` to copy its full contents.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-collection-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"folder_id": "1756059545"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `folder_id` | string | Yes | collection folder id |
| `pn` | integer | No | Page number |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "has_more": true,
    "info": {
      "attr": 22,
      "cnt_info": {
        "collect": 1,
        "play": 0,
        "share": 0,
        "thumb_up": 0
      },
      "cover": "http://i1.hdslb.com/bfs/archive/970cd038dd3fdffd6824748be0425e8f71ba5c2f.jpg",
      "cover_type": 2,
      "ctime": 1662826672,
      "fav_state": 0,
      "fid": 17560595,
      "id": 1756059545,
      "intro": "",
      "is_kid_playlist": false,
      "is_top": false,
      "kid_playlist_desc": ""
    },
    "medias": [
      {
        "attr": 0,
        "bv_id": "BV1MF411A7HS",
        "bvid": "BV1MF411A7HS",
        "cnt_info": {
          "collect": 2733,
          "danmaku": 287,
          "play": 347087,
          "play_switch": 0,
          "reply": 0,
          "view_text_1": "34.7万",
          "vt": 0
        },
        "cover": "http://i1.hdslb.com/bfs/archive/970cd038dd3fdffd6824748be0425e8f71ba5c2f.jpg",
        "ctime": 1659170909,
        "duration": 122,
        "fav_time": 1785408355,
        "id": 301480273,
        "intro": "尔等年纪轻轻，便前来送死吗？——舒克B站唯一账号",
        "link": "bilibili://video/301480273",
        "media_list_link": "bilibili://music/playlist/playpage/1934419845?page_type=3&oid=301480273&otype=2"
      }
    ],
    "ttl": 1793690874
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.has_more` | Shows whether more pages follow the current one. `true` means you can request the next `pn`. |
| `data.info.title / data.info.intro` | The folder name and its description. `intro` can be an empty string. |
| `data.info.media_count` | The number of items in the folder. |
| `data.info.upper.mid / data.info.upper.name` | The ID and display name of the user who owns the folder. |
| `data.info.ctime / data.info.mtime` | Timestamps for when the folder was created and last changed. They are Unix times in seconds. |
| `data.medias[].bvid` | The BV ID of the saved video. `bv_id` holds the same value. |
| `data.medias[].title / data.medias[].intro` | The title and description text of the video. |
| `data.medias[].cnt_info.play / collect / danmaku` | Counts of plays, collects and danmaku comments for the video. `view_text_1` is the play count as display text. |
| `data.medias[].duration` | The length of the video. The value is a plain number, so check it against a known video before assuming the unit. |
| `data.medias[].pubtime / data.medias[].fav_time` | Unix timestamps for when the video was published and when it was added to the folder. |
| `data.medias[].upper.mid / data.medias[].upper.name` | The ID and name of the creator who uploaded the video. |

### Notes

- Find a `folder_id` with [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders), which lists the folders a user owns.
- Send `pn` to move between pages. Keep going while `data.has_more` is `true`.
- Pass a video's `bvid` to [Bilibili Video Details](/apis/bilibili/web/one-video) to get full details for one item.
- Timestamps such as `ctime`, `pubtime` and `fav_time` are Unix times in seconds.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/user-collection-videos.json`](../../../../catalog/models/bilibili/web/user-collection-videos.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-collection-videos
