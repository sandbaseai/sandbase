# Douyin Xingtu Creator Search API: pricing, parameters and code examples

`douyin/xingtu-v3/gsearch-search-for-author-square` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.071429 per call · **Modes:** sync

Search Douyin Creator Marketplace (Xingtu) creators by keyword and structured filters for audience, pricing, content, performance, and campaign fit. Use it to build and compare campaign shortlists.

## Pricing

- **$0.071429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/gsearch-search-for-author-square"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/gsearch-search-for-author-square', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/gsearch-search-for-author-square", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/gsearch-search-for-author-square", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/gsearch-search-for-author-square` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `sort` | string |  | Creator search sorting. Values: FANS sorts by follower count descending, DEFAULT uses Xingtu score ranking. one of: `DEFAULT`, `FANS`; default `"FANS"` |
| `gender` | string |  | Creator gender. Available values: MALE/1/男性, FEMALE/2/女性. one of: `MALE`, `FEMALE` |
| `keyword` | string |  | Search keyword.  |
| `industry` | string |  | Recommended industry filter. Pass enum name, numeric industry ID, or Chinese industry label. Available values: - ALL/0/不限; - 1901: 3C及电器; - 1938: 购物; - 1903: 食品饮料; - 1904: 服装配饰; - 1905: 医药健康; - 1936: 医疗机构; - 1909:… one of: `ALL`, `ELECTRONICS_AND_APPLIANCES`, `SHOPPING`, `FOOD_AND_BEVERAGE`, `CLOTHING_AND_ACCESSORIES`, `HEALTHCARE_AND_MEDICAL`, `MEDICAL_INSTITUTIONS`, `HOME_AND_BUILDING_MATERIALS`, `LOCAL_SERVICES`, `BUSINESS_SERVICES`, `CULTURE_SPORTS_ENTERTAINMENT`, `BEAUTY_SERVICES` …; default `"ALL"` |
| `location` | string |  | Creator location filter. Pass Chinese province or city names separated by commas. Available province values include: 北京市, 天津市, 河北省, 山西省, 内蒙古自治区, 辽宁省, 吉林省, 黑龙江省, 上海市, 江苏省, 浙江省, 安徽省, 福建省, 江西省, 山东省, 河南省, 湖北省, 湖南省, 广东省,…  |
| `fansImage` | string |  | Fan profile filter from Xingtu Fan Image. Pass one or more shortcut values separated by commas. Only the values listed below are accepted. For gender thresholds, pass at most one GENDER_MALE_* value and at most one…  |
| `authorList` | string |  | Activity-curated creator list under Xingtu Topic Recommendations. Select at most one value. Pass an enum name, numeric list ID, or Chinese label. Available values:… one of: `SHORT_LIVE_ENTERTAINMENT_CREATORS`, `SHORT_DRAMA_ACTORS`, `WECHAT_QUICK_CONNECT_CREATORS`, `AI_STAR_PLAN_CREATORS`, `COMMERCE_ADVANTAGE_CREATORS`, `HIGH_VALUE_CREATORS`, `SEEDING_ADVANTAGE_CREATORS`, `BASKETBALL_CREATORS`, `PREMIUM_CONTENT_MEDIA`, `TREND_SETTING_MEDIA`, `FACTORY_TRACEABILITY_MEDIA`, `RUNNING_CREATORS` … |
| `contentTag` | string |  | Creator category filter. Pass Xingtu first-level or second-level category labels separated by commas. Available values: - 美妆: 美妆教程, 妆容展示, 护肤保养, 美妆测评种草; - 时尚: 穿搭, 街拍, 造型, 时尚媒体; - 萌宠: 日常宠物, 特别宠物, 宠物周边; - 测评: 美妆测评,…  |
| `personaTag` | string |  | Creator persona or background labels. Pass Xingtu labels or numeric tag IDs separated by commas. Available values: - 人群属性: Z世代, 新锐白领, 精致妈妈, 都市蓝领, 资深中产, 小镇青年, 小镇中老年, 都市银发; - 社会身份: 音乐人, 非遗传人, 画家; - 主要出镜人物: 海外华人, 外国友人,…  |
| `searchType` | string |  | Search criteria type. one of: `NICKNAME`, `CONTENT`; default `"NICKNAME"` |
| `isSuperstar` | boolean |  | Whether to filter celebrity creators. default `false` |
| `tonalityTag` | string |  | Creator tonality labels. Pass Xingtu first-level or second-level tonality labels separated by commas. Available values: - 身份/爱好: 马术, 高尔夫, 橄榄球, 时尚爱好者, 企业高管, 汽车爱好者, 学者专家, 古玩收藏; - 精致达人: 设计师, 高阶潮玩, 职业模特, 造型顾问, 独立设计师,…  |
| `contentTheme` | string |  | Content theme filter. Pass Xingtu second-level content theme labels separated by commas. Only labels listed after each colon are accepted; category headings before the colons are descriptive only and must not be…  |
| `kolPriceType` | string |  | Creator quote type from the current Xingtu marketplace options. one of: `PRODUCT_PLACEMENT_VIDEO`, `CUSTOM_VIDEO`, `CUSTOM_SHORT_DRAMA_EPISODE`, `NATURAL_PLAY_CPM`, `SHORT_LIVE_SEEDING_VIDEO`, `SHORT_LIVE_WARMUP_VIDEO`, `CELEBRITY_SHORT_LIVE_SEEDING`, `CELEBRITY_SHORT_LIVE_WARMUP`, `CELEBRITY_VIDEO`, `COLLECTION_VIDEO`, `DOUYIN_SHORT_VIDEO_CO_CREATION_MAIN_CREATOR`, `DOUYIN_SHORT_VIDEO_CO_CREATION_PARTICIPANT` |
| `audienceImage` | string |  | Audience profile filter from Xingtu Audience Image. Pass one or more shortcut values separated by commas. Only the values listed below are accepted. For gender thresholds, pass at most one GENDER_MALE_* value and at…  |
| `followerRange` | string |  | Raw follower count range in min-max format. Example: 1000-2000 means 1,000 to 2,000 followers; 5000000-10000000 means 5 million to 10 million followers.  |
| `kolPriceRange` | string |  | Creator quote range in min-max format (e.g., 10000-50000). Requires kolPriceType; omit kolPriceRange to use the full range for the selected quote type.  |
| `viralRateRange` | string |  | Viral content rate range in decimal min-max format. Page presets include 0-0.1, 0.1-0.25, 0.25-0.5, 0.5-0.99, and 0.99 or above. For open-ended presets, pass a high upper bound such as 0.99-1. Example: 0.1-0.25.  |
| `isCuratedAuthor` | boolean |  | Whether to include only Xingtu curated creators under Topic Recommendations. default `false` |
| `marketingTarget` | string |  | Marketing goal. Available values: BRAND_EXPOSURE/1/品牌曝光, CIRCLE_SEEDING/2/破圈种草, ACTION_CONVERSION/3/行动转化. one of: `BRAND_EXPOSURE`, `CIRCLE_SEEDING`, `ACTION_CONVERSION` |
| `expectedCpeRange` | string |  | Expected CPE range in min-max format. Example values matching Xingtu packs: 0-1, 0-2, 0-3, 0-5, 0-10, 10-1000000.  |
| `expectedCpmRange` | string |  | Expected CPM range in min-max format. Example values matching Xingtu packs: 0-10, 0-20, 0-30, 0-50, 0-100, 100-1000000.  |
| `expectedPlayRange` | string |  | Expected play count range. Use raw counts in min-max format. Page presets include 10000000 or above, 5000000-10000000, 3000000-5000000, 1000000-3000000, 100000-1000000, and 0-100000. For open-ended presets, pass a high…  |
| `progressTaskRange` | string |  | In-progress task count range. Place a colon between the day count and the min-max range; omit either bound for an open range. Example: 30:8-  |
| `connectedUserRange` | string |  | Connected user count range. Pass raw user counts in min-max format. Example: 1000000-3000000  |
| `completionRateRange` | string |  | Completion rate range in decimal min-max format. Example values: 0.1-1 for 10% or above, 0.2-1 for 20% or above.  |
| `interactionRateRange` | string |  | Interaction rate range in decimal min-max format. Example values: 0.01-1 for 1% or above, 0.02-1 for 2% or above.  |

## Details

Returns a page of Douyin Creator Marketplace (Xingtu) creators that match a keyword and optional filters. Each creator comes with a `star_id`, profile attributes, top videos with play counts, and quote prices. All inputs are optional, so an empty request returns the first page of creators.

### Use cases

- Build a shortlist of beauty creators for a campaign by filtering on `keyword`, `industry` and `followerRange`.
- Compare quote prices across many creators by reading `task_infos[].price_infos[].price`.
- Collect `star_id` values to feed into creator profile and audience APIs for deeper vetting.
- Rank creators by top video play counts to spot accounts with strong recent reach.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/gsearch-search-for-author-square" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `audienceImage` | string | No | Audience profile filter from Xingtu Audience Image. Pass one or more shortcut values separated by commas. Only the values listed below are accepted. For gender thresholds, pass at most one GENDER_MALE_* value and at most |
| `authorList` | string | No | Activity-curated creator list under Xingtu Topic Recommendations. Select at most one value. Pass an enum name, numeric list ID, or Chinese label. Available values: SHORT_LIVE_ENTERTAINMENT_CREATORS/7540478044453486642/短直 |
| `completionRateRange` | string | No | Completion rate range in decimal min-max format. Example values: 0.1-1 for 10% or above, 0.2-1 for 20% or above. |
| `connectedUserRange` | string | No | Connected user count range. Pass raw user counts in min-max format. Example: 1000000-3000000 |
| `contentTag` | string | No | Creator category filter. Pass Xingtu first-level or second-level category labels separated by commas. Available values: - 美妆: 美妆教程, 妆容展示, 护肤保养, 美妆测评种草; - 时尚: 穿搭, 街拍, 造型, 时尚媒体; - 萌宠: 日常宠物, 特别宠物, 宠物周边; - 测评: 美妆测评, 3C数码测评,  |
| `contentTheme` | string | No | Content theme filter. Pass Xingtu second-level content theme labels separated by commas. Only labels listed after each colon are accepted; category headings before the colons are descriptive only and must not be passed.  |
| `expectedCpeRange` | string | No | Expected CPE range in min-max format. Example values matching Xingtu packs: 0-1, 0-2, 0-3, 0-5, 0-10, 10-1000000. |
| `expectedCpmRange` | string | No | Expected CPM range in min-max format. Example values matching Xingtu packs: 0-10, 0-20, 0-30, 0-50, 0-100, 100-1000000. |
| `expectedPlayRange` | string | No | Expected play count range. Use raw counts in min-max format. Page presets include 10000000 or above, 5000000-10000000, 3000000-5000000, 1000000-3000000, 100000-1000000, and 0-100000. For open-ended presets, pass a high u |
| `fansImage` | string | No | Fan profile filter from Xingtu Fan Image. Pass one or more shortcut values separated by commas. Only the values listed below are accepted. For gender thresholds, pass at most one GENDER_MALE_* value and at most one GENDE |
| `followerRange` | string | No | Raw follower count range in min-max format. Example: 1000-2000 means 1,000 to 2,000 followers; 5000000-10000000 means 5 million to 10 million followers. |
| `gender` | string | No | Creator gender. Available values: MALE/1/男性, FEMALE/2/女性. |
| `industry` | string | No | Recommended industry filter. Pass enum name, numeric industry ID, or Chinese industry label. Available values: - ALL/0/不限; - 1901: 3C及电器; - 1938: 购物; - 1903: 食品饮料; - 1904: 服装配饰; - 1905: 医药健康; - 1936: 医疗机构; - 1909: 家居建材;  |
| `interactionRateRange` | string | No | Interaction rate range in decimal min-max format. Example values: 0.01-1 for 1% or above, 0.02-1 for 2% or above. |
| `isCuratedAuthor` | boolean | No | Whether to include only Xingtu curated creators under Topic Recommendations. |
| `isSuperstar` | boolean | No | Whether to filter celebrity creators. |
| `keyword` | string | No | Search keyword. |
| `kolPriceRange` | string | No | Creator quote range in min-max format (e.g., 10000-50000). Requires kolPriceType; omit kolPriceRange to use the full range for the selected quote type. |
| `kolPriceType` | string | No | Creator quote type from the current Xingtu marketplace options. |
| `location` | string | No | Creator location filter. Pass Chinese province or city names separated by commas. Available province values include: 北京市, 天津市, 河北省, 山西省, 内蒙古自治区, 辽宁省, 吉林省, 黑龙江省, 上海市, 江苏省, 浙江省, 安徽省, 福建省, 江西省, 山东省, 河南省, 湖北省, 湖南省, 广东省, 广西壮族 |
| `marketingTarget` | string | No | Marketing goal. Available values: BRAND_EXPOSURE/1/品牌曝光, CIRCLE_SEEDING/2/破圈种草, ACTION_CONVERSION/3/行动转化. |
| `page` | integer | No | Page number for pagination. |
| `personaTag` | string | No | Creator persona or background labels. Pass Xingtu labels or numeric tag IDs separated by commas. Available values: - 人群属性: Z世代, 新锐白领, 精致妈妈, 都市蓝领, 资深中产, 小镇青年, 小镇中老年, 都市银发; - 社会身份: 音乐人, 非遗传人, 画家; - 主要出镜人物: 海外华人, 外国友人, 情侣,  |
| `progressTaskRange` | string | No | In-progress task count range. Place a colon between the day count and the min-max range; omit either bound for an open range. Example: 30:8- |
| `searchType` | string | No | Search criteria type. |
| `sort` | string | No | Creator search sorting. Values: FANS sorts by follower count descending, DEFAULT uses Xingtu score ranking. |
| `tonalityTag` | string | No | Creator tonality labels. Pass Xingtu first-level or second-level tonality labels separated by commas. Available values: - 身份/爱好: 马术, 高尔夫, 橄榄球, 时尚爱好者, 企业高管, 汽车爱好者, 学者专家, 古玩收藏; - 精致达人: 设计师, 高阶潮玩, 职业模特, 造型顾问, 独立设计师, 美术/画廊/展 |
| `viralRateRange` | string | No | Viral content rate range in decimal min-max format. Page presets include 0-0.1, 0.1-0.25, 0.25-0.5, 0.5-0.99, and 0.99 or above. For open-ended presets, pass a high upper bound such as 0.99-1. Example: 0.1-0.25. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "authors": [
    {
      "attribute_datas": {
        "author_avatar_frame_icon": "0",
        "author_ecom_level": "L3",
        "author_level_game": "Lv1",
        "author_level_other": "Lv1",
        "author_status": "1",
        "author_thin_mid_word_association_index": "{\"年轻人\":0.043,\"洁面\":1837.8594707888255,\"清爽\":11.143999999999997,\"绵密\":0.042,\"美白\":29.…",
        "author_type": "2",
        "avatar_uri": "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-i-0813c000-ce_os7G9…"
      },
      "extra_data": {
        "content_query_from_word": "",
        "content_query_score": 0,
        "debug_info": "",
        "demander_behavior": {
          "added_author_list": false,
          "cooperated": false,
          "viewd_author_page": false
        },
        "recall_from": [
          "1_0"
        ],
        "recall_return_infos": {},
        "recommend_types": []
      },
      "items": [
        {
          "item_id": "7675969038563986698",
          "video_tag": 3,
          "vv": 348216762
        }
      ],
      "star_id": "6870161898013196295",
      "task_infos": [
        {
          "online_status": 1,
          "platform_source": 1,
          "price_infos": [
            {
              "end_time": "2145916800",
              "platform_source": 1,
              "price": 50000,
              "price_extra_info": {},
              "start_time": "1782835200",
              "task_category": 1,
              "video_type": 61,
              "video_type_status": 1
            }
          ],
          "task_category": 1,
          "task_status": 1
        }
      ]
    }
  ],
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "extra_data": {
    "is_cpm_project_search": false,
    "search_author_count": 0,
    "search_item_count": 0,
    "search_session_id": "77038448…",
    "speaker_live_base_dis": []
  },
  "pagination": {
    "has_more": true,
    "limit": 20,
    "page": 1,
    "total_count": 10000
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `authors[].star_id` | Xingtu creator ID. Use it to look up the creator in other Xingtu APIs. |
| `authors[].attribute_datas.author_ecom_level` | Creator e-commerce level as a label, for example `L0`, `L3` or `L6`. |
| `authors[].attribute_datas.author_type` | Creator type code returned as a string. The response does not explain what each code means. |
| `authors[].attribute_datas.avatar_uri` | URL of the creator's avatar image. |
| `authors[].attribute_datas.author_thin_mid_word_association_index` | JSON string that maps keywords to numeric association scores. The response does not state what the scores measure. It is `{}` when the creator has no data. |
| `authors[].items[].item_id / authors[].items[].vv` | ID of one of the creator's top videos and its `vv` value, which looks like a view count. `video_tag` is a numeric label for the video. |
| `authors[].task_infos[].price_infos[].price` | Quote price for one video type. A value of `0` appears for some creators. |
| `authors[].task_infos[].price_infos[].video_type` | Numeric code for the quoted video format. Each price row also has `start_time` and `end_time` as Unix timestamp strings. |
| `authors[].task_infos[].task_status / online_status` | Status flags for the creator's task offering. The value `1` appears on all returned creators. |
| `pagination.has_more / pagination.total_count` | Whether more pages exist and the total match count. `limit` is the page size (20) and `page` is the current page. |

### Notes

- Pass `page` to move through results. The sample response shows `limit` of 20 and `page` of 1.
- Use `sort` with `FANS` for follower count order or `DEFAULT` for Xingtu score ranking. Set `searchType` to `NICKNAME` or `CONTENT` to choose what `keyword` matches.
- Use `kolPriceType` with `kolPriceRange` to filter by quote price. `kolPriceRange` needs `kolPriceType`.
- Take `star_id` from a result and call [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info) or [Douyin Xingtu Audience Distribution](/apis/douyin/xingtu-v3/data-sp-author-audience-distribution) next.

### Pricing

$0.071429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/gsearch-search-for-author-square.json`](../../../../catalog/models/douyin/xingtu-v3/gsearch-search-for-author-square.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/gsearch-search-for-author-square
