# YouTube Post Comment Replies API: pricing, parameters and code examples

`youtube/web-v2/post-comment-replies` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns second-level comment replies for a YouTube post. Supports pagination using continuation tokens, along with optional country and language localization settings.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/post-comment-replies", "continuation_token": "<continuation_token>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/post-comment-replies', {'continuation_token': '<continuation_token>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/post-comment-replies", {
  "continuation_token": "<continuation_token>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/post-comment-replies", sandbase.Params{
	"continuation_token": "<continuation_token>",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/post-comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to format data, default `true`  |
| `country_code` | string |  | Country code, default `"US"`  |
| `language_code` | string |  | Language code, default `"zh-CN"`  |
| `continuation_token` | string | yes | Next page token (if more replies)  |

## Details

Retrieve second-level replies for a post comment using `continuation_token`. Optional parameters include `country_code`, `language_code`, and `need_format`.

### Use cases

- Display nested discussion threads under community post comments.
- Analyze conversation chains and follow-up viewer interactions.
- Paginate through reply threads for comprehensive sentiment monitoring.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/post-comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"continuation_token": "<continuation_token>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `continuation_token` | string | Yes | Next page token (if more replies) |
| `need_format` | boolean | No | Whether to format data, default `true` |
| `country_code` | string | No | Country code, default `"US"` |
| `language_code` | string | No | Language code, default `"zh-CN"` |

### Notes

- `continuation_token` is required to paginate through subsequent comment replies.
- `country_code` defaults to `"US"` and `language_code` defaults to `"zh-CN"`.
- `need_format` determines whether to format the data and defaults to `true`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/post-comment-replies.json`](../../../../catalog/models/youtube/web-v2/post-comment-replies.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/post-comment-replies
