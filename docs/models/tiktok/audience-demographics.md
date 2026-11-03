# TikTok Audience Demographics API: pricing, parameters and code examples

`tiktok/audience-demographics` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.018 per call · **Modes:** sync

Get the audience country breakdown (follower count and share per country) for a TikTok creator by handle.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.018**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/audience-demographics", "handle": "shakira"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/audience-demographics', {'handle': 'shakira'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/audience-demographics", {
  "handle": "shakira"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/audience-demographics", sandbase.Params{
	"handle": "shakira",
})
```

Same call via the path form: `POST /v1/api/tiktok/audience-demographics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | TikTok username without the leading @ (e.g. "shakira").  |

## Details

Returns the country breakdown of a TikTok creator's audience. Each row gives a country, its follower count and its share of the audience. The only input is the creator's `handle`.

### Use cases

- Check whether a creator's audience sits in the countries a campaign targets.
- Compare the top audience countries of several creators before picking partners.
- Flag creators whose audience is concentrated in markets that do not match their stated niche.
- Add audience location data to an influencer report or database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/audience-demographics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "shakira"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | TikTok username without the leading @ (e.g. "shakira"). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "audienceLocations": [
      {
        "count": 101,
        "country": "United States",
        "countryCode": "US",
        "percentage": "8.51%"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the creator was found and audience data was returned. A lookup that finds nothing returns `false`. |
| `data.audienceLocations[]` | List of countries in the creator's audience. Each item is one country. |
| `data.audienceLocations[].country` | Country name in English, for example `United States`. |
| `data.audienceLocations[].countryCode` | Two-letter country code, for example `US`. |
| `data.audienceLocations[].count` | Number of audience members counted for this country. |
| `data.audienceLocations[].percentage` | Share of the audience in this country, returned as a string with a percent sign, for example `8.51%`. |

### Notes

- Pass `handle` without the leading `@`, for example `shakira`.
- `percentage` is a string, so strip the `%` sign before you do math on it.
- The response shows the countries in descending order of `count`.

### Pricing

Billed at the actual cost of each call, about $0.018 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/audience-demographics.json`](../../../catalog/models/tiktok/audience-demographics.json) · Store page: https://www.sandbase.ai/model/tiktok/audience-demographics
