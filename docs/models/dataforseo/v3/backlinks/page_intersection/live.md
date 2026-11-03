# DataForSEO Backlinks Page Intersection API: pricing, parameters and code examples

`dataforseo/v3/backlinks/page_intersection/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02436 per call · **Modes:** sync

Referring pages that link to all (or some) of up to 20 target pages or domains.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02436**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/page_intersection/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/page_intersection/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/page_intersection/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/page_intersection/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/page_intersection/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of referring pages to return.  |
| `targets` | object |  | Object of up to 20 targets keyed "1", "2", ... (pages or domains).  |

## Details

Returns pages that link to several targets at once, such as competitor sites. It needs a `targets` object with up to 20 pages or domains and an optional `limit`. Each result row shows the backlink to every target from the same referring page.

### Use cases

- Find sites that link to both Nike and Adidas to build an outreach list of pages that already cover your market.
- Spot link gaps by checking which pages link to your competitors but not to you.
- Check anchor text and `sponsored` attributes on pages that link to several brands.
- Filter out low quality link sources using the spam score of each backlink.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/page_intersection/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": {"1": "https://www.nike.com/", "2": "https://www.adidas.com/"}, "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of referring pages to return. |
| `targets` | object | No | Object of up to 20 targets keyed "1", "2", ... (pages or domains). |

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
        "function": "page_intersection",
        "limit": 10,
        "targets": {
          "1": "https://www.nike.com/",
          "2": "https://www.adidas.com/"
        }
      },
      "id": "11030828-2190-0287-0000-797cda96fcbf",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "page_intersection": {
                "1": [
                  {
                    "alt": null,
                    "anchor": "Nike",
                    "attributes": null,
                    "backlink_spam_score": 5,
                    "dofollow": true,
                    "domain_from": "library.alterbridge.edu.ge",
                    "domain_from_country": "GE",
                    "domain_from_ip": "134.209.81.146"
                  }
                ],
                "2": [
                  {
                    "alt": null,
                    "anchor": "Adidas",
                    "attributes": null,
                    "backlink_spam_score": 5,
                    "dofollow": true,
                    "domain_from": "library.alterbridge.edu.ge",
                    "domain_from_country": "GE",
                    "domain_from_ip": "134.209.81.146"
                  }
                ]
              },
              "summary": {
                "intersections_count": 2
              }
            }
          ],
          "items_count": 10,
          "targets": {
            "1": "https://www.nike.com/",
            "2": "https://www.adidas.com/"
          },
          "total_count": 612
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "1.0446 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "1.0538 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of referring pages that match the targets. The request in this example returned 612. |
| `tasks[].result[].items_count` | Number of rows returned in this response. |
| `tasks[].result[].items[].summary.intersections_count` | How many of the targets this referring page links to. A value of `2` means it links to both targets. |
| `tasks[].result[].items[].page_intersection.1[] / tasks[].result[].items[].page_intersection.2[]` | Backlinks from the referring page to the target with that key. The key matches the key in the `targets` object. |
| `tasks[].result[].items[].page_intersection.1[].anchor` | Anchor text of the link, for example `Nike`. |
| `tasks[].result[].items[].page_intersection.1[].dofollow` | `true` if the link is a dofollow link. |
| `tasks[].result[].items[].page_intersection.1[].attributes` | Link attributes such as `sponsored`. The value is `null` when none are set. |
| `tasks[].result[].items[].page_intersection.1[].backlink_spam_score` | Spam score of the backlink. Lower values mean the link looks less spammy. |
| `tasks[].result[].items[].page_intersection.1[].domain_from / tasks[].result[].items[].page_intersection.1[].domain_from_country / tasks[].result[].items[].page_intersection.1[].domain_from_ip` | Domain that hosts the link, with its country code and IP address. The country can be `null`. |

### Notes

- Key `targets` as `"1"`, `"2"` and so on. The same keys label the lists inside `page_intersection`.
- Use `limit` to set how many referring pages come back. Compare `items_count` with `total_count` to see how many matches remain.
- Results sit in `tasks[].result`. Each call runs one task.
- To list every backlink for a single target, call [Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live). To compare at domain level, use [Backlinks Domain Intersection](/apis/dataforseo/v3/backlinks/domain_intersection/live).

### Pricing

Billed at the actual cost of each call, about $0.02436 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/page_intersection/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/page_intersection/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/page_intersection/live
