# Douban Recent Hot Tv

`douban/recent-hot-tv` · api · Douban

Get a paginated list of TV titles currently featured in Douban's recent-hot collection. Use it to discover popular series and continue through result pages.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douban/recent-hot-tv"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douban/recent-hot-tv', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douban/recent-hot-tv", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douban/recent-hot-tv", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douban/recent-hot-tv` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |

## Details

Get a paginated list of TV titles currently featured in Douban's recent-hot collection. Use it to discover popular series and continue through result pages.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douban/recent-hot-tv" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douban/recent-hot-tv.json`](../../../catalog/models/douban/recent-hot-tv.json) · Store page: https://www.sandbase.ai/model/douban/recent-hot-tv
