# TikTok Creators card API: pricing, parameters and code examples

`tiktok/ads/creators-card` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get creators card on TikTok. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/creators-card"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/creators-card', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/creators-card", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/creators-card", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/ads/creators-card` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cookie` | string |  | Custom Cookie string (optional)  |
| `tt_uids` | array |  | Creator ID list  |
| `creator_type` | integer |  | Creator type default `2` |
| `need_loader_list` | array |  | Data module IDs, empty for all  |

## Details

Returns a creator card for each TikTok creator ID you pass in `tt_uids`. The card holds pricing, audience distribution, and performance data for the creator. You can limit the data with `need_loader_list`.

### Use cases

- Check a creator's follower tier and engagement rate before you shortlist them for a campaign.
- Compare a creator's engagement rate with the benchmark value in `engagementRateBenchMark`.
- Read audience breakdowns by age, gender, region, and device brand to judge audience fit.
- Look up a creator's quoted starting rate in `esData.price` when planning a budget.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/creators-card" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tt_uids": ["6532037588893564929"], "creator_type": 1, "need_loader_list": [101, 102, 103, 104, 105, 106, 107, 125]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cookie` | string | No | Custom Cookie string (optional) |
| `creator_type` | integer | No | Creator type |
| `need_loader_list` | array | No | Data module IDs, empty for all |
| `tt_uids` | array | No | Creator ID list |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "baseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "creators": [
    {
      "aioCreatorID": "6532037588893564929",
      "contentLabels": [],
      "creatorProfile": {
        "price": {}
      },
      "creatorTTInfo": {},
      "creatorType": 2,
      "displayType": 2,
      "esData": {
        "appearOnSearchSetting": false,
        "price": {
          "currency": "",
          "isLowQuotationCreator": false,
          "recommendRate100k": "0",
          "startingRate100k": "0",
          "storeRegionCurrency": "",
          "storeRegionStartingRate100k": "0"
        },
        "status": 0
      },
      "isCarveOut": false,
      "priceIndex": 0,
      "statisticData": {
        "algo": {},
        "followerCountHistory": {},
        "followerDistriData": {
          "active": [],
          "age": [],
          "deviceBrand": [],
          "gender": [],
          "region": []
        },
        "latestDSUpdateTime": "0",
        "overallPerformance": {
          "avgSixSecondsViewsBenchMarkViews": 0,
          "avgSixSecondsViewsRate": 0,
          "avgSixSecondsViewsRateRank": 1,
          "engagementRate": 0,
          "engagementRateBenchMark": 0,
          "engagementRateRank": 1,
          "followerCount": 0,
          "followerTier": 0
        },
        "ttBasicInfo": {},
        "videoPerformance": {}
      },
      "ttUID": "0"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `baseResp.StatusCode / baseResp.StatusMessage` | Status of the call. `0` with an empty message means the request succeeded. |
| `creators[].aioCreatorID` | The creator ID that matches the value you sent in `tt_uids`. |
| `creators[].ttUID` | A second creator ID field. In this response it is `0`, so use `aioCreatorID` to match results to your input. |
| `creators[].creatorType / creators[].displayType` | Numeric creator type and display type codes for the card. |
| `creators[].esData.price.startingRate100k / creators[].esData.price.recommendRate100k` | Starting and recommended rate values as strings. They come with `currency` in the same object. |
| `creators[].esData.price.isLowQuotationCreator` | Boolean flag for creators marked as having a low quotation. |
| `creators[].statisticData.overallPerformance.engagementRate / creators[].statisticData.overallPerformance.engagementRateBenchMark` | The creator's engagement rate next to a benchmark value. `engagementRateRank` gives the rank. |
| `creators[].statisticData.overallPerformance.followerCount / creators[].statisticData.overallPerformance.followerTier` | Follower count and the tier number the creator falls into. |
| `creators[].statisticData.overallPerformance.avgSixSecondsViewsRate / creators[].statisticData.overallPerformance.avgSixSecondsViewsBenchMarkViews` | Average six-second view rate and its benchmark views value. |
| `creators[].statisticData.followerDistriData.age / gender / region / deviceBrand / active` | Lists that break down the follower audience by age, gender, region, device brand, and activity. |

### Notes

- Pass one or more creator IDs in `tt_uids`. You can get creator IDs (`creatorID`) from [TikTok Top contents list](/apis/tiktok/ads/top-contents-list).
- Leave `need_loader_list` empty to request all data modules. The sample request used `101` to `107` and `125`.
- Many objects and lists can come back empty, such as `ttBasicInfo`, `videoPerformance`, and the follower distribution lists. In this sample, the numeric performance values are `0`.
- The `creatorType` in the response was `2` even though the request sent `creator_type` as `1`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tiktok/ads/creators-card.json`](../../../../catalog/models/tiktok/ads/creators-card.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/creators-card
