# Bilibili Web Video Details API: pricing, parameters and code examples

`bilibili/web/video-detail` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata, season sections, and episode listings for a specific Bilibili video using its unique video identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/video-detail", "aid": "114902186396822"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/video-detail', {'aid': '114902186396822'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/video-detail", {
  "aid": "114902186396822"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/video-detail", sandbase.Params{
	"aid": "114902186396822",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aid` | string | yes | Video id  |

## Details

Returns metadata for one Bilibili video: title-level details, uploader card, tags, stats, and a list of related videos. It needs the numeric video id as `aid`.

### Use cases

- Pull the view counts, `like`, `coin` and `favorite` numbers for a single Bilibili video.
- Read the uploader's follower count and total likes next to a video to judge a creator.
- Collect the tags and related videos of a video to map a topic cluster.
- Get the part list and durations of a multi-part upload before fetching play data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aid": "114902186396822"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aid` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "Card": {
      "archive_count": 222,
      "article_count": 0,
      "card": {
        "DisplayRank": "0",
        "Official": {
          "desc": "",
          "role": 1,
          "title": "bilibili 知名军事UP主",
          "type": 0
        },
        "approve": false,
        "article": 0,
        "attention": 273,
        "attentions": [],
        "birthday": "",
        "description": ""
      },
      "follower": 251245,
      "following": false,
      "like_num": 1345184,
      "space": {
        "l_img": "https://i0.hdslb.com/bfs/space/cb1c3ef50e22b6096fde67febe863494caefebad.png",
        "s_img": "https://i1.hdslb.com/bfs/activity-plat/static/LRjqHhi0wL.png"
      }
    },
    "Related": [
      {
        "ai_rcmd": {
          "goto": "av",
          "id": 113548684496734,
          "trackid": "web_related_0.router-related-2479604-s7xkd.1793690888895.501",
          "uniq_id": ""
        },
        "aid": 113548684496734,
        "attribute_v3": 4,
        "bvid": "BV1K4zGYHEzk",
        "cid": 27040352696,
        "copyright": 1,
        "cover43": "",
        "ctime": 1732615519,
        "current_state": 0,
        "desc": "-",
        "dimension": {
          "height": 1920,
          "rotate": 0,
          "width": 1080
        },
        "duration": 12
      }
    ],
    "Reply": {
      "page": null,
      "replies": [
        {
          "action": 0,
          "assist": 0,
          "attr": 0,
          "content": null,
          "count": 0,
          "ctime": 0,
          "dialog": 0,
          "fansgrade": 0
        }
      ]
    },
    "Spec": null,
    "Tags": [
      {
        "jump_url": "",
        "music_id": "",
        "tag_id": 59110,
        "tag_name": "枪械",
        "tag_type": "old_channel"
      }
    ],
    "View": {
      "aid": 114902186396822,
      "argue_info": {
        "argue_link": "",
        "argue_msg": "",
        "argue_type": 0
      },
      "bvid": "BV12f8wz1Eit",
      "cid": 31230396201,
      "copyright": 2,
      "ctime": 1753269413,
      "desc": "https://youtu.be/UbNuAmhqer0?si=ntYRKNqVeOoRc_od",
      "desc_v2": [
        {
          "biz_id": 0,
          "raw_text": "https://youtu.be/UbNuAmhqer0?si=ntYRKNqVeOoRc_od",
          "type": 1
        }
      ],
      "dimension": {
        "height": 2160,
        "rotate": 0,
        "width": 3840
      },
      "disable_show_up_info": false,
      "duration": 2447,
      "dynamic": ""
    },
    "elec": null,
    "emergency": {
      "no_coin": false,
      "no_fav": false,
      "no_like": false,
      "no_share": false
    },
    "guide": null,
    "hot_share": {
      "list": [],
      "show": false
    },
    "is_hit_labour_day_activity": false,
    "module_ctrl": null
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.View.bvid / data.View.aid / data.View.cid` | The video's BV id, numeric `aid`, and the `cid` of its first part. |
| `data.View.owner.name / data.View.owner.mid` | Name and numeric user id of the uploader. |
| `data.View.pubdate / data.View.ctime` | Publish time and creation time of the video, as Unix timestamps in seconds. |
| `data.View.duration` | Video length. For this example the value is `2447`. |
| `data.View.stat.like / data.View.stat.coin / data.View.stat.favorite / data.View.stat.danmaku` | Counts of likes, coins, favorites and danmaku comments for the video. |
| `data.View.pages[].part` | Title of each part of the video. Each row also has `cid`, `page` and `duration`. |
| `data.View.season_id` | Id of the season the video belongs to. |
| `data.Card.follower / data.Card.like_num / data.Card.archive_count` | Uploader's follower count, total likes received, and number of uploaded videos. |
| `data.Tags[].tag_name` | Tags attached to the video. |
| `data.Related[].bvid / data.Related[].title / data.Related[].stat.like` | BV id, title and like count of each related video. Each row also has `owner`, `duration` and `pubdate`. |

### Notes

- The `aid` is the numeric video id. If you only have a BV id such as `BV12f8wz1Eit`, convert it first with [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid).
- The request has no pagination parameters. The response holds one video and a short `data.Related` list.
- To read comments on the video, call [Bilibili Video Comments (Web)](/apis/bilibili/web/video-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-detail.json`](../../../../catalog/models/bilibili/web/video-detail.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-detail
