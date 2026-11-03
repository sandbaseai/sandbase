# DataForSEO Technologies Summary by Region API: pricing, parameters and code examples

`dataforseo/v3/domain_analytics/technologies/technologies_summary/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

Number of websites using given technologies, broken down by country, language and category.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/domain_analytics/technologies/technologies_summary/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/domain_analytics/technologies/technologies_summary/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/domain_analytics/technologies/technologies_summary/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/domain_analytics/technologies/technologies_summary/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/domain_analytics/technologies/technologies_summary/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | string |  | Optional keywords to match in site titles.  |
| `countries` | array |  | Optional array of country codes.  |
| `technologies` | array |  | Array of technology names, e.g. ["Nginx"].  |

## Details

Returns how many websites use the technologies you name, split by country, content language, language and site keywords. You send a list of technology names in `technologies`, such as `Nginx`, and can narrow the count with `countries` or `keywords`.

### Use cases

- Compare how many sites run Nginx in each country to find regional adoption patterns.
- Check which content languages are most common among sites that use a given technology.
- Find which site keywords appear most often among sites on a technology, to see what kinds of sites use it.
- Size a market for a hosting or web server product before you plan regional sales.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/domain_analytics/technologies/technologies_summary/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"technologies": ["Nginx"], "countries": ["US"]}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `countries` | array | No | Optional array of country codes. |
| `keywords` | string | No | Optional keywords to match in site titles. |
| `technologies` | array | No | Array of technology names, e.g. ["Nginx"]. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "domain_analytics",
        "function": "technologies_summary",
        "se": "technologies",
        "technologies": [
          "Nginx"
        ]
      },
      "id": "11030829-1614-0492-0000-98ac967ece7e",
      "path": [
        "v3"
      ],
      "result": [
        {
          "content_languages": {
            "de": 794608,
            "en": 12879881,
            "es": 280981,
            "fr": 234032,
            "it": 137907,
            "ja": 2172216,
            "nl": 265957,
            "pt": 259629
          },
          "countries": {
            "AU": 308738,
            "BR": 303917,
            "CN": 1369301,
            "DE": 973543,
            "GA": 1063449,
            "GB": 915823,
            "JP": 403769,
            "NL": 593502
          },
          "keywords": {
            "brandable domains": 110695,
            "business domains": 110570,
            "buy domain names": 110571,
            "domain marketplace": 110709,
            "domain names for sale": 110708,
            "domain purchasing": 110568,
            "high-quality domains": 110568,
            "premium domains": 110926
          },
          "languages": {
            "": 176577,
            "de": 1648257,
            "en": 17095215,
            "es": 289057,
            "fr": 201682,
            "ja": 983838,
            "ko": 158735,
            "nl": 207137
          }
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "7.3571 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "7.3760 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].countries` | Map of country code to the number of websites using the technology in that country. For example, `CN` and `GA` show the highest counts in this sample. |
| `tasks[].result[].content_languages` | Map of language code to the number of websites using the technology, grouped by the language of the site content. |
| `tasks[].result[].languages` | Map of language code to the number of websites using the technology, grouped by the `languages` value. An empty key `""` holds sites with no language value. |
| `tasks[].result[].keywords` | Map of keyword phrase to the number of websites using the technology that match that keyword. |
| `tasks[].result_count` | Number of items in `result`. It is `1` in this response. |
| `tasks[].data.technologies` | The technology names the task ran for. It echoes your request. |
| `tasks[].id` | Unique ID of the task. |
| `tasks[].status_code / tasks[].status_message` | Status of the task. `20000` with `Ok.` means the task succeeded. |

### Notes

- Pass technology names exactly as they are written, for example `Nginx`, in the `technologies` array.
- Each map in the result uses the key as the label and the value as a website count, so you can sort the entries yourself to rank them.
- The `countries` parameter takes country codes such as `US`. The `countries` map in the response lists counts for several country codes.

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/domain_analytics/technologies/technologies_summary/live.json`](../../../../../../../catalog/models/dataforseo/v3/domain_analytics/technologies/technologies_summary/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/domain_analytics/technologies/technologies_summary/live
