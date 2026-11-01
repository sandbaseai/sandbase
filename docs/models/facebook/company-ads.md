# Facebook Company Ads

`facebook/company-ads` · api · Facebook

List the Meta Ad Library ads a company is running by page ID or company name (creative text, format, platforms, and run dates) with cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/company-ads"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/company-ads', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/company-ads", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/company-ads", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/facebook/company-ads` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor.  |
| `pageId` | string |  | Company's Ad Library page ID. Provide either pageId or companyName.  |
| `sortBy` | string |  | Sort order: impressions (highest first, the default) or recent (most recent). one of: `impressions`, `recent` |
| `status` | string |  | Ad status filter. Defaults to ACTIVE. one of: `ALL`, `ACTIVE`, `INACTIVE` |
| `country` | string |  | Two-letter country code to scope results. Defaults to all countries.  |
| `endDate` | string |  | Filter to ads with impressions on or before this date, in YYYY-MM-DD format.  |
| `language` | string |  | Two-letter language code to filter ads (e.g. "EN", "ES", "FR").  |
| `mediaType` | string |  | Creative media type filter. one of: `ALL`, `IMAGE`, `VIDEO`, `MEME`, `IMAGE_AND_MEME`, `NONE` |
| `startDate` | string |  | Filter to ads with impressions on or after this date, in YYYY-MM-DD format.  |
| `companyName` | string |  | Company name to search (e.g. "nike"). Exact-match and case-sensitive against the Meta Ad Library index; an advertiser with no indexed page returns found:false.  |

## Details

List the Meta Ad Library ads a company is running by page ID or company name (creative text, format, platforms, and run dates) with cursor pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/company-ads" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"pageId": "15087023444", "sortBy": "recent"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `companyName` | string | No | Company name to search (e.g. "nike"). Exact-match and case-sensitive against the Meta Ad Library index; an advertiser with no indexed page returns found:false. |
| `country` | string | No | Two-letter country code to scope results. Defaults to all countries. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. |
| `endDate` | string | No | Filter to ads with impressions on or before this date, in YYYY-MM-DD format. |
| `language` | string | No | Two-letter language code to filter ads (e.g. "EN", "ES", "FR"). |
| `mediaType` | string | No | Creative media type filter. One of: `ALL`, `IMAGE`, `VIDEO`, `MEME`, `IMAGE_AND_MEME`, `NONE`. |
| `pageId` | string | No | Company's Ad Library page ID. Provide either pageId or companyName. |
| `sortBy` | string | No | Sort order: impressions (highest first, the default) or recent (most recent). One of: `impressions`, `recent`. |
| `startDate` | string | No | Filter to ads with impressions on or after this date, in YYYY-MM-DD format. |
| `status` | string | No | Ad status filter. Defaults to ACTIVE. One of: `ALL`, `ACTIVE`, `INACTIVE`. |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/company-ads.json`](../../../catalog/models/facebook/company-ads.json) · Store page: https://www.sandbase.ai/model/facebook/company-ads
