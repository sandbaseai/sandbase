# Polymarket Get public profile by wallet address API: pricing, parameters and code examples

`polymarket/public-profile` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get public profile by wallet address from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/public-profile", "address": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/public-profile', {'address': '0xfe787d2da716d60e8acff57fb87eb13cd4d10319'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/public-profile", {
  "address": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/public-profile", sandbase.Params{
	"address": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
})
```

Same call via the path form: `POST /v1/api/polymarket/public-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `address` | string | yes | The wallet address (proxy wallet or user address)  |

## Details

Returns the public Polymarket profile for a wallet address. It includes the display name, pseudonym, proxy wallet, taker tier, weighted volume and account flags. The input is one wallet address, either a proxy wallet or a user address.

### Use cases

- Show a trader's display name and pseudonym next to their wallet address in a dashboard.
- Check a wallet's `takerTierName` and `weightedVolume` to rank or screen traders.
- Find out when a Polymarket account was created from its `createdAt` timestamp.
- Check whether an account has a verified badge or moderator and creator roles before listing it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/public-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"address": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `address` | string | Yes | The wallet address (proxy wallet or user address) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "$schema": "https://gamma-api.polymarket.com/schemas/PublicProfileResponse.json",
  "createdAt": "2026-03-25T18:19:26.033805Z",
  "displayUsernamePublic": true,
  "name": "ferrariChampions2026",
  "proxyWallet": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
  "pseudonym": "Glaring-Salt",
  "takerTier": 6,
  "takerTierName": "Obsidian",
  "users": [
    {
      "communityMod": false,
      "creator": false,
      "id": "6957592",
      "mod": false
    }
  ],
  "verifiedBadge": false,
  "weightedVolume": 10196172.112641
}
```

### Response fields

| Field | Meaning |
|---|---|
| `name / pseudonym` | `name` is the profile's display name. `pseudonym` is the generated alias on the profile (for example `Glaring-Salt`). |
| `displayUsernamePublic` | Boolean. `true` means the user has chosen to show their username publicly. |
| `proxyWallet` | The proxy wallet address tied to this profile. |
| `createdAt` | Timestamp of when the profile was created, in ISO 8601 format (UTC). |
| `takerTier / takerTierName` | The numeric taker tier and its label. In this response, tier `6` is named `Obsidian`. |
| `weightedVolume` | A number for the profile's weighted trading volume. In the sample it is about 10.2 million. |
| `verifiedBadge` | Boolean. `true` means the profile has a verified badge. |
| `users[].id` | The user ID attached to the profile, returned as a string. |
| `users[].mod / users[].communityMod / users[].creator` | Boolean role flags for the user: moderator, community moderator and creator. |

### Notes

- Pass the wallet address in `address`. Both a proxy wallet and a user address are accepted.
- Use [Polymarket Wallet Positions](/apis/polymarket/positions) with the `proxyWallet` value to see what this wallet currently holds.
- Use [Polymarket Wallet Activity](/apis/polymarket/activity) to see this wallet's trades and other actions.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/public-profile.json`](../../../catalog/models/polymarket/public-profile.json) · Store page: https://www.sandbase.ai/model/polymarket/public-profile
