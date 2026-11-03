# Twitter User about profile API: pricing, parameters and code examples

`twitter/web/user-about` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get user about profile on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-about", "screen_name": "elonmusk"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-about', {'screen_name': 'elonmusk'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-about", {
  "screen_name": "elonmusk"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-about", sandbase.Params{
	"screen_name": "elonmusk",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-about` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `screen_name` | string | yes | Screen Name  |

## Details

Returns the "About this account" data for a Twitter user, such as the country the account is based in, how many times the username changed, and verification status. It needs one input: the `screen_name` of the account, without the @ sign.

### Use cases

- Check where an account says it is based and how it was sourced before you trust its posts.
- Flag accounts that changed their username by reading `about.username_changes.count`.
- Confirm whether an account is verified, protected or active before you add it to a monitoring list.
- Find the affiliated organization of an account from its affiliate label.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-about" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "elonmusk"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `screen_name` | string | Yes | Screen Name |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "about": {
    "account_based_in": "United States",
    "affiliate_username": "X",
    "learn_more_url": "https://help.twitter.com/managing-your-account/about-twitter-verified-accounts",
    "location_accurate": false,
    "source": "United States App Store",
    "username_changes": {
      "count": "0"
    }
  },
  "affiliates": {
    "label": {
      "badge": {
        "url": "https://pbs.twimg.com/profile_images/1955359038532653056/OSHY3ewP_bigger.jpg"
      },
      "description": "X",
      "url": {
        "url": "https://twitter.com/X",
        "urlType": "DeepLink"
      },
      "userLabelDisplayType": "Badge",
      "userLabelType": "BusinessLabel"
    }
  },
  "avatar": "https://pbs.twimg.com/profile_images/2103567689515954176/aR-Kjpp4_normal.jpg",
  "blue_verified": true,
  "business_account": null,
  "id": "44196397",
  "name": "Elon Musk",
  "profile": "elonmusk",
  "protected": false,
  "rest_id": "44196397",
  "status": "active",
  "verified_since": "-156836000000000"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `about.account_based_in` | Country or region shown as the place the account is based in. |
| `about.source` | Where the location information comes from, for example `United States App Store`. |
| `about.location_accurate` | Boolean flag for whether the location is marked as accurate. |
| `about.username_changes.count` | Number of username changes, returned as a string. |
| `about.affiliate_username` | Username of the affiliated account, such as `X`. |
| `affiliates.label.description / affiliates.label.url.url` | Name and link of the affiliated organization shown as a badge on the profile. |
| `blue_verified` | `true` if the account has the blue verified mark. |
| `verified_since` | Raw value for when the account became verified. It is a negative number string in this response, so treat it as an opaque value. |
| `id / rest_id` | Numeric ID of the user. Both fields hold the same value in this response. |
| `profile / name / protected / status` | Screen name, display name, whether the account is protected, and the account state such as `active`. |

### Notes

- Pass the handle in `screen_name` without the @ sign, for example `elonmusk`.
- Use the `rest_id` value with [Twitter Profiles by rest ids](/apis/twitter/web/user-profiles-by-rest-ids) to look up other users by ID.
- For follower counts, bio and other profile details, call [Twitter (X) User Profile](/apis/twitter/web/user-profile).
- For the full list of affiliated accounts, call [Twitter User affiliates](/apis/twitter/web/user-affiliates).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/web/user-about.json`](../../../../catalog/models/twitter/web/user-about.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-about
