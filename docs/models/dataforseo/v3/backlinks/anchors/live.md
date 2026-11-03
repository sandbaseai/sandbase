# DataForSEO Backlinks Anchors API: pricing, parameters and code examples

`dataforseo/v3/backlinks/anchors/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02418 per call · **Modes:** sync

Returns anchor text distribution metrics for backlinks pointing to a target website or page. Helps SEO professionals analyze link profile diversity and anchor text optimization.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02418**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/anchors/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/anchors/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/anchors/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/anchors/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/anchors/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `target` | string |  | Target domain or page, e.g. "nike.com".  |

## Details

Returns the anchor texts used in backlinks that point to a target domain or page. Each row shows how many backlinks use that anchor, along with spam, broken link and rank figures. You send a `target` such as `nike.com` and an optional `limit`.

### Use cases

- Check which anchor texts dominate a site's link profile, such as the brand name versus empty anchors.
- Spot anchors with a high `backlinks_spam_score` that may point to spammy or paid links.
- Find anchors with many `broken_backlinks` and fix or redirect the pages they point to.
- Compare the anchor mix of your site against a competitor's site by running the same `target` query for each.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/anchors/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "limit": 5}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of results (up to 100). |
| `target` | string | No | Target domain or page, e.g. "nike.com". |

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
        "function": "anchors",
        "limit": 5,
        "target": "nike.com"
      },
      "id": "11030828-2190-0272-0000-3c0bcba7dd42",
      "path": [
        "v3"
      ],
      "result": [
        {
          "items": [
            {
              "anchor": null,
              "backlinks": 5206265,
              "backlinks_spam_score": 7,
              "broken_backlinks": 1350116,
              "broken_pages": 1175929,
              "first_seen": "2019-01-15 23:06:25 +00:00",
              "lost_date": null,
              "rank": 577
            }
          ],
          "items_count": 5,
          "target": "nike.com",
          "total_count": 183725
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "1.9332 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "1.9428 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].anchor` | The anchor text of the links. It is `null` when the links have no anchor text, as in the first row of the sample. |
| `tasks[].result[].items[].backlinks` | Number of backlinks that use this anchor text. |
| `tasks[].result[].items[].backlinks_spam_score` | Spam score for the backlinks with this anchor. A higher value means a higher spam risk. |
| `tasks[].result[].items[].broken_backlinks / tasks[].result[].items[].broken_pages` | Count of broken backlinks with this anchor, and count of broken pages those links point to. |
| `tasks[].result[].items[].first_seen / tasks[].result[].items[].lost_date` | When the anchor was first found, in `YYYY-MM-DD HH:MM:SS +00:00` format, and when it was lost. `lost_date` is `null` if the anchor is still present. |
| `tasks[].result[].items[].rank` | Rank score of the backlinks with this anchor. Higher values go with stronger links in the sample. |
| `tasks[].result[].total_count` | Total number of anchors found for the target. It can be larger than `items_count`. |
| `tasks[].result[].items_count` | Number of anchor rows returned in this response. |

### Notes

- Set `target` to a bare domain such as `nike.com` or to a page URL.
- `limit` caps the rows returned and accepts values up to 100. Compare `items_count` with `total_count` to see how many anchors you did not receive.
- The first row can have a `null` anchor, so handle empty values in your code.
- To see the individual links behind an anchor, call [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live). For overall totals, use [DataForSEO Backlinks Summary](/apis/dataforseo/v3/backlinks/summary/live).

### Pricing

Billed at the actual cost of each call, about $0.02418 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.
- [DataForSEO Backlinks Competitors](/apis/dataforseo/v3/backlinks/competitors/live): Returns domains that compete for similar backlink profiles.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/anchors/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/anchors/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/anchors/live
