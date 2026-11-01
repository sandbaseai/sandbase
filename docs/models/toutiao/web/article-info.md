# Toutiao Article Details (Web)

`toutiao/web/article-info` · api · Toutiao

Returns detailed post information and interface action settings for a specified Toutiao article based on its unique post identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/web/article-info", "aweme_id": "7450114952884503059"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/web/article-info', {'aweme_id': '7450114952884503059'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/web/article-info", {
  "aweme_id": "7450114952884503059"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/web/article-info", sandbase.Params{
	"aweme_id": "7450114952884503059",
})
```

Same call via the path form: `POST /v1/api/toutiao/web/article-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Post ID  |

## Details

Look up metadata and configuration details for a specific Toutiao post by passing `aweme_id`.

### Use cases

- Retrieve article details using a known post identifier.
- Inspect layout and action bar settings for Toutiao web content.
- Extract post data for external content indexing.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/web/article-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7450114952884503059"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Post ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "h5_extra": {
      "itemCell": {
        "actionCtrl": {
          "actionBar": {
            "actionSettingList": [
              {
                "actionType": 1
              }
            ]
          }
        }
      }
    }
  }
}
```

### Notes

- Requires `aweme_id` representing the unique post identifier.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Toutiao Specified Video Details](/model/toutiao/web/video-info): Returns detailed information for a specified Toutiao video post.

---
Machine-readable: [`catalog/models/toutiao/web/article-info.json`](../../../../catalog/models/toutiao/web/article-info.json) · Store page: https://www.sandbase.ai/model/toutiao/web/article-info
