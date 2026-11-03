# Zhihu Column Comment Configuration API: pricing, parameters and code examples

`zhihu/web/column-comment-config` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comment settings and options for a Zhihu column article based on the provided article identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/column-comment-config", "article_id": "669214677"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/column-comment-config', {'article_id': '669214677'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/column-comment-config", {
  "article_id": "669214677"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/column-comment-config", sandbase.Params{
	"article_id": "669214677",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/column-comment-config` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `article_id` | string | yes | Article ID  |

## Details

Access comment configurations for specific Zhihu column articles by providing the target `article_id`.

### Use cases

- Check comment configuration options for a Zhihu column article.
- Verify supported sync settings before submitting article feedback.
- Inspect article comment capabilities within Zhihu reader interfaces.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-comment-config" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"article_id": "669214677"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `article_id` | string | Yes | Article ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "setting": [
    {
      "id": "publish_sync_pin",
      "title": "同步到想法"
    }
  ]
}
```

### Notes

- Requires a valid `article_id` to retrieve settings.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-comment-config.json`](../../../../catalog/models/zhihu/web/column-comment-config.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-comment-config
