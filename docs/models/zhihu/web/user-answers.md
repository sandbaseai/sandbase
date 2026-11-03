# Zhihu User Answers API: pricing, parameters and code examples

`zhihu/web/user-answers` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns answers posted by a specific Zhihu user based on their user token. Supports pagination and sorting results by creation date or upvote count.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/user-answers", "user_url_token": "ren-gong-zhi-neng-90"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/user-answers', {'user_url_token': 'ren-gong-zhi-neng-90'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/user-answers", {
  "user_url_token": "ren-gong-zhi-neng-90"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/user-answers", sandbase.Params{
	"user_url_token": "ren-gong-zhi-neng-90",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/user-answers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of answers per page  |
| `offset` | string |  | Offset  |
| `sort_type` | string |  | Sort Type one of: `created`, `voteups` |
| `user_url_token` | string | yes | User ID  |

## Details

Returns the answers a Zhihu user has posted, looked up by the user's URL token. The response holds a list of answers plus paging details. You can sort by creation date or upvote count.

### Use cases

- Pull the most upvoted answers of a Zhihu author with `sort_type` set to `voteups`.
- Check a Zhihu expert for new answers by sorting with `created`.
- Page through an author's full answer history for profile research.
- Check how many answers a Zhihu user has from `paging.totals` before fetching them all.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/user-answers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_url_token": "excited-vczh"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_url_token` | string | Yes | User ID |
| `limit` | string | No | Number of answers per page |
| `offset` | string | No | Offset |
| `sort_type` | string | No | Sort Type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [],
  "need_force_login": false,
  "paging": {
    "is_end": true,
    "is_start": true,
    "next": "http://www.zhihu.com/api/v4/members/excited-vczh/answers?user_url_token=excited-…",
    "previous": "http://www.zhihu.com/api/v4/members/excited-vczh/answers?user_url_token=excited-…",
    "totals": 7
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data` | List of answers for the requested page. It is an empty list in the sample response, even though `paging.totals` is 7. |
| `paging.totals` | Total count of answers the API reports for this user. |
| `paging.is_end` | `true` when the current page is the last page. |
| `paging.is_start` | `true` when the current page is the first page. |
| `paging.next` | URL for the next page. It carries the `limit` and `offset` values to use next. |
| `paging.previous` | URL for the previous page, with its `limit` and `offset` values. |
| `need_force_login` | Flag that shows whether the request needs a logged-in session. It is `false` in the sample. |

### Notes

- Take `user_url_token` from the Zhihu profile URL of the user, for example `excited-vczh`.
- Page with `limit` and `offset`. The `paging.next` URL in the sample uses `limit=20` and `offset=20`.
- Stop paging when `paging.is_end` is `true`.
- To get the full text of one answer, call [Zhihu Answer Details](/apis/zhihu/web/answer-detail) with its numeric ID. For the author's profile, use [Zhihu Web User Profile](/apis/zhihu/web/user-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/user-answers.json`](../../../../catalog/models/zhihu/web/user-answers.json) · Store page: https://www.sandbase.ai/model/zhihu/web/user-answers
