# TikTok Profile Region API: pricing, parameters and code examples

`tiktok/profile-region` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Resolve the home region (country) of a TikTok creator by handle.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/profile-region", "handle": "stoolpresidente"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/profile-region', {'handle': 'stoolpresidente'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/profile-region", {
  "handle": "stoolpresidente"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/profile-region", sandbase.Params{
	"handle": "stoolpresidente",
})
```

Same call via the path form: `POST /v1/api/tiktok/profile-region` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | TikTok username without the leading @ (e.g. "stoolpresidente").  |

## Details

Returns the home region of a TikTok creator as a two-letter country code. It needs one input, the creator's `handle` without the leading @.

### Use cases

- Check whether a creator is based in the US before adding them to a regional influencer campaign.
- Filter a list of TikTok handles by country before outreach.
- Add a country column to a creator database that only stores usernames.
- Confirm a creator's market before you buy or plan local ads.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/profile-region" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "stoolpresidente"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | TikTok username without the leading @ (e.g. "stoolpresidente"). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "handle": "stoolpresidente",
    "profileUrl": "https://www.tiktok.com/@stoolpresidente",
    "region": "US"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the handle matched a TikTok profile. A lookup that finds nothing returns `found: false`. |
| `data.region` | Two-letter country code for the creator's home region, for example `US`. |
| `data.handle` | The TikTok username that was looked up, without the @. |
| `data.profileUrl` | Direct link to the creator's TikTok profile page. |

### Notes

- Pass `handle` without the leading @, for example `stoolpresidente`.
- Check `found` before you read `data.region`.
- For creator details beyond region, try [TikTok Creator Info and Milestones](/apis/tiktok/analytics/creator-info-and-milestones).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/profile-region.json`](../../../catalog/models/tiktok/profile-region.json) · Store page: https://www.sandbase.ai/model/tiktok/profile-region
