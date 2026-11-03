# DataForSEO Google Categories for Keywords API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/categories_for_keywords/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01224 per call · **Modes:** sync

Map up to 100 keywords to Google product and service category codes to group and analyze keyword lists by topic.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01224**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/categories_for_keywords/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/categories_for_keywords/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/categories_for_keywords/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/categories_for_keywords/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/categories_for_keywords/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  |   |
| `language_code` | string |  |   |

## Details

This API maps keywords to Google product and service category codes. Send a `keywords` array (up to 100 items) and a `language_code`. It returns one entry per keyword with a list of numeric category codes.

### Use cases

- Group a large keyword list into topic buckets by sharing category codes.
- Check which product categories a keyword such as `laptop` belongs to before building a product ad campaign.
- Find keywords in a list that fall outside the category you target.
- Prepare input for category-based keyword research by collecting the codes that appear most often.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/categories_for_keywords/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes", "laptop"], "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keywords` | array | No |  |
| `language_code` | string | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "dataforseo_labs",
        "function": "categories_for_keywords",
        "keywords": [
          "running shoes"
        ],
        "language_code": "en",
        "se_type": "google"
      },
      "id": "11030828-2190-0587-0000-2e8d646e9918",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "categories": [
                13616
              ],
              "keyword": "running shoes"
            }
          ],
          "items_count": 2,
          "language_code": "en"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0817 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.0882 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].keyword` | The keyword from your request that this row describes. |
| `tasks[].result[].items[].categories` | List of numeric Google category codes assigned to the keyword. For example, `running shoes` returns `13616`, `13605` and `10014`. |
| `tasks[].result[].items_count` | Number of keyword rows in the result. |
| `tasks[].result[].language_code` | Language code the categories were matched for. |
| `tasks[].data.keywords` | Echo of the keywords you sent in the request. |
| `tasks[].id` | Unique ID of the task. |
| `status_code / tasks[].status_code` | Status code for the whole response and for each task. `20000` means the call succeeded. |
| `tasks_count / tasks_error` | Number of tasks in the response and how many of them returned an error. |

### Notes

- Pass `keywords` as a JSON array of strings. The array accepts at most 100 items.
- The response gives category codes only, with no category names. Match the codes yourself against a Google category list.
- Read results from `tasks[0].result[0].items`. Each task holds one `result` object.

### Pricing

Billed at the actual cost of each call, about $0.01224 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/categories_for_keywords/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/categories_for_keywords/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/categories_for_keywords/live
