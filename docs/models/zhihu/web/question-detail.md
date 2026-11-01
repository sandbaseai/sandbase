# Zhihu Question Detail

`zhihu/web/question-detail` · api · Zhihu

Retrieves question information on Zhihu using a question ID. Returns the question title, answer counts, comment counts, follower counts, and view statistics.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/question-detail", "question_id": "37811449"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/question-detail', {'question_id': '37811449'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/question-detail", {
  "question_id": "37811449"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/question-detail", sandbase.Params{
	"question_id": "37811449",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/question-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `question_id` | string | yes | Question ID  |

## Details

Look up metadata and engagement metrics for a specific Zhihu discussion via its `question_id`. It returns headline details alongside visit, answer, and follower statistics.

### Use cases

- Analyze engagement levels and visit counts for specific Zhihu questions.
- Track answer and follower counts across platform discussions over time.
- Extract question titles and discussion metadata for content research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/question-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"question_id": "37811449"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `question_id` | string | Yes | Question ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "answer_count": 90,
  "answer_count_description": "全部内容 90",
  "comment_count": 9,
  "follower_count": 2912,
  "id": "37811449",
  "question_type": "normal",
  "title": "有哪些优雅的 Windows 10 壁纸？",
  "type": "question",
  "updated_time": 1521972248,
  "url": "https://www.zhihu.com/api/v4/questions/37811449",
  "visit_count": 3350451
}
```

### Notes

- Requires a valid `question_id` to look up discussion details.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/question-detail.json`](../../../../catalog/models/zhihu/web/question-detail.json) · Store page: https://www.sandbase.ai/model/zhihu/web/question-detail
