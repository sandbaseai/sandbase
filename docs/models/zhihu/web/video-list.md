# Zhihu Video List API: pricing, parameters and code examples

`zhihu/web/video-list` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves a paginated list of videos from the Zhihu web platform. Supports pagination controls through page size and offset index parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/video-list", "limit": "12", "offset": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/video-list', {'limit': '12', 'offset': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/video-list", {
  "limit": "12",
  "offset": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/video-list", sandbase.Params{
	"limit": "12",
	"offset": "0",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of videos per page default `"12"` |
| `offset` | string |  | Offset default `"0"` |

## Details

Returns a page of videos from the Zhihu recommended video feed. It takes no required input. You can set `limit` for page size and `offset` for the start position.

### Use cases

- Page through the Zhihu recommended video feed to log which videos appear.
- Build a dashboard that shows a rolling sample of Zhihu video entries.
- Check whether more pages exist before running a bulk collection job.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | string | No | Number of videos per page |
| `offset` | string | No | Offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [],
  "paging": {
    "is_end": false,
    "is_start": true,
    "next": "https://www.zhihu.com/api/v4/zvideo-tabs/tabs/choice/feeds/recommend?include=cre…",
    "previous": "",
    "totals": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | List of video entries on the current page. It was empty in the sample response, so check the length before reading items. |
| `paging.is_end` | `true` when there are no more pages after this one. |
| `paging.is_start` | `true` when this is the first page of the list. |
| `paging.next` | URL of the next page. It includes `limit=12` and `offset=12` as query values. |
| `paging.previous` | URL of the previous page. It is an empty string on the first page. |
| `paging.totals` | Total count reported for the list. It was `0` in the sample response. |

### Notes

- Both `limit` and `offset` are sent as strings. The defaults are `12` and `0`.
- To get the next page, add `limit` to `offset` and call again. The `paging.next` URL shows the same values.
- Stop paging when `paging.is_end` is `true`.
- To search videos by keyword instead, use [Zhihu Video Search (V3)](/apis/zhihu/web/video-search-v3).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/video-list.json`](../../../../catalog/models/zhihu/web/video-list.json) · Store page: https://www.sandbase.ai/model/zhihu/web/video-list
