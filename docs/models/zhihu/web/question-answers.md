# Zhihu Question Answers API: pricing, parameters and code examples

`zhihu/web/question-answers` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of answers for a specified Zhihu question. Supports pagination through cursor or offset parameters and sorting by time or default rank.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/question-answers", "limit": 20, "question_id": "2089412797440455404"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/question-answers', {'limit': 20, 'question_id': '2089412797440455404'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/question-answers", {
  "limit": 20,
  "question_id": "2089412797440455404"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/question-answers", sandbase.Params{
	"limit": 20,
	"question_id": "2089412797440455404",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/question-answers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of answers per page, default 5  |
| `order` | string |  | Sort order, default=default sort, updated=sort by time  |
| `cursor` | string |  | Pagination cursor for next page, extracted from response fields  |
| `offset` | integer |  | Offset, default 0  |
| `session_id` | string |  | Session ID for pagination state, extracted from response fields  |
| `question_id` | string | yes | Question ID  |

## Details

Retrieve answers submitted to a Zhihu question using its `question_id`. Responses support pagination via `cursor`, `offset`, and `session_id`.

### Use cases

- Read answers submitted to a specific Zhihu question.
- Track community responses to relevant discussion topics over time.
- Gather public discussions and viewpoints for topic analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/question-answers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"question_id": "<question_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `question_id` | string | Yes | Question ID |
| `limit` | integer | No | Number of answers per page, default 5 |
| `order` | string | No | Sort order, default=default sort, updated=sort by time |
| `cursor` | string | No | Pagination cursor for next page, extracted from response fields |
| `offset` | integer | No | Offset, default 0 |
| `session_id` | string | No | Session ID for pagination state, extracted from response fields |

### Notes

- Use `cursor` and `session_id` values extracted from response fields to page through results.
- The `limit` parameter controls how many answers return per page and defaults to 5.
- The `offset` parameter defaults to 0 for index-based pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/question-answers.json`](../../../../catalog/models/zhihu/web/question-answers.json) · Store page: https://www.sandbase.ai/model/zhihu/web/question-answers
