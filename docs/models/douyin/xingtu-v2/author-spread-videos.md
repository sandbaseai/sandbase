# Douyin Author Spread Videos API: pricing, parameters and code examples

`douyin/xingtu-v2/author-spread-videos` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call · **Modes:** sync

Get Author Spread Videos on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.002 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-spread-videos", "o_author_id": "7112600044674482187"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-spread-videos', {'o_author_id': '7112600044674482187'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-spread-videos", {
  "o_author_id": "7112600044674482187"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-spread-videos", sandbase.Params{
	"o_author_id": "7112600044674482187",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-spread-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, 1 for Douyin default `1` |
| `platform_channel` | integer |  | Platform channel, 1 for short video default `1` |

## Details

Returns a list of a Douyin creator's spread videos, with title, duration, publish time and engagement stats for each video. It needs the creator ID in `o_author_id`. `platform_source` and `platform_channel` both default to `1` (Douyin, short video).

### Use cases

- Compare view and like counts across a creator's spread videos before a brand deal.
- Rank a creator's videos by `interact_rate` to find the content that drew the most engagement.
- Pull video titles and hashtags to review the topics a creator promotes.
- Build a report of a creator's recent video performance for a campaign pitch.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-spread-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7112600044674482187", "platform_source": 1, "platform_channel": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `platform_channel` | integer | No | Platform channel, 1 for short video |
| `platform_source` | integer | No | Platform source, 1 for Douyin |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "spread_videos": [
    {
      "author_id": "78050876812",
      "cover_uri": "tos-cn-i-0813c001/oYABexOFAf75I3BBLPADUIQGUAnG1ApEsve2jt",
      "create_time": "1735039831",
      "duration": 272.044,
      "id": "7451907165419359488",
      "stats": {
        "avg_watch_dura": "0",
        "comment_cnt": "22784",
        "favorite_cnt": "55867",
        "interact_rate": 0.0319,
        "like_cnt": "567682",
        "share_cnt": "378214",
        "watch_cnt": "30308258"
      },
      "title": "头皮发麻#美妆 #好物分享 #化妆日常",
      "url": "https://www.iesdouyin.com/share/video/7451907165419359488/?region=CN&mid=7451907…",
      "video_id": "v0300fg10000ctl7nkfog65pgevhdio0"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `spread_videos[].id` | ID of the video. |
| `spread_videos[].video_id` | Second video identifier, a string that starts with `v0300`. |
| `spread_videos[].title` | Video caption, including its hashtags. |
| `spread_videos[].create_time` | Publish time as a Unix timestamp in seconds, returned as a string. |
| `spread_videos[].duration` | Length of the video. The values (for example `272.044`) look like seconds. |
| `spread_videos[].stats.watch_cnt` | Number of views the video has. |
| `spread_videos[].stats.like_cnt / spread_videos[].stats.comment_cnt / spread_videos[].stats.share_cnt / spread_videos[].stats.favorite_cnt` | Counts of likes, comments, shares and favorites. They come back as strings. |
| `spread_videos[].stats.interact_rate` | Interaction rate of the video as a decimal number, for example `0.0319`. |
| `spread_videos[].url` | Share link to the video on Douyin. |
| `spread_videos[].author_id` | ID of the author the video belongs to. |

### Notes

- `o_author_id` is the creator ID used by Xingtu. If you only have a Douyin ID, look it up with [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id).
- The `author_id` inside each video (for example `78050876812`) differs from the `o_author_id` you send in the request.
- `avg_watch_dura` was `"0"` for every video in this response, so do not rely on it.
- For the creator's own homepage posts, call [Douyin Xingtu Author Homepage Videos](/apis/douyin/xingtu-v2/author-homepage-videos).

### Pricing

$0.002 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-spread-videos.json`](../../../../catalog/models/douyin/xingtu-v2/author-spread-videos.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-spread-videos
