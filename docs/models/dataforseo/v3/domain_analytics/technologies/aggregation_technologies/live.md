# DataForSEO Domain Technology Aggregations API: pricing, parameters and code examples

`dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.018 per call · **Modes:** sync

Returns aggregated domain technology data across tracked websites. Analyze the distribution and adoption trends of specific web technologies and platforms.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.018**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `technology` | string |  | Technology name, e.g. "Nginx".  |

## Details

Returns aggregated counts for a web technology, such as Nginx, across the domains tracked in the technology index. Each row shows the technology, its category and group, and how many domains match. It needs a `technology` name as input.

### Use cases

- Compare how many domains run Nginx against other web servers like OpenResty.
- Measure the size of a technology's footprint before choosing which platform to build an integration for.
- Find which technologies are listed in the same category as a competitor's tool.
- Pull the group and category of a technology to sort a list of tools into a taxonomy.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"technology": "Nginx", "limit": 5}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of results (up to 100). |
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
        "function": "aggregation_technologies",
        "limit": 5,
        "se": "technologies",
        "technology": "Nginx"
      },
      "id": "11030829-1614-0491-0000-1db00da91ee0",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "categories_count": 51252780,
              "category": "web_servers",
              "group": "servers",
              "groups_count": 113276408,
              "technologies_count": 37226431,
              "technology": "Nginx",
              "type": "aggregation_technologies_item"
            }
          ],
          "items_count": 5,
          "offset": 0,
          "total_count": 213
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "8.0797 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "8.0967 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].technology` | Name of the technology in this row. The first row matches the requested technology and later rows are related technologies. |
| `tasks[].result[].items[].technologies_count` | Number of domains counted for this technology. |
| `tasks[].result[].items[].category` | Category the technology belongs to, for example `web_servers`. |
| `tasks[].result[].items[].categories_count` | Number of domains counted for the whole category, shared by all rows in that category. |
| `tasks[].result[].items[].group` | Broader group the technology belongs to, for example `servers`. |
| `tasks[].result[].items[].groups_count` | Number of domains counted for the whole group, shared by all rows in that group. |
| `tasks[].result[].items_count` | Number of rows returned in this response. |
| `tasks[].result[].total_count` | Total number of matching rows available for the request. |
| `tasks[].result[].offset` | Position of the first returned row in the full result list. |

### Notes

- Pass the technology name as plain text in `technology`, for example `Nginx`. Use `limit` to cap the rows returned, up to 100.
- `total_count` can be larger than `items_count`. Compare the two to see whether more rows exist beyond your `limit`.
- To work out a technology's share of its category, divide `technologies_count` by `categories_count` from the same row.

### Pricing

Billed at the actual cost of each call, about $0.018 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live.json`](../../../../../../../catalog/models/dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/domain_analytics/technologies/aggregation_technologies/live
