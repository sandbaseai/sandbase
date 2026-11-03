# DataForSEO Domain Analytics Technology Stats API: pricing, parameters and code examples

`dataforseo/v3/domain_analytics/technologies/technology_stats/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0672 per call · **Modes:** sync

Returns aggregated technology usage statistics across websites and web domains. Enables analysis of market adoption and trends for specific web technologies.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0672**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/domain_analytics/technologies/technology_stats/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/domain_analytics/technologies/technology_stats/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/domain_analytics/technologies/technology_stats/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/domain_analytics/technologies/technology_stats/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/domain_analytics/technologies/technology_stats/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `technology` | string |  | Technology name, e.g. "Nginx".  |

## Details

Returns monthly usage statistics for one web technology, such as Nginx. Each row shows how many domains use the technology, with breakdowns by country, language and domain rank range. The call needs the technology name in `technology`.

### Use cases

- Chart the growth of a web server or framework over time using monthly `domains_count` values.
- Compare which countries use a technology the most for regional market sizing.
- Check which languages the sites using a technology are written in.
- See how many users of a technology sit in high-ranking versus low-ranking domain ranges.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/domain_analytics/technologies/technology_stats/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"technology": "Nginx"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `technology` | string | No | Technology name, e.g. "Nginx". |

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
        "function": "technology_stats",
        "se": "technologies",
        "technology": "Nginx"
      },
      "id": "11030829-1614-0558-0000-ab200336c7e7",
      "path": [
        "v3"
      ],
      "result": [
        {
          "date_from": null,
          "date_to": null,
          "items": [
            {
              "countries": {
                "40": 3,
                "AC": 1,
                "AD": 22,
                "AE": 11732,
                "AF": 477,
                "AG": 38,
                "AI": 4107,
                "AL": 1330
              },
              "date": "2022-10-31 00:00:00 +00:00",
              "domains_count": 14964512,
              "domains_rank": {
                "0-100": 8690615,
                "101-200": 4006926,
                "201-300": 1596276,
                "301-400": 521581,
                "401-500": 136266,
                "501-600": 41537,
                "601-700": 22256,
                "701-800": 795
              },
              "languages": {
                "af": 152,
                "am": 72,
                "ar": 12058,
                "as": 3,
                "az": 894,
                "ba": 34,
                "be": 253,
                "bg": 3337
              },
              "type": "technology_stats_item"
            }
          ],
          "items_count": 46,
          "technology": "Nginx"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.0615 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1170 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].technology` | The technology name the statistics describe. |
| `tasks[].result[].items_count` | Number of monthly rows available for this technology. The response shows 46. |
| `tasks[].result[].items[].date` | The date of the data point, as a timestamp such as `2022-10-31 00:00:00 +00:00`. Each row is one month-end. |
| `tasks[].result[].items[].domains_count` | Number of domains using the technology on that date. |
| `tasks[].result[].items[].countries` | Map of country code to the number of domains using the technology in that country. Codes are mostly two letters, such as `AE`. |
| `tasks[].result[].items[].languages` | Map of language code to the number of domains using the technology with that language, such as `ar` or `bg`. |
| `tasks[].result[].items[].domains_rank` | Map of rank range to the number of domains in that range, such as `0-100` or `101-200`. |
| `tasks[].result[].date_from / date_to` | Date range of the results. Both are `null` in this response, so no range was applied. |

### Notes

- Pass the technology name exactly as in the example, for instance `Nginx`.
- Rows in `items` come in date order, oldest first. Compare consecutive `domains_count` values to get month-over-month change.
- The `countries`, `languages` and `domains_rank` objects are maps, so read them by key rather than by list position.

### Pricing

Billed at the actual cost of each call, about $0.0672 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/domain_analytics/technologies/technology_stats/live.json`](../../../../../../../catalog/models/dataforseo/v3/domain_analytics/technologies/technology_stats/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/domain_analytics/technologies/technology_stats/live
