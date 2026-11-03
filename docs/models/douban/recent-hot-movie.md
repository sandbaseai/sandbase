# Douban Recent Hot Movie API: pricing, parameters and code examples

`douban/recent-hot-movie` · data API · Douban · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get a paginated list of movies currently featured in Douban's recent-hot collection. Use it to discover popular movie titles and continue through result pages.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douban/recent-hot-movie"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douban/recent-hot-movie', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douban/recent-hot-movie", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douban/recent-hot-movie", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douban/recent-hot-movie` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |

## Details

This API returns a paginated list of movies in Douban's recent-hot collection, with title, poster, rating and a short credits line for each movie. It needs no input except an optional `page` number.

### Use cases

- Build a feed of newly listed Douban movies with posters and ratings.
- Track how the `rating.value` and `rating.count` of new releases change between calls.
- Collect Douban movie IDs to pass to a detail or review API.
- Filter the list by country, genre or director by parsing `card_subtitle`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douban/recent-hot-movie" \
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
  "category": "最新",
  "items": [
    {
      "card_subtitle": "2026 / 法国 意大利 / 喜剧 动作 惊悚 犯罪 / 托马斯·文森特 / 斯坦利·图齐 维克多·贝尔蒙多",
      "episodes_info": "",
      "id": "37660136",
      "is_new": false,
      "pic": {
        "large": "https://img9.doubanio.com/view/photo/m_ratio_poster/public/p2936095806.jpg",
        "normal": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2936095806.jpg"
      },
      "rating": {
        "count": 635,
        "max": 10,
        "star_count": 3.0,
        "value": 5.7
      },
      "title": "偷天父子兵",
      "type": "movie",
      "uri": "douban://douban.com/movie/37660136"
    }
  ],
  "recommend_tags": [
    {
      "category": "热门",
      "selected": false,
      "title": "热门",
      "type": "全部"
    }
  ],
  "tags": [
    {
      "category": "热门",
      "selected": false,
      "title": "热门电影",
      "types": [
        {
          "selected": false,
          "title": "全部",
          "type": "全部"
        }
      ]
    }
  ],
  "total": 495,
  "type": "全部"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].id` | Douban ID of the movie, as a string. |
| `items[].title` | Movie title as shown on Douban. |
| `items[].card_subtitle` | One text line joined with ` / `. In the sample it holds year, countries, genres, director and lead actors, in that order. |
| `items[].rating.value / items[].rating.max` | Average rating and the top of the rating scale (`10` in the sample). |
| `items[].rating.count` | Number of ratings behind the average. |
| `items[].pic.large / items[].pic.normal` | URLs of the poster image in a larger and a smaller size. |
| `items[].is_new` | Boolean flag that marks a movie as new in the list. |
| `items[].uri` | Deep link to the movie in the Douban app, built from the movie `id`. |
| `total` | Total number of movies in the current collection (`495` in the sample). |
| `category / type` | The collection and the type filter this response shows. The sample returns `最新` and `全部`. |

### Notes

- Send `page` in the request body to move through the list. It starts at `1` and defaults to `1`.
- Use `total` and the number of `items` on each page to decide when to stop paging.
- `recommend_tags` and `tags` list the other collections (`热门`, `最新`, `豆瓣高分`) and their type filters. This API only accepts `page`, so the request cannot select them.
- Pass `items[].id` to [Douban Subject Details](/apis/douban/subject-detail) for full movie data. For TV, call [Douban Recent Hot Tv](/apis/douban/recent-hot-tv).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/douban/recent-hot-movie.json`](../../../catalog/models/douban/recent-hot-movie.json) · Store page: https://www.sandbase.ai/model/douban/recent-hot-movie
