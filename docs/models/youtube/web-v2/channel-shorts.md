# YouTube Channel Shorts API: pricing, parameters and code examples

`youtube/web-v2/channel-shorts` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a list of YouTube Shorts from a specified channel. Supports lookups by channel identifier or URL, optional response formatting, and pagination tokens for next-page results.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/channel-shorts"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/channel-shorts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/channel-shorts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/channel-shorts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/channel-shorts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string |  | Channel ID (recommended, e.g., UCuAXFkgsw1L7xaCfnd5JJOw)  |
| `channel_url` | string |  | Channel URL (optional, ignored if channel_id is provided)  |
| `need_format` | boolean |  | Whether to format data (default true) default `true` |
| `continuation_token` | string |  | Pagination token (optional, for next page)  |

## Details

Retrieve short videos from a YouTube channel using `channel_id` or `channel_url`. Pass a `continuation_token` to browse subsequent pages of Shorts.

### Use cases

- Track newly posted Shorts from target YouTube channels.
- Analyze short-form video output across a creator portfolio.
- Collect channel Shorts feeds for media aggregation platforms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/channel-shorts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | No | Channel ID (recommended, e.g., UCuAXFkgsw1L7xaCfnd5JJOw) |
| `channel_url` | string | No | Channel URL (optional, ignored if channel_id is provided) |
| `need_format` | boolean | No | Whether to format data (default true) |
| `continuation_token` | string | No | Pagination token (optional, for next page) |

### Notes

- `channel_url` is ignored if `channel_id` is provided.
- `continuation_token` enables pagination to fetch subsequent pages of results.
- `need_format` defaults to true to control whether output data is formatted.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/channel-shorts.json`](../../../../catalog/models/youtube/web-v2/channel-shorts.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/channel-shorts
