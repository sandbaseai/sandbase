# DataForSEO Keyword Trend by Demographic API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/dataforseo_trends/demography/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0024 per call (free daily quota) · **Modes:** sync

Get keyword interest split by age and gender from an independent trends dataset. DataForSEO Trends demography for up to 5 keywords.

## Pricing

- **$0.0024 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/dataforseo_trends/demography/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/dataforseo_trends/demography/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/dataforseo_trends/demography/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/dataforseo_trends/demography/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/dataforseo_trends/demography/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | List of keywords (up to 100 per call).  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns keyword interest split by age group and by gender for up to 5 keywords in one location. You send a `keywords` list and a `location_code`, and the response holds one `demography` item with `age` and `gender` breakdowns.

### Use cases

- Check which age group searches for a product term the most before you pick ad targeting.
- Compare female and male interest in a keyword to tune product copy or campaign creative.
- Compare demographic profiles of several competing product keywords in one call.
- Build audience reports for SEO clients that show who is interested in their topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/dataforseo_trends/demography/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No | List of keywords (up to 100 per call). |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

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
        "function": "demography",
        "keywords": [
          "running shoes"
        ],
        "location_code": 2840,
        "se": "dataforseo_trends"
      },
      "id": "11030829-1614-0574-0000-b1e7a57cdb94",
      "path": [
        "v3"
      ],
      "result": [
        {
          "datetime": "2026-11-03 08:29:18 +00:00",
          "items": [
            {
              "demography": {
                "age": [
                  {
                    "keyword": "running shoes",
                    "values": [
                      {
                        "type": "18-24",
                        "value": 58
                      }
                    ]
                  }
                ],
                "gender": [
                  {
                    "keyword": "running shoes",
                    "values": [
                      {
                        "type": "female",
                        "value": 100
                      }
                    ]
                  }
                ]
              },
              "demography_comparison": null,
              "keywords": [
                "running shoes"
              ],
              "position": 1,
              "type": "demography"
            }
          ],
          "items_count": 1,
          "keywords": [
            "running shoes"
          ],
          "language_code": null,
          "location_code": 2840,
          "type": "trends"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "1.4406 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "1.4576 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].demography.age[].keyword` | The keyword that the age values belong to. |
| `tasks[].result[].items[].demography.age[].values[].type` | Age bracket label, for example `18-24`, `25-34` or `35-44`. |
| `tasks[].result[].items[].demography.age[].values[].value` | Interest score for that age bracket. In the sample, the highest score in the age list is `86` for `35-44`, so scores look relative rather than absolute counts. |
| `tasks[].result[].items[].demography.gender[].keyword` | The keyword that the gender values belong to. |
| `tasks[].result[].items[].demography.gender[].values[].type` | Gender label, `female` or `male`. |
| `tasks[].result[].items[].demography.gender[].values[].value` | Interest score for that gender. In the sample, `female` is `100` and `male` is `79`. |
| `tasks[].result[].items[].demography_comparison` | Comparison block. It is `null` in this response, where only one keyword was sent. |
| `tasks[].result[].items[].keywords` | The keywords covered by this item. |
| `tasks[].result[].location_code` | The location code used for the data, `2840` in this call. |
| `tasks[].result[].datetime` | Date and time of the result, in the format `2026-11-03 08:29:18 +00:00`. |

### Notes

- Each item in `age[]` and `gender[]` holds one keyword and its `values[]` list, so expect one entry per keyword when you send several.
- The sample response lists only three age brackets, so do not assume a fixed set of brackets in your code.
- `language_code` is `null` in the result, and the request only needs `keywords` and `location_code`.
- `tasks[].result[].items_count` tells you how many items came back.

### Pricing

$0.0024 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/dataforseo_trends/demography/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/dataforseo_trends/demography/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/dataforseo_trends/demography/live
