# Xiaohongshu (RED) Web Note Details API: pricing, parameters and code examples

`xiaohongshu/web-v3/note-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specific Xiaohongshu note using its identifier and security token obtained from a web share link.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/web-v3/note-detail", "note_id": "example", "xsec_token": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/web-v3/note-detail', {'note_id': 'example', 'xsec_token': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/web-v3/note-detail", {
  "note_id": "example",
  "xsec_token": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/web-v3/note-detail", sandbase.Params{
	"note_id": "example",
	"xsec_token": "example",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/web-v3/note-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `note_id` | string | yes | Note ID, can be obtained from the sharing link of Xiaohongshu  |
| `xsec_token` | string | yes | Security token, can be obtained from the sharing link of Xiaohongshu  |

## Details

Retrieve detailed note data from Xiaohongshu by providing the `note_id` and corresponding `xsec_token`.

### Use cases

- Retrieve complete note content and metadata for external analytics.
- Monitor engagement and post information for specific platform notes.
- Archive note attributes extracted from shared platform links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/web-v3/note-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id": "6a2f423d000000001003cb36", "xsec_token": "ABtexB6bX5HgLD42SFrK1scGUmSO8YV5_isaLrDy9sLxQ="}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `note_id` | string | Yes | Note ID, can be obtained from the sharing link of Xiaohongshu |
| `xsec_token` | string | Yes | Security token, can be obtained from the sharing link of Xiaohongshu |

### Notes

- Both `note_id` and `xsec_token` can be extracted directly from a Xiaohongshu share link.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Homepage Feed](/apis/xiaohongshu/web-v3/homefeed): Retrieves recommended notes from the Xiaohongshu homepage feed.
- [Xiaohongshu (RED) Homepage Categories](/apis/xiaohongshu/web-v3/homefeed-categories): Returns a list of available homefeed category channels on Xiaohongshu (RED).
- [Xiaohongshu (RED) Search Suggestions](/apis/xiaohongshu/web-v3/search-suggest): Returns search query suggestions and autocomplete terms from Xiaohongshu (RED).

---
Machine-readable: [`catalog/models/xiaohongshu/web-v3/note-detail.json`](../../../../catalog/models/xiaohongshu/web-v3/note-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/web-v3/note-detail
