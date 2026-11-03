# DataForSEO Backlinks Referring Networks API: pricing, parameters and code examples

`dataforseo/v3/backlinks/referring_networks/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02436 per call · **Modes:** sync

Referring IP addresses or subnets pointing to a target, with backlink counts per network.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02436**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/referring_networks/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/referring_networks/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/referring_networks/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/referring_networks/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/referring_networks/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of networks to return.  |
| `target` | string |  | Domain, subdomain or page URL.  |
| `network_address_type` | string |  | Optional: "ip" or "subnet" (default "ip").  |

## Details

This API returns the IP addresses or subnets that host sites linking to a target, with backlink counts for each network. It needs a `target`, which can be a domain, subdomain or page URL.

### Use cases

- Spot a cluster of backlinks that come from a single IP, which can point to a link network or a shared host.
- Find the networks that hold the most broken backlinks to a domain and plan link reclamation.
- Compare how many referring domains sit behind each IP to see how spread out a link profile is.
- Switch to subnet view to group links by wider address blocks when auditing a competitor.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/referring_networks/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of networks to return. |
| `network_address_type` | string | No | Optional: "ip" or "subnet" (default "ip"). |
| `target` | string | No | Domain, subdomain or page URL. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "backlinks",
        "function": "referring_networks",
        "limit": 10,
        "target": "nike.com"
      },
      "id": "11030828-2190-0332-0000-84229c8b9ee4",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "backlinks": 4621943,
              "broken_backlinks": 5687,
              "broken_pages": 27,
              "first_seen": "2019-01-23 21:50:43 +00:00",
              "lost_date": null,
              "network_address": "172.66.0.96",
              "rank": 508,
              "referring_domains": 52
            }
          ],
          "items_count": 10,
          "target": "nike.com",
          "total_count": 63231
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "1.8951 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "1.9022 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].target` | The target the networks were counted for. |
| `tasks[].result[].total_count` | Total number of referring networks found for the target. The call returns only the rows set by `limit`. |
| `tasks[].result[].items_count` | Number of networks returned in this response. |
| `tasks[].result[].items[].network_address` | The IP address (or subnet, if requested) that hosts the linking sites. |
| `tasks[].result[].items[].backlinks` | Number of backlinks to the target that come from this network. |
| `tasks[].result[].items[].referring_domains` | Number of distinct referring domains on this network that link to the target. |
| `tasks[].result[].items[].broken_backlinks / broken_pages` | Number of backlinks that point to broken pages, and the number of broken target pages those links hit. |
| `tasks[].result[].items[].rank` | Rank score for the network. Higher values appear on the networks with more link weight in this sample. |
| `tasks[].result[].items[].first_seen / lost_date` | When the network was first seen linking to the target, as a timestamp with a UTC offset. `lost_date` is `null` when the network has not been marked as lost. |

### Notes

- Set `network_address_type` to `ip` (default) or `subnet` to choose the grouping.
- Use `limit` to set how many networks come back. Compare `items_count` with `total_count` to see how many remain.
- For the domains behind the links, call [DataForSEO Backlinks Referring Domains](/apis/dataforseo/v3/backlinks/referring_domains/live). For a target-level overview, use [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live).

### Pricing

Billed at the actual cost of each call, about $0.02436 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/referring_networks/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/referring_networks/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/referring_networks/live
