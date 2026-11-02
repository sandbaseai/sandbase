# Xiaohongshu Pugongying Note Details API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/note-id-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Xiaohongshu Pugongying details for a known note ID. Use it to review an individual note during creator or campaign research.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/note-id-detail", "noteId": "6abccf9c000000000a02609a"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/note-id-detail', {'noteId': '6abccf9c000000000a02609a'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/note-id-detail", {
  "noteId": "6abccf9c000000000a02609a"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/note-id-detail", sandbase.Params{
	"noteId": "6abccf9c000000000a02609a",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/note-id-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `noteId` | string | yes | Note's unique ID.  |

## Details

Get Xiaohongshu Pugongying details for a known note ID. Use it to review an individual note during creator or campaign research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/note-id-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"noteId": "6abccf9c000000000a02609a"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `noteId` | string | Yes | Note's unique ID. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/note-id-detail.json`](../../../../catalog/models/xiaohongshu/pgy-v2/note-id-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/note-id-detail
