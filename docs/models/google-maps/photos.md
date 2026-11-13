# Google Maps Photos API: pricing, parameters and code examples

`google-maps/photos` · data API · Google Maps · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get photos of a Google Maps place by data ID, with image URLs, categories and paging.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-maps/photos", "data_id": "0x8644b741914e0c8d:0xcb6fba98ff70f342"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-maps/photos', {'data_id': '0x8644b741914e0c8d:0xcb6fba98ff70f342'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-maps/photos", {
  "data_id": "0x8644b741914e0c8d:0xcb6fba98ff70f342"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-maps/photos", sandbase.Params{
	"data_id": "0x8644b741914e0c8d:0xcb6fba98ff70f342",
})
```

Same call via the path form: `POST /v1/api/google-maps/photos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hl` | string |  | Parameter defines the language to use for the Google Maps Photos search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or…  |
| `data_id` | string | yes | Parameter defines the Google Maps data ID. Find the data ID of a place using our Google Maps API.  |
| `category_id` | string |  | Parameter defines the ID of a category. The number, and the type of categories can vary between places, and a search returns no results for a category the place doesn't have. Common categories: `CgIgAQ` - All (default)…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `next_page_token` | string |  | Parameter defines the next page token. It is used for retrieving the next page results. `10` results are returned per page.  |

## Details

Get photos of a Google Maps place by data ID, with image URLs, categories and paging.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-maps/photos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"data_id": "0x8644b741914e0c8d:0xcb6fba98ff70f342"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `data_id` | string | Yes | Parameter defines the Google Maps data ID. Find the data ID of a place using our Google Maps API. |
| `hl` | string | No | Parameter defines the language to use for the Google Maps Photos search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region cod |
| `category_id` | string | No | Parameter defines the ID of a category. The number, and the type of categories can vary between places, and a search returns no results for a category the place doesn't have. Common categories: `CgIgAQ` - All (default) `CgIgARICGAI` - Lates |
| `next_page_token` | string | No | Parameter defines the next page token. It is used for retrieving the next page results. `10` results are returned per page. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-maps/photos.json`](../../../catalog/models/google-maps/photos.json) · Store page: https://www.sandbase.ai/model/google-maps/photos
