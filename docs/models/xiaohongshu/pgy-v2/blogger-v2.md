# Xiaohongshu Pugongying Creator Search API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/blogger-v2` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.071429 per call · **Modes:** sync

Search Xiaohongshu Pugongying creators with campaign filters and sorting by followers, daily-note median reads or interactions, or quoted price. Use it to build a creator shortlist.

## Pricing

- **$0.071429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/blogger-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/blogger-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/blogger-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/blogger-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/blogger-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number. default `1` |
| `sort` | string |  | Creator search sorting. Values: FANS sorts by follower count descending; DEFAULT uses Pugongying intelligent ranking; READ_MEDIAN sorts by daily-note median reads descending; ENGAGEMENT_MEDIAN sorts by daily-note… one of: `DEFAULT`, `FANS`, `READ_MEDIAN`, `ENGAGEMENT_MEDIAN`, `PRICE_ASC`, `PRICE_DESC`; default `"FANS"` |
| `gender` | string |  | KOL's gender. one of: `ALL`, `MALE`, `FEMALE`; default `"ALL"` |
| `fansAge` | string |  | Target fans age group. one of: `ALL`, `LT_18`, `AGE_18_24`, `AGE_25_34`, `AGE_35_44`, `GT_44`; default `"ALL"` |
| `keyword` | string |  | Search keyword.  |
| `industry` | string |  | Pugongying industry preset for industry assistant style creator recommendations. one of: `BEAUTY_PERSONAL_CARE_BEAUTY`, `BEAUTY_PERSONAL_CARE_SKINCARE`, `BEAUTY_PERSONAL_CARE_PERSONAL_CARE`, `BEAUTY_PERSONAL_CARE_FRAGRANCE`, `FOOD_BEVERAGE_SNACKS`, `FOOD_BEVERAGE_DRINKS`, `FOOD_BEVERAGE_HEALTH_FOOD`, `FOOD_BEVERAGE_DAIRY`, `FOOD_BEVERAGE_ALCOHOL`, `FOOD_BEVERAGE_GRAINS_OIL`, `FOOD_BEVERAGE_CROSS_BORDER_FOOD`, `FOOD_BEVERAGE_FRESH_FOOD` … |
| `location` | string |  | Creator profile location filter. Pass Pugongying location labels separated by English or Chinese commas. Country, China province or region, city-level paths, and district/county-level paths are supported. China…  |
| `noteType` | string |  | Note type filter. Values: ALL=all note types, PHOTO_TEXT=mainly photo-text notes, VIDEO=mainly video notes. one of: `ALL`, `PHOTO_TEXT`, `VIDEO`; default `"ALL"` |
| `fansNumUp` | boolean |  | Whether to exclude bloggers whose fan count is dropping.  |
| `notePrice` | string |  | Photo-text cooperation quote range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound.  |
| `tradeType` | string |  | Recent cooperation industry filter from Pugongying.  |
| `avgAgmv90d` | string |  | Average live sales amount range. Pass two comma-separated numeric bounds.  |
| `contentTag` | string |  | Content category filter. Pass first-level or second-level category labels from Pugongying, separated by commas. Available values: - 美妆: 整体妆容, 唇妆, 眼妆, 美甲, 底妆, 美妆合集, 香水, 美妆其他 - 护肤: 面部保养, 面部清洁, 护肤合集, 护肤其他 - 个人护理: 头发产品,…  |
| `fansGender` | string |  | Target fans gender. one of: `ALL`, `MALE_HIGH`, `FE_MALE_HIGH`; default `"ALL"` |
| `searchType` | string |  | Search criteria type. one of: `NICKNAME`, `NOTE`; default `"NICKNAME"` |
| `videoPrice` | string |  | Video cooperation quote range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound.  |
| `featureTags` | string |  | Good-at content tag filter. Pass label values separated by commas.  |
| `kliveCnt30d` | string |  | Live count in the last 30 days range. Pass two comma-separated numeric bounds.  |
| `mCpuvNum30d` | string |  | Cooperation note outer-store median range. Pass two comma-separated numeric bounds.  |
| `similarWord` | string |  | Similar creator keyword shown by Pugongying. `similarUserId` and `similarWord` must be provided together.  |
| `fansLocation` | string |  | Follower audience location filter. Pass Pugongying follower-region labels separated by English or Chinese commas. Country, China province, and city-level paths are supported; district/county-level paths are not…  |
| `marketTarget` | string |  | Marketing target filter. Pass one Pugongying marketing target value. Available values: - estimateAllCpm: Exposure - exposure performance - cost - mAccumImpNum: Exposure - exposure performance - scale - readCost:…  |
| `personalTags` | string |  | Blogger persona tag filter. Pass one or more Pugongying persona labels separated by English or Chinese commas. Available values: - 妈妈 - 萌娃 - 爸爸 - 奶奶 - 情侣 - 夫妻 - 家庭 - 闺蜜 - 兄弟 - 备孕中 - 孕期中 - 12岁以上 - 传统行业 - 互联网 - 教育科研 -…  |
| `readMidNor30` | string |  | Daily note read median range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound.  |
| `audienceGroup` | string |  | Audience target filter. Pass Pugongying audience group IDs (`dmpGroupId`) separated by English or Chinese commas. These IDs are dynamic and account-specific, so there is no fixed global value list. Use the audience…  |
| `interMidNor30` | string |  | Daily note interaction median range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound.  |
| `readMidCoop30` | string |  | Cooperation note read median range. Pass two comma-separated numeric bounds.  |
| `similarUserId` | string |  | Similar creator user ID. `similarUserId` and `similarWord` must be provided together.  |
| `interMidCoop30` | string |  | Cooperation note interaction median range. Pass two comma-separated numeric bounds.  |
| `estimateCpuv30d` | string |  | Estimated outer-store visit unit price range. Pass two comma-separated numeric bounds.  |
| `fansNumberLower` | integer |  | Minimum number of fans.  |
| `fansNumberUpper` | integer |  | Maximum number of fans.  |
| `avgLiveViewerNum` | string |  | Average live viewer count range. Pass two comma-separated numeric bounds.  |
| `estimateVideoCpm` | string |  | Estimated video CPM range. Pass two comma-separated numeric bounds.  |
| `excludeLowActive` | boolean |  | Whether to exclude low-activity bloggers.  |
| `fansChildAgeInfo` | string |  | Mother-and-baby audience stage filter. Pass Pugongying labels or numeric codes separated by English or Chinese commas. Available values: - 1: 备孕 - 2: 0-6月 - 3: 7-12月 - 4: 1-3岁 - 5: 4-6岁 - 6: 7-12岁 - 7: 孕早期 - 8: 孕晚期  |
| `progressOrderCnt` | string |  | Current cooperation order count range. Pass two comma-separated numeric bounds.  |
| `top20CrowdsLabel` | string |  | Top-20 audience filter. Pass top-level or child audience labels separated by commas; child labels are converted to Pugongying request values.  |
| `contentSceneLabel` | string |  | Content scene label filter. Pass full Pugongying note category scene label paths separated by English or Chinese commas. Available values: - 汽车 理性决策 选车攻略 政策 - 汽车 理性决策 选车攻略 购车顾虑 - 汽车 理性决策 选车攻略 配置 - 汽车 理性决策 选车攻略 能源类型优势对比…  |
| `contentThemeLabel` | string |  | Content theme filter. Pass Pugongying value IDs or label values separated by commas; labels are converted to value IDs.  |
| `estimatePictureCpm` | string |  | Estimated photo-text CPM range. Pass two comma-separated numeric bounds.  |
| `tradeReportBrandIds` | string |  | Recent cooperation brand IDs, separated by English or Chinese commas.  |
| `estimatePicReadPrice` | string |  | Estimated photo-text read unit price range. Pass two comma-separated numeric bounds.  |
| `thousandLikePercent30` | string |  | Thousand-like note ratio range. Pass fractional ratios such as 0.4,null or percentage values such as 40,null.  |
| `estimateVideoReadPrice` | string |  | Estimated video read unit price range. Pass two comma-separated numeric bounds.  |
| `inviteReply48hNumRatio` | string |  | 48-hour invite reply ratio range. Pass fractional ratios such as 0.9,0.95 or percentage values such as 90,95.  |
| `accumCoopImpMedinNum30d` | string |  | Cooperation note exposure median range. Pass two comma-separated numeric bounds.  |
| `estimateVideoEngageCost` | string |  | Estimated video engagement unit price range. Pass two comma-separated numeric bounds.  |
| `accumCommonImpMedinNum30d` | string |  | Daily note exposure median range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound.  |
| `estimatePictureEngageCost` | string |  | Estimated photo-text engagement unit price range. Pass two comma-separated numeric bounds.  |
| `excludeTradeReportBrandIds` | boolean |  | Whether to exclude creators who cooperated with the selected recent cooperation brands.  |
| `industrySpecificCrowdsMotorDom` | string |  | Industry-specific portrait filter. Pass Pugongying portrait value IDs or label values separated by commas.  |

## Details

Returns a page of Xiaohongshu Pugongying creators that match a keyword and filters. Each creator row carries follower count, estimated ad cost metrics, content tags and note counts. All inputs are optional, and an empty request returns the default list sorted by followers.

### Use cases

- Build a shortlist of fitness or skincare creators within a follower range for a campaign.
- Rank creators by estimated cost per thousand views to find cheaper picks for picture or video notes.
- Filter by audience age, audience gender or creator location to match a target buyer group.
- Compare creators by 30-day follower growth and follower activity before outreach.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/blogger-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `accumCommonImpMedinNum30d` | string | No | Daily note exposure median range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound. |
| `accumCoopImpMedinNum30d` | string | No | Cooperation note exposure median range. Pass two comma-separated numeric bounds. |
| `audienceGroup` | string | No | Audience target filter. Pass Pugongying audience group IDs (`dmpGroupId`) separated by English or Chinese commas. These IDs are dynamic and account-specific, so there is no fixed global value list. Use the audience group |
| `avgAgmv90d` | string | No | Average live sales amount range. Pass two comma-separated numeric bounds. |
| `avgLiveViewerNum` | string | No | Average live viewer count range. Pass two comma-separated numeric bounds. |
| `contentSceneLabel` | string | No | Content scene label filter. Pass full Pugongying note category scene label paths separated by English or Chinese commas. Available values: - 汽车 理性决策 选车攻略 政策 - 汽车 理性决策 选车攻略 购车顾虑 - 汽车 理性决策 选车攻略 配置 - 汽车 理性决策 选车攻略 能源类型优势对比 - |
| `contentTag` | string | No | Content category filter. Pass first-level or second-level category labels from Pugongying, separated by commas. Available values: - 美妆: 整体妆容, 唇妆, 眼妆, 美甲, 底妆, 美妆合集, 香水, 美妆其他 - 护肤: 面部保养, 面部清洁, 护肤合集, 护肤其他 - 个人护理: 头发产品, 身体护理 |
| `contentThemeLabel` | string | No | Content theme filter. Pass Pugongying value IDs or label values separated by commas; labels are converted to value IDs. |
| `estimateCpuv30d` | string | No | Estimated outer-store visit unit price range. Pass two comma-separated numeric bounds. |
| `estimatePicReadPrice` | string | No | Estimated photo-text read unit price range. Pass two comma-separated numeric bounds. |
| `estimatePictureCpm` | string | No | Estimated photo-text CPM range. Pass two comma-separated numeric bounds. |
| `estimatePictureEngageCost` | string | No | Estimated photo-text engagement unit price range. Pass two comma-separated numeric bounds. |
| `estimateVideoCpm` | string | No | Estimated video CPM range. Pass two comma-separated numeric bounds. |
| `estimateVideoEngageCost` | string | No | Estimated video engagement unit price range. Pass two comma-separated numeric bounds. |
| `estimateVideoReadPrice` | string | No | Estimated video read unit price range. Pass two comma-separated numeric bounds. |
| `excludeLowActive` | boolean | No | Whether to exclude low-activity bloggers. |
| `excludeTradeReportBrandIds` | boolean | No | Whether to exclude creators who cooperated with the selected recent cooperation brands. |
| `fansAge` | string | No | Target fans age group. |
| `fansChildAgeInfo` | string | No | Mother-and-baby audience stage filter. Pass Pugongying labels or numeric codes separated by English or Chinese commas. Available values: - 1: 备孕 - 2: 0-6月 - 3: 7-12月 - 4: 1-3岁 - 5: 4-6岁 - 6: 7-12岁 - 7: 孕早期 - 8: 孕晚期 |
| `fansGender` | string | No | Target fans gender. |
| `fansLocation` | string | No | Follower audience location filter. Pass Pugongying follower-region labels separated by English or Chinese commas. Country, China province, and city-level paths are supported; district/county-level paths are not accepted. |
| `fansNumUp` | boolean | No | Whether to exclude bloggers whose fan count is dropping. |
| `fansNumberLower` | integer | No | Minimum number of fans. |
| `fansNumberUpper` | integer | No | Maximum number of fans. |
| `featureTags` | string | No | Good-at content tag filter. Pass label values separated by commas. |
| `gender` | string | No | KOL's gender. |
| `industry` | string | No | Pugongying industry preset for industry assistant style creator recommendations. |
| `industrySpecificCrowdsMotorDom` | string | No | Industry-specific portrait filter. Pass Pugongying portrait value IDs or label values separated by commas. |
| `interMidCoop30` | string | No | Cooperation note interaction median range. Pass two comma-separated numeric bounds. |
| `interMidNor30` | string | No | Daily note interaction median range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound. |
| `inviteReply48hNumRatio` | string | No | 48-hour invite reply ratio range. Pass fractional ratios such as 0.9,0.95 or percentage values such as 90,95. |
| `keyword` | string | No | Search keyword. |
| `kliveCnt30d` | string | No | Live count in the last 30 days range. Pass two comma-separated numeric bounds. |
| `location` | string | No | Creator profile location filter. Pass Pugongying location labels separated by English or Chinese commas. Country, China province or region, city-level paths, and district/county-level paths are supported. China province  |
| `mCpuvNum30d` | string | No | Cooperation note outer-store median range. Pass two comma-separated numeric bounds. |
| `marketTarget` | string | No | Marketing target filter. Pass one Pugongying marketing target value. Available values: - estimateAllCpm: Exposure - exposure performance - cost - mAccumImpNum: Exposure - exposure performance - scale - readCost: Exposure |
| `notePrice` | string | No | Photo-text cooperation quote range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound. |
| `noteType` | string | No | Note type filter. Values: ALL=all note types, PHOTO_TEXT=mainly photo-text notes, VIDEO=mainly video notes. |
| `page` | integer | No | Page number. |
| `personalTags` | string | No | Blogger persona tag filter. Pass one or more Pugongying persona labels separated by English or Chinese commas. Available values: - 妈妈 - 萌娃 - 爸爸 - 奶奶 - 情侣 - 夫妻 - 家庭 - 闺蜜 - 兄弟 - 备孕中 - 孕期中 - 12岁以上 - 传统行业 - 互联网 - 教育科研 - 金融法律 |
| `progressOrderCnt` | string | No | Current cooperation order count range. Pass two comma-separated numeric bounds. |
| `readMidCoop30` | string | No | Cooperation note read median range. Pass two comma-separated numeric bounds. |
| `readMidNor30` | string | No | Daily note read median range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound. |
| `searchType` | string | No | Search criteria type. |
| `similarUserId` | string | No | Similar creator user ID. `similarUserId` and `similarWord` must be provided together. |
| `similarWord` | string | No | Similar creator keyword shown by Pugongying. `similarUserId` and `similarWord` must be provided together. |
| `sort` | string | No | Creator search sorting. Values: FANS sorts by follower count descending; DEFAULT uses Pugongying intelligent ranking; READ_MEDIAN sorts by daily-note median reads descending; ENGAGEMENT_MEDIAN sorts by daily-note median  |
| `thousandLikePercent30` | string | No | Thousand-like note ratio range. Pass fractional ratios such as 0.4,null or percentage values such as 40,null. |
| `top20CrowdsLabel` | string | No | Top-20 audience filter. Pass top-level or child audience labels separated by commas; child labels are converted to Pugongying request values. |
| `tradeReportBrandIds` | string | No | Recent cooperation brand IDs, separated by English or Chinese commas. |
| `tradeType` | string | No | Recent cooperation industry filter from Pugongying. |
| `videoPrice` | string | No | Video cooperation quote range. Pass two comma-separated numeric bounds; use -1 or null for an open upper bound. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "highlightWords": [],
  "kols": [
    {
      "accumCommonImpMedinNum30d": 7498187,
      "accumCoopImpMedinNum30d": 10662619,
      "accumPicCommonImpMedinNum30d": 7498187,
      "accumVideoCommonImpMedinNum30d": 0,
      "activityList": [
        "6adb6413e4b078c833452df1"
      ],
      "algoRecommendReasons": null,
      "authorityList": null,
      "avgAgmv90d": 0.0,
      "avgLiveViewerNum": 0.0,
      "businessNoteCount": 181,
      "buyerType": 2,
      "classifyCode": 1
    }
  ],
  "redirect2NickSearch": false,
  "resultType": 2,
  "total": 5000,
  "trackId": "kolSearch_00fbc9950e0d451ba597c36cafd6b555"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `kols[]` | One creator result. The list holds the creators on the requested page. |
| `kols[].fansNum` | Follower count of the creator. Results sorted by `FANS` are ordered by this value. |
| `kols[].fans30GrowthRate` | Follower growth rate over 30 days, as shown in the response. Negative values mean the creator lost followers. |
| `kols[].fansActiveIn28dLv / kols[].fansEngageNum30dLv` | Follower activity level over 28 days and follower engagement level over 30 days. The key names show the time windows. |
| `kols[].estimatePictureCpm / kols[].estimateVideoCpm` | Estimated cost per thousand views for picture notes and for video notes. |
| `kols[].estimatePictureEngageCost / kols[].estimateVideoEngageCost` | Estimated cost per engagement for picture notes and for video notes. |
| `kols[].estimatePictureCpmCompare / kols[].estimateVideoCpmCompare` | Comparison values paired with the CPM estimates. Use them to see how a creator ranks against the CPM figure. |
| `kols[].accumCommonImpMedinNum30d / kols[].accumCoopImpMedinNum30d` | Median impression figures over 30 days for regular notes and for cooperation notes. |
| `kols[].businessNoteCount` | Number of business notes recorded for the creator. |
| `kols[].contentTags[].taxonomy1Tag / kols[].contentTags[].taxonomy2Tags[]` | First-level content category and its second-level categories for the creator. The value can be `null`. |
| `total` | Total number of matching creators reported for the search. |

### Notes

- Send `page` to move through results. Keep the same filters and `sort` on each call.
- `contentTag` values use the first-level and second-level labels listed in the parameter description. Separate several values with commas.
- To go deeper on one creator, call [Xiaohongshu Pugongying Creator Profile](/apis/xiaohongshu/pgy-v2/blogger-user-id) or [Xiaohongshu Pugongying Creator Core Metrics](/apis/xiaohongshu/pgy-v2/data-core-data).
- Use `trackId` from the response to identify a search.

### Pricing

$0.071429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/blogger-v2.json`](../../../../catalog/models/xiaohongshu/pgy-v2/blogger-v2.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/blogger-v2
