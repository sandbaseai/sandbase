# Bilibili App Popular Feed API: pricing, parameters and code examples

`bilibili/app/popular-feed` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves popular video feed items from the Bilibili app. Supports pagination through page index and previous video identifiers.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/popular-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/popular-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/popular-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/popular-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/app/popular-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `idx` | integer |  | Page index (starting from 1) default `1` |
| `last_param` | string |  | Last video ID from previous page (for pagination)  |

## Details

Returns a page of popular video cards from the Bilibili app popular feed. Each card has a title, BV ID, cover, duration, creator text and view text. The request needs no input, and you can pass `idx` and `last_param` to page through the feed.

### Use cases

- Build a daily snapshot of the videos shown on the Bilibili popular feed.
- Collect `bvid` values from popular cards and send them to a video detail API.
- Compare which creators and topics appear on the popular feed over time.
- Show the current popular titles and covers in an external dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/popular-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `idx` | integer | No | Page index (starting from 1) |
| `last_param` | string | No | Last video ID from previous page (for pagination) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "config": {
    "bottom_text": "已经到达热门的尽头惹，<em class=\"keyword\">关于热门</em>",
    "bottom_text_cover": "https://i0.hdslb.com/bfs/archive/10814950191d33ba6eb6f29439e27399c3eeee37.png",
    "bottom_text_url": "https://www.bilibili.com/blackboard/activity-RKWxGjjMb.html",
    "head_image": "https://i0.hdslb.com/bfs/legacy/1e7a9273bba1e3c20fecd7e69274278affd52e0f.png",
    "item_title": "当前热门",
    "share_info": {
      "current_title": "全部热门",
      "current_top_photo": "https://i0.hdslb.com/bfs/legacy/1e7a9273bba1e3c20fecd7e69274278affd52e0f.png",
      "share_desc": "",
      "share_icon": "https://i0.hdslb.com/bfs/activity-plat/static/20190424/df3e2ff90b315fca2f8d24a29…",
      "share_sub_title": "全站最热的视频都在这儿，你最喜欢哪一个？",
      "share_title": "哔哩哔哩热门"
    },
    "top_items": [
      {
        "entrance_id": 4,
        "icon": "http://i0.hdslb.com/bfs/archive/a3f11218aaf4521b4967db2ae164ecd3052586b9.png",
        "module_id": "rank",
        "title": "排行榜",
        "uri": "bilibili://rank?type=all"
      }
    ]
  },
  "data": [
    {
      "args": {},
      "bvid": "BV19P4w6aEk3",
      "card_goto": "av",
      "card_type": "small_cover_v5",
      "cover": "http://i0.hdslb.com/bfs/archive/0721196fe0577d7c60837786d44e9130da985544.jpg",
      "cover_right_text_1": "20:33",
      "from_type": "recommend",
      "goto": "av",
      "idx": 2,
      "is_popular": true,
      "param": "117546359521318",
      "rcmd_reason_style": {
        "bg_style": 2,
        "border_color": "#FFFB9E60",
        "border_color_night": "#BC7A4F",
        "text": "2万分享",
        "text_color": "#FFFB9E60",
        "text_color_night": "#BC7A4F"
      }
    }
  ],
  "message": "OK",
  "ver": "1793690839"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].title` | Video title shown on the card. |
| `data[].bvid` | BV ID of the video. Use it to look up the video elsewhere. |
| `data[].param` | Numeric video ID as a string. This is the same number that appears in the `uri` value. |
| `data[].cover` | Cover image URL of the video. |
| `data[].cover_right_text_1` | Video duration shown on the cover, for example `20:33`. |
| `data[].right_desc_1` | Creator line shown on the card. It can be one name or a joint creation label such as `摸鱼事务所 等联合创作`. |
| `data[].right_desc_2` | Display text with the view count and the time since publishing, for example `32万观看 · 4小时前`. It is a text label, not a number. |
| `data[].rcmd_reason_style.text` | Short reason label shown on some cards, for example `2万分享`. Many cards do not have this field. |
| `data[].idx` | Position number of the card in the feed. |
| `data[].uri` | In-app deep link for the video. It includes the `cid` as a query value. |
| `config.top_items[].title / config.top_items[].uri` | Title and link of the entrance tiles at the top of the popular page, such as the ranking list. |

### Notes

- `idx` is the page index and starts at 1. Pass the `param` value of the last card on the previous page as `last_param` to get the next page.
- Take `bvid` from `data[]` and pass it to [Bilibili Video Details](/apis/bilibili/web/one-video) for more data on one video.
- To read the comments on a video, call [Bilibili Video Comments (App)](/apis/bilibili/app/video-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili App Bangumi Tab](/apis/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/apis/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/apis/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/popular-feed.json`](../../../../catalog/models/bilibili/app/popular-feed.json) · Store page: https://www.sandbase.ai/model/bilibili/app/popular-feed
