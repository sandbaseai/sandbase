# Instagram Post Details

`instagram/post-detail` · api · Instagram

Get an Instagram post by its shortcode. Use it to look up a known post before content review, archiving, comment analysis, or related workflows.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/post-detail", "code": "C3Kg3F7vHeK"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/post-detail', {'code': 'C3Kg3F7vHeK'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/post-detail", {
  "code": "C3Kg3F7vHeK"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/post-detail", sandbase.Params{
	"code": "C3Kg3F7vHeK",
})
```

Same call via the path form: `POST /v1/api/instagram/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` | string | yes | The unique shortcode from the Instagram post URL.  |

## Details

Get an Instagram post by its shortcode. Use it to look up a known post before content review, archiving, comment analysis, or related workflows.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code": "C3Kg3F7vHeK"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | string | Yes | The unique shortcode from the Instagram post URL. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/instagram/post-detail.json`](../../../catalog/models/instagram/post-detail.json) · Store page: https://www.sandbase.ai/model/instagram/post-detail
