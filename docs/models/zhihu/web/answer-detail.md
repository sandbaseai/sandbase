# Zhihu Answer Details API: pricing, parameters and code examples

`zhihu/web/answer-detail` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/answer-detail", "answer_id": "2054145988235880002"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/answer-detail', {'answer_id': '2054145988235880002'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/answer-detail", {
  "answer_id": "2054145988235880002"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/answer-detail", sandbase.Params{
	"answer_id": "2054145988235880002",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/answer-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `answer_id` | string | yes | Answer ID (the numeric id in the page URL .../answer/{answer_id})  |

## Details

Retrieves full content and metadata for an individual Zhihu answer using `answer_id`. It returns details such as the body text, timestamps, and answer URL.

### Use cases

- Extract the full text content of a Zhihu response.
- Retrieve posting timestamps and URLs for archiving purposes.
- Collect answer metadata for content analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/answer-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"answer_id": "2054145988235880002"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `answer_id` | string | Yes | Answer ID (the numeric id in the page URL .../answer/{answer_id}) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "answer_type": "normal",
  "content": "我哥是万年老二，再一次输给傅寒澈，他说他得了绝症。「妹！哥没多少日子了，哥这辈子就想赢傅寒澈一次，就一次！」看着我哥省吃俭用刚给我买的限量款包包，我咽了咽口水。「哥，您说话！」我…",
  "content_need_truncated": false,
  "created_time": 1782526567,
  "id": "2054145988235880002",
  "share_text": "有没有一上来就很刺激的甜文！? - 回答作者: 白泽丧葬用品店 https://zhihu.com/question/5721660615/answer/205414598823…",
  "type": "answer",
  "updated_time": 1782526567,
  "url": "https://www.zhihu.com/api/v4/answers/2054145988235880002"
}
```

### Notes

- Locate the `answer_id` from the numeric segment in the Zhihu answer URL path.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…
- [Zhihu Column Article Detail](/model/zhihu/web/column-article-detail): Returns detailed information and metadata for a specific Zhihu column article, including author profile details, using a provided article ID.

---
Machine-readable: [`catalog/models/zhihu/web/answer-detail.json`](../../../../catalog/models/zhihu/web/answer-detail.json) · Store page: https://www.sandbase.ai/model/zhihu/web/answer-detail
