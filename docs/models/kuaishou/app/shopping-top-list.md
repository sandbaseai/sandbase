# Kuaishou Shopping Top List API: pricing, parameters and code examples

`kuaishou/app/shopping-top-list` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns ranked shopping live streams and top product leaderboards from Kuaishou. Filter results by specific sub-tab identifiers or names.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/shopping-top-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/shopping-top-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/shopping-top-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/shopping-top-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/shopping-top-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `subTabId` | integer |  | 子标签ID/Sub tag ID default `0` |
| `subTabName` | string |  | 子标签名称/Sub tag name default `""` |

## Details

Retrieve trending Kuaishou shopping live streams and top-ranked broadcast entries. Specify `subTabId` or `subTabName` to inspect specific shopping categories.

### Use cases

- Track popular Kuaishou e-commerce live streams in real time.
- Analyze trending sellers and broadcast rankings across shopping categories.
- Monitor top-performing shopping streams for market intelligence.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/shopping-top-list" \
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
            "linkUrl": "kwai://liveaggregatesquare?path=/rest/n/live/feed/common/slide/more&selectedLiveStreamId=…",
            "title": "鹿5号12点生日狂欢 全场补贴",
            "viewType": 2,
            "logInfo": {
              "authorid": "98878703",
              "id": "98878703",
              "type": "USER"
            },
            "signalParams": {
              "author_id": "98878703"
            }
          }
        ]
      }
    ]
  }
}
```

### Notes

- Filter category results by passing optional `subTabId` or `subTabName`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/shopping-top-list.json`](../../../../catalog/models/kuaishou/app/shopping-top-list.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/shopping-top-list
