# Xiaohongshu (RED) PGY Note Detail

`xiaohongshu/pgy/note-detail` · api · Xiaohongshu

Returns detailed information for a specific Pugongying (PGY) note on Xiaohongshu (RED). Look up content and metadata using a note identifier.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/note-detail", "note_id": "6a20edfa0000000021020951"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/note-detail', {'note_id': '6a20edfa0000000021020951'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/note-detail", {
  "note_id": "6a20edfa0000000021020951"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/note-detail", sandbase.Params{
	"note_id": "6a20edfa0000000021020951",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/note-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `note_id` | string | yes | Note ID, e.g. "6a20edfa0000000021020951"  |

## Details

Fetch detailed information for a Pugongying note on Xiaohongshu (RED) using its `note_id`. This endpoint returns metadata and data records associated with the note.

### Use cases

- Inspect individual Pugongying note information and details.
- Monitor performance metadata for sponsored Xiaohongshu (RED) posts.
- Integrate commercial partner note data into external analytics tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/note-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id": "<note_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `note_id` | string | Yes | Note ID, e.g. "6a20edfa0000000021020951" |

### Notes

- Supply the target note identifier using `note_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/model/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/model/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/model/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/note-detail.json`](../../../../catalog/models/xiaohongshu/pgy/note-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/note-detail
