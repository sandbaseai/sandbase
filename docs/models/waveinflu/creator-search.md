# Waveinflu Creator AI Search API: pricing, parameters and code examples

`waveinflu/creator-search` · data API · Waveinflu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.004977 to $0.4977 per run, depending on parameters · **Modes:** sync

Finds creators from a natural-language brief instead of a seed account. `platform` and `query` are required; add `limit` (1–100, default 40) and the same optional `filters` as Similar Creators.

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
  -d '{"model": "waveinflu/creator-search", "query": "beauty creators in the US"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('waveinflu/creator-search', {'query': 'beauty creators in the US'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("waveinflu/creator-search", {
  "query": "beauty creators in the US"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "waveinflu/creator-search", sandbase.Params{
	"query": "beauty creators in the US",
})
```

Same call via the path form: `POST /v1/api/waveinflu/creator-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of creators to return. Default 25, range 1–100. Caps the billed count. default `25`; range 1–100 |
| `query` | string | yes | Natural-language description of the creators you are looking for.  |
| `filters` | object |  | Optional filters applied before matching. All fields are optional.  |
| `platform` | string |  | Target platform. one of: `instagram`, `tiktok`, `youtube`; default `"youtube"` |

## Details

Returns a list of Instagram, TikTok or YouTube creators that match a plain-language description. Each creator comes with profile details, audience and play statistics, and a match score. The call needs `query` and `platform`.

### Use cases

- Build an outreach list of fitness coaches on Instagram from a short brief.
- Shortlist creators in a size range by combining `query` with `minFollowers` and `maxFollowers` filters.
- Compare candidates by median play count and engagement rate before choosing who to contact.
- Find creators in one region or language for a local campaign.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/waveinflu/creator-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "fitness coach", "platform": "instagram", "limit": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Natural-language description of the creators you are looking for. |
| `filters` | object | No | Optional filters applied before matching. All fields are optional. |
| `limit` | integer | No | Maximum number of creators to return. Default 25, range 1–100. Caps the billed count. |
| `platform` | string | No | Target platform. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "billingRequestId": "5df8cd63-dadf-4810-966a-a0a20f61897f",
  "data": {
    "count": 1,
    "items": [
      {
        "accountPositioning": [
          "personal trainer"
        ],
        "ageRange": "unknown",
        "aiDescription": "A fitness coach and personal trainer showcasing workout routines and strength tr…",
        "averageEngagementRate": 0.042229385044690974,
        "averagePlayCount": 71630.81818181818,
        "biography": "🏋️Home personal training available \n🏋️gym trainer\n🥰Wish Me On 02 February",
        "email": "danishraj8969@gmail.com",
        "ethnicity": "asian",
        "faceVisibility": "clear_face",
        "followerCount": 70508,
        "fullName": "Shizu",
        "gender": "female"
      }
    ]
  },
  "requestId": "0765aec0-65cd-492e-aeac-b9608be3e36e"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of creators returned in this response. |
| `data.items[].username / data.items[].fullName` | The creator's handle and display name on the platform. |
| `data.items[].profileUrl` | Link to the creator's profile page. |
| `data.items[].id` | The creator's ID on the platform, returned as a string. |
| `data.items[].score` | Match score for the creator against the `query`. A higher value means a closer match. |
| `data.items[].followerCount` | Number of followers the creator has. |
| `data.items[].averagePlayCount / data.items[].medianPlayCount` | Average and median play counts for the creator's content. The median is less affected by a few viral posts. |
| `data.items[].averageEngagementRate / data.items[].medianEngagementRate` | Average and median engagement rate as decimal values. For example, `0.042` is 4.2%. |
| `data.items[].accountPositioning / data.items[].aiDescription` | Short labels and a text summary of what the creator posts about. |
| `data.items[].gender / data.items[].ethnicity / data.items[].ageRange / data.items[].faceVisibility` | Inferred audience-facing traits of the creator. `ageRange` can be `unknown`. `faceVisibility` uses values such as `clear_face`. |
| `data.items[].region / data.items[].language` | Creator region as a country code, and language code. |
| `data.items[].biography / data.items[].email` | Profile bio text and a contact email when one is available. |

### Notes

- `platform` accepts `instagram`, `tiktok` or `youtube`.
- `filters` can narrow results by `minFollowers`, `maxFollowers`, `regions`, `languages`, `genders` and more. Set `playCountMetric` to `median` or `average` to choose how `minPlayCount` and `maxPlayCount` are compared.
- Use `limit` (1 to 100) to set how many creators come back. This API has no pagination parameter.
- To start from a known account instead of a brief, use [Waveinflu Similar Creators](/apis/waveinflu/similar-creators). To find contact details for a creator, try [Waveinflu Email Lookup](/apis/waveinflu/email-lookup).

### Pricing

Billed at the actual cost of each call, about $0.124425 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/waveinflu/creator-search.json`](../../../catalog/models/waveinflu/creator-search.json) · Store page: https://www.sandbase.ai/model/waveinflu/creator-search
