# Shorts search (raw data, recommend V2) API: pricing, parameters and code examples

`youtube/web-v2/shorts-search` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

YouTube Shorts specialized search using native YouTube API.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/shorts-search", "search_query": "Python编程"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/shorts-search', {'search_query': 'Python编程'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/shorts-search", {
  "search_query": "Python编程"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/shorts-search", sandbase.Params{
	"search_query": "Python编程",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/shorts-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort_by` |  |  | Sort by for Shorts  |
| `time_zone` | string |  | Time zone (e.g., America/Los_Angeles, Asia/Shanghai) default `"America/Los_Angeles"` |
| `upload_time` |  |  | Upload time filter for Shorts  |
| `country_code` | string |  | Country code affecting regional relevance default `"US"` |
| `search_query` | string | yes | Search keyword  |
| `language_code` | string |  | Language code (zh-CN for Chinese, en-US for English) default `"en-US"` |
| `continuation_token` |  |  | Pagination token  |
| `filter_mixed_content` | boolean |  | Whether to filter long videos from mixed content (default true) default `true` |

## Details

YouTube Shorts specialized search using native YouTube API. It is suitable for youtube workflows.

### Capability

YouTube Shorts specialized search using native YouTube API. It helps applications, agents, and automated workflows turn that capability into repeatable tasks and useful downstream experiences.

### Common use cases

- Search and discover relevant records for research, monitoring, and product experiences.
- Create repeatable integrations that pass structured results to downstream business systems.
- Support scheduled jobs, internal tools, and agent workflows with structured results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/shorts-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_query": "NASA"}'
```

The result is returned in `outputs[0].data` in YouTube's own response format.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sort_by` | string | No | Sort by for Shorts. |
| `time_zone` | string | No | Time zone (e.g., America/Los_Angeles, Asia/Shanghai). Default `America/Los_Angeles`. |
| `upload_time` | string | No | Upload time filter for Shorts. |
| `country_code` | string | No | Country code affecting regional relevance. Default `US`. |
| `search_query` | string | Yes | Search keyword. |
| `language_code` | string | No | Language code (zh-CN for Chinese, en-US for English). Default `en-US`. |
| `continuation_token` | string | No | Pagination token. |
| `filter_mixed_content` | boolean | No | Whether to filter long videos from mixed content (default `true`). |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/youtube/web-v2/shorts-search.json`](../../../../catalog/models/youtube/web-v2/shorts-search.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/shorts-search
