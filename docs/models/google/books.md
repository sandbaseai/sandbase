# Google Books API: pricing, parameters and code examples

`google/books` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Google Books by keyword and get titles, authors, snippets, publication info and preview links.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/books", "q": "machine learning"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/books', {'q': 'machine learning'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/books", {
  "q": "machine learning"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/books", sandbase.Params{
	"q": "machine learning",
})
```

Same call via the path form: `POST /v1/api/google/books` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Google Books search: a title, an author, a subject, or a quote. Search operators such as `intitle:`, `inauthor:`,…  |
| `gl` | string |  | Parameter defines the country to use for the Google Books search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). It defaults to `us`. Head to the Google…  |
| `hl` | string |  | Parameter defines the language to use for the Google Books search. It's a two-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French). It defaults to `en`. Head to the Google languages page…  |
| `tbs` | string |  | (to be searched) parameter defines advanced search parameters that aren't possible in the regular query field. `view`, `document_type`, `start_date`, and `end_date` override the corresponding components (e.g., `bkt:s`…  |
| `nfpr` | string |  | Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `1` to exclude these results, or `0` to include them (default). Note that this…  |
| `view` | string |  | Parameter defines how much of the books must be viewable on Google Books. It defaults to any view. Available options: `preview` - Preview and full view `full` - Full view  |
| `start` | string |  | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `10` is the 2nd page of results, `20` is the 3rd page of results,…  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `end_date` | string |  | Parameter defines the latest publication date of the results. The format is `YYYYMMDD` (e.g., `19690731`). This parameter overrides `cdr` and `cd_max` components of `tbs` parameter.  |
| `start_date` | string |  | Parameter defines the earliest publication date of the results. The format is `YYYYMMDD` (e.g., `19690701`). This parameter overrides `cdr` and `cd_min` components of `tbs` parameter.  |
| `document_type` | string |  | Parameter defines the type of documents to search. It defaults to any document. Available options: `books` - Books `magazines` - Magazines `newspapers` - Newspapers Newspapers are the scanned newspapers of the Google…  |
| `google_domain` | string |  | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains page for a full list of supported Google domains.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search Google Books by keyword and get titles, authors, snippets, publication info and preview links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/books" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "machine learning"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Google Books search: a title, an author, a subject, or a quote. Search operators such as `intitle:`, `inauthor:`, `inpublisher:`, `subject: |
| `google_domain` | string | No | Parameter defines the Google domain to use. It defaults to `google.com`. Head to the Google domains page for a full list of supported Google domains. |
| `gl` | string | No | Parameter defines the country to use for the Google Books search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France). It defaults to `us`. Head to the Google countries page for a  |
| `hl` | string | No | Parameter defines the language to use for the Google Books search. It's a two-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French). It defaults to `en`. Head to the Google languages page for a full list of su |
| `view` | string | No | Parameter defines how much of the books must be viewable on Google Books. It defaults to any view. Available options: `preview` - Preview and full view `full` - Full view |
| `document_type` | string | No | Parameter defines the type of documents to search. It defaults to any document. Available options: `books` - Books `magazines` - Magazines `newspapers` - Newspapers Newspapers are the scanned newspapers of the Google News Archive. |
| `start_date` | string | No | Parameter defines the earliest publication date of the results. The format is `YYYYMMDD` (e.g., `19690701`). This parameter overrides `cdr` and `cd_min` components of `tbs` parameter. |
| `end_date` | string | No | Parameter defines the latest publication date of the results. The format is `YYYYMMDD` (e.g., `19690731`). This parameter overrides `cdr` and `cd_max` components of `tbs` parameter. |
| `nfpr` | string | No | Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to `1` to exclude these results, or `0` to include them (default). Note that this parameter may not prevent Goog |
| `tbs` | string | No | (to be searched) parameter defines advanced search parameters that aren't possible in the regular query field. `view`, `document_type`, `start_date`, and `end_date` override the corresponding components (e.g., `bkt:s` for newspapers). |
| `start` | string | No | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `10` is the 2nd page of results, `20` is the 3rd page of results, etc.). |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/books.json`](../../../catalog/models/google/books.json) · Store page: https://www.sandbase.ai/model/google/books
