# Xiaohongshu PGY note featured comments API: pricing, parameters and code examples

`xiaohongshu/pgy/note-comments` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get PGY note featured comments on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/note-comments", "note_id": "6a20edfa0000000021020951"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/note-comments', {'note_id': '6a20edfa0000000021020951'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/note-comments", {
  "note_id": "6a20edfa0000000021020951"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/note-comments", sandbase.Params{
	"note_id": "6a20edfa0000000021020951",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/note-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `note_id` | string | yes | Note ID  |

## Details

Get PGY note featured comments on Xiaohongshu. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/note-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id": "6a20edfa0000000021020951"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `note_id` | string | Yes | Note ID |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/note-comments.json`](../../../../catalog/models/xiaohongshu/pgy/note-comments.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/note-comments
