# DataForSEO YouTube Video Comments API: pricing, parameters and code examples

`dataforseo/v3/serp/youtube/video_comments/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Top-level comments on a YouTube video by video id, with author, text, likes, reply counts and timestamps.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/youtube/video_comments/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/youtube/video_comments/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/youtube/video_comments/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/youtube/video_comments/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/youtube/video_comments/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string |  | YouTube video id, e.g. "dQw4w9WgXcQ".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Top-level comments on a YouTube video by video id, with author, text, likes, reply counts and timestamps.

Request fields follow the official DataForSEO `/v3/serp/youtube/video_comments/live/advanced` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/youtube/video_comments/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ", "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `video_id` | YouTube video id, e.g. "dQw4w9WgXcQ". |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Reference

- Official docs: https://docs.dataforseo.com/v3/serp/youtube/video_comments/live/advanced/

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/youtube/video_comments/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/youtube/video_comments/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/youtube/video_comments/live/advanced
