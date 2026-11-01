# Bilibili User Collection Folder Videos

`bilibili/web/user-collection-videos` · api · Bilibili

Returns video data stored within a specified collection folder on Bilibili. Supports pagination to browse through items in the folder.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-collection-videos", "folder_id": "1756059545"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-collection-videos', {'folder_id': '1756059545'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-collection-videos", {
  "folder_id": "1756059545"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-collection-videos", sandbase.Params{
	"folder_id": "1756059545",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-collection-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pn` | integer |  | Page number  |
| `folder_id` | string | yes | collection folder id  |

## Details

Query videos inside a user collection folder by specifying `folder_id`. Use `pn` to navigate across multiple pages of results.

### Use cases

- List videos saved in a specific Bilibili collection folder.
- Track media items curated within user collection directories.
- Paginate through large folders of saved video content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-collection-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"folder_id": "<folder_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `folder_id` | string | Yes | collection folder id |
| `pn` | integer | No | Page number |

### Notes

- Specify the target collection using `folder_id`.
- Use `pn` to set the page number for paginated results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/user-collection-videos.json`](../../../../catalog/models/bilibili/web/user-collection-videos.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-collection-videos
