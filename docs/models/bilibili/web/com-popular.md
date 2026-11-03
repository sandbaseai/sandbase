# Bilibili Comprehensive Popular Videos API: pricing, parameters and code examples

`bilibili/web/com-popular` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a comprehensive list of trending videos on Bilibili, including video metadata, author details, and engagement statistics across pages.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/com-popular"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/com-popular', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/com-popular", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/com-popular", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/web/com-popular` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pn` | integer |  | Page number default `1` |

## Details

Returns one page of trending videos on Bilibili. Each item has video metadata, author details, category names and engagement counts. The only input is the optional page number `pn`, which defaults to 1.

### Use cases

- Build a daily snapshot of which videos are trending on Bilibili and track how `stat.his_rank` changes.
- Compare `stat.like`, `stat.coin` and `stat.favorite` across trending videos to see which content earns the most engagement.
- Group trending videos by `pid_name_v2` or `tnamev2` to see which categories dominate the list.
- Collect creator `owner.mid` values from trending videos to find authors worth tracking.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/com-popular" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `pn` | integer | No | Page number |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "list": [
      {
        "ai_rcmd": null,
        "aid": 117547651307164,
        "attribute_v3": 4,
        "bvid": "BV19b4A6PECX",
        "cid": 43272309199,
        "copyright": 1,
        "cover43": "http://i0.hdslb.com/bfs/archive/9f5f456a7fb8b8ab9a3517ff21edbec7d4c3ca67.jpg",
        "ctime": 1793635087,
        "current_state": 0,
        "desc": "与能源相关的实验都存在一定的危险性，所以工作人员需要时刻保持谨慎的态度。\n不妨多问问自己：有日程可控的预期吗？有数据稳定的可能吗？有提前完成的风险吗？\n\n中文C…",
        "dimension": {
          "height": 1080,
          "rotate": 0,
          "width": 2560
        },
        "duration": 681
      }
    ],
    "no_more": false
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.list[].bvid / data.list[].aid` | The video's BV ID and its numeric AID. Both identify the same video. |
| `data.list[].title / data.list[].desc` | The video title and its description text. Long descriptions are cut in this sample. |
| `data.list[].owner.mid / data.list[].owner.name / data.list[].owner.face` | The author's numeric ID, display name and avatar image URL. |
| `data.list[].stat.like / data.list[].stat.coin / data.list[].stat.favorite / data.list[].stat.danmaku` | Engagement counts for the video: likes, coins, favorites and danmaku (on-screen comments). |
| `data.list[].stat.his_rank` | A rank value for the video. It is `0` for videos without a rank. |
| `data.list[].pid_name_v2 / data.list[].tnamev2` | The top-level category name and the finer sub-category name of the video. |
| `data.list[].pubdate / data.list[].ctime` | Unix timestamps in seconds. `pubdate` is the publish time and `ctime` is the creation time. |
| `data.list[].duration / data.list[].dimension.width / data.list[].dimension.height` | The video length (in the value's own unit, seconds by the sample values) and the frame width and height in pixels. |
| `data.list[].rcmd_reason.content` | A short recommendation label such as a like count badge. It is an empty string when there is none. |
| `data.list[].short_link_v2` | A short b23.tv link to the video page. |
| `data.no_more` | A boolean that shows whether more pages remain. `false` means more pages may be available. |

### Notes

- Set `pn` to request later pages. Start at `1` and increase by one while `data.no_more` is `false`.
- Video IDs come as `bvid` (a string starting with `BV`) and `aid` (a number). Use [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid) to convert a BV ID to an AID.
- Pass a `bvid` from this list to [Bilibili Video Details](/apis/bilibili/web/one-video) to get details for one video.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/com-popular.json`](../../../../catalog/models/bilibili/web/com-popular.json) · Store page: https://www.sandbase.ai/model/bilibili/web/com-popular
