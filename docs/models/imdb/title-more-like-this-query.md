# IMDb Recommendations API: pricing, parameters and code examples

`imdb/title-more-like-this-query` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get IMDb titles similar to a specified title ID using selected language and country preferences. Use it to support related-title discovery, recommendations, or catalog curation.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-more-like-this-query", "id": "tt0111161"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-more-like-this-query', {'id': 'tt0111161'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-more-like-this-query", {
  "id": "tt0111161"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-more-like-this-query", sandbase.Params{
	"id": "tt0111161",
})
```

Same call via the path form: `POST /v1/api/imdb/title-more-like-this-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The IMDb title identifier in tt<digits> format.  |
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |

## Details

Returns a list of IMDb title IDs that IMDb considers similar to a given title. It needs one IMDb title ID in `tt<digits>` format, and it accepts an optional `languageCountry` value.

### Use cases

- Build a "more like this" row on a movie page from the returned title IDs.
- Seed a recommendation list for a film you already know, such as `tt0111161`.
- Expand a catalog by collecting titles related to your existing entries.
- Chain the returned IDs into other IMDb calls to fill in names, plots, and ratings.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-more-like-this-query" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "tt0111161"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | The IMDb title identifier in tt<digits> format. |
| `languageCountry` | string | No | Language and country preferences. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "title": {
    "connections": {
      "edges": []
    },
    "moreLikeThisTitles": {
      "edges": [
        {
          "node": {
            "id": "tt0114369"
          }
        }
      ]
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title.moreLikeThisTitles.edges[]` | One similar title per list item. |
| `title.moreLikeThisTitles.edges[].node.id` | IMDb ID of a similar title, in `tt<digits>` format. For `tt0111161` the response includes `tt0114369`, `tt0120689`, and `tt0108052`. |
| `title.connections.edges[]` | List of connected titles. It was empty in this response, so some titles may return no connections. |

### Notes

- The response holds IDs only. Pass each `node.id` to [IMDb Base Info](/apis/imdb/title-base-query) to get the title name and basic details.
- For story text on a returned title, call [IMDb Plot Summary](/apis/imdb/title-plot-query) with its ID.
- Get the `id` input from the IMDb title page URL. It starts with `tt` followed by digits.
- `languageCountry` accepts `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, or `es_MX`. The default is `en_US`.

### Pricing

$0.007143 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/imdb/title-more-like-this-query.json`](../../../catalog/models/imdb/title-more-like-this-query.json) · Store page: https://www.sandbase.ai/model/imdb/title-more-like-this-query
