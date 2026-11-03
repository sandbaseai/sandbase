# Exa Contents API: pricing, parameters and code examples

`exa/contents` · data API · Exa · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0045 per call · **Modes:** sync

Extract clean page contents for a list of URLs: full text, highlights, AI summaries and metadata, from cache or with a live crawl.

## Pricing

- **$0.0045 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "exa/contents", "ids": ["https://static.sandbase.ai/examples/a0ad9eef-966a-46c6-8f69-4c42f972fe58/input/31c6cd46-ab5b-48a4-97da-a0a5d9b01220.bin"], "text": true}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('exa/contents', {'ids': ['https://static.sandbase.ai/examples/a0ad9eef-966a-46c6-8f69-4c42f972fe58/input/31c6cd46-ab5b-48a4-97da-a0a5d9b01220.bin'], 'text': True})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("exa/contents", {
  "ids": [
    "https://static.sandbase.ai/examples/a0ad9eef-966a-46c6-8f69-4c42f972fe58/input/31c6cd46-ab5b-48a4-97da-a0a5d9b01220.bin"
  ],
  "text": true
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "exa/contents", sandbase.Params{
	"ids": []any{"https://static.sandbase.ai/examples/a0ad9eef-966a-46c6-8f69-4c42f972fe58/input/31c6cd46-ab5b-48a4-97da-a0a5d9b01220.bin"},
	"text": true,
})
```

Same call via the path form: `POST /v1/api/exa/contents` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ids` | array | yes | The URLs (or Exa result ids) to fetch contents for.  |
| `text` | boolean |  | Return the full page text.  |
| `summary` | boolean |  | Return an AI-generated summary of the page.  |
| `subpages` | integer |  | Number of linked subpages to also fetch.  |
| `livecrawl` | string |  | Freshness policy: always live-crawl, fall back to live crawl on cache miss, or never live-crawl. one of: `always`, `fallback`, `never` |
| `highlights` | boolean |  | Return highlighted relevant snippets.  |

## Details

Fetch the content of web pages by URL with Exa: full text, highlighted snippets most relevant to a query, or an AI summary, plus title, author, publish date and image. Pages are served from Exa's cache or crawled live.

### Use cases

- Get clean text of pages found by a search API for RAG.
- Pull only the relevant passages of long pages with `highlights`.
- Summarize a list of URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/exa/contents" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ids": ["https://developers.openai.com/codex"], "highlights": true}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ids` | array | Yes | The URLs (or Exa result ids) to fetch contents for. |
| `highlights` | boolean | No | Return highlighted relevant snippets. |
| `livecrawl` | string | No | Freshness policy: always live-crawl, fall back to live crawl on cache miss, or never live-crawl. |
| `subpages` | integer | No | Number of linked subpages to also fetch. |
| `summary` | boolean | No | Return an AI-generated summary of the page. |
| `text` | boolean | No | Return the full page text. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "requestId": "5b59ba53e260d94b59baf3c1436137f1",
  "results": [
    {
      "author": null,
      "highlights": [
        "ChatGPT | ChatGPT Learn\n\n### Suggested\n\nresponses createreasoning_effortrealtime…"
      ],
      "id": "https://developers.openai.com/codex",
      "image": "https://learn.chatgpt.com/og/docs.png",
      "title": "ChatGPT | ChatGPT Learn",
      "url": "https://developers.openai.com/codex"
    }
  ],
  "searchTime": 33.52916099992581,
  "statuses": [
    {
      "id": "https://developers.openai.com/codex",
      "source": "cached",
      "status": "success"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[]` | One entry per URL: `url`, `title`, `author`, `publishedDate`, `image`, and `text`, `highlights` or `summary` as requested. |
| `statuses[]` | Per-URL status: `success` or an error, and `source` (`cached` or live). |
| `searchTime` | Time spent in milliseconds. |

### Notes

- Pass up to several URLs in `ids`. Use `livecrawl` to force a fresh crawl of pages that change often.
- Pages that cannot be fetched appear in `statuses` with an error.

### Pricing

$0.0045 per successful call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/exa/contents.json`](../../../catalog/models/exa/contents.json) · Store page: https://www.sandbase.ai/model/exa/contents
