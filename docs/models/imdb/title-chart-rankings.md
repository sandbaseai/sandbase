# IMDb Chart Rankings API: pricing, parameters and code examples

`imdb/title-chart-rankings` · data API · IMDb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007143 per call (free daily quota) · **Modes:** sync

Get the IMDb Top 250 movie or TV chart selected by ranking type using language and country preferences. Use it to monitor chart positions or compare highly ranked titles.

## Pricing

- **$0.007143 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/title-chart-rankings", "rankingsChartType": "TOP_250"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('imdb/title-chart-rankings', {'rankingsChartType': 'TOP_250'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("imdb/title-chart-rankings", {
  "rankingsChartType": "TOP_250"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "imdb/title-chart-rankings", sandbase.Params{
	"rankingsChartType": "TOP_250",
})
```

Same call via the path form: `POST /v1/api/imdb/title-chart-rankings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `languageCountry` | string |  | Language and country preferences. one of: `en_US`, `fr_CA`, `fr_FR`, `de_DE`, `hi_IN`, `it_IT`, `pt_BR`, `es_ES`, `es_US`, `es_MX`; default `"en_US"` |
| `rankingsChartType` | string | yes | Type of rankings chart to retrieve. one of: `TOP_250`, `TOP_250_TV` |

## Details

Get the IMDb Top 250 movie or TV chart selected by ranking type using language and country preferences. Use it to monitor chart positions or compare highly ranked titles.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/imdb/title-chart-rankings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"rankingsChartType": "TOP_250"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `rankingsChartType` | string | Yes | Type of rankings chart to retrieve. |
| `languageCountry` | string | No | Language and country preferences. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/imdb/title-chart-rankings.json`](../../../catalog/models/imdb/title-chart-rankings.json) · Store page: https://www.sandbase.ai/model/imdb/title-chart-rankings
