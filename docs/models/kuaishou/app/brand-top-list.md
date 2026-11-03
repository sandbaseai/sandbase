# Kuaishou Brand Top List API: pricing, parameters and code examples

`kuaishou/app/brand-top-list` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns top brand rankings and related live stream links from Kuaishou. Allows filtering ranking data by sub-tab category ID or sub-tab name.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/brand-top-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/brand-top-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/brand-top-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/brand-top-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/brand-top-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `subTabId` | integer |  | 子标签ID/Sub tag ID default `0` |
| `subTabName` | string |  | 子标签名称/Sub tag name default `""` |

## Details

Look up Kuaishou brand leaderboard rankings and live feed entries using optional `subTabId` and `subTabName` parameters.

### Use cases

- Track leading brands featured across Kuaishou leaderboards.
- Inspect top-ranked live streaming sessions linked to specific brands.
- Segment brand performance rankings across different category sub-tabs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/brand-top-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subTabId` | integer | No | — |
| `subTabName` | string | No | — |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "topList": {
    "data": [
      {
        "list": [
          {
            "linkUrl": "kwai://live/play/iXyv7aayTZI?serverExpTag=feed_live|iXyv7aayTZI|2957169798|1_a/2010185635…",
            "title": "韩束",
            "viewType": 2,
            "logInfo": {
              "authorid": "2957169798",
              "id": "2957169798",
              "type": "USER"
            }
          }
        ]
      }
    ]
  }
}
```

### Notes

- Filter rankings by specifying `subTabId` or `subTabName`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.
- [Kuaishou Hot Board Detail](/apis/kuaishou/app/hot-board-detail): Returns trending topics and search keywords from Kuaishou hot boards based on the specified board identifier and board type.

---
Machine-readable: [`catalog/models/kuaishou/app/brand-top-list.json`](../../../../catalog/models/kuaishou/app/brand-top-list.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/brand-top-list
