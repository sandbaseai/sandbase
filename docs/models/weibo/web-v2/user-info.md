# Weibo User Profile Details (Web V2) API: pricing, parameters and code examples

`weibo/web-v2/user-info` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed Weibo user profile information including nickname, avatar, bio, following count, and followers count by user ID or custom username.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-info", "uid": "2062052743"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-info', {'uid': '2062052743'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-info", {
  "uid": "2062052743"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-info", sandbase.Params{
	"uid": "2062052743",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` |  |  | User ID (optional, choose one with custom)  |
| `custom` |  |  | Custom username (optional, choose one with uid)  |

## Details

Retrieve detailed profile metrics and public information for a Weibo user using `uid` or `custom`.

### Use cases

- Look up Weibo account metrics such as follower counts and following counts.
- Display user avatar, nickname, and biography details in user dashboards.
- Verify Weibo public profiles using either account IDs or custom usernames.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | No | User ID (optional, choose one with custom) |
| `custom` | string | No | Custom username (optional, choose one with uid) |

### Notes

- Provide either `uid` or `custom` to identify the target account.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-info.json`](../../../../catalog/models/weibo/web-v2/user-info.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-info
