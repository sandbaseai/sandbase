# General search (raw data, recommend V2) API: pricing, parameters and code examples

`youtube/web-v2/general-search` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

YouTube comprehensive search with multiple filter options for precise result filtering.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/general-search", "search_query": "NASA"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/general-search', {'search_query': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/general-search", {
  "search_query": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/general-search", sandbase.Params{
	"search_query": "NASA",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/general-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `feature` |  |  | Feature filter  |
| `sort_by` |  |  | Sort by  |
| `duration` |  |  | Duration filter  |
| `time_zone` | string |  | Time zone setting default `"America/Los_Angeles"` |
| `upload_time` |  |  | Upload time filter  |
| `content_type` |  |  | Content type filter  |
| `country_code` | string |  | Country code affecting regional relevance default `"US"` |
| `search_query` | string | yes | Search keyword  |
| `language_code` | string |  | Language code (zh-CN for Chinese, en-US for English) default `"zh-CN"` |
| `continuation_token` |  |  | Pagination token  |

## Details

YouTube comprehensive search with multiple filter options for precise result filtering. It is suitable for youtube workflows.

### Capability

YouTube comprehensive search with multiple filter options for precise result filtering. It helps applications, agents, and automated workflows turn that capability into repeatable tasks and useful downstream experiences.

### Common use cases

- Search and discover relevant records for research, monitoring, and product experiences.
- Create repeatable integrations that pass structured results to downstream business systems.
- Support scheduled jobs, internal tools, and agent workflows with structured results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/general-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_query": "NASA"}'
```

The result is returned in `outputs[0].data` in YouTube's own response format.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `feature` | string | No | Feature filter. |
| `sort_by` | string | No | Sort by. |
| `duration` | string | No | Duration filter. |
| `time_zone` | string | No | Time zone setting. Default `America/Los_Angeles`. |
| `upload_time` | string | No | Upload time filter. |
| `content_type` | string | No | Content type filter. |
| `country_code` | string | No | Country code affecting regional relevance. Default `US`. |
| `search_query` | string | Yes | Search keyword. |
| `language_code` | string | No | Language code (zh-CN for Chinese, en-US for English). Default `zh-CN`. |
| `continuation_token` | string | No | Pagination token. |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/youtube/web-v2/general-search.json`](../../../../catalog/models/youtube/web-v2/general-search.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/general-search
