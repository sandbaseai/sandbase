# Xiaohongshu Note Details

`xiaohongshu/note-detail` · api · Xiaohongshu

Get Xiaohongshu (RedNote) details for a note identified by a note ID or supported explore URL. Use it to perform direct note lookup and content review from stored identifiers or shared explore links.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/note-detail", "noteId": "6ae00b99000000001200a9f9"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/note-detail', {'noteId': '6ae00b99000000001200a9f9'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/note-detail", {
  "noteId": "6ae00b99000000001200a9f9"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/note-detail", sandbase.Params{
	"noteId": "6ae00b99000000001200a9f9",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/note-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `noteId` | string | yes | A Xiaohongshu note ID or an explore URL containing /explore/.  |

## Details

Get Xiaohongshu (RedNote) details for a note identified by a note ID or supported explore URL. Use it to perform direct note lookup and content review from stored identifiers or shared explore links.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/note-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"noteId": "6ae00b99000000001200a9f9"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `noteId` | string | Yes | A Xiaohongshu note ID or an explore URL containing /explore/. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/note-detail.json`](../../../catalog/models/xiaohongshu/note-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/note-detail
