# LinkedIn Post Comments API: pricing, parameters and code examples

`linkedin/web-v2/post-comments` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** sync

Returns comments for a specific LinkedIn post using its activity URN. Supports filtering by share URN, sorting by relevance or recency, and paginating through results.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/web-v2/post-comments", "urn": "7267273010393358336"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/web-v2/post-comments', {'urn': '7267273010393358336'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/web-v2/post-comments", {
  "urn": "7267273010393358336"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/web-v2/post-comments", sandbase.Params{
	"urn": "7267273010393358336",
})
```

Same call via the path form: `POST /v1/api/linkedin/web-v2/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `urn` | string | yes | Post activity urn (the numeric part of .../urn:li:activity:<urn>/).  |
| `page` |  |  | Page number, starting at 1.  |
| `sort_by` |  |  | Most relevant (default) or Most recent.  |
| `share_urn` |  |  | Optional share urn for shared posts.  |
| `pagination_token` |  |  | Token returned by the previous response.  |

## Details

Retrieve comments for a LinkedIn post by providing the target activity identifier in `urn`. You can sort by recency or relevance and navigate multi-page discussions.

### Use cases

- Review audience feedback and replies on specific LinkedIn posts.
- Monitor post discussions sorted by either recency or relevance.
- Ingest comment threads across multiple pages using pagination tokens.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/web-v2/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"urn": "<urn>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `urn` | string | Yes | Post activity urn (the numeric part of .../urn:li:activity:<urn>/). |
| `page` | string | No | Page number, starting at 1. |
| `sort_by` | string | No | Most relevant (default) or Most recent. |
| `share_urn` | string | No | Optional share urn for shared posts. |
| `pagination_token` | string | No | Token returned by the previous response. |

### Notes

- Provide the numeric portion of urn:li:activity:<urn> in `urn`.
- Sort options for `sort_by` include Most relevant (default) and Most recent.
- Pagination is handled via `page` starting at 1 or by passing `pagination_token` from previous responses.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [LinkedIn Company Posts](/model/linkedin/web-v2/company-posts): Returns posts from a LinkedIn organization page using the company URL.
- [LinkedIn Company Profile](/model/linkedin/web-v2/company-profile): Returns LinkedIn company profile details, including affiliated organizations, using a direct company page URL.
- [LinkedIn Job Details](/model/linkedin/web-v2/job-detail): Returns detailed information for a specific LinkedIn job posting via its URL.

---
Machine-readable: [`catalog/models/linkedin/web-v2/post-comments.json`](../../../../catalog/models/linkedin/web-v2/post-comments.json) · Store page: https://www.sandbase.ai/model/linkedin/web-v2/post-comments
