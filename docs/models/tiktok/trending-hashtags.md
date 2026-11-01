# TikTok Trending Hashtags

`tiktok/trending-hashtags` · api · TikTok

Rank TikTok's trending hashtags for one country and industry, with each hashtag's daily popularity curve, post count, video views, and leading creators. Ranks 15 industry categories, or omit industry for the all-industries board. TikTok publishes only the top 3 hashtags per board to anonymous callers, so limit 1-3 is served cheaply; a limit above 3 routes to a dearer authenticated source that returns the full ranking. Covers 27 markets: AE, AR, AU, BR, CA, CO, DE, EG, ES, FR, GB, ID, IL, IT, JP, KR, MX, MY, PH, SA, SG, TH, TR, TW, US, VN, ZA.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/trending-hashtags"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/trending-hashtags', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/trending-hashtags", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/trending-hashtags", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/trending-hashtags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of ranked hashtags to return, from 1 through 100 (default 3). TikTok publishes only the top 3 hashtags per board to anonymous callers, so 1 through 3 is served by the cheapest source; a higher limit… default `3`; range 1–100 |
| `period` | integer |  | Lookback window in days that the ranking and the popularity curve cover (default 7). one of: `7`, `30`, `90`; default `7` |
| `region` | string |  | Two-letter country code of the market whose hashtag ranking to read (default US). Each market is ranked independently, so US and DE return different boards. one of: `US`, `FR`, `DE`, `IT`, `ES`, `GB`, `AR`, `AU`, `BR`, `CA`, `CO`, `EG` …; default `"US"` |
| `industry` | string |  | Restrict the ranking to one industry. Omit for the all-industries board. one of: `apparel_accessories`, `baby_kids_maternity`, `beauty_personal_care`, `education`, `food_beverage`, `games`, `health`, `home_improvement`, `household_products`, `news_entertainment`, `pets`, `sports_outdoor` … |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `industryIds`, and it is served only by a source that returns every…  |

## Details

Rank TikTok's trending hashtags for one country and industry, with each hashtag's daily popularity curve, post count, video views, and leading creators. Ranks 15 industry categories, or omit industry for the all-industries board. TikTok publishes only the top 3 hashtags per board to anonymous callers, so limit 1-3 is served cheaply; a limit above 3 routes to a dearer authenticated source that returns the full ranking. Covers 27 markets: AE, AR, AU, BR, CA, CO, DE, EG, ES, FR, GB, ID, IL, IT, JP, KR, MX, MY, PH, SA, SG, TH, TR, TW, US, VN, ZA.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/trending-hashtags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "period": 7, "region": "US"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `industry` | string | No | Restrict the ranking to one industry. Omit for the all-industries board. One of: `apparel_accessories`, `baby_kids_maternity`, `beauty_personal_care`, `education`, `food_beverage`, `games`, `health`, `home_improvement`,  |
| `limit` | integer | No | Maximum number of ranked hashtags to return, from 1 through 100 (default 3). TikTok publishes only the top 3 hashtags per board to anonymous callers, so 1 through 3 is served by the cheapest source; a higher limit routes |
| `period` | integer | No | Lookback window in days that the ranking and the popularity curve cover (default 7). One of: `7`, `30`, `90`. |
| `region` | string | No | Two-letter country code of the market whose hashtag ranking to read (default US). Each market is ranked independently, so US and DE return different boards. One of: `US`, `FR`, `DE`, `IT`, `ES`, `GB`, `AR`, `AU`, `BR`, ` |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `industryIds`, and it is served only by a source that returns every on |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/trending-hashtags.json`](../../../catalog/models/tiktok/trending-hashtags.json) · Store page: https://www.sandbase.ai/model/tiktok/trending-hashtags
