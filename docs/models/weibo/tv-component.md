# Weibo TV Video Details

`weibo/tv-component` · api · Weibo

Get Weibo TV video details for a colon-delimited object ID (OID). Use it to look up a known TV video for content review, cataloging, or downstream processing.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/tv-component", "oid": "1022:2309405359416706203708"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/tv-component', {'oid': '1022:2309405359416706203708'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/tv-component", {
  "oid": "1022:2309405359416706203708"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/tv-component", sandbase.Params{
	"oid": "1022:2309405359416706203708",
})
```

Same call via the path form: `POST /v1/api/weibo/tv-component` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `oid` | string | yes | Weibo video/object ID.  |

## Details

Get Weibo TV video details for a colon-delimited object ID (OID). Use it to look up a known TV video for content review, cataloging, or downstream processing.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/tv-component" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oid": "1022:2309405359416706203708"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oid` | string | Yes | Weibo video/object ID. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/weibo/tv-component.json`](../../../catalog/models/weibo/tv-component.json) · Store page: https://www.sandbase.ai/model/weibo/tv-component
