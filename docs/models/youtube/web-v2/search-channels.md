# YouTube Channel Search API: pricing, parameters and code examples

`youtube/web-v2/search-channels` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches YouTube channels by query terms and returns channel listings. Supports paginated results using continuation tokens and optional data formatting.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/search-channels"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/search-channels', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/search-channels", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/search-channels", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/search-channels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` |  |  | Search keyword (required for first request)  |
| `need_format` | boolean |  | Whether to format data (default true) default `true` |
| `continuation_token` | string |  | Pagination token (optional, for next page)  |

## Details

Query YouTube channels matching a specific `keyword`. Use `continuation_token` to retrieve subsequent pages of results.

### Use cases

- Discover YouTube channels matching specific keywords or brand names.
- Gather channel search results for creator discovery workflows.
- Page through multi-page channel query listings using continuation tokens.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/search-channels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search keyword (required for first request) |
| `need_format` | boolean | No | Whether to format data (default true) |
| `continuation_token` | string | No | Pagination token (optional, for next page) |

### Notes

- `keyword` is required for the initial request.
- Use `continuation_token` to fetch the next page of search results.
- `need_format` defaults to true to format returned data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/search-channels.json`](../../../../catalog/models/youtube/web-v2/search-channels.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/search-channels
