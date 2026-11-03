# Douyin Author Homepage Videos V1 API: pricing, parameters and code examples

`douyin/xingtu/author-homepage-videos-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get Author Homepage Videos V1 on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/author-homepage-videos-v1", "oAuthorId": "7386881810501730341"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/author-homepage-videos-v1', {'oAuthorId': '7386881810501730341'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/author-homepage-videos-v1", {
  "oAuthorId": "7386881810501730341"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/author-homepage-videos-v1", sandbase.Params{
	"oAuthorId": "7386881810501730341",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/author-homepage-videos-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starts from 1, 20 items per page default `1` |
| `oAuthorId` | string | yes | Xingtu author ID  |
| `videoType` | string |  | PERSONAL/XINGTU / Traffic type: ALL/PERSONAL/XINGTU default `"ALL"` |
| `onlyAssign` | boolean |  | Only return assigned videos default `false` |

## Details

Returns a page of videos from a Douyin author's Xingtu homepage, with title, engagement counts, and rates for each video. It needs the Xingtu author ID in `oAuthorId`.

### Use cases

- Review an author's recent videos and their view and like counts before choosing a creator for a campaign.
- Compare `finish_rate` and `interact_rate` across an author's videos to find the content that holds attention best.
- Export the full video list of a creator by paging through `pagination`.
- Separate personal videos from Xingtu videos with `videoType` to check how each type performs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/author-homepage-videos-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "7386881810501730341", "page": 1, "videoType": "ALL", "onlyAssign": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Xingtu author ID |
| `onlyAssign` | boolean | No | Only return assigned videos |
| `page` | integer | No | Page number, starts from 1, 20 items per page |
| `videoType` | string | No | PERSONAL/XINGTU / Traffic type: ALL/PERSONAL/XINGTU |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "items": [
    {
      "comment_cnt": "2376",
      "content_theme_labels": [],
      "cover_uri": "tos-cn-i-0813c000-ce/oUKnEYF9AgQvhS5dJADAIyue7CVg7FDBAeECfU",
      "create_time": "1792928944",
      "duration": 761.334,
      "finish_rate": 0.116147,
      "interact_rate": 0.063783,
      "item_id": "7700571178000135673",
      "like_cnt": "234612",
      "title": "在大量的聊天中发现了少量的化妆技巧 #vlog #宝妈 #发疯文学 #精神状态 #化妆",
      "url": "https://www.iesdouyin.com/share/video/7700571178000135673/?region=CN&mid=7700571…",
      "video_id": "v2800fgi0000dbeumffog65m66333310"
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 20,
    "page": 1,
    "total_count": 55
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].item_id / items[].video_id` | Identifiers for the video. `item_id` is a numeric string that also appears in the share `url`. `video_id` is a separate string ID. |
| `items[].title` | Video caption, including its hashtags. |
| `items[].create_time` | Creation time of the video as a Unix timestamp in seconds, returned as a string. |
| `items[].duration` | Length of the video. The values look like seconds (for example `761.334`). |
| `items[].watch_cnt / items[].like_cnt / items[].comment_cnt` | View, like and comment counts for the video. They are returned as strings. |
| `items[].finish_rate / items[].interact_rate` | Completion rate and interaction rate for the video, as decimals (for example `0.116147`). |
| `items[].url` | Share link to the video on Douyin. |
| `items[].cover_uri` | Path of the video cover image. `content_theme_labels` lists theme labels and can be empty. |
| `pagination.page / pagination.limit` | Current page number and the number of items per page. |
| `pagination.has_more / pagination.total_count` | `has_more` shows whether another page exists. `total_count` is the total number of videos for this query. |

### Notes

- Pages start at 1 and hold 20 items. Increase `page` while `pagination.has_more` is `true`.
- `videoType` accepts `ALL`, `PERSONAL` or `XINGTU`. Set `onlyAssign` to `true` to return only assigned videos.
- If you only have a Douyin user ID, get the Xingtu ID first with [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid).
- For the author's profile, call [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu/author-homepage-videos-v1.json`](../../../../catalog/models/douyin/xingtu/author-homepage-videos-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/author-homepage-videos-v1
