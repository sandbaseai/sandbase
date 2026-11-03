# Kuaishou Stream Top List API: pricing, parameters and code examples

`kuaishou/app/live-top-list` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns ranking information for trending streams on Kuaishou. Accepts optional tab parameters to filter leaderboards by category.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/live-top-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/live-top-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/live-top-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/live-top-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/live-top-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `subTabId` | integer |  | 子标签ID/Sub tag ID default `0` |
| `subTabName` | string |  | 子标签名称/Sub tag name default `""` |

## Details

Returns the ranking of trending live streams on Kuaishou, grouped by leaderboard tab. The request has no required input. You can pass `subTabId` or `subTabName` to pick a tab.

### Use cases

- Track which streamers hold the top spots on the overall live ranking.
- Compare `hotValue` scores across streamers to see how close the ranks are.
- Collect streamer IDs from the ranking and feed them into user lookups.
- List the available leaderboard tabs and their IDs to build a category filter.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/live-top-list" \
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
  "host-name": "public-bjzey-c34-kce-node3936.idchb1az3.hb1.kwaidc.com",
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
                  "url": "http://tx2.a.yximgs.com/uhead/AB/2022/02/25/18/BMjAyMjAyMjUxODM5MjhfMTM4Njc2MTMy…"
                }
              ],
              "linkUrl": "kwai://liveaggregatesquare?path=/rest/n/live/feed/common/slide/more&selectedLive…",
              "liveType": 1,
              "shapeType": 0,
              "url": [
                {
                  "cdn": "ty2.a.kwimgs.com",
                  "url": "http://ty2.a.kwimgs.com/uhead/AB/2022/02/25/18/BMjAyMjAyMjUxODM5MjhfMTM4Njc2MTMy…"
                }
              ]
            },
            "feedLogCtx": {
              "stExParams": null,
              "stidContainer": "InIxfDIwMDY0NTYxNzMwMDE3NDA3NzB8VVNFUjoxMzg2NzYxMzIxfHsicGciOiJ1bmtub3cifXx7ImJp…"
            },
            "linkUrl": "kwai://liveaggregatesquare?path=/rest/n/live/feed/common/slide/more&selectedLive…",
            "logInfo": {
              "authorid": "1386761321",
              "id": "1386761321",
              "params": {
                "hotValue": 142786,
                "id": "15042369132",
                "normalindex": "1",
                "type": "LIVE"
              },
              "type": "USER"
            },
            "order": {
              "index": 1,
              "shapeType": 0
            },
            "renderStrategyIcon": null,
            "rightView": {
              "icon": {
                "shapeType": 0
              },
              "text": {
                "content": "14.3万人气"
              }
            },
            "signalParams": {
              "author_id": 1386761321
            }
          }
        ],
        "subTabId": 100,
        "subTabName": "总榜"
      }
    ],
    "dataType": 2,
    "moduleType": 14
  },
  "ussid": "MzAxXzBfMTc5MzY5MTM1MTcwMF9fOTY5OQ"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `topList.data[].subTabId / topList.data[].subTabName` | ID and name of a leaderboard tab. The sample response includes `100` (总榜, the overall board), `102` (音乐, music) and `107` (舞蹈, dance). |
| `topList.data[].list[]` | Ranked stream entries for that tab. In the sample response only the first tab, `100`, carries a `list`. |
| `topList.data[].list[].order.index` | Rank position of the entry, starting at `1`. |
| `topList.data[].list[].logInfo.params.hotValue` | Numeric popularity score used for the ranking, such as `142786` for the top entry. |
| `topList.data[].list[].rightView.text.content` | Popularity label shown in the app, such as `14.3万人气`. It is a display version of the score. |
| `topList.data[].list[].logInfo.authorid / topList.data[].list[].signalParams.author_id` | Streamer's user ID. The first is a string and the second is a number. |
| `topList.data[].list[].logInfo.params.id` | ID of the entry's live item. Its `type` is `LIVE`. |
| `topList.data[].list[].avatar.icon[].url` | Streamer avatar image URLs, one per CDN host. |
| `topList.data[].list[].linkUrl` | In-app `kwai://` deep link that opens the live stream. It contains `selectedLiveStreamId` and a comma-separated `liveStreamId` list. |

### Notes

- Call once with `{}` to see the tab list. Then pass a returned `subTabId` or `subTabName` to request that tab.
- Tabs other than the overall board may come back without a `list` in the sample response, so check that the key exists.
- Use the streamer ID from `logInfo.authorid` with [Kuaishou User Broadcast Details](/apis/kuaishou/app/user-live-info) or [Kuaishou Single User Data (V2)](/apis/kuaishou/app/one-user-v2) to get more about a streamer.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/live-top-list.json`](../../../../catalog/models/kuaishou/app/live-top-list.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/live-top-list
