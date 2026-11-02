# Weibo All Groups Information API: pricing, parameters and code examples

`weibo/web-v2/all-groups` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves complete group information on the Weibo platform. Returns details for both default system groups and user-defined custom groups.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/all-groups"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/all-groups', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/all-groups", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/all-groups", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/all-groups` with the body above minus `model`.

## Details

Access complete group details across the Weibo platform. This endpoint requires no input parameters and returns both default and custom groups.

### Use cases

- Display available default and custom groups in a Weibo management interface.
- Inspect user-defined group categories for targeted content organization.
- Map group structures across accounts to analyze audience segmentation.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/all-groups" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/all-groups.json`](../../../../catalog/models/weibo/web-v2/all-groups.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/all-groups
