# Xiaohongshu Pugongying Data Summary API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/data-v3-data-summary` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get the Xiaohongshu Pugongying data summary for a creator's daily or cooperation notes. Use it to compare aggregate creator performance between business modes.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/data-v3-data-summary", "userId": "64b898310000000014037b21"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/data-v3-data-summary', {'userId': '64b898310000000014037b21'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/data-v3-data-summary", {
  "userId": "64b898310000000014037b21"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/data-v3-data-summary", sandbase.Params{
	"userId": "64b898310000000014037b21",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/data-v3-data-summary` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |
| `business` | string |  | Business type. one of: `DAILY_NOTE`, `COOPERATE_NOTE`; default `"DAILY_NOTE"` |

## Details

Get the Xiaohongshu Pugongying data summary for a creator's daily or cooperation notes. Use it to compare aggregate creator performance between business modes.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/data-v3-data-summary" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "64b898310000000014037b21"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |
| `business` | string | No | Business type. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/data-v3-data-summary.json`](../../../../catalog/models/xiaohongshu/pgy-v2/data-v3-data-summary.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/data-v3-data-summary
