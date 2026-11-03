# Kuaishou Hot Search Person Board API: pricing, parameters and code examples

`kuaishou/app/hot-search-person` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the current Kuaishou hot search person board rankings. Delivers real-time trending individuals and popular figures featured across the platform.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/hot-search-person"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/hot-search-person', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/hot-search-person", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/hot-search-person", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/hot-search-person` with the body above minus `model`.

## Details

Returns the current Kuaishou hot search person board as a ranked list of users. It takes no input parameters, so send an empty JSON object `{}`.

### Use cases

- Pull the current top trending creators on Kuaishou and store the ranking on a schedule.
- Compare `hotValue` across calls to see which people gain search heat.
- Collect user IDs of rising creators, then look up their profiles or videos.
- Check the `recoReason` tag to see why a person entered the board, such as a new post or a jump in searches.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/hot-search-person" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "host-name": "public-bjzey-c97-kce-node64.idchb1az3.hb1.kwaidc.com",
  "result": 1,
  "topList": {
    "data": [
      {
        "backGroundImage": [],
        "list": [
          {
            "avatar": {
              "icon": [
                {
                  "cdn": "ty2.a.kwimgs.com",
                  "url": "http://ty2.a.kwimgs.com/uhead/AB/2026/10/14/21/BMjAyNjEwMTQyMTEwNTRfMTQ4MDU2MjUz…"
                }
              ],
              "linkUrl": "kwai://search?keyword=%E8%82%96%E5%A4%A9%E8%B5%90&backRecommend=false&sessionId=…",
              "shapeType": 0,
              "url": [
                {
                  "cdn": "ty2.a.kwimgs.com",
                  "url": "http://ty2.a.kwimgs.com/uhead/AB/2026/10/14/21/BMjAyNjEwMTQyMTEwNTRfMTQ4MDU2MjUz…"
                }
              ]
            },
            "feedLogCtx": {
              "stExParams": null,
              "stidContainer": "InIxfDIwMDY0NTYxODg3NDA3Mzg3ODZ8VVNFUjoxNDgwNTYyNTM4fHsicGciOiJ1bmtub3cifXx7ImJp…"
            },
            "linkUrl": "kwai://search?keyword=%E8%82%96%E5%A4%A9%E8%B5%90&backRecommend=false&sessionId=…",
            "logInfo": {
              "authorid": "1480562538",
              "id": "1480562538",
              "params": {
                "hotValue": 10520593,
                "normalindex": "1",
                "recoReason": [
                  "作品更新"
                ]
              },
              "type": "USER"
            },
            "order": {
              "index": 1,
              "shapeType": 0
            },
            "pendant": {},
            "renderStrategyIcon": null,
            "rightView": {
              "icon": {
                "shapeType": 0
              },
              "isPrefix": 1,
              "text": {
                "content": "1052.1万"
              }
            }
          }
        ]
      }
    ],
    "dataType": 1,
    "moduleType": 13
  },
  "ussid": "MzAxXzBfMTc5MzY5MTM1NDk0MV9fODI1Nw"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `topList.data[].list[]` | The ranked entries on the board. Each entry is one Kuaishou user. |
| `topList.data[].list[].logInfo.id / topList.data[].list[].logInfo.authorid` | The Kuaishou user ID of the person. Both fields hold the same value in the sample. |
| `topList.data[].list[].logInfo.type` | The entry type. The sample shows `USER`. |
| `topList.data[].list[].logInfo.params.hotValue` | The numeric heat value for the person. Some entries do not include it. |
| `topList.data[].list[].logInfo.params.normalindex` | The position label on the board as a string. Values such as `2.1` appear on entries that have no `hotValue`. |
| `topList.data[].list[].logInfo.params.recoReason[]` | Text tags that give the reason the person is listed. The sample shows values like 作品更新 (work updated) and 近期搜索量飙升 (recent search volume surge). |
| `topList.data[].list[].order.index` | The numeric rank of the entry. It is absent on entries that carry an `order.icon` image instead. |
| `topList.data[].list[].rightView.text.content` | The heat value as display text, for example `1052.1万`. |
| `topList.data[].list[].avatar.icon[].url` | Avatar image URLs for the person, one per CDN host. |
| `topList.data[].list[].linkUrl` | A `kwai://search` deep link that opens a Kuaishou search for the person's name. The `keyword` query value holds the URL-encoded name. |

### Notes

- The request has no parameters. Send `{}` as the body.
- Entries with `normalindex` like `2.1` and no `hotValue` or `rightView` are listed under a rank and use an icon instead of a number in `order`.
- Use `logInfo.id` as the user ID input for related APIs such as [Kuaishou Single User Data (V2)](/apis/kuaishou/app/one-user-v2) or [Kuaishou User Video List (V2)](/apis/kuaishou/app/user-post-v2).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/hot-search-person.json`](../../../../catalog/models/kuaishou/app/hot-search-person.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/hot-search-person
