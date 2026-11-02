# Twitter Post Comments API: pricing, parameters and code examples

`twitter/post-comments` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get the latest comments for an X (Twitter) post identified by tweet ID, with cursor pagination. Use it to review recent discussion on a known post and continue through additional comment pages.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/post-comments", "tweetId": "1585341984679469056"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/post-comments', {'tweetId': '1585341984679469056'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/post-comments", {
  "tweetId": "1585341984679469056"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/post-comments", sandbase.Params{
	"tweetId": "1585341984679469056",
})
```

Same call via the path form: `POST /v1/api/twitter/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor returned by the previous response.  |
| `tweetId` | string | yes | The unique identifier of the X (Twitter) post.  |

## Details

Get the latest comments for an X (Twitter) post identified by tweet ID, with cursor pagination. Use it to review recent discussion on a known post and continue through additional comment pages.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweetId": "1585341984679469056"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweetId` | string | Yes | The unique identifier of the X (Twitter) post. |
| `cursor` | string | No | Pagination cursor returned by the previous response. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/twitter/post-comments.json`](../../../catalog/models/twitter/post-comments.json) · Store page: https://www.sandbase.ai/model/twitter/post-comments
