# Google Scholar Author API: pricing, parameters and code examples

`google/scholar-author` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get a Google Scholar author profile by author ID with affiliation, interests, citation counts, h-index, co-authors and article list.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/scholar-author", "author_id": "LSsXyncAAAAJ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/scholar-author', {'author_id': 'LSsXyncAAAAJ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/scholar-author", {
  "author_id": "LSsXyncAAAAJ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/scholar-author", sandbase.Params{
	"author_id": "LSsXyncAAAAJ",
})
```

Same call via the path form: `POST /v1/api/google/scholar-author` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hl` | string |  | Parameter defines the language to use for the Google Scholar Author search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter…  |
| `num` | string |  | Parameter defines the number of results to return. (e.g., `20` (default) returns 20 results, `40` returns 40 results, etc.). Maximum number of results to return is `100`.  |
| `sort` | string |  | Parameter is used for sorting and refining articles. Available options: `title` - Sorts articles by "Title". `pubdate` - Sorts articles by publish "date". By default, articles are sorted by the number of citations.  |
| `start` | string |  | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `20` is the 2nd page of results, `40` is the 3rd page of results,…  |
| `view_op` | string |  | Parameter is used for viewing specific parts of a page. It has two options: `view_citation` - Select to view citations. `citation_id` is required. `list_colleagues` - Select to view all co-authors  |
| `author_id` | string | yes | Parameter defines the ID of an author. You can find the ID either by using our Google Scholar Profiles API or by going to the Google Scholar user profile page and getting it from there (e.g.,…  |
| `citation_id` | string |  | Parameter is used for retrieving individual article citation. It is a required parameter when `view_op=view_citation` is selected. You can access IDs inside our structured JSON response.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get a Google Scholar author profile by author ID with affiliation, interests, citation counts, h-index, co-authors and article list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/scholar-author" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_id": "LSsXyncAAAAJ"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `author_id` | string | Yes | Parameter defines the ID of an author. You can find the ID either by using our Google Scholar Profiles API or by going to the Google Scholar user profile page and getting it from there (e.g., `https://scholar.google.com/citations?user={auth |
| `hl` | string | No | Parameter defines the language to use for the Google Scholar Author search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region  |
| `view_op` | string | No | Parameter is used for viewing specific parts of a page. It has two options: `view_citation` - Select to view citations. `citation_id` is required. `list_colleagues` - Select to view all co-authors |
| `sort` | string | No | Parameter is used for sorting and refining articles. Available options: `title` - Sorts articles by "Title". `pubdate` - Sorts articles by publish "date". By default, articles are sorted by the number of citations. |
| `citation_id` | string | No | Parameter is used for retrieving individual article citation. It is a required parameter when `view_op=view_citation` is selected. You can access IDs inside our structured JSON response. |
| `start` | string | No | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `20` is the 2nd page of results, `40` is the 3rd page of results, etc.). |
| `num` | string | No | Parameter defines the number of results to return. (e.g., `20` (default) returns 20 results, `40` returns 40 results, etc.). Maximum number of results to return is `100`. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/scholar-author.json`](../../../catalog/models/google/scholar-author.json) · Store page: https://www.sandbase.ai/model/google/scholar-author
