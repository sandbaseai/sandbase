# YouTube Channel Description API: pricing, parameters and code examples

`youtube/web-v2/channel-description` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links. Filter by country and language.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/channel-description", "channel_id": "UCeu6U67OzJhV1KwBansH3Dg", "country_code": "US", "language_code": "zh-CN", "need_format": true}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/channel-description', {'channel_id': 'UCeu6U67OzJhV1KwBansH3Dg', 'country_code': 'US', 'language_code': 'zh-CN', 'need_format': True})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/channel-description", {
  "channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
  "country_code": "US",
  "language_code": "zh-CN",
  "need_format": true
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/channel-description", sandbase.Params{
	"channel_id": "UCeu6U67OzJhV1KwBansH3Dg",
	"country_code": "US",
	"language_code": "zh-CN",
	"need_format": true,
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/channel-description` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string |  | **Purpose**: Channel ID for first request to get basic channel info  |
| `need_format` | boolean |  | **Purpose**: Whether to return cleaned simplified data default `true` |
| `country_code` | string |  | **Purpose**: Set region code default `"US"` |
| `language_code` | string |  | **Purpose**: Set language preference default `"zh-CN"` |
| `continuation_token` | string |  | **Purpose**: Pagination token for second request to get advanced info  |

## Details

Look up metadata and profile details for a YouTube channel using `channel_id`. Supports regional localization and pagination via `continuation_token`.

### Use cases

- Retrieve channel statistics such as view counts and subscriber metrics.
- Extract social links and about-page text from channel profiles.
- Review channel join dates and metadata localized by region or language.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/channel-description" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCeu6U67OzJhV1KwBansH3Dg", "language_code": "zh-CN", "country_code": "US"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | No | Purpose: Channel ID for first request to get basic channel info |
| `need_format` | boolean | No | Purpose: Whether to return cleaned simplified data |
| `country_code` | string | No | Purpose: Set region code |
| `language_code` | string | No | Purpose: Set language preference |
| `continuation_token` | string | No | Purpose: Pagination token for second request to get advanced info |

### Notes

- Set `need_format` to true to receive cleaned, simplified channel data.
- Supply `continuation_token` on follow-up calls to fetch advanced information.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.
- [YouTube Channel Shorts](/apis/youtube/web-v2/channel-shorts): Returns a list of YouTube Shorts from a specified channel.

---
Machine-readable: [`catalog/models/youtube/web-v2/channel-description.json`](../../../../catalog/models/youtube/web-v2/channel-description.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/channel-description
