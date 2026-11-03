# Twitter (X) Trending Topics API: pricing, parameters and code examples

`twitter/web/trending` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get trending topics on Twitter / X by country: trend names with their category context, for the United States, Japan, India, the UK and other markets.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/trending"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/trending', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/trending", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/trending", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/twitter/web/trending` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `country` | string |  | Country, default is UnitedStates, other optional values are as follows: China; India; Japan; Russia; Germany; Indonesia; Brazil; France; UnitedKingdom; Turkey; Italy; Mexico; SouthKorea; Canada; Spain; SaudiArabia;… default `"UnitedStates"` |

## Details

Returns the current list of trending topics on Twitter (X) for one country. The only input is the optional `country` parameter, which defaults to `UnitedStates`.

### Use cases

- Check which topics trend in Japan, India or the UK at the moment you call.
- Flag a brand or keyword when its name appears in the `name` field of a trend.
- Group trends by their `context` label, such as NFL, to see which categories dominate a market.
- Pick topics to search for or write about while they trend.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/trending" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country` | string | No | Country, default is UnitedStates, other optional values are as follows: China; India; Japan; Russia; Germany; Indonesia; Brazil; France; UnitedKingdom; Turkey; Italy; Mexico; SouthKorea; Canada; Spain; SaudiArabia; Egypt |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "trends": [
    {
      "context": "NFL · Trending",
      "description": null,
      "name": "Bears"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `trends[]` | List of trending topics for the chosen country. |
| `trends[].name` | The trend text as shown on X, for example a team, person or hashtag. |
| `trends[].context` | Short label that shows where the trend sits, for example `NFL · Trending`. The part before the dot names the category. |
| `trends[].description` | Extra text about the trend. It is `null` when none is given. |

### Notes

- Pass `country` as a full name without spaces, such as `UnitedStates`, `UnitedKingdom`, `SouthKorea` or `SaudiArabia`. An empty request returns `UnitedStates`.
- The response has no pagination, tweet counts or rank field. The order of `trends` is the order returned.
- To see posts about a trend, pass its `name` to [Twitter (X) Search](/apis/twitter/web/search-timeline).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Twitter (X) Search](/apis/twitter/web/search-timeline): Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).
- [Twitter Tweet Detail](/apis/twitter/web/tweet-detail): Get a single tweet (X post) by ID: full text, author, media, and like, retweet, reply, quote, bookmark and view counts.
- [Twitter (X) User Profile](/apis/twitter/web/user-profile): Get a Twitter / X user profile by screen name or user ID: name, bio, follower and following counts, post and media counts, verification and creation date.

---
Machine-readable: [`catalog/models/twitter/web/trending.json`](../../../../catalog/models/twitter/web/trending.json) · Store page: https://www.sandbase.ai/model/twitter/web/trending
