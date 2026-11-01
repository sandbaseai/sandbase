# Xiaohongshu (RED) Homepage Feed

`xiaohongshu/web-v3/homefeed` · api · Xiaohongshu

Retrieves recommended notes from the Xiaohongshu homepage feed. Supports filtering by category channel, restricting results to image notes, and paginating via cursor score.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/web-v3/homefeed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/web-v3/homefeed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/web-v3/homefeed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/web-v3/homefeed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/web-v3/homefeed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `num` | integer |  | Number of results, max 40 default `20`; range –40 |
| `category` | string |  | Category channel ID default `"homefeed_recommend"` |
| `cursor_score` | string |  | Pagination cursor default `""` |
| `need_filter_image` | boolean |  | Image notes only default `false` |

## Details

Access recommended homepage feed notes using optional parameters such as `category`, `num`, `cursor_score`, and `need_filter_image`.

### Use cases

- Retrieve recommended note feeds for discovery analysis.
- Filter homepage recommendations to image-only note posts.
- Monitor trending content across specific category channels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/web-v3/homefeed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `num` | integer | No | Number of results, max 40 |
| `category` | string | No | Category channel ID |
| `cursor_score` | string | No | Pagination cursor |
| `need_filter_image` | boolean | No | Image notes only |

### Notes

- `num` specifies the count of returned results up to a maximum of 40.
- Use `cursor_score` to paginate through subsequent pages of the feed.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Homepage Categories](/model/xiaohongshu/web-v3/homefeed-categories): Returns a list of available homefeed category channels on Xiaohongshu (RED).
- [Xiaohongshu (RED) Web Note Details](/model/xiaohongshu/web-v3/note-detail): Returns detailed information for a specific Xiaohongshu note using its identifier and security token obtained from a web share link.
- [Xiaohongshu (RED) Search Suggestions](/model/xiaohongshu/web-v3/search-suggest): Returns search query suggestions and autocomplete terms from Xiaohongshu (RED).

---
Machine-readable: [`catalog/models/xiaohongshu/web-v3/homefeed.json`](../../../../catalog/models/xiaohongshu/web-v3/homefeed.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/web-v3/homefeed
