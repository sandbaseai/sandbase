# Pipixia Hashtag Details

`pipixia/app/hashtag-detail` · api · Pipixia

Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/hashtag-detail", "hashtag_id": "129559"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/hashtag-detail', {'hashtag_id': '129559'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/hashtag-detail", {
  "hashtag_id": "129559"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/hashtag-detail", sandbase.Params{
	"hashtag_id": "129559",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/hashtag-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hashtag_id` | string | yes | AKA hashtag id, can be obtained from the share link.  |

## Details

Returns detailed hashtag information from Pipixia using the required `hashtag_id` parameter.

### Use cases

- Look up metadata and avatar assets for a Pipixia topic tag.
- Inspect specific hashtag information extracted from a share URL.
- Display Pipixia hashtag profiles within content tracking tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/hashtag-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hashtag_id": "129559"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag_id` | string | Yes | AKA hashtag id, can be obtained from the share link. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "hashtag": {
      "base_hashtag": {
        "avatars": [
          {}
        ]
      }
    }
  }
}
```

### Notes

- The `hashtag_id` can be obtained from the topic share link.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Post List](/model/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/model/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.
- [Pipixia Home Short Drama Feed](/model/pipixia/app/home-short-drama-feed): Returns short drama and novel recommendations from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/hashtag-detail.json`](../../../../catalog/models/pipixia/app/hashtag-detail.json) · Store page: https://www.sandbase.ai/model/pipixia/app/hashtag-detail
