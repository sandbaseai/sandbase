# Brave Image Search

`brave/images` · api · Brave

Image Search from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/images", "q": "golden gate bridge"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/images', {'q': 'golden gate bridge'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/images", {
  "q": "golden gate bridge"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/images", sandbase.Params{
	"q": "golden gate bridge",
})
```

Same call via the path form: `POST /v1/api/brave/images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query.  |
| `count` | integer |  | The number of search results returned in response. The maximum is 200. The actual number delivered may be less than requested. NOTE: Image search is not paginated and has no offset parameter. Raise count to get more… default `50`; range 1–200 |
| `country` | string |  | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries and ALL for worldwide. one of: `AR`, `AU`, `AT`, `BE`, `BR`, `CA`, `CL`, `DK`, `FI`, `FR`, `DE`, `GR` …; default `"US"` |
| `safesearch` | string |  | Filters search results for adult content. The following values are supported: off - No content filtering (except for illegal content). strict - Drops all adult content from search results. one of: `off`, `strict`; default `"strict"` |
| `spellcheck` | boolean |  | Whether to spell check provided query. If the spell checker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model. default `true` |
| `search_lang` | string |  | The search language preference. The 2 or more character language code for which the search results are provided. one of: `ar`, `eu`, `bn`, `bg`, `ca`, `zh-hans`, `zh-hant`, `hr`, `cs`, `da`, `nl`, `en` …; default `"en"` |

## Details

Image Search from Brave. Returns the official Brave API response unchanged.

The response is the official Brave API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "golden gate bridge"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | The number of search results returned in response. The maximum is 200. The actual number delivered may be less than requested. NOTE: Image search is not paginat |
| `country` | string | No | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries and ALL for worldwide. |
| `q` | string | Yes | The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query. |
| `safesearch` | string | No | Filters search results for adult content. The following values are supported: off - No content filtering (except for illegal content). strict - Drops all adult  |
| `search_lang` | string | No | The search language preference. The 2 or more character language code for which the search results are provided. |
| `spellcheck` | boolean | No | Whether to spell check provided query. If the spell checker is enabled, the modified query is always used for search. The modified query can be found in altered |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/brave/images.json`](../../../catalog/models/brave/images.json) · Store page: https://www.sandbase.ai/model/brave/images
