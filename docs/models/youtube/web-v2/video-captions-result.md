# YouTube Video Captions Job Result API: pricing, parameters and code examples

`youtube/web-v2/video-captions-result` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the status and finished captions for an asynchronous video caption request by job ID. Supports output formats including SRT, XML, JSON3, and TXT once completed.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/video-captions-result", "job_id": "<job_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/video-captions-result', {'job_id': '<job_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/video-captions-result", {
  "job_id": "<job_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/video-captions-result", sandbase.Params{
	"job_id": "<job_id>",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/video-captions-result` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `format` | string |  | Caption format (applies only when the job is completed) one of: `srt`, `xml`, `json3`, `txt` |
| `job_id` | string | yes | Async job ID (returned by `/get_video_captions`)  |

## Details

Retrieve finished captions or check task progress for an asynchronous job using `job_id`. Specify the desired output layout with `format` once processing completes.

### Use cases

- Check the status of an asynchronous caption extraction task.
- Retrieve completed video subtitles in SRT, XML, JSON3, or TXT format.
- Extract subtitle transcripts for text analysis or translation workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-captions-result" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"job_id": "<job_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `job_id` | string | Yes | Async job ID (returned by `/get_video_captions`) |
| `format` | string | No | Caption format (applies only when the job is completed) |

### Notes

- `job_id` is obtained from the caption extraction endpoint.
- Supported `format` values include srt, xml, json3, and txt once the job completes.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-captions-result.json`](../../../../catalog/models/youtube/web-v2/video-captions-result.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-captions-result
