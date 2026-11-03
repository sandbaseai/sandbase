# Pipixia Home Short Drama Feed API: pricing, parameters and code examples

`pipixia/app/home-short-drama-feed` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns short drama and novel recommendations from the Pipixia home feed. Supports pagination to browse through items sequentially.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/home-short-drama-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/home-short-drama-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/home-short-drama-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/home-short-drama-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/pipixia/app/home-short-drama-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default is 1, add 1 for each page. default `1` |

## Details

Browse the Pipixia home short drama feed using the `page` parameter to retrieve featured drama and novel recommendations.

### Use cases

- Display Pipixia short drama recommendations within custom applications.
- Track popular drama titles and categories featured on the platform feed.
- Browse through novel and short drama catalog listings sequentially.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/home-short-drama-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number, default is 1, add 1 for each page. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "feed_data": {
        "book_data": [
          {
            "toutiao_click_rate": "0",
            "book_data": {
              "book_id": "7520802446843579417",
              "book_name": "这个破盆是宝物",
              "book_type": "0",
              "category": "武侠",
              "creation_status": "1",
              "item_schema_url": "sslocal://novel_business?category_name=&enter_from=&group_id=7520802446843579417&is_exter…"
            }
          }
        ]
      }
    }
  ]
}
```

### Notes

- Use `page` to paginate through results, defaulting to 1 and increasing by 1 for each page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/home-short-drama-feed.json`](../../../../catalog/models/pipixia/app/home-short-drama-feed.json) · Store page: https://www.sandbase.ai/model/pipixia/app/home-short-drama-feed
