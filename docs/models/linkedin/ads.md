# LinkedIn Ads Library API: pricing, parameters and code examples

`linkedin/ads` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0331 per call · **Modes:** sync

Search the LinkedIn Ad Library by search URL and list the matching ads (advertiser, creative text, format).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0331**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/ads", "url": "https://www.linkedin.com/company/stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/ads', {'url': 'https://www.linkedin.com/company/stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/ads", {
  "url": "https://www.linkedin.com/company/stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/ads", sandbase.Params{
	"url": "https://www.linkedin.com/company/stripe",
})
```

Same call via the path form: `POST /v1/api/linkedin/ads` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | LinkedIn Ad Library search URL or a LinkedIn company URL (e.g. https://www.linkedin.com/ad-library/search?companyIds=1035).  |
| `limit` | integer |  | Maximum number of results to return (1-20, default 20). You are billed per result returned, so a lower limit costs less. range 1–20 |

## Details

Returns a list of ads from the LinkedIn Ad Library that match a search URL or a LinkedIn company page URL. Each ad includes the advertiser name, the ad text, the ad format, and a link to the ad detail page. The `url` parameter is required, and `limit` caps the number of ads returned (1-20).

### Use cases

- Review the ads a competitor currently runs on LinkedIn by passing their company page URL.
- Collect ad copy from one advertiser to study messaging and calls to action.
- Compare ad formats such as `VIDEO`, `SINGLE_IMAGE` and `MESSAGE` that a brand uses.
- Build a list of ad IDs and detail URLs to fetch full ad details later.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/ads" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/company/stripe", "limit": 3}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | LinkedIn Ad Library search URL or a LinkedIn company URL (e.g. https://www.linkedin.com/ad-library/search?companyIds=1035). |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). You are billed per result returned, so a lower limit costs less. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "advertiser": "Stripe",
        "advertiserLogo": "https://media.licdn.com/dms/image/v2/D560BAQE2ZfJyfn-VCg/company-logo_100_100/B5…",
        "format": "MESSAGE",
        "id": "1662503636",
        "image": "",
        "text": "%FIRSTNAME% 様、Stripe Japan チームの Youngah Lee と申します。11月24日 (火) に開催される SaaS Platfor…",
        "url": "https://www.linkedin.com/ad-library/detail/1662503636"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].advertiser` | Name of the company that runs the ad. |
| `data.items[].advertiserLogo` | URL of the advertiser logo image. It can be an empty string. |
| `data.items[].format` | Ad format, for example `MESSAGE`, `VIDEO` or `SINGLE_IMAGE`. |
| `data.items[].id` | ID of the ad in the LinkedIn Ad Library, given as a string. |
| `data.items[].text` | Creative text of the ad. Long text may end with an ellipsis. |
| `data.items[].image` | URL of the ad image. It is an empty string when the ad has no image, such as `MESSAGE` and `VIDEO` ads in this sample. |
| `data.items[].url` | Link to the ad detail page in the LinkedIn Ad Library. |
| `found` | `true` when the lookup returned results. |

### Notes

- Pass a LinkedIn company URL such as `https://www.linkedin.com/company/stripe`, or an Ad Library search URL such as `https://www.linkedin.com/ad-library/search?companyIds=1035`.
- The response shows no pagination parameter. Use `limit` (maximum 20) to control how many ads come back.
- Use the `id` value of an ad with [LinkedIn Ad Details](/apis/linkedin/ad) to get more on a single ad.
- To search ads by keyword or other filters, try [LinkedIn Ad Search](/apis/linkedin/ads-search).

### Pricing

Billed at the actual cost of each call, about $0.0331 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/ads.json`](../../../catalog/models/linkedin/ads.json) · Store page: https://www.sandbase.ai/model/linkedin/ads
