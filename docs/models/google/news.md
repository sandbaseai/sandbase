# Google News API: pricing, parameters and code examples

`google/news` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Google News by keyword, topic or publication and get headlines with source, date, thumbnail and story clusters, localized by country and language.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/news"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/news', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/news", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/news", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/google/news` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Parameter defines the query you want to search. You can use anything that you would use in a regular Google News search. e.g. `site:`, `when:`. Parameter can't be used together with any of the `Advanced parameters`.  |
| `gl` | string |  | Parameter defines the country to use for the Google News search. It's a two-letter country code. (e.g., `us` for the United States (default), `uk` for United Kingdom, or `fr` for France). Head to the Google countries…  |
| `hl` | string |  | Parameter defines the language to use for the Google News search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or…  |
| `so` | string |  | Parameter defines the sorting method. Results can be sorted by relevance or by date. By default, the results are sorted by relevance. List of supported values are: `0` - Relevance `1` - Date Parameter can be used…  |
| `kgmid` | string |  | Parameter defines the Knowledge Graph ID (`KGMID`) of a topic or location for Google News results. It is a string that starts with `/m/` or `/g/`. You can look up entities on Wikidata and use their "Freebase ID" as the…  |
| `story_token` | string |  | Parameter defines the Google News story token. It is used for accessing the news results with full coverage of a specific story. The token can be found in our JSON response or the URL of the Google News page (in the…  |
| `topic_token` | string |  | Parameter defines the Google News topic token. It is used for accessing the news results for a specific topic (e.g., "World", "Business", "Technology"). The token can be found in our JSON response or the URL of the…  |
| `section_token` | string |  | Parameter defines the Google News section token. It is used for accessing the sub-section of a specific topic. (e.g., "Business -> Economy"). The token can be found in our JSON response or the URL of the Google News…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `publication_token` | string |  | Parameter defines the Google News publication token. It is used for accessing the news results from a specific publisher (e.g., "CNN", "BBC", "The Guardian"). The token can be found in our JSON response or the URL of…  |

## Details

Search Google News by keyword, topic or publication and get headlines with source, date, thumbnail and story clusters, localized by country and language.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/news" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "artificial intelligence"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | No | Parameter defines the query you want to search. You can use anything that you would use in a regular Google News search. e.g. `site:`, `when:`. Parameter can't be used together with any of the `Advanced parameters`. |
| `gl` | string | No | Parameter defines the country to use for the Google News search. It's a two-letter country code. (e.g., `us` for the United States (default), `uk` for United Kingdom, or `fr` for France). Head to the Google countries page for a full list of |
| `hl` | string | No | Parameter defines the language to use for the Google News search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region code (e.g. |
| `topic_token` | string | No | Parameter defines the Google News topic token. It is used for accessing the news results for a specific topic (e.g., "World", "Business", "Technology"). The token can be found in our JSON response or the URL of the Google News page (in the  |
| `kgmid` | string | No | Parameter defines the Knowledge Graph ID (`KGMID`) of a topic or location for Google News results. It is a string that starts with `/m/` or `/g/`. You can look up entities on Wikidata and use their "Freebase ID" as the kgmid. For example, ` |
| `publication_token` | string | No | Parameter defines the Google News publication token. It is used for accessing the news results from a specific publisher (e.g., "CNN", "BBC", "The Guardian"). The token can be found in our JSON response or the URL of the Google News page (i |
| `section_token` | string | No | Parameter defines the Google News section token. It is used for accessing the sub-section of a specific topic. (e.g., "Business -> Economy"). The token can be found in our JSON response or the URL of the Google News page (in the URL, it is  |
| `story_token` | string | No | Parameter defines the Google News story token. It is used for accessing the news results with full coverage of a specific story. The token can be found in our JSON response or the URL of the Google News page (in the URL, it is a string of c |
| `so` | string | No | Parameter defines the sorting method. Results can be sorted by relevance or by date. By default, the results are sorted by relevance. List of supported values are: `0` - Relevance `1` - Date Parameter can be used together with `story_token` |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/news.json`](../../../catalog/models/google/news.json) · Store page: https://www.sandbase.ai/model/google/news
