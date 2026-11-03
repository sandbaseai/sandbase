# Bilibili Room Stream Data API: pricing, parameters and code examples

`bilibili/web/live-videos` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns stream URLs and playback connection details for a specific Bilibili broadcast room. Filter using the unique room identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/live-videos", "room_id": "1815229528"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/live-videos', {'room_id': '1815229528'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/live-videos", {
  "room_id": "1815229528"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/live-videos", sandbase.Params{
	"room_id": "1815229528",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/live-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Live room ID  |

## Details

Returns stream URLs and quality settings for one Bilibili live room. The only input is `room_id`, the live room ID, sent as a string.

### Use cases

- Pull the FLV stream URLs for a live room to feed an external video player.
- Check which quality level a room is currently streaming at.
- Compare the backup stream endpoints listed for a room.
- List the quality labels a room offers before choosing a stream.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/live-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "1815229528"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "accept_quality": [
      "4"
    ],
    "current_qn": 10000,
    "current_quality": 4,
    "durl": [
      {
        "length": 0,
        "order": 1,
        "p2p_type": -1,
        "stream_type": 0,
        "url": "https://d1--ov-gotcha07.bilivideo.com/live-bvc/251381/live_1777360364_82518558.f…"
      }
    ],
    "quality_description": [
      {
        "desc": "原画",
        "qn": 10000
      }
    ]
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.durl[].url` | Full stream URL for the room. The query string carries values such as `expires` and `qn`. |
| `data.durl[].order` | Position of the stream URL in the list, starting at 1. Each entry points to a different host. |
| `data.durl[].stream_type / data.durl[].p2p_type / data.durl[].length` | Stream type code, P2P type code and length value for each URL. In the sample, `stream_type` is `0`, `p2p_type` is `-1` and `length` is `0`. |
| `data.current_qn` | Quality number of the stream now being served. The sample returns `10000`. |
| `data.current_quality` | Current quality level as a small integer. The sample returns `4`. |
| `data.accept_quality[]` | Quality levels the room accepts, returned as strings. The sample lists `"4"`. |
| `data.quality_description[].qn` | Quality number that matches a quality label. |
| `data.quality_description[].desc` | Text label for the quality number. In the sample, `10000` is labeled `原画`. |
| `code / message` | Status of the call. `code` is `0` and `message` is `OK` on success. |

### Notes

- Send `room_id` as a string, for example `"1815229528"`.
- The stream URLs contain an `expires` value in the query string, so fetch a fresh response before you play a stream.
- To get room details such as title or host info, call [Bilibili Live Room Details](/apis/bilibili/web/live-room-detail).
- To browse live categories, call [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/live-videos.json`](../../../../catalog/models/bilibili/web/live-videos.json) · Store page: https://www.sandbase.ai/model/bilibili/web/live-videos
