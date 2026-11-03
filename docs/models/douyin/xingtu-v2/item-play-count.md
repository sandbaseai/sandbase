# Douyin Video Play Count API: pricing, parameters and code examples

`douyin/xingtu-v2/item-play-count` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Get the play count (watch_cnt) of a Douyin video from XingTu, plus video details such as author, cover, duration and publish time.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/item-play-count", "item_id": "7630036460159111515", "need_cover_url": true, "platform_source": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/item-play-count', {'item_id': '7630036460159111515', 'need_cover_url': True, 'platform_source': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/item-play-count", {
  "item_id": "7630036460159111515",
  "need_cover_url": true,
  "platform_source": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/item-play-count", sandbase.Params{
	"item_id": "7630036460159111515",
	"need_cover_url": true,
	"platform_source": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/item-play-count` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video (item) ID  |
| `need_cover_url` | boolean |  | Whether to return cover URL, default true default `true` |
| `platform_source` | integer |  | Platform source, default 1 default `1` |

## Details

Returns the play count (`watch_cnt`) of a Douyin video, plus video details such as author ID, title, cover URL, duration, publish time and engagement stats. It needs the video ID in `item_id`.

### Use cases

- Check the play count of a sponsored Douyin video for campaign reports.
- Compare `like_cnt`, `share_cnt` and `comment_cnt` against `watch_cnt` to judge how well a video engages viewers.
- Pull the cover image and title of a video to show it in a dashboard.
- Link a video back to its creator through `item.author_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/item-play-count" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7630036460159111515"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video (item) ID |
| `need_cover_url` | boolean | No | Whether to return cover URL, default true |
| `platform_source` | integer | No | Platform source, default 1 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "exist": true,
  "item": {
    "author_id": "78050876812",
    "cover_uri": "tos-cn-i-0813c001/okH4NI7QDNMW1CqOgEf3AZAAbF1cApAAr229eG",
    "cover_url": "https://p26-star-fe-sign.byteimg.com/tos-cn-i-0813c001/okH4NI7QDNMW1CqOgEf3AZAAb…",
    "create_time": "1776506300",
    "duration": 28.234,
    "id": "7630036460159111515",
    "stats": {
      "avg_watch_dura": "0",
      "comment_cnt": "905",
      "favorite_cnt": "13473",
      "interact_rate": 0.0155,
      "like_cnt": "143631",
      "share_cnt": "52842",
      "watch_cnt": "12706869"
    },
    "status": 102,
    "title": "哈哈哈哈哈哈哈哈哈  我还以为真不怕痛呢 哈哈哈哈哈哈哈哈",
    "topic_ids": [],
    "url": "https://www.iesdouyin.com/share/video/7630036460159111515/?region=CN&mid=7630036…",
    "video_id": "v0d00fg10000d7hlb0vog65k07cn1neg"
  },
  "item_id": "7630036460159111515",
  "stats": {
    "avg_watch_dura": "0",
    "comment_cnt": "905",
    "favorite_cnt": "13473",
    "interact_rate": 0.0155,
    "like_cnt": "143631",
    "share_cnt": "52842",
    "watch_cnt": "12706869"
  },
  "watch_cnt": 12706869
}
```

### Response fields

| Field | Meaning |
|---|---|
| `watch_cnt` | Play count of the video as a number. The same value also appears as a string in `stats.watch_cnt`. |
| `exist` | Whether the video was found. A `true` value means the video data is filled in. |
| `stats.like_cnt / stats.comment_cnt / stats.favorite_cnt / stats.share_cnt` | Counts of likes, comments, favorites and shares. They come back as strings. |
| `stats.interact_rate` | Interaction rate of the video as a decimal number, for example `0.0155`. |
| `stats.avg_watch_dura` | Average watch duration. The sample value is `"0"`, and the unit is not shown in the response. |
| `item.title` | Video caption text. |
| `item.author_id` | ID of the creator who posted the video. |
| `item.create_time` | Publish time as a Unix timestamp in seconds, returned as a string. |
| `item.duration` | Video length. The sample value is `28.234`. |
| `item.cover_url` | Link to the video cover image. It is a signed URL with an `x-expires` parameter. |

### Notes

- `item_id` is the numeric Douyin video ID, which also appears in the `item.url` share link.
- `need_cover_url` defaults to `true`. Set it to `false` if you do not need `item.cover_url`.
- The `stats` object and `watch_cnt` are also at the top level, so you can read the play count without opening `item`.
- To get stats for many videos in one call, use [Douyin Xingtu Batch Video Stats](/apis/douyin/xingtu-v2/multi-get-item-stats). For creator details, call [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info) with the author ID.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Get Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Get creator audience profile distribution.
- [Get Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Get creator/author base information.
- [Get Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Get creator/author business card information.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/item-play-count.json`](../../../../catalog/models/douyin/xingtu-v2/item-play-count.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/item-play-count
