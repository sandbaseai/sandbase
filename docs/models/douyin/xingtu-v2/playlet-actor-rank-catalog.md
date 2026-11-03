# Douyin Xingtu Playlet Actor Rank Catalog API: pricing, parameters and code examples

`douyin/xingtu-v2/playlet-actor-rank-catalog` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the ranking catalog options for Douyin Xingtu playlet actors. Use this endpoint to inspect available categories and ranking classifications.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/playlet-actor-rank-catalog"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/playlet-actor-rank-catalog', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/playlet-actor-rank-catalog", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/playlet-actor-rank-catalog", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/playlet-actor-rank-catalog` with the body above minus `model`.

## Details

Returns the ranking catalog for playlet actors on Douyin Xingtu. The `catalog` field holds a JSON string that lists the available ranking lists and their classifications. The request takes no input.

### Use cases

- Read which playlet actor ranking lists exist before you request a specific leaderboard.
- Collect the identifier keys in the catalog tree to build a category picker.
- Compare the catalog over time to detect new or removed ranking classifications.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/playlet-actor-rank-catalog" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "catalog": "{\"type\":1,\"children\":{\"playlet_actor_list\":{\"type\":2,\"children\":{\"playlet_actor_…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_resp.status_code` | Status code of the call. `0` means the call succeeded. |
| `base_resp.status_message` | Status text. It is an empty string in the sample response. |
| `catalog` | A JSON-encoded string, so parse it before use. It holds a nested tree of ranking options, with names such as `playlet_actor_list` and `playlet_actor_composite_list` and numeric identifiers such as `30` and `20250930` as keys. |

### Notes

- The `catalog` value is a string, not an object. Run it through a JSON parser to walk the tree.
- The tree nests several levels deep, and the keys at each level are the identifiers of the ranking options.
- Call [Douyin Xingtu Playlet Actor Ranking List](/apis/douyin/xingtu-v2/playlet-actor-rank-list) next to fetch a leaderboard.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/playlet-actor-rank-catalog.json`](../../../../catalog/models/douyin/xingtu-v2/playlet-actor-rank-catalog.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/playlet-actor-rank-catalog
