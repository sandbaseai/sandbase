# Google Autocomplete API: pricing, parameters and code examples

`google/autocomplete` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Google search box suggestions for a partial query, localized by country and language.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/autocomplete", "q": "how to make cold"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/autocomplete', {'q': 'how to make cold'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/autocomplete", {
  "q": "how to make cold"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/autocomplete", sandbase.Params{
	"q": "how to make cold",
})
```

Same call via the path form: `POST /v1/api/google/autocomplete` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the search query. A query that would be used to provide completion options.  |
| `cp` | string |  | Cursor pointer defines the position of cursor for the query provided, position starts from 0 which is a case where cursor is placed before the query `\|query`. If not provided acts as cursor is placed in the end of…  |
| `gl` | string |  | Parameter defines the country to use for the Google search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for a full…  |
| `hl` | string |  | Parameter defines the language to use for the Google Autocomplete search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or…  |
| `client` | string |  | Parameter used to define client for autocomplete. List of supported clients.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Google search box suggestions for a partial query, localized by country and language.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/autocomplete" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "how to make cold"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the search query. A query that would be used to provide completion options. |
| `gl` | string | No | Parameter defines the country to use for the Google search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for a full list of supported Googl |
| `hl` | string | No | Parameter defines the language to use for the Google Autocomplete search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region co |
| `cp` | string | No | Cursor pointer defines the position of cursor for the query provided, position starts from 0 which is a case where cursor is placed before the query `/query`. If not provided acts as cursor is placed in the end of query `query/`. |
| `client` | string | No | Parameter used to define client for autocomplete. List of supported clients. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/autocomplete.json`](../../../catalog/models/google/autocomplete.json) · Store page: https://www.sandbase.ai/model/google/autocomplete
