# Zhihu Answer Details API: pricing, parameters and code examples

`zhihu/web/answer-detail` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.

## Pricing

- **$0.001 per call** (USD)
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

Returns the full record for one Zhihu answer: the HTML body, an excerpt, timestamps, the author, the parent question and a share text. It needs one input, the numeric `answer_id` from the answer page URL.

### Use cases

- Archive the full HTML body of a Zhihu answer together with its `created_time` and `updated_time`.
- Link an answer back to its parent question using `question.id` and `question.title`.
- Collect author names and profile tokens for answers you have already found.
- Build share messages or citations from the ready-made `share_text` and `url` values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/answer-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"answer_id": "2054145988235880002"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `answer_id` | string | Yes | Answer ID (the numeric id in the page URL .../answer/{answer_id}) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "allow_segment_interaction": 1,
  "answer_type": "normal",
  "author": {
    "avatar_url": "https://picx.zhimg.com/v2-497a418999540453d381c2a22d40759c_l.jpg?source=2c26e567",
    "avatar_url_template": "https://pic1.zhimg.com/v2-497a418999540453d381c2a22d40759c.jpg?source=2c26e567",
    "badge": [],
    "badge_v2": {
      "detail_badges": [],
      "icon": "",
      "merged_badges": [],
      "night_icon": "",
      "title": "我不癫 文集搜索：《白泽合集》 天瞳搜：《天瞳大全》"
    },
    "gender": 0,
    "headline": "我不癫 文集搜索：《白泽合集》 天瞳搜：《天瞳大全》",
    "id": "974e867264de46d0cab4c9420eb421fc",
    "is_advertiser": false,
    "is_org": false,
    "is_privacy": false,
    "name": "白泽丧葬用品店",
    "type": "people"
  },
  "biz_ext": {
    "share_guide": {
      "has_positive_bubble": false,
      "has_time_bubble": false,
      "hit_share_guide_cluster": false
    }
  },
  "content": "<p data-pid=\"JjvPL_Bi\">我哥是万年老二，再一次输给傅寒澈，他说他得了绝症。</p><p data-pid=\"aQhuG9ar\">「妹！哥没…",
  "content_need_truncated": false,
  "created_time": 1782526567,
  "excerpt": "我哥是万年老二，再一次输给傅寒澈，他说他得了绝症。 「妹！哥没多少日子了，哥这辈子就想赢傅寒澈一次，就一次！」 看着我哥省吃俭用刚给我买的限量款包包，我咽了咽口…",
  "extras": "",
  "force_login_when_click_read_more": false,
  "id": "2054145988235880002",
  "is_collapsed": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `content` | Full answer body as HTML. Paragraphs are `<p>` tags with a `data-pid` attribute. |
| `excerpt` | Plain-text preview of the start of the answer. |
| `created_time / updated_time` | Unix timestamps for when the answer was created and last updated. The values look like seconds. |
| `id / type / answer_type` | The answer ID, the object type (`answer`) and the answer kind (for example `normal`). |
| `author.name / author.headline` | Display name and profile headline of the answer author. |
| `author.id / author.url_token` | Identifiers for the author. Use them to look up the author's profile or other answers. |
| `question.id / question.title` | ID and title of the question this answer belongs to. |
| `question.created / question.updated_time` | Unix timestamps for the parent question's creation and last update. |
| `share_text` | Ready-to-post text with the question title, author name and the public answer link. |
| `podcast_audio_enter.text` | Short label for the audio version of the answer, such as the number of listeners. |

### Notes

- Take `answer_id` from the number after `/answer/` in a Zhihu answer URL.
- `url` is an API address. The public page link is inside `share_text`, in the form `zhihu.com/question/{question_id}/answer/{answer_id}`.
- To list other answers to the same question, pass `question.id` to [Zhihu Question Answers](/apis/zhihu/web/question-answers).
- To read the discussion under an answer, use [Zhihu Answer Comments](/apis/zhihu/web/comment-v5).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…
- [Zhihu Column Article Detail](/apis/zhihu/web/column-article-detail): Returns detailed information and metadata for a specific Zhihu column article, including author profile details, using a provided article ID.

---
Machine-readable: [`catalog/models/zhihu/web/answer-detail.json`](../../../../catalog/models/zhihu/web/answer-detail.json) · Store page: https://www.sandbase.ai/model/zhihu/web/answer-detail
