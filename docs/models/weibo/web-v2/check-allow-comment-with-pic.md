# Weibo Image Comment Permission Check API: pricing, parameters and code examples

`weibo/web-v2/check-allow-comment-with-pic` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Checks whether a specific Weibo post permits image attachments in user comments. Returns the image comment eligibility status using the provided post ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/check-allow-comment-with-pic", "id": "5092682368025584"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/check-allow-comment-with-pic', {'id': '5092682368025584'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/check-allow-comment-with-pic", {
  "id": "5092682368025584"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/check-allow-comment-with-pic", sandbase.Params{
	"id": "5092682368025584",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/check-allow-comment-with-pic` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Weibo post ID (required)  |

## Details

Determines whether image comments are permitted on a given post by querying the target post `id`.

### Use cases

- Check if image attachments are supported before displaying media upload options.
- Verify post comment permissions across monitored Weibo threads.
- Filter target posts based on their image comment eligibility status.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/check-allow-comment-with-pic" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "5092682368025584"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Weibo post ID (required) |

### Notes

- The `id` parameter specifies the target Weibo post ID.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/check-allow-comment-with-pic.json`](../../../../catalog/models/weibo/web-v2/check-allow-comment-with-pic.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/check-allow-comment-with-pic
