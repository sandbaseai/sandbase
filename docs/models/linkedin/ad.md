# LinkedIn Ad Details API: pricing, parameters and code examples

`linkedin/ad` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Look up a single LinkedIn Ad Library ad by URL and get the advertiser, headline, creative text, format, CTA, targeting, run dates, and impressions as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/ad", "url": "https://www.linkedin.com/ad-library/detail/1487405616"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/ad', {'url': 'https://www.linkedin.com/ad-library/detail/1487405616'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/ad", {
  "url": "https://www.linkedin.com/ad-library/detail/1487405616"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/ad", sandbase.Params{
	"url": "https://www.linkedin.com/ad-library/detail/1487405616",
})
```

Same call via the path form: `POST /v1/api/linkedin/ad` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | LinkedIn Ad Library ad URL (e.g. "https://www.linkedin.com/ad-library/detail/666281156").  |

## Details

This API returns the details of one ad from the LinkedIn Ad Library. It needs the ad's Ad Library URL in the `url` parameter. The response includes the advertiser, headline, description, call to action, and media links.

### Use cases

- Save the headline, description, and CTA of a competitor's LinkedIn ad for a swipe file.
- Download the video or image link of an ad to review its creative.
- Check which company page runs an ad by reading the advertiser name and page link.
- Verify that an Ad Library URL still resolves to a live ad record.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/ad" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/ad-library/detail/1487405616"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | LinkedIn Ad Library ad URL (e.g. "https://www.linkedin.com/ad-library/detail/666281156"). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "adType": "Video Ad",
    "advertiser": "Microsoft Copilot",
    "advertiserLinkedinPage": "https://www.linkedin.com/company/3509299",
    "advertiserLogo": "https://media.licdn.com/dms/image/v2/D560BAQE0EPOgjrUOug/company-logo_100_100/B5…",
    "cta": "Sign Up",
    "description": "Get ahead of what’s important with Copilot in Outlook.",
    "destinationUrl": "",
    "endDate": "",
    "headline": "The apps you know go further with Copilot",
    "id": "1487405616",
    "image": "",
    "startDate": ""
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the ad was found. A lookup that finds nothing returns `found: false`. |
| `data.id` | The ad ID. It matches the number at the end of the Ad Library URL. |
| `data.adType` | The ad format, for example `Video Ad`. |
| `data.advertiser` | Name of the company that runs the ad. |
| `data.advertiserLinkedinPage / data.advertiserLogo` | Link to the advertiser's LinkedIn page and to its logo image. |
| `data.headline / data.description` | The headline and the body text of the ad. |
| `data.cta` | The call-to-action button label, for example `Sign Up`. |
| `data.videoUrl / data.image` | Media links for the ad creative. `videoUrl` is set for video ads. `image` is an empty string when the ad has no image. |
| `data.destinationUrl` | The landing page of the ad. It can be an empty string. |
| `data.startDate / data.endDate / data.totalImpressions` | Run dates and impression count of the ad. These can be empty strings when the Ad Library does not show them for the ad. |

### Notes

- Copy the ad URL from the LinkedIn Ad Library. It has the form `https://www.linkedin.com/ad-library/detail/<id>`.
- Empty strings in `data` mean the value is not available for that ad.
- To find ads before looking up one, use [LinkedIn Ad Search](/apis/linkedin/ads-search) or [LinkedIn Ads Library](/apis/linkedin/ads).
- To learn more about the advertiser, call [LinkedIn Company](/apis/linkedin/company).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/ad.json`](../../../catalog/models/linkedin/ad.json) · Store page: https://www.sandbase.ai/model/linkedin/ad
