# Bilibili Video Danmaku API: pricing, parameters and code examples

`bilibili/video-danmu` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get one page of danmaku comments for a Bilibili video segment identified by AID and CID. Use it to review time-synchronized audience reactions or page through danmaku for a known video.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/video-danmu", "aid": "80433022", "cid": "137649199"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/video-danmu', {'aid': '80433022', 'cid': '137649199'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/video-danmu", {
  "aid": "80433022",
  "cid": "137649199"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/video-danmu", sandbase.Params{
	"aid": "80433022",
	"cid": "137649199",
})
```

Same call via the path form: `POST /v1/api/bilibili/video-danmu` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aid` | string | yes | Bilibili Archive ID (AID).  |
| `cid` | string | yes | Bilibili Chat ID (CID).  |
| `page` | string |  | Page number for pagination.  |

## Details

Returns one page of danmaku (time-synced viewer comments) for a Bilibili video segment. It needs the video's `aid` and `cid`, and takes an optional `page` number.

### Use cases

- Read the on-screen audience reactions for a specific video segment.
- Collect danmaku text for sentiment or keyword analysis on a known video.
- Plot when viewers comment most by grouping entries on their `stime` value.
- Page through all danmaku of a video by increasing `page`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/video-danmu" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aid": "80433022", "cid": "137649199"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aid` | string | Yes | Bilibili Archive ID (AID). |
| `cid` | string | Yes | Bilibili Chat ID (CID). |
| `page` | string | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "color": 16777215,
    "date": 1593092327,
    "dmid": "34576873522987015",
    "id": 34576873522987015,
    "mode": 1,
    "size": 25,
    "stime": 95453,
    "text": "80年代迪厅必放金曲",
    "uhash": "d2b24dbe",
    "weight": 9
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `text` | The danmaku comment text shown on screen. |
| `stime` | Time position of the comment in the video. The value 95453 suggests milliseconds, but the response does not state the unit. |
| `date` | Time the comment was posted, as a Unix timestamp in seconds. |
| `id / dmid` | Unique ID of the danmaku. `dmid` is the same number as `id`, returned as a string. |
| `uhash` | Hashed ID of the user who sent the comment. It is not a plain user ID. |
| `color` | Comment color as a decimal number. The value `16777215` is white (`#FFFFFF`). |
| `mode / size / weight` | Display mode, font size and weight value of the comment. All three are plain numbers. |

### Notes

- The response is a top-level JSON array. Each item is one danmaku comment.
- Use `page` to move through further pages for the same `aid` and `cid`.
- To find the `aid` from a BV ID, call [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid).
- To list the parts of a video and get their `cid` values, call [Bilibili Video Parts](/apis/bilibili/web/video-parts).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/bilibili/video-danmu.json`](../../../catalog/models/bilibili/video-danmu.json) · Store page: https://www.sandbase.ai/model/bilibili/video-danmu
