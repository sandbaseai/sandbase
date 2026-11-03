# Bilibili App Cinema Tab API: pricing, parameters and code examples

`bilibili/app/cinema-tab` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/cinema-tab"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/cinema-tab', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/cinema-tab", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/cinema-tab", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/app/cinema-tab` with the body above minus `model`.

## Details

Returns the content layout of the Bilibili app cinema tab: banner modules, function entries, hot recommendations, and category regions. It needs no input. Send an empty JSON object as the request body.

### Use cases

- Read the banner items to see which movies and shows Bilibili promotes on the cinema tab.
- Collect `season_id` and `episode_id` values from banners to feed a catalog of promoted titles.
- Track changes in module titles and item order to study how the cinema tab layout changes over time.
- List the cinema category entries, such as documentary, movie and TV series, with their icons and app links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/cinema-tab" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "message": "success",
  "result": {
    "hot": {
      "desc": "查看更多",
      "items": [],
      "title": "热点推荐",
      "wid": 0
    },
    "modules": [
      {
        "attr": {
          "follow": 0,
          "header": 0,
          "random": 0
        },
        "headers": [],
        "items": [
          {
            "badge_info": {
              "bg_color": "",
              "bg_color_night": "",
              "text": ""
            },
            "cover": "https://i0.hdslb.com/bfs/bangumi/image/ef8e0830ba7f817362c9d2166e71e3fbe4aaa2d9.…",
            "is_preview": 0,
            "item_id": 156505,
            "link": "https://www.bilibili.com/bangumi/play/ss45270?theme=movie",
            "oid": 45270,
            "report": {
              "card_type": "banner",
              "item_id": "156505",
              "module_id": "85",
              "module_type": "banner",
              "oid": "https://www.bilibili.com/bangumi/play/ss45270?theme=movie"
            },
            "season_id": 45270
          }
        ],
        "module_id": "85",
        "report": {
          "module_id": "85",
          "module_type": "banner"
        },
        "size": 6,
        "style": "banner",
        "title": "banner",
        "type": 1,
        "wid": [
          288
        ]
      }
    ],
    "regions": [
      {
        "icon": "http://i0.hdslb.com/bfs/bangumi/image/c8ad7c4053e80927f0a29c508089ea2781aba317.p…",
        "report": {
          "card_type": "function",
          "item_id": "103591",
          "module_id": "248",
          "module_type": "function"
        },
        "title": "纪录片",
        "url": "bilibili://pgc/partition_page?page_name=documentary-operation&title=%E7%BA%AA%E5…"
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `result.modules[]` | The content blocks of the tab. Each block has a `title`, a `style` (for example `banner`, `function` or `static`), a `module_id`, and a list of `items`. |
| `result.modules[].items[].cover` | URL of the cover image for the item. |
| `result.modules[].items[].link` | Link for the item. It is either a Bilibili web play page or an in-app `bilibili://` link. |
| `result.modules[].items[].season_id / result.modules[].items[].episode_id` | IDs of the season or episode the item points to. They appear only on items that link to a play page. |
| `result.modules[].items[].aid / result.modules[].items[].cid` | Numeric video IDs attached to some items. |
| `result.modules[].items[].title` | Label of an entry, such as 电影 (movie) or 电视剧 (TV series). It appears on function entries. |
| `result.modules[].items[].badge_info.text` | Text of the badge shown on the item. It is an empty string when there is no badge. |
| `result.modules[].report` | Tracking info for the module, with `module_id` and `module_type`. |
| `result.hot.title / result.hot.items` | Title and items of the hot recommendation section. `items` can be empty. |
| `result.regions[].title / result.regions[].icon / result.regions[].url` | Name, icon image and in-app link of each cinema category, such as documentary, movie and TV series. |

### Notes

- The request takes no parameters. Send `{}` as the body.
- Some modules return an empty `items` list, so check the list length before you read it.
- Links that start with `bilibili://` open inside the Bilibili app. Links that start with `https://` open a web page.
- To see anime recommendations instead, call [Bilibili App Bangumi Tab](/apis/bilibili/app/bangumi-tab).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili App Bangumi Tab](/apis/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Home Feed](/apis/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.
- [Bilibili App Single Video Details](/apis/bilibili/app/one-video): Returns detailed video metadata for a specific Bilibili video.

---
Machine-readable: [`catalog/models/bilibili/app/cinema-tab.json`](../../../../catalog/models/bilibili/app/cinema-tab.json) · Store page: https://www.sandbase.ai/model/bilibili/app/cinema-tab
