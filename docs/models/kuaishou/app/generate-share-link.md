# Kuaishou App Share Link API: pricing, parameters and code examples

`kuaishou/app/generate-share-link` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Generates a shareable URL for Kuaishou application content using a specified object identifier. Returns share link details for the target item.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/generate-share-link", "shareObjectId": "3xg5wjqdtekbb3u"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/generate-share-link', {'shareObjectId': '3xg5wjqdtekbb3u'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/generate-share-link", {
  "shareObjectId": "3xg5wjqdtekbb3u"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/generate-share-link", sandbase.Params{
	"shareObjectId": "3xg5wjqdtekbb3u",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/generate-share-link` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shareObjectId` | string | yes | 作品ID/Photo ID  |

## Details

This endpoint produces a share link for a specific Kuaishou app object using `shareObjectId`.

### Use cases

- Produce Kuaishou sharing links for specified app objects.
- Format direct links for sharing Kuaishou items across external channels.
- Direct users to target Kuaishou media via generated share URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/generate-share-link" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shareObjectId": "<shareObjectId>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shareObjectId` | string | Yes | — |

### Notes

- `shareObjectId` is a required parameter identifying the target object.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.
- [Kuaishou Hot Board Detail](/model/kuaishou/app/hot-board-detail): Returns trending topics and search keywords from Kuaishou hot boards based on the specified board identifier and board type.

---
Machine-readable: [`catalog/models/kuaishou/app/generate-share-link.json`](../../../../catalog/models/kuaishou/app/generate-share-link.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/generate-share-link
