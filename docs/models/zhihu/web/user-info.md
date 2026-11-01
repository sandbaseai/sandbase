# Zhihu Web User Profile

`zhihu/web/user-info` · api · Zhihu

Retrieves public profile metrics and details for a Zhihu user. Returns article counts, answer counts, follower totals, and user account metadata.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/user-info", "user_url_token": "ming-he-43-93"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/user-info', {'user_url_token': 'ming-he-43-93'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/user-info", {
  "user_url_token": "ming-he-43-93"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/user-info", sandbase.Params{
	"user_url_token": "ming-he-43-93",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_url_token` | string | yes | User ID  |

## Details

Access public Zhihu user account metrics by specifying a user token in `user_url_token`. This endpoint returns summary statistics including follower count, article count, and answer count.

### Use cases

- Analyze user audience size and engagement metrics on Zhihu.
- Retrieve author details and content publication totals.
- Display Zhihu creator profile statistics within external dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_url_token": "ming-he-43-93"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_url_token` | string | Yes | User ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "answer_count": 9,
  "articles_count": 87,
  "available_medals_count": 0,
  "follower_count": 2830,
  "follower_count_num": "2830",
  "follower_count_text": "2830",
  "id": "bd76ac15154a7024a8adbcc2997efc8d",
  "name": "洺河",
  "project_count": 0,
  "type": "people",
  "url": "https://www.zhihu.com/api/v4/people/ming-he-43-93",
  "user_type": "people"
}
```

### Notes

- Requires the Zhihu profile slug passed via `user_url_token`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/user-info.json`](../../../../catalog/models/zhihu/web/user-info.json) · Store page: https://www.sandbase.ai/model/zhihu/web/user-info
