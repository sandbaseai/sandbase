# Zhihu Question Detail API: pricing, parameters and code examples

`zhihu/web/question-detail` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves question information on Zhihu using a question ID. Returns the question title, answer counts, comment counts, follower counts, and view statistics.

## Pricing

- **$0.001 per call** (USD)
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

Returns metadata for one Zhihu question: its title, creation and update times, answer, comment and follower counts, and a visit count. It needs the `question_id` of the question.

### Use cases

- Track how `visit_count` and `follower_count` of a Zhihu question change across repeated calls.
- Pull the title and answer count of a question before deciding whether to collect its answers.
- Compare engagement across a list of questions on one topic, such as wallpapers or software.
- Check whether a question is still under review using the `review_info` flags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/question-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"question_id": "37811449"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `question_id` | string | Yes | Question ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "answer_count": 90,
  "answer_count_description": "全部内容 90",
  "comment_count": 9,
  "created": 1448289701,
  "detail": "",
  "excerpt": "",
  "follower_count": 2912,
  "id": "37811449",
  "question_type": "normal",
  "relationship": {
    "is_following": false
  },
  "review_info": {
    "edit_is_reviewing": false,
    "edit_tips": "",
    "is_reviewing": false,
    "tips": "",
    "type": ""
  },
  "title": "有哪些优雅的 Windows 10 壁纸？"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title` | The question title as shown on Zhihu. |
| `id` | The question ID, returned as a string. It matches the `question_id` you sent. |
| `answer_count` | Number of answers on the question. |
| `answer_count_description` | Text label for the answer count. In the example it reads `全部内容 90`. |
| `comment_count` | Number of comments on the question itself. |
| `follower_count` | Number of users following the question. |
| `visit_count` | Number of visits recorded for the question. |
| `created / updated_time` | Unix timestamps in seconds for when the question was created and last updated. |
| `question_type / type` | Kind of question and kind of object. The example returns `normal` and `question`. |
| `review_info.is_reviewing / review_info.edit_is_reviewing` | Flags that show whether the question or an edit to it is under review. |

### Notes

- The `question_id` is the number at the end of a Zhihu question URL, for example `37811449` in `https://www.zhihu.com/question/37811449`.
- `detail` and `excerpt` can come back as empty strings, as they do in the example.
- To read the answers themselves, call [Zhihu Question Answers](/apis/zhihu/web/question-answers) with the same question ID.
- To read a single answer in full, use [Zhihu Answer Details](/apis/zhihu/web/answer-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/question-detail.json`](../../../../catalog/models/zhihu/web/question-detail.json) · Store page: https://www.sandbase.ai/model/zhihu/web/question-detail
