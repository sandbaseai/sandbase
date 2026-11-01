# Weibo Post Detail

`weibo/web-v2/post-detail` · api · Weibo

Get the full data of a single Weibo post by its ID: text (including long posts), author, publish time, location and repost, comment and like counts.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/post-detail", "id": "5350731756601957", "is_get_long_text": "true"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/post-detail', {'id': '5350731756601957', 'is_get_long_text': 'true'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/post-detail", {
  "id": "5350731756601957",
  "is_get_long_text": "true"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/post-detail", sandbase.Params{
	"id": "5350731756601957",
	"is_get_long_text": "true",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Weibo post ID (required)  |
| `is_get_long_text` | string |  | Whether to get full text of long posts (default "true") default `"true"` |

## Details

Pass a Weibo post ID and get back the complete post as JSON: the full text, author profile, publish time and region, attached images, and engagement counts.

### Use cases

- Track how a specific post performs over time (reposts, comments, likes).
- Archive posts referenced in news or brand monitoring.
- Enrich search results from the Weibo search APIs with full post details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "5350554563773695"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Weibo post ID (required) |
| `is_get_long_text` | string | No | Whether to get full text of long posts (default "true") |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "id": 5350554563773695,
  "mblogid": "Rld9CfPI3",
  "created_at": "Mon Oct 05 07:04:39 +0800 2026",
  "reposts_count": 40,
  "comments_count": 34,
  "attitudes_count": 151,
  "region_name": "发布于 美国",
  "text_raw": "OpenAI Codex 承诺连续 28 天：每天上新，否则重置额度  OpenAI 给 Codex 用户立了个 28 天的规矩：每天要么上线一项多数人用得上…",
  "user": {
    "screen_name": "<user>"
  }
}
```

### Notes

- The post ID is the numeric `id` / `mid`, or the `weibo_id` returned by Weibo search.
- Long posts are expanded to full text by default (`is_get_long_text` = `"true"`).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Hot Search List](/model/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.
- [Weibo AI Search Content Extension](/model/weibo/web-v2/ai-related-search): Get content extensions related to keyword (related questions, blogger recommendations, reference posts).

---
Machine-readable: [`catalog/models/weibo/web-v2/post-detail.json`](../../../../catalog/models/weibo/web-v2/post-detail.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/post-detail
