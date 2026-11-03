# Weibo App AI Smart Search API: pricing, parameters and code examples

`weibo/app/ai-smart-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/ai-smart-search", "page": 1, "query": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/ai-smart-search', {'page': 1, 'query': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/ai-smart-search", {
  "page": 1,
  "query": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/ai-smart-search", sandbase.Params{
	"page": 1,
	"query": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/weibo/app/ai-smart-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starts from 1 (default 1) default `1`; range 1– |
| `query` | string | yes | Search keyword (required)  |

## Details

Retrieves AI search channel data from Weibo for a given `query`. Results can be navigated across pages using `page`.

### Use cases

- Explore Weibo AI search feed channels for specific keywords.
- Collect search metadata and timestamps for topic monitoring.
- Track keyword results across app search channels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/ai-smart-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required) |
| `page` | integer | No | Page number, starts from 1 (default 1) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "channelInfo": {
    "channels": [
      {
        "pageDataType": "flow",
        "title": "综合",
        "params": {
          "search_time": 1791290327
        }
      }
    ]
  }
}
```

### Notes

- `query` is required to execute the search.
- `page` starts at 1 and defaults to 1.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.
- [Weibo Hot Search Categories](/apis/weibo/app/hot-search-categories): Returns all available hot search categories from Weibo.

---
Machine-readable: [`catalog/models/weibo/app/ai-smart-search.json`](../../../../catalog/models/weibo/app/ai-smart-search.json) · Store page: https://www.sandbase.ai/model/weibo/app/ai-smart-search
