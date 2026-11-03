# Bilibili App Bangumi Tab API: pricing, parameters and code examples

`bilibili/app/bangumi-tab` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/bangumi-tab"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/bangumi-tab', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/bangumi-tab", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/bangumi-tab", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/app/bangumi-tab` with the body above minus `model`.

## Details

Returns the layout of the Bilibili app bangumi tab: banner modules, function entry buttons, and region links. The request takes no parameters, so you send an empty JSON object.

### Use cases

- Capture the current banner lineup on the bangumi tab and the episode each banner links to.
- Read the `link` and `episode_id` of each banner item to find which anime episodes the app is promoting.
- List the region shortcuts, such as 番剧 and 国创, with their icons and in-app deep links.
- Compare the module layout of the tab over time by storing `module_id`, `style` and `title`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/bangumi-tab" \
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
            "cover": "http://i0.hdslb.com/bfs/bangumi/image/c030ff67970da5e456dc16af0cb1242880ab8b2c.p…",
            "episode_id": 424179,
            "is_preview": 0,
            "item_id": 150352,
            "link": "https://www.bilibili.com/bangumi/play/ep424179",
            "oid": 424179,
            "report": {
              "card_type": "banner",
              "item_id": "150352",
              "module_id": "83",
              "module_type": "banner",
              "oid": "https://www.bilibili.com/bangumi/play/ep424179"
            }
          }
        ],
        "module_id": 83,
        "report": {
          "module_id": "83",
          "module_type": "banner"
        },
        "size": 6,
        "style": "banner",
        "title": "新版banner",
        "type": 1,
        "wid": [
          283
        ]
      }
    ],
    "regions": [
      {
        "icon": "http://i0.hdslb.com/bfs/bangumi/image/2e6f9066e4eb5f30d75a28c3bcaa7541dad5c95d.p…",
        "report": {
          "card_type": "function",
          "item_id": "24386",
          "module_id": "241",
          "module_type": "function"
        },
        "title": "全部内容",
        "url": "bilibili://pgc/bangumi/index"
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code / message` | Status of the call. `code` is `0` and `message` is `success` when the request works. |
| `result.modules[]` | List of content blocks on the tab. Each block holds a group of items and has its own layout settings. |
| `result.modules[].module_id / style / title` | ID, layout style and name of the module. Seen styles include `banner`, `function` and `tip`. |
| `result.modules[].items[].cover` | URL of the cover image for the item. |
| `result.modules[].items[].link` | Target of the item. It is a web URL for banner items or a `bilibili://` app link for function items. |
| `result.modules[].items[].episode_id / oid` | Episode ID for banner items. In the banner items shown, both fields hold the same value. |
| `result.modules[].items[].title` | Label of a function item, for example 番剧, 国创 or 时间表. Banner items do not carry this field. |
| `result.regions[].title / icon / url` | Name, icon image URL and in-app deep link for each region shortcut on the tab. |
| `result.hot.title / result.hot.items[]` | Title of the hot recommendation section and its items. `items` was empty in this response. |

### Notes

- The endpoint has no request parameters. Send `{}` as the body.
- Some modules, such as the `tip` module, can return an empty `items` list.
- Banner `link` values point to a play page in the form `https://www.bilibili.com/bangumi/play/ep<episode_id>`.
- To look at other app tabs, call [Bilibili App Cinema Tab](/apis/bilibili/app/cinema-tab) or [Bilibili App Home Feed](/apis/bilibili/app/home-feed).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili App Cinema Tab](/apis/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/apis/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.
- [Bilibili App Single Video Details](/apis/bilibili/app/one-video): Returns detailed video metadata for a specific Bilibili video.

---
Machine-readable: [`catalog/models/bilibili/app/bangumi-tab.json`](../../../../catalog/models/bilibili/app/bangumi-tab.json) · Store page: https://www.sandbase.ai/model/bilibili/app/bangumi-tab
