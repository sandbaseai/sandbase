# Polymarket Get related tags (relationships) by tag id API: pricing, parameters and code examples

`polymarket/tags-related-tags` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get related tags (relationships) by tag id from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tags-related-tags", "id": 2}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tags-related-tags', {'id': 2})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tags-related-tags", {
  "id": 2
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tags-related-tags", sandbase.Params{
	"id": 2,
})
```

Same call via the path form: `POST /v1/api/polymarket/tags-related-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | id  |
| `status` | string |  | status one of: `active`, `closed`, `all` |
| `omit_empty` | boolean |  | omit_empty  |

## Details

Returns the relationship rows for one Polymarket tag. Each row links the tag you pass in `id` to a related tag and gives its rank. The only required input is the integer tag `id`.

### Use cases

- Build a "related topics" list for a Polymarket tag page, ordered by `rank`.
- Walk the tag graph from one tag to find neighbouring categories of markets.
- Collect related tag ids, then look up their names and slugs to label a topic map.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tags-related-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | id |
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
| `id` | ID of the relationship row itself, returned as a string. It is not a tag id. |
| `rank` | Position of the related tag in the list for this tag. `1` is the first entry. |
| `relatedTagID` | Tag id of the related tag. Use it to look up that tag's details. |
| `tagID` | Tag id the relationship belongs to. It matches the `id` you sent in the request. |

### Notes

- `omit_empty` and `status` are optional. `status` accepts `active`, `closed` or `all`. The example response was requested with only `id`.
- The response is a plain JSON array. It has no pagination fields in this example.
- Call [Polymarket Get tag by id](/apis/polymarket/tags-by-id) with a `relatedTagID` value to get the name of that tag.
- [Polymarket Get tags related to a tag id](/apis/polymarket/tags-related-tags-tags) is a separate API that returns the related tags themselves.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/tags-related-tags.json`](../../../catalog/models/polymarket/tags-related-tags.json) · Store page: https://www.sandbase.ai/model/polymarket/tags-related-tags
