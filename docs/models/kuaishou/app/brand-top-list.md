# Kuaishou Brand Top List API: pricing, parameters and code examples

`kuaishou/app/brand-top-list` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns top brand rankings and related live stream links from Kuaishou. Allows filtering ranking data by sub-tab category ID or sub-tab name.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/brand-top-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/brand-top-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/brand-top-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/brand-top-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/brand-top-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `subTabId` | integer |  | 子标签ID/Sub tag ID default `0` |
| `subTabName` | string |  | 子标签名称/Sub tag name default `""` |

## Details

Returns the Kuaishou brand top list. Each sub-tab holds a ranked list of brands, and each brand links to a live stream. Both inputs are optional: `subTabId` and `subTabName` filter the result by category.

### Use cases

- Compare which beauty brands rank highest on the Kuaishou brand list.
- Collect the live stream links that go with each ranked brand.
- List the available brand categories, such as beauty, clothing and cars, with their IDs.
- Track the live stream host account behind each brand entry.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/brand-top-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subTabId` | integer | No |  |
| `subTabName` | string | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "host-name": "public-bjzey-c34-kce-node1156.idchb1az3.hb1.kwaidc.com",
  "result": 1,
  "topList": {
    "banner": {
      "duration": 5,
      "items": [
        {
          "bannerId": 622,
          "item": {
            "linkUrl": "https://brand-activity-page.e.kuaishou.com/brand/activity?id=24400&source=53&lay…",
            "shapeType": 0,
            "url": [
              {
                "cdn": "ty2.a.kwimgs.com",
                "url": "https://ty2.a.kwimgs.com/kos/nlav11021/activity_1003_tanliuli_2026-10-26_16:22:3…"
              }
            ]
          },
          "promotion": "广告"
        }
      ]
    },
    "data": [
      {
        "backGroundImage": [],
        "list": [
          {
            "avatar": {
              "icon": [
                {
                  "cdn": "tx2.a.yximgs.com",
                  "url": "https://tx2.a.yximgs.com/udata/pkg/doodle_static/upload/5734be76b678070cf8e4d89a…"
                }
              ],
              "linkUrl": "kwai://live/play/RVCWXKJoY3s?serverExpTag=feed_live|RVCWXKJoY3s|2957169798|1_a/2…",
              "liveType": 2,
              "shapeType": 0,
              "url": [
                {
                  "cdn": "tx2.a.yximgs.com",
                  "url": "https://tx2.a.yximgs.com/udata/pkg/doodle_static/upload/5734be76b678070cf8e4d89a…"
                }
              ]
            },
            "feedLogCtx": {
              "stExParams": null,
              "stidContainer": "InMxfDIwMTAyNjcwNTQyNzQ4MDMwODl8VVNFUjoyOTU3MTY5Nzk4fHsicGciOiJtc2JyYW5kIn18eyJi…"
            },
            "linkUrl": "kwai://live/play/RVCWXKJoY3s?serverExpTag=feed_live|RVCWXKJoY3s|2957169798|1_a/2…",
            "logInfo": {
              "authorid": "2957169798",
              "id": "2957169798",
              "params": {
                "id": "15035317543",
                "normalindex": null,
                "type": "LIVE"
              },
              "type": "USER"
            },
            "renderStrategyIcon": null,
            "rightView": {
              "icon": {
                "icon": [
                  {
                    "cdn": "ty2.a.kwimgs.com",
                    "url": "https://ty2.a.kwimgs.com/udata/pkg/se-cdn/huomiao.png"
                  }
                ],
                "shapeType": 0,
                "url": [
                  {
                    "cdn": "tx2.a.yximgs.com",
                    "url": "https://tx2.a.yximgs.com/udata/pkg/se-cdn/huomiao.png"
                  }
                ]
              },
              "isPrefix": 1,
              "text": {
                "content": "20.4万"
              }
            },
            "title": "韩束",
            "viewType": 2
          }
        ],
        "subTabId": 5,
        "subTabName": "美妆"
      }
    ],
    "dataType": 1,
    "moduleType": 1
  },
  "ussid": "MzAxXzBfMTc5MzY5MTM0MTE5M19fNDk1NA"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `topList.data[].subTabId / topList.data[].subTabName` | ID and name of a brand category sub-tab, for example `5` and `美妆` (beauty). Pass these values back as request parameters to filter. |
| `topList.data[].list[].title` | Brand name for the ranked entry, for example `韩束`. |
| `topList.data[].list[].rightView.text.content` | Display text shown beside the brand, for example `20.4万`. It is a formatted string, not a plain number. |
| `topList.data[].list[].linkUrl` | Deep link in `kwai://live/play/...` form that opens the live stream tied to the brand. |
| `topList.data[].list[].logInfo.authorid / topList.data[].list[].logInfo.id` | Kuaishou user ID of the account behind the live stream entry. |
| `topList.data[].list[].logInfo.params.id` | Numeric ID with the type `LIVE`, tied to the live stream entry. |
| `topList.data[].list[].avatar.url[].url` | Image URL for the brand avatar, offered on several CDN hosts. |
| `topList.banner.items[].linkUrl` | Landing page link for a banner. The banner `promotion` field is `广告` (advertisement) in this response. |

### Notes

- In the sample response, only the first sub-tab contains a `list`. The other sub-tabs list just `subTabId` and `subTabName`.
- Call with an empty body to see all sub-tabs, then send one `subTabId` or `subTabName` to filter.
- Image objects repeat the same file under different `cdn` hosts, so use any one `url`.
- For other Kuaishou live rankings, see [Kuaishou Stream Top List](/apis/kuaishou/app/live-top-list) and [Kuaishou Shopping Top List](/apis/kuaishou/app/shopping-top-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.
- [Kuaishou Hot Board Detail](/apis/kuaishou/app/hot-board-detail): Returns trending topics and search keywords from Kuaishou hot boards based on the specified board identifier and board type.

---
Machine-readable: [`catalog/models/kuaishou/app/brand-top-list.json`](../../../../catalog/models/kuaishou/app/brand-top-list.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/brand-top-list
