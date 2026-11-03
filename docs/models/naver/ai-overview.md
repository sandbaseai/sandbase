# Naver AI Overview API: pricing, parameters and code examples

`naver/ai-overview` · data API · Naver · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Naver's AI-generated overview answer for a search query, with the cited sources.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "naver/ai-overview", "query": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('naver/ai-overview', {'query': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("naver/ai-overview", {
  "query": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "naver/ai-overview", sandbase.Params{
	"query": "coffee",
})
```

Same call via the path form: `POST /v1/api/naver/ai-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | param name inferred from sibling engine=naver, not independently confirmed  |

## Details

This API returns Naver's AI-generated overview answer for a search query. It needs one input, the search `query`. The response has the answer as Markdown and as structured text blocks, plus the cited sources.

### Use cases

- Show Naver's AI answer for a keyword next to your own search results.
- Collect the sources Naver cites for a topic to see which sites it favors.
- Track how the overview text for a brand or product keyword changes between runs.
- Feed the structured text blocks and their source links into a Korean-language research tool.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/naver/ai-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | param name inferred from sibling engine=naver, not independently confirmed |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "markdown": "커피는 커피나무 열매의 씨앗인 원두를 볶고 갈아 물에 타 마시는 음료로, 각성 효과를 주는 카페인을 함유하고 있습니다.[1]\n\n### 커피의 기…",
  "media": [
    {
      "link": "https://namu.wiki/w/%EC%BB%A4%ED%94%BC",
      "platform": "나무위키",
      "position": 1,
      "thumbnail": "https://i.namu.wiki/i/TJ2S7OjGghZz9-weVWcfWMStWAnmfwETnPV_vL1NnmkUBqUiDQvKOJ0Xtb…",
      "title": "커피 - 나무위키",
      "type": "image"
    }
  ],
  "references": [
    {
      "index": 1,
      "link": "https://namu.wiki/w/%EC%BB%A4%ED%94%BC",
      "snippet": "개요 Coffee 커피나무 열매의 씨앗(원두)을 볶아 향을 내고 , 딱딱한 씨앗의 성분이 물에 잘 우러나오도록 갈은 뒤, 물에 타서 마시는 음료…",
      "source": "나무위키",
      "source_icon": "https://namu.wiki/favicon.svg",
      "title": "커피 - 나무위키"
    }
  ],
  "text_blocks": [
    {
      "reference_indexes": [
        1
      ],
      "snippet": "커피는 커피나무 열매의 씨앗인 원두를 볶고 갈아 물에 타 마시는 음료로, 각성 효과를 주는 카페인을 함유하고 있습니다.",
      "type": "paragraph"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `markdown` | The full overview answer as one Markdown string. Citation markers such as `[1]` point to entries in `references`. |
| `text_blocks[].type` | The kind of block: `paragraph`, `header` or `list`. |
| `text_blocks[].snippet` | The text of a paragraph or header block. |
| `text_blocks[].reference_indexes` | The `index` values of the references that support this block. |
| `text_blocks[].list[].snippet / text_blocks[].list[].reference_indexes` | The text of one list item and the references that support it. Lists appear in blocks where `type` is `list`, and `list_type` tells you if the list is `unordered`. |
| `references[].index` | The number of the source. Match it to the citation markers in `markdown` and to `reference_indexes`. |
| `references[].title / references[].link / references[].source` | The title, URL and site name of a cited source. |
| `references[].snippet` | A short excerpt from the cited page. |
| `media[].link / media[].title / media[].platform` | The URL, title and site name of a related media item, such as a wiki page or a Naver blog post. |
| `media[].thumbnail / media[].position` | The thumbnail image URL of a media item and its order in the list. |

### Notes

- Pass the search text in `query`. The example request uses `coffee`.
- The `query` parameter name is inferred from the sibling Naver APIs and is not independently confirmed.
- The answer text is in Korean in the example response.
- Media items can include a `name` field, for example the blog name for a Naver blog post.

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/naver/ai-overview.json`](../../../catalog/models/naver/ai-overview.json) · Store page: https://www.sandbase.ai/model/naver/ai-overview
