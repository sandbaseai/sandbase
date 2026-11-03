# Waveinflu Similar Creators API: pricing, parameters and code examples

`waveinflu/similar-creators` · data API · Waveinflu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.004977 to $0.4977 per run, depending on parameters · **Modes:** sync

Finds creators similar to a seed account on Instagram, TikTok, or YouTube.

## Pricing

- Depends on parameters (`params.limit`).

| parameters | USD |
|---|---|
| limit=1 | 0.004977 |
| limit=25 | 0.124425 |
| limit=100 | 0.4977 |

Formula: `0.004977 * Math.max(1.0, Math.min(100.0, (params.limit ?? 25) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "waveinflu/similar-creators", "target_account": "@onkimia"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('waveinflu/similar-creators', {'target_account': '@onkimia'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("waveinflu/similar-creators", {
  "target_account": "@onkimia"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "waveinflu/similar-creators", sandbase.Params{
	"target_account": "@onkimia",
})
```

Same call via the path form: `POST /v1/api/waveinflu/similar-creators` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of creators to return. Default 25, range 1–100. Caps the billed count. default `25`; range 1–100 |
| `filters` | object |  | Optional filters applied before matching. All fields are optional.  |
| `platform` | string |  | Target platform. one of: `instagram`, `tiktok`, `youtube`; default `"youtube"` |
| `target_account` | string | yes | Seed account: a creator handle (with or without @) or profile URL to find similar creators for.  |

## Details

Returns a list of creators similar to a seed account on Instagram, TikTok, or YouTube. You send a creator handle or profile URL in `target_account`, and each result includes profile details, follower count, engagement rates, play counts, and a similarity `score`.

### Use cases

- Build a shortlist of lookalike creators for an influencer campaign, starting from a brand or creator you already work with.
- Find competitor or peer accounts to a brand on Instagram.
- Narrow candidates by region, language, or follower range with `filters` before outreach.
- Collect contact emails and profile URLs of similar creators to start outreach.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/waveinflu/similar-creators" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target_account": "nike", "platform": "instagram", "limit": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `target_account` | string | Yes | Seed account: a creator handle (with or without @) or profile URL to find similar creators for. |
| `filters` | object | No | Optional filters applied before matching. All fields are optional. |
| `limit` | integer | No | Maximum number of creators to return. Default 25, range 1–100. Caps the billed count. |
| `platform` | string | No | Target platform. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "billingRequestId": "16e7593e-3f9e-4751-aa4a-daebfcf29794",
  "data": {
    "count": 1,
    "items": [
      {
        "accountPositioning": [
          "athletic apparel and footwear brand"
        ],
        "ageRange": "unknown",
        "aiDescription": "An athletic apparel and footwear brand focused on sports, fitness, and lifestyle…",
        "averageEngagementRate": 0.017512453823882265,
        "averagePlayCount": 25949.3,
        "biography": "Nuestra misión es que seas mejor.\n#ProtectThisHouse",
        "email": "servicioalcliente@ua-argentina.com",
        "ethnicity": "unknown",
        "faceVisibility": "mixed",
        "followerCount": 1158642,
        "fullName": "Under Armour LATAM",
        "gender": "unknown"
      }
    ]
  },
  "requestId": "ae10aaf0-ff77-4ce2-9940-204f2830a746"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of creators returned in `data.items`. |
| `data.items[].username / data.items[].fullName / data.items[].profileUrl` | Handle, display name, and profile link of the matched creator. |
| `data.items[].score` | Similarity score between the matched creator and the seed account. In this response a higher value means a closer match (0.90 for the sample). |
| `data.items[].followerCount` | Follower count of the matched account. |
| `data.items[].averageEngagementRate / data.items[].medianEngagementRate` | Average and median engagement rate for the account, given as a decimal fraction (0.0175 is about 1.75%). |
| `data.items[].averagePlayCount / data.items[].medianPlayCount` | Average and median play count across the account's content. |
| `data.items[].accountPositioning / data.items[].aiDescription` | Short labels and a text summary of what the account is about. |
| `data.items[].region / data.items[].language` | Region (country code) and language code inferred for the creator, such as `CO` and `es`. |
| `data.items[].gender / data.items[].ethnicity / data.items[].ageRange / data.items[].faceVisibility` | Inferred audience-facing attributes of the creator. Values can be `unknown`, and `faceVisibility` can be `mixed`. |
| `data.items[].email / data.items[].biography` | Contact email and bio text from the profile, when present. |

### Notes

- Set `platform` to `instagram`, `tiktok`, or `youtube`. The default is `youtube`.
- `target_account` accepts a handle with or without `@`, or a profile URL.
- `limit` ranges from 1 to 100 and defaults to 25.
- To find creators by a text description instead of a seed account, use [Waveinflu Creator AI Search](/apis/waveinflu/creator-search). To look up a contact email, use [Waveinflu Email Lookup](/apis/waveinflu/email-lookup).

### Pricing

Billed at the actual cost of each call, about $0.124425 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/waveinflu/similar-creators.json`](../../../catalog/models/waveinflu/similar-creators.json) · Store page: https://www.sandbase.ai/model/waveinflu/similar-creators
