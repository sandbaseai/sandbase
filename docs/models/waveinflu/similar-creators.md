# Waveinflu Similar Creators

`waveinflu/similar-creators` · api · Waveinflu

Finds creators similar to a seed account on Instagram, TikTok, or YouTube.

## Pricing

- Depends on parameters (`params.limit`).

| parameters | USD |
|---|---|
| limit=1 | 0.004977 |
| limit=25 | 0.124425 |
| limit=100 | 0.4977 |

Formula: `0.004977 * Math.max(1.0, Math.min(100.0, (params.limit ?? 25) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "waveinflu/similar-creators", "target_account": "@onkimia"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('waveinflu/similar-creators', {'target_account': '@onkimia'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("waveinflu/similar-creators", {
  "target_account": "@onkimia"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "waveinflu/similar-creators", sandbase.Params{
	"target_account": "@onkimia",
})
```

Same call via the path form: `POST /v1/api/waveinflu/similar-creators` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of creators to return. Default 25, range 1–100. Caps the billed count. default `25`; range 1–100 |
| `filters` | object |  | Optional filters applied before matching. All fields are optional.  |
| `platform` | string |  | Target platform. one of: `instagram`, `tiktok`, `youtube`; default `"youtube"` |
| `target_account` | string | yes | Seed account: a creator handle (with or without @) or profile URL to find similar creators for.  |

## Details

Finds creators similar to a seed account on Instagram, TikTok, or YouTube.

The response is the official Waveinflu API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/waveinflu/similar-creators" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target_account": "nike", "platform": "instagram", "limit": 1}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `filters` | object | No | Optional filters applied before matching. All fields are optional. |
| `limit` | integer | No | Maximum number of creators to return. Default 25, range 1–100. Caps the billed count. |
| `platform` | string | No | Target platform. |
| `target_account` | string | Yes | Seed account: a creator handle (with or without @) or profile URL to find similar creators for. |

### Pricing

$0.004977 per creator requested (limit, default 25, max 100). Failed calls are not charged.

---
Machine-readable: [`catalog/models/waveinflu/similar-creators.json`](../../../catalog/models/waveinflu/similar-creators.json) · Store page: https://www.sandbase.ai/model/waveinflu/similar-creators
