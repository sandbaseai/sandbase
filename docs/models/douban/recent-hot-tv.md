# Douban Recent Hot Tv API: pricing, parameters and code examples

`douban/recent-hot-tv` · data API · Douban · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get a paginated list of TV titles currently featured in Douban's recent-hot collection. Use it to discover popular series and continue through result pages.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douban/recent-hot-tv"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douban/recent-hot-tv', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douban/recent-hot-tv", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douban/recent-hot-tv", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douban/recent-hot-tv` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |

## Details

Returns a paginated list of TV series from Douban's recent-hot collection. Each item has a title, rating, episode status and poster. The only input is an optional `page` number.

### Use cases

- Build a chart of the TV series that Douban users are watching and rating right now.
- Track which new series are airing by reading `episodes_info`, such as ongoing or finished status.
- Collect Douban IDs of popular series to fetch full details for each one.
- Compare ratings and rating counts across current hit shows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douban/recent-hot-tv" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "category": "tv",
  "items": [
    {
      "card_subtitle": "2026 / 中国大陆 / 剧情 / 张晓波 / 肖战 倪大红",
      "episodes_info": "29集全",
      "id": "36675942",
      "is_new": false,
      "pic": {
        "large": "https://img2.doubanio.com/view/photo/m_ratio_poster/public/p2936709341.jpg",
        "normal": "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2936709341.jpg"
      },
      "rating": {
        "count": 272690,
        "max": 10,
        "star_count": 4.0,
        "value": 8.0
      },
      "title": "小城良方",
      "type": "tv",
      "uri": "douban://douban.com/tv/36675942"
    }
  ],
  "recommend_tags": [
    {
      "category": "tv",
      "selected": true,
      "title": "综合",
      "type": "tv"
    }
  ],
  "tags": [
    {
      "category": "tv",
      "selected": true,
      "title": "最近热门剧集",
      "types": [
        {
          "selected": true,
          "title": "综合",
          "type": "tv"
        }
      ]
    }
  ],
  "total": 229,
  "type": "tv"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].id` | Douban ID of the TV title. Use it to look up more details about the title. |
| `items[].title` | Title of the series. |
| `items[].card_subtitle` | One line summary with year, country or region, genres, director and lead actors, separated by `/`. |
| `items[].episodes_info` | Episode status text, for example `29集全` for a finished series or `更新至26集` for one still airing. |
| `items[].rating.value / items[].rating.max` | Average rating and the top of the rating scale. |
| `items[].rating.count` | Number of ratings the title has received. |
| `items[].rating.star_count` | Rating shown as stars. The values in the response are in steps of 0.5. |
| `items[].pic.large / items[].pic.normal` | URLs of the poster image in a larger and a smaller size. |
| `items[].is_new` | Boolean flag that marks a title as new. |
| `total` | Total number of items in the collection. |
| `tags[].types[].type / recommend_tags[].type` | Category codes such as `tv`, `tv_domestic`, `tv_american` and `show`. The `selected` flag shows which one this response uses. |

### Notes

- Send `page` to move through results. It starts at `1` by default. Compare the number of items collected with `total` to know when to stop.
- The `id` in each item is a string of digits. Pass it to [Douban Subject Details](/apis/douban/subject-detail) to get full details of a title.
- For movies instead of TV, use [Douban Recent Hot Movie](/apis/douban/recent-hot-movie).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/douban/recent-hot-tv.json`](../../../catalog/models/douban/recent-hot-tv.json) · Store page: https://www.sandbase.ai/model/douban/recent-hot-tv
