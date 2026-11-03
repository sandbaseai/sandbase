# Kuaishou Shopping Top List API: pricing, parameters and code examples

`kuaishou/app/shopping-top-list` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns ranked shopping live streams and top product leaderboards from Kuaishou. Filter results by specific sub-tab identifiers or names.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/shopping-top-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/shopping-top-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/shopping-top-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/shopping-top-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/shopping-top-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `subTabId` | integer |  | 子标签ID/Sub tag ID default `0` |
| `subTabName` | string |  | 子标签名称/Sub tag name default `""` |

## Details

Returns the Kuaishou shopping leaderboard as a list of sub-tabs, such as hot streamers and best-selling products. Each sub-tab can hold a ranked list of live stream entries. The request takes an optional `subTabId` or `subTabName`, and an empty body works.

### Use cases

- Pull the ranked list of hot shopping streamers and store their author IDs for tracking.
- Collect the live stream IDs inside each `linkUrl` to build a list of streams currently ranked.
- Compare the heat values shown for each ranked streamer to see who leads the board.
- List the available sub-tabs and their IDs, then call again with one `subTabId` to focus on a single board.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/shopping-top-list" \
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
  "host-name": "public-bjzey-c97-kce-node51.idchb1az3.hb1.kwaidc.com",
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
                  "cdn": "tx2.a.yximgs.com",
                  "url": "http://tx2.a.yximgs.com/uhead/AB/2026/06/12/11/BMjAyNjA2MTIxMTQyNDBfNDAzMDgyMzAy…"
                }
              ],
              "linkUrl": "kwai://liveaggregatesquare?path=/rest/n/live/feed/common/slide/more&selectedLive…",
              "liveType": 1,
              "shapeType": 0,
              "url": [
                {
                  "cdn": "ty2.a.kwimgs.com",
                  "url": "http://ty2.a.kwimgs.com/uhead/AB/2026/06/12/11/BMjAyNjA2MTIxMTQyNDBfNDAzMDgyMzAy…"
                }
              ]
            },
            "feedLogCtx": {
              "stExParams": null,
              "stidContainer": "InAxfDIwMDY0NTA4MTY1MTIyMzY0MzR8VVNFUjo0MDMwODIzMDJ8eyJwZyI6Im1zZ3doIn18eyJiaXoi…"
            },
            "linkUrl": "kwai://liveaggregatesquare?path=/rest/n/live/feed/common/slide/more&selectedLive…",
            "logInfo": {
              "authorid": "403082302",
              "id": "403082302",
              "params": {
                "id": "15042128727",
                "normalindex": null,
                "type": "LIVE"
              },
              "type": "USER"
            },
            "pendant": {},
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
                    "cdn": "ty2.a.kwimgs.com",
                    "url": "https://ty2.a.kwimgs.com/udata/pkg/se-cdn/huomiao.png"
                  }
                ]
              },
              "isPrefix": 1,
              "text": {
                "content": "7182.2万"
              }
            },
            "signalParams": {
              "author_id": "403082302"
            }
          }
        ],
        "subTabId": 101,
        "subTabName": "热门主播"
      }
    ],
    "dataType": 1,
    "moduleType": 3
  },
  "ussid": "MzAxXzBfMTc5MzY5MTM2ODI0OV9fNDE3MQ"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `topList.data[]` | One sub-tab of the leaderboard. Each item holds a `subTabId`, a `subTabName` and, for some tabs, a `list` of entries. |
| `topList.data[].subTabId / topList.data[].subTabName` | ID and display name of the sub-tab. In this response `101` is `热门主播` (hot streamers) and `102` is `热销商品` (best-selling products). |
| `topList.data[].list[]` | Ranked entries inside a sub-tab, in the order returned. A sub-tab may have no `list`, as `102` does here. |
| `topList.data[].list[].logInfo.authorid / topList.data[].list[].signalParams.author_id` | Kuaishou ID of the streamer for this entry. |
| `topList.data[].list[].logInfo.params.id` | Numeric ID attached to the entry, with `type` set to `LIVE`. |
| `topList.data[].list[].linkUrl` | In-app `kwai://` deep link to the live stream square. It carries `selectedLiveStreamId` for this entry and a `liveStreamId` list of streams in the ranking. |
| `topList.data[].list[].avatar.icon[].url` | Avatar image URLs for the streamer, served from different CDN hosts. |
| `topList.data[].list[].rightView.text.content` | Text shown on the right of the entry, such as `7182.2万`. It appears next to a small icon and is likely a popularity count, but the response does not label it. |
| `result` | Status flag of the call. The value is `1` in this response. |

### Notes

- Call with an empty body to get every sub-tab. Then pass `subTabId` (for example `101`) or `subTabName` to filter.
- Read `subTabId` and `subTabName` from the first response to know which values to pass in later calls.
- Streamer IDs in `logInfo.authorid` are numeric strings. Use them as the input for other Kuaishou user APIs, such as [Kuaishou User Broadcast Details](/apis/kuaishou/app/user-live-info).
- For a general stream ranking, see [Kuaishou Stream Top List](/apis/kuaishou/app/live-top-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/shopping-top-list.json`](../../../../catalog/models/kuaishou/app/shopping-top-list.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/shopping-top-list
