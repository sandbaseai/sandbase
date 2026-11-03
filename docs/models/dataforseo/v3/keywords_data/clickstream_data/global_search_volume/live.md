# DataForSEO Global Search Volume API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/clickstream_data/global_search_volume/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.18 per call · **Modes:** sync

Get worldwide clickstream search volume for keywords split by country. DataForSEO clickstream global search volume for a keyword list.

## Pricing

- **$0.18 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/clickstream_data/global_search_volume/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/clickstream_data/global_search_volume/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/clickstream_data/global_search_volume/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/clickstream_data/global_search_volume/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/clickstream_data/global_search_volume/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | List of keywords (up to 100 per call).  |

## Details

Returns clickstream-based search volume for each keyword you send, plus a split of that volume by country. The only input is a `keywords` array of up to 100 keywords.

### Use cases

- Find which countries drive the most searches for a product keyword such as `running shoes`.
- Compare the worldwide search volume of several keywords in one call.
- Pick target markets for a new store by ranking countries by `search_volume`.
- Check how concentrated a keyword is in one country before planning localized content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/clickstream_data/global_search_volume/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"]}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No | List of keywords (up to 100 per call). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "keywords_data",
        "function": "global_search_volume",
        "keywords": [
          "running shoes"
        ],
        "se": "clickstream_data"
      },
      "id": "11030829-1614-0592-0000-367bd67e0246",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "country_distribution": [
                {
                  "country_iso_code": "IN",
                  "percentage": 25.73878,
                  "search_volume": 68693
                }
              ],
              "keyword": "running shoes",
              "search_volume": 266886
            }
          ],
          "items_count": 1
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.1225 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1452 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The keyword from your request that this row describes. |
| `tasks[].result[].items[].search_volume` | Worldwide search volume for the keyword. It is the total across all countries. |
| `tasks[].result[].items[].country_distribution[].country_iso_code` | Two-letter country code, such as `US` or `IN`. |
| `tasks[].result[].items[].country_distribution[].search_volume` | Search volume for the keyword in that country. |
| `tasks[].result[].items[].country_distribution[].percentage` | The country's share of the worldwide `search_volume`, as a percent. |
| `tasks[].result[].items_count` | Number of keyword rows in `items`. |
| `tasks[].data.keywords` | Echo of the keywords the task received. |
| `tasks[].status_code / tasks[].status_message` | Status of the task. `20000` with `Ok.` means it succeeded. |

### Notes

- Send up to 100 keywords in the `keywords` array in a single call.
- Read results from `tasks[].result[].items[]`. Each requested keyword gets one item, with its countries listed in `country_distribution`.
- `tasks_count` and `tasks_error` at the top level show how many tasks ran and how many failed.

### Pricing

$0.18 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/clickstream_data/global_search_volume/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/clickstream_data/global_search_volume/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/clickstream_data/global_search_volume/live
