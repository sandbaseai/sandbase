# Polymarket Get related tags (relationships) by tag slug API: pricing, parameters and code examples

`polymarket/tags-slug-related-tags` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get related tags (relationships) by tag slug from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tags-slug-related-tags", "slug": "politics"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tags-slug-related-tags', {'slug': 'politics'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tags-slug-related-tags", {
  "slug": "politics"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tags-slug-related-tags", sandbase.Params{
	"slug": "politics",
})
```

Same call via the path form: `POST /v1/api/polymarket/tags-slug-related-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | slug  |
| `status` | string |  | status one of: `active`, `closed`, `all` |
| `omit_empty` | boolean |  | omit_empty  |

## Details

Returns the tag relationships for a Polymarket tag, looked up by its tag slug. Each row links the tag to one related tag and gives its rank. The only required input is `slug`, such as `politics`.

### Use cases

- Build a "related topics" list for a Polymarket category page, ordered by `rank`.
- Map how tags connect to each other to build a topic graph of Polymarket markets.
- Find the related tag IDs of a topic, then fetch each tag's details to show names and labels.
- Filter the relationships by `status` to see only tags that have active or closed markets.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tags-slug-related-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "politics"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | slug |
| `omit_empty` | boolean | No | omit_empty |
| `status` | string | No | status |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "id": "49569",
    "rank": 1,
    "relatedTagID": 126,
    "tagID": 2
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | ID of the relationship record, returned as a string. |
| `rank` | Position of the related tag in the list for this tag. Rank 1 comes first. |
| `tagID` | Numeric ID of the tag you asked for, found from the `slug`. It has the same value in every row. |
| `relatedTagID` | Numeric ID of the tag that is related to `tagID`. |

### Notes

- The response is a plain JSON array. Each item holds only IDs, not tag names or slugs.
- To get the name and slug of a `relatedTagID`, call [Polymarket Get tag by id](/apis/polymarket/tags-by-id).
- To look up relationships by numeric tag ID instead of slug, use [Polymarket Get related tags (relationships) by tag id](/apis/polymarket/tags-related-tags).
- To get the full tag objects for related tags, use [Polymarket Get tags related to a tag id](/apis/polymarket/tags-related-tags-tags).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/tags-slug-related-tags.json`](../../../catalog/models/polymarket/tags-slug-related-tags.json) · Store page: https://www.sandbase.ai/model/polymarket/tags-slug-related-tags
