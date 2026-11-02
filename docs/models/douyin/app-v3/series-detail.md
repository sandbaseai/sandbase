# Douyin Series Detail API: pricing, parameters and code examples

`douyin/app-v3/series-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information and UI configuration data for a Douyin playlet or video series using its unique series identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/series-detail", "series_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/series-detail', {'series_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/series-detail", {
  "series_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/series-detail", sandbase.Params{
	"series_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/series-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `series_id` | string | yes | Series id  |

## Details

Retrieve playlet and video series metadata from Douyin by specifying the target `series_id`.

### Use cases

- Inspect series UI configurations and tag placement details.
- Retrieve metadata for specific Douyin playlets.
- Track series attributes for content cataloging.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/series-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "7585746250092251178"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_id` | string | Yes | Series id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "series_info": {
    "series_ui_config": {
      "general_position_tag_infos": [
        {
          "tag_position": 903
        }
      ]
    }
  }
}
```

### Notes

- Requires a valid `series_id` to look up series information.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/series-detail.json`](../../../../catalog/models/douyin/app-v3/series-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/series-detail
