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

Pass one or more URLs and get their contents ready for an LLM: page text, highlights or summaries, with live crawling when the cache is stale.

### Use cases

- Fetch full text for RAG after a search.
- Summarize a list of web pages.
- Monitor page changes with live crawls.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/exa/contents" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ids": ["https://developers.openai.com/codex"], "highlights": true}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ids` | array | Yes | The URLs (or Exa result ids) to fetch contents for. |
| `text` | boolean | No | Return the full page text. |
| `summary` | boolean | No | Return an AI-generated summary of the page. |
| `subpages` | integer | No | Number of linked subpages to also fetch. |
| `livecrawl` | string | No | Freshness policy: always live-crawl, fall back to live crawl on cache miss, or never live-crawl. |
| `highlights` | boolean | No | Return highlighted relevant snippets. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "results": [
    {
      "id": "https://developers.openai.com/codex",
      "url": "https://developers.openai.com/codex",
      "title": "ChatGPT | ChatGPT Learn",
      "highlights": [
        "ChatGPT | ChatGPT Learn ... responses createreasoning_effortrealtimeprompt cach…"
      ]
    }
  ]
}
```

### Notes

- `livecrawl`: always, fallback (on cache miss) or never.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/exa/contents.json`](../../../catalog/models/exa/contents.json) · Store page: https://www.sandbase.ai/model/exa/contents
