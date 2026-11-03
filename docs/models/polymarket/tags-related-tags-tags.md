# Polymarket Get tags related to a tag id API: pricing, parameters and code examples

`polymarket/tags-related-tags-tags` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get tags related to a tag id from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tags-related-tags-tags", "id": 2}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tags-related-tags-tags', {'id': 2})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tags-related-tags-tags", {
  "id": 2
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tags-related-tags-tags", sandbase.Params{
	"id": 2,
})
```

Same call via the path form: `POST /v1/api/polymarket/tags-related-tags-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | id  |
| `status` | string |  | status one of: `active`, `closed`, `all` |
| `omit_empty` | boolean |  | omit_empty  |

## Details

Returns a list of Polymarket tags that are related to a given tag. It needs a numeric tag `id` as input. Each result has the related tag's label, slug, and a count of active events.

### Use cases

- Build a topic explorer that suggests neighboring topics, such as moving from one political tag to `Midterms` or `Senate Elections`.
- Rank related tags by `activeEventsCount` to see which linked topics have the most open events.
- Expand a tag filter by collecting related tag `id` values to use when searching for events.
- Map how Polymarket groups topics by walking from one tag to its related tags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tags-related-tags-tags" \
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
    "activeEventsCount": 333,
    "createdAt": "2023-11-02T21:23:16.39Z",
    "forceShow": false,
    "id": "126",
    "label": "Trump",
    "publishedAt": "2023-11-02 21:23:16.384+00",
    "slug": "trump",
    "updatedAt": "2026-04-17T20:39:14.206724Z",
    "updatedBy": 15
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[].id` | ID of the related tag, returned as a string. |
| `[].label` | Display name of the related tag, such as `Trump` or `Midterms`. |
| `[].slug` | URL-style name of the related tag. Use it to look up the tag by slug. |
| `[].activeEventsCount` | Number of active events that carry this tag. |
| `[].createdAt / updatedAt` | Timestamps for when the tag was created and last changed, in ISO 8601 format. |
| `[].publishedAt` | Time the tag was published. It appears only on some tags and uses a different date format from `createdAt`. |
| `[].forceShow` | Boolean flag on the tag. It is missing on some tags. |
| `[].updatedBy` | Numeric ID of the user who last updated the tag. It appears only on some tags. |

### Notes

- The response is a bare JSON array, not an object. Some optional fields, such as `forceShow`, `publishedAt` and `updatedBy`, are missing on some items.
- Get the tag `id` from [Polymarket List tags](/apis/polymarket/tags) or [Polymarket Get tag by slug](/apis/polymarket/tags-slug).
- `status` accepts `active`, `closed` or `all`. `omit_empty` is a boolean filter.
- For the relationship records between tags, call [Polymarket Get related tags (relationships) by tag id](/apis/polymarket/tags-related-tags).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/tags-related-tags-tags.json`](../../../catalog/models/polymarket/tags-related-tags-tags.json) · Store page: https://www.sandbase.ai/model/polymarket/tags-related-tags-tags
