# Waveinflu Email Lookup API: pricing, parameters and code examples

`waveinflu/email-lookup` · data API · Waveinflu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001991 per call (free daily quota) · **Modes:** sync

Looks up the contact email for one Instagram, TikTok, or YouTube creator from a profile URL.

## Pricing

- **$0.001991 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "waveinflu/email-lookup"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('waveinflu/email-lookup', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("waveinflu/email-lookup", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "waveinflu/email-lookup", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/waveinflu/email-lookup` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `profile_url` | string |  | Instagram, TikTok, or YouTube creator profile URL.  |

## Details

Returns the contact email for one Instagram, TikTok, or YouTube creator. You pass the creator's profile URL in `profile_url`. The response also reports the detected platform and whether an email was found.

### Use cases

- Build an outreach list by turning creator profile URLs into contact emails.
- Check whether a creator has a public contact email before you add them to a campaign.
- Enrich a creator database with emails for profiles you already track on Instagram, TikTok, or YouTube.
- Run the same lookup across several platforms with one request format.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/waveinflu/email-lookup" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"profile_url": "https://www.instagram.com/nike/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `profile_url` | string | No | Instagram, TikTok, or YouTube creator profile URL. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "billingRequestId": "94acd447-30d1-4f7e-85ca-108ccf39f39d",
  "data": {
    "email": {
      "status": "missing",
      "value": null
    },
    "platform": "instagram",
    "profile_url": "https://www.instagram.com/nike/"
  },
  "requestId": "7e09d403-9d9c-4208-8ebe-b02c1906c4bf"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.email.status` | Result of the lookup. The sample shows `missing`, which means no email was found for this profile. |
| `data.email.value` | The contact email as a string. It is `null` when `data.email.status` is `missing`. |
| `data.platform` | Platform detected from the URL, for example `instagram`. |
| `data.profile_url` | The profile URL the lookup ran for. It echoes the `profile_url` you sent. |
| `requestId` | ID of this request. Keep it when you need to report a problem with a call. |
| `billingRequestId` | ID tied to the billing record for this call. |

### Notes

- Send the full creator profile URL, such as `https://www.instagram.com/onkimia/`. The same parameter accepts TikTok and YouTube profile URLs.
- Check `data.email.status` before you read `data.email.value`. A `missing` status comes with a `null` value.
- To find creators first, use [Waveinflu Creator AI Search](/apis/waveinflu/creator-search) or [Waveinflu Similar Creators](/apis/waveinflu/similar-creators), then pass their profile URLs to this API.

### Pricing

$0.001991 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/waveinflu/email-lookup.json`](../../../catalog/models/waveinflu/email-lookup.json) · Store page: https://www.sandbase.ai/model/waveinflu/email-lookup
