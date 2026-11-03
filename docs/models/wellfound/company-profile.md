# Wellfound Company Profile API: pricing, parameters and code examples

`wellfound/company-profile` · data API · Wellfound · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

Retrieve a company profile by slug, including description, size, badges, and basic info. Returns stale_input if the company is not found.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wellfound/company-profile", "company_slug": "stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wellfound/company-profile', {'company_slug': 'stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wellfound/company-profile", {
  "company_slug": "stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wellfound/company-profile", sandbase.Params{
	"company_slug": "stripe",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/wellfound/company-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `company_slug` | string | yes | Company slug (e.g., 'mixpanel', 'juniper-square')  |

## Details

Returns a Wellfound company profile for one company slug. The response includes the company name, a product description, a size bucket, badges, and a logo URL. You send the `company_slug` value as input.

### Use cases

- Enrich a list of startup names with a description and logo for a CRM or sales tool.
- Filter target companies by size bucket such as `SIZE_5000_PLUS` before outreach.
- Tag companies by badges like `B2B` or `Scale Stage` in a market map.
- Check that a slug exists before you fetch its open jobs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wellfound/company-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"company_slug": "stripe"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `company_slug` | string | Yes | Company slug (e.g., 'mixpanel', 'juniper-square') |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "badges": [
      {
        "label": "B2B",
        "tooltip": null
      }
    ],
    "companySize": "SIZE_5000_PLUS",
    "id": "37232",
    "logoUrl": "https://photos.wellfound.com/startups/i/37232-b86e6247bcd9846c18c91fe65ca0355d-m…",
    "name": "Stripe",
    "productDescription": "Stripe is a software platform for starting and running internet businesses. Mill…",
    "slug": "stripe"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name` | Display name of the company, for example `Stripe`. |
| `data.slug` | Company slug on Wellfound. It matches the `company_slug` you sent. |
| `data.id` | Wellfound company ID, returned as a string. |
| `data.productDescription` | Text description of what the company does. Long text may be cut short. |
| `data.companySize` | Size bucket as a code, for example `SIZE_5000_PLUS`. |
| `data.badges[].label` | Short badge name such as `B2B`, `Scale Stage` or `Top Investors`. |
| `data.badges[].tooltip` | Explanation text for the badge. It is `null` when the badge has none. |
| `data.logoUrl` | URL of the company logo image. |
| `status` | Result status of the call. `success` means the profile was found. |

### Notes

- Take the slug from the company page URL on Wellfound. Examples are `stripe`, `mixpanel` and `juniper-square`.
- If the company is not found, the API returns `stale_input` instead of a profile.
- Call [Wellfound Company Jobs](/apis/wellfound/company-jobs) next to list open roles at the company.

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wellfound/company-profile.json`](../../../catalog/models/wellfound/company-profile.json) · Store page: https://www.sandbase.ai/model/wellfound/company-profile
