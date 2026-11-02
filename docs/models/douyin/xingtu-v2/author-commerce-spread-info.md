# Douyin Author Commerce Spread Info API: pricing, parameters and code examples

`douyin/xingtu-v2/author-commerce-spread-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call · **Modes:** sync

Get Author Commerce Spread Info on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.003 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-commerce-spread-info", "o_author_id": "7112600044674482187"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-commerce-spread-info', {'o_author_id': '7112600044674482187'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-commerce-spread-info", {
  "o_author_id": "7112600044674482187"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-commerce-spread-info", sandbase.Params{
	"o_author_id": "7112600044674482187",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-commerce-spread-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `o_author_id` | string | yes | Creator ID  |

## Details

Get Author Commerce Spread Info on Douyin. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-commerce-spread-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7112600044674482187"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-commerce-spread-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-commerce-spread-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-commerce-spread-info
