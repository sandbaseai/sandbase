# Weibo Keyword Search API: pricing, parameters and code examples

`weibo/search-all` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search Weibo posts by keyword within a required day-and-hour time range, with page-based pagination, hot or time sorting, and filters for pictures, video, music, or links.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/search-all", "q": "新闻", "startDay": "2026-10-22", "startHour": 0, "endDay": "2026-10-29", "endHour": 23}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/search-all', {'q': '新闻', 'startDay': '2026-10-22', 'startHour': 0, 'endDay': '2026-10-29', 'endHour': 23})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/search-all", {
  "q": "新闻",
  "startDay": "2026-10-22",
  "startHour": 0,
  "endDay": "2026-10-29",
  "endHour": 23
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/search-all", sandbase.Params{
	"q": "新闻",
	"startDay": "2026-10-22",
	"startHour": 0,
	"endDay": "2026-10-29",
	"endHour": 23,
})
```

Same call via the path form: `POST /v1/api/weibo/search-all` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Search Keywords.  |
| `page` | integer |  | Page number, starting with 1. default `1` |
| `endDay` | string | yes | End Day (yyyy-MM-dd).  |
| `endHour` | integer | yes | End Hour (0-23).  |
| `hotSort` | boolean |  | Hot sort, true for hot sort, false for time sort. Default is false. default `false` |
| `contains` | string |  | Contains filter for the result set. one of: `ALL`, `PICTURE`, `VIDEO`, `MUSIC`, `LINK`; default `"ALL"` |
| `startDay` | string | yes | Start Day (yyyy-MM-dd).  |
| `startHour` | integer | yes | Start Hour (0-23).  |

## Details

Returns Weibo posts that match a keyword within a required start and end day-and-hour range. Each post includes its text, author, engagement counts, topics, and any video link. You pass the keyword in `q` and the time range in `startDay`, `startHour`, `endDay` and `endHour`.

### Use cases

- Collect posts about a news event during a specific window, such as the day after a announcement.
- Track which accounts post most often about a keyword and how much engagement they get.
- Find posts that carry a video by setting `contains` to `VIDEO` and read the `video_url` values.
- Gather hashtags used with a keyword by reading the `topics` field across results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/search-all" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "新闻", "startDay": "2026-10-22", "startHour": 0, "endDay": "2026-10-29", "endHour": 23}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `endDay` | string | Yes | End Day (yyyy-MM-dd). |
| `endHour` | integer | Yes | End Hour (0-23). |
| `q` | string | Yes | Search Keywords. |
| `startDay` | string | Yes | Start Day (yyyy-MM-dd). |
| `startHour` | integer | Yes | Start Hour (0-23). |
| `contains` | string | No | Contains filter for the result set. |
| `hotSort` | boolean | No | Hot sort, true for hot sort, false for time sort. Default is false. |
| `page` | integer | No | Page number, starting with 1. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "has_next_page": true,
  "weibo_list": [
    {
      "article_url": "",
      "at_users": "",
      "attitudes_count": "357",
      "bid": "RoXFjgJp5",
      "comments_count": "1",
      "created_at": "2026-10-29 23:00",
      "forwarded": "false",
      "id": "5359492293987783",
      "location": "",
      "pics": "",
      "reposts_count": "2",
      "retweet_id": ""
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `has_next_page` | Shows whether more results exist. When it is `true`, request the next `page`. |
| `weibo_list[]` | The list of matching posts for the current page. |
| `weibo_list[].id / weibo_list[].bid` | Identifiers of the post. `id` is a numeric string and `bid` is a short code. |
| `weibo_list[].text` | The post text. It can include leading spaces, hashtags marked with `#`, and a cut-off ending. |
| `weibo_list[].created_at` | Time the post was created, in `yyyy-MM-dd HH:mm` format. |
| `weibo_list[].screen_name / weibo_list[].user_id` | Display name and numeric ID of the author. |
| `weibo_list[].attitudes_count / weibo_list[].comments_count / weibo_list[].reposts_count` | Counts of likes, comments and reposts for the post. Values are strings. |
| `weibo_list[].topics` | Hashtag topics in the post, joined by commas without the `#` signs. |
| `weibo_list[].video_url` | Link to the post video. It is an empty string when the post has no video. |
| `weibo_list[].source` | The client or channel the post was published from, such as `微博网页版`. |

### Notes

- All five of `q`, `startDay`, `startHour`, `endDay` and `endHour` are required. Dates use `yyyy-MM-dd` and hours run from 0 to 23.
- Page through results with `page`, starting at 1. Keep going while `has_next_page` is `true`.
- Set `hotSort` to `true` to sort by hot instead of time. Set `contains` to `PICTURE`, `VIDEO`, `MUSIC` or `LINK` to filter the result set.
- Empty fields such as `pics`, `location` and `retweet_id` come back as empty strings, and numeric values come back as strings.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/weibo/search-all.json`](../../../catalog/models/weibo/search-all.json) · Store page: https://www.sandbase.ai/model/weibo/search-all
