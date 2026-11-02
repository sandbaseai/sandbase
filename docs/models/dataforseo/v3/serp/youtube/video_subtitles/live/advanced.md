# DataForSEO YouTube Subtitles API: pricing, parameters and code examples

`dataforseo/v3/serp/youtube/video_subtitles/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.006 per call (free daily quota) · **Modes:** sync

Fetch the subtitle track of a YouTube video with timestamps. Subtitles of a YouTube video by video_id and language.

## Pricing

- **$0.006 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/youtube/video_subtitles/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/youtube/video_subtitles/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/youtube/video_subtitles/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/youtube/video_subtitles/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/youtube/video_subtitles/live/advanced` with the body above minus `model`.

## Details

Fetch the subtitle track of a YouTube video with timestamps.

Request fields follow the official DataForSEO `/v3/serp/youtube/video_subtitles/live/advanced` task schema (one task per call; send `{"tasks": [...]}` for several). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/youtube/video_subtitles/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ", "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `video_id` | YouTube video ID. |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Reference

- Official docs: https://docs.dataforseo.com/v3/serp/youtube/video_subtitles/live/advanced/

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/youtube/video_subtitles/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/youtube/video_subtitles/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/youtube/video_subtitles/live/advanced
