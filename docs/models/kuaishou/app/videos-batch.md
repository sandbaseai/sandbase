# Kuaishou Batch Video Details API: pricing, parameters and code examples

`kuaishou/app/videos-batch` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.04 per call · **Modes:** sync

Retrieves video details for multiple Kuaishou posts in a single request. Specify comma-separated photo IDs to look up information for up to 40 videos at once.

## Pricing

- **$0.04 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/videos-batch", "photo_ids": "5228960823332207296,5196309727975443273,5222486898325987583"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/videos-batch', {'photo_ids': '5228960823332207296,5196309727975443273,5222486898325987583'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/videos-batch", {
  "photo_ids": "5228960823332207296,5196309727975443273,5222486898325987583"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/videos-batch", sandbase.Params{
	"photo_ids": "5228960823332207296,5196309727975443273,5222486898325987583",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/videos-batch` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `photo_ids` | string | yes | Photo ID list, multiple IDs separated by commas, max 40 per request  |

## Details

Query details for multiple Kuaishou videos simultaneously using `photo_ids`.

### Use cases

- Retrieve metadata for a list of Kuaishou videos simultaneously.
- Monitor engagement and view stats across multiple video posts.
- Sync video catalog records in bulk using their photo IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/videos-batch" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_ids": "5228960823332207296,5196309727975443273,5222486898325987583"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_ids` | string | Yes | Photo ID list, multiple IDs separated by commas, max 40 per request |

### Notes

- Supply comma-separated IDs to `photo_ids` with a maximum of 40 IDs per request.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/videos-batch.json`](../../../../catalog/models/kuaishou/app/videos-batch.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/videos-batch
