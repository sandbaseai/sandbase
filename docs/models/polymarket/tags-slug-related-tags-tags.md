# Polymarket Get tags related to a tag slug API: pricing, parameters and code examples

`polymarket/tags-slug-related-tags-tags` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get tags related to a tag slug from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tags-slug-related-tags-tags", "slug": "politics"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tags-slug-related-tags-tags', {'slug': 'politics'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tags-slug-related-tags-tags", {
  "slug": "politics"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tags-slug-related-tags-tags", sandbase.Params{
	"slug": "politics",
})
```

Same call via the path form: `POST /v1/api/polymarket/tags-slug-related-tags-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | slug  |
| `status` | string |  | status one of: `active`, `closed`, `all` |
| `omit_empty` | boolean |  | omit_empty  |

## Details

Returns a list of Polymarket tags that are related to a given tag slug. Each tag includes its label, slug, id, and a count of active events. The only required input is `slug`, such as `politics`.

### Use cases

- Build a topic navigation menu that suggests tags next to `politics`.
- Rank related topics by `activeEventsCount` to find the busiest areas of Polymarket.
- Expand a tag filter so a market browser also shows events from related tags.
- Track when related tags were created or last changed using `createdAt` and `updatedAt`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tags-slug-related-tags-tags" \
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
    "activeEventsCount": 334,
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
| `[].label` | Display name of the related tag, for example `Trump` or `Midterms`. |
| `[].slug` | URL-style identifier of the related tag. Use it as the `slug` input in other tag calls. |
| `[].id` | Tag id as a string. Use it to look up the tag by id. |
| `[].activeEventsCount` | Number of active events that carry this tag. |
| `[].createdAt / [].updatedAt` | ISO 8601 timestamps for when the tag was created and last changed. |
| `[].publishedAt` | Publish time of the tag. It appears only on some tags and uses a different format from `createdAt`. |
| `[].forceShow` | Boolean flag on the tag. It is missing on some tags. |
| `[].updatedBy` | Numeric id of the user who last updated the tag. It appears only on some tags. |

### Notes

- Use the `slug` of a tag from [Polymarket List tags](/apis/polymarket/tags) as the input.
- `omit_empty` is a boolean and `status` accepts `active`, `closed` or `all`.
- To look up related tags by numeric id instead, call [Polymarket Get tags related to a tag id](/apis/polymarket/tags-related-tags-tags).
- Some fields, such as `forceShow`, `publishedAt` and `updatedBy`, are missing on some items, so check for them before reading.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/tags-slug-related-tags-tags.json`](../../../catalog/models/polymarket/tags-slug-related-tags-tags.json) · Store page: https://www.sandbase.ai/model/polymarket/tags-slug-related-tags-tags
