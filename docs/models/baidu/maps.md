# Baidu Maps Search API: pricing, parameters and code examples

`baidu/maps` · data API · Baidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search places on Baidu Maps by keyword in a city or around coordinates, with name, address, category, rating, phone and coordinates.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "baidu/maps", "q": "咖啡"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('baidu/maps', {'q': '咖啡'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("baidu/maps", {
  "q": "咖啡"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "baidu/maps", sandbase.Params{
	"q": "咖啡",
})
```

Same call via the path form: `POST /v1/api/baidu/maps` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `c` | string |  | Parameter defines the city to search in, with its Baidu Maps city code (e.g., `131` for Beijing, `289` for Shanghai, or `257` for Guangzhou). Head to the Baidu Maps cities page for the cities of China. Cities in other…  |
| `q` | string | yes | Parameter defines the search query. You can use anything that you would use in a regular Baidu Maps search: a type of place, a business, a brand, or a landmark (e.g., `咖啡` (coffee), `酒店` (hotels), `星巴克` (Starbucks), or…  |
| `lat` | string |  | Parameter defines the latitude to search near (e.g., `39.908776`). Results are the places near these coordinates, and their `distance` field says how far each one is. In China, including Hong Kong, Macau and Taiwan,…  |
| `lon` | string |  | Parameter defines the longitude to search near (e.g., `116.39759`). Results are the places near these coordinates, and their `distance` field says how far each one is. In China, including Hong Kong, Macau and Taiwan,…  |
| `page` | string |  | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Baidu Maps returns up to 10 results per page.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search places on Baidu Maps by keyword in a city or around coordinates, with name, address, category, rating, phone and coordinates.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/baidu/maps" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "咖啡", "c": "131"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the search query. You can use anything that you would use in a regular Baidu Maps search: a type of place, a business, a brand, or a landmark (e.g., `咖啡` (coffee), `酒店` (hotels), `星巴克` (Starbucks), or `故宫` (the Forbidden C |
| `c` | string | No | Parameter defines the city to search in, with its Baidu Maps city code (e.g., `131` for Beijing, `289` for Shanghai, or `257` for Guangzhou). Head to the Baidu Maps cities page for the cities of China. Cities in other countries have codes t |
| `lat` | string | No | Parameter defines the latitude to search near (e.g., `39.908776`). Results are the places near these coordinates, and their `distance` field says how far each one is. In China, including Hong Kong, Macau and Taiwan, Baidu Maps uses coordina |
| `lon` | string | No | Parameter defines the longitude to search near (e.g., `116.39759`). Results are the places near these coordinates, and their `distance` field says how far each one is. In China, including Hong Kong, Macau and Taiwan, Baidu Maps uses coordin |
| `page` | string | No | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Baidu Maps returns up to 10 results per page. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/baidu/maps.json`](../../../catalog/models/baidu/maps.json) · Store page: https://www.sandbase.ai/model/baidu/maps
