# Douyin Video search V3 API: pricing, parameters and code examples

`douyin/search/video-search-v3` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Fetch video search V3 on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/video-search-v3"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/video-search-v3', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/video-search-v3", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/video-search-v3", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/video-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string |  | Search keyword default `"美食"` |
| `date_type` | integer |  | Publish date filter: 0=any, 3=last 3 days, 7=last 7 days, 30=last 30 days default `0` |
| `label_type` | integer |  | Video type filter: 0=any, 1=low-follower hit, 2=high completion rate, 3=high follower growth, 4=high like rate default `0` |
| `duration_type` | integer |  | Duration filter: 0=any, 1=0-15s, 6=15-60s, 7=60-120s, 8=120-180s, 9=over 180s default `0` |

## Details

Searches Douyin videos by keyword and returns a list of matching videos with the author, like count, follower count, duration and a link to each video. You send a `query` and can filter by publish date, video type and duration.

### Use cases

- Find recent Douyin videos on a topic by setting `date_type` to 3, 7 or 30.
- Spot videos from small accounts that got a lot of attention by setting `label_type` to 1.
- Collect short videos under 15 seconds, or long videos over 180 seconds, for a keyword with `duration_type`.
- Build a list of creators in a niche using `nickname` and `fans`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/video-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "美食", "date_type": 0, "label_type": 0, "duration_type": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_type` | integer | No | Publish date filter: 0=any, 3=last 3 days, 7=last 7 days, 30=last 30 days |
| `duration_type` | integer | No | Duration filter: 0=any, 1=0-15s, 6=15-60s, 7=60-120s, 8=120-180s, 9=over 180s |
| `label_type` | integer | No | Video type filter: 0=any, 1=low-follower hit, 2=high completion rate, 3=high follower growth, 4=high like rate |
| `query` | string | No | Search keyword |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "avatarUrl": "https://p3-byteindex-sign.byteimg.com/aweme-avatar/tos-cn-i-0813c000-ce_osD7MQgO…",
      "createTime": "2026-10-30 23:34:15",
      "duration": 72,
      "fans": 13248,
      "index": "657817",
      "isHighFansRiseRate": 0,
      "isHighLikeRate": 1,
      "isHighPlayOverRate": 0,
      "isLowFansButHot": 1,
      "itemId": "7702484601909857590",
      "likes": "226165",
      "nickname": "明食记"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].itemId` | ID of the video. Use it to look up the same video in other Douyin APIs. |
| `data[].url` | Direct link to the video page on douyin.com. |
| `data[].title` | Video caption, including its hashtags. |
| `data[].nickname / data[].fans` | Display name of the author and the author's follower count. |
| `data[].likes` | Like count of the video. It arrives as a string. |
| `data[].duration` | Length of the video. The value is a number, such as 72 or 274. |
| `data[].createTime` | Publish time as a `YYYY-MM-DD HH:MM:SS` string. |
| `data[].isLowFansButHot / data[].isHighLikeRate / data[].isHighPlayOverRate / data[].isHighFansRiseRate` | Flags with the value 0 or 1. They match the `label_type` filters: low-follower hit, high like rate, high completion rate and high follower growth. |
| `data[].index` | Numeric score returned as a string for each video. The response does not explain how it is calculated. |
| `data[].avatarUrl / data[].thumbnail` | Image links for the author's avatar and the video cover. The links carry an `x-expires` value, so they may stop working. |

### Notes

- `label_type` values: `0` any, `1` low-follower hit, `2` high completion rate, `3` high follower growth, `4` high like rate.
- `duration_type` values: `0` any, `1` 0-15s, `6` 15-60s, `7` 60-120s, `8` 120-180s, `9` over 180s.
- The request has no pagination parameter. Each call returns one list under `data`.
- For full details of one video, pass `itemId` to [Douyin Video Detail](/apis/douyin/app-v3/one-video-v3). Other search versions are [Douyin Video Search (V1)](/apis/douyin/search/video-search-v1) and [Douyin Video search V4](/apis/douyin/search/video-search-v4).

### Pricing

$0.01 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/search/video-search-v3.json`](../../../../catalog/models/douyin/search/video-search-v3.json) · Store page: https://www.sandbase.ai/model/douyin/search/video-search-v3
