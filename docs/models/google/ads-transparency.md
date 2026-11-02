# Google Ads Transparency Center API: pricing, parameters and code examples

`google/ads-transparency` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Ads an advertiser is running on Google, from the Ads Transparency Center: creatives, formats, first and last shown dates.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/ads-transparency"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/ads-transparency', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/ads-transparency", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/ads-transparency", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/google/ads-transparency` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `num` | integer |  | results to return; default 40. Unlike engine=google, `num` IS documented here  |
| `text` | string |  | free-text advertiser or domain to search for. Supply either this OR advertiser_id — neither is individually mandatory but one is needed  |
| `region` | string |  | geographic region the search originates from. REQUIRED when political_ads is true  |
| `end_date` | string |  | YYYYMMDD  |
| `platform` | string |  | where the ad ran: PLAY \| MAPS \| SEARCH \| SHOPPING \| YOUTUBE  |
| `start_date` | string |  | YYYYMMDD  |
| `advertiser_id` | string |  | a specific advertiser id, or several comma-separated  |
| `political_ads` | boolean |  | restrict to political advertising; forces `region` to be set  |
| `creative_format` | string |  | text \| image \| video  |
| `next_page_token` | string |  | cursor from the previous response's serpapi_pagination  |

## Details

Ads an advertiser is running on Google, from the Ads Transparency Center: creatives, formats, first and last shown dates.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/ads-transparency" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "apple.com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `advertiser_id` | string | No | a specific advertiser id, or several comma-separated |
| `creative_format` | string | No | text / image / video |
| `end_date` | string | No | YYYYMMDD |
| `next_page_token` | string | No | cursor from the previous response's serpapi_pagination |
| `num` | integer | No | results to return; default 40. Unlike engine=google, `num` IS documented here |
| `platform` | string | No | where the ad ran: PLAY / MAPS / SEARCH / SHOPPING / YOUTUBE |
| `political_ads` | boolean | No | restrict to political advertising; forces `region` to be set |
| `region` | string | No | geographic region the search originates from. REQUIRED when political_ads is true |
| `start_date` | string | No | YYYYMMDD |
| `text` | string | No | free-text advertiser or domain to search for. Supply either this OR advertiser_id — neither is individually mandatory but one is needed |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/ads-transparency.json`](../../../catalog/models/google/ads-transparency.json) · Store page: https://www.sandbase.ai/model/google/ads-transparency
