# TikTok Location Search

`tiktok/app-v3/location-search` · api · TikTok

Searches for locations on TikTok using a text query. Returns matching place results with pagination support via offset and count parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/location-search", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/location-search', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/location-search", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/location-search", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/location-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `offset` | integer |  | Offset default `0` |
| `keyword` | string | yes | Keyword  |

## Details

Search for locations on TikTok by submitting a query string in `keyword`. Page through matching results using `offset` and `count`.

### Use cases

- Search for specific places or venues on TikTok by name.
- Tag TikTok posts with relevant venue locations.
- Explore geographic points of interest across TikTok datasets.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/location-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Keyword |
| `count` | integer | No | Number |
| `offset` | integer | No | Offset |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "global_doodle_config": {
    "feedback_survey": [
      {
        "multiple_choices": [
          {
            "value": "Unrelated location"
          }
        ]
      }
    ]
  }
}
```

### Notes

- Paginate through results by adjusting `offset` and `count`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/location-search.json`](../../../../catalog/models/tiktok/app-v3/location-search.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/location-search
