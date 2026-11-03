# Weibo Recommended Homepage Feed API: pricing, parameters and code examples

`weibo/web-v2/user-recommend-timeline` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended timeline posts from the Weibo homepage feed. Supports filtering by group ID or container ID, custom feed counts, refresh types, and cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-recommend-timeline"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-recommend-timeline', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-recommend-timeline", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-recommend-timeline", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-recommend-timeline` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count (default 10, suggested 5-20)  |
| `max_id` | string |  | Pagination cursor, pass "0" for first request  |
| `refresh` | integer |  | Refresh type (0=normal refresh, 1=force refresh)  |
| `extparam` | string |  | Extended parameters (default "discover\|new_feed")  |
| `group_id` | string |  | Group ID (can be obtained through fetch_all_groups)  |
| `containerid` | string |  | Container ID (usually same as group_id)  |

## Details

Retrieve personalized recommended feed posts from the Weibo homepage. Use `max_id` for pagination, `count` to specify batch size, and `group_id` or `containerid` to target specific groups.

### Use cases

- Display personalized Weibo homepage posts in external reader applications.
- Analyze trending and recommended status items across feed streams.
- Monitor engagement metrics including comment and attitude counts on suggested posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-recommend-timeline" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Count (default 10, suggested 5-20) |
| `max_id` | string | No | Pagination cursor, pass "0" for first request |
| `refresh` | integer | No | Refresh type (0=normal refresh, 1=force refresh) |
| `extparam` | string | No | Extended parameters (default "discover/new_feed") |
| `group_id` | string | No | Group ID (can be obtained through fetch_all_groups) |
| `containerid` | string | No | Container ID (usually same as group_id) |

### Notes

- Pass `0` to `max_id` on the initial request for pagination.
- Set `refresh` to `0` for normal refresh or `1` for force refresh.
- Obtain `group_id` values via fetch_all_groups, noting that `containerid` is usually identical.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-recommend-timeline.json`](../../../../catalog/models/weibo/web-v2/user-recommend-timeline.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-recommend-timeline
