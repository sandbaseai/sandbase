# YouTube Video Sponsors

`youtube/video-sponsors` · api · YouTube

Detect suspected sponsors and paid promotions in a YouTube video by URL (sponsor names, websites, confidence).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-sponsors", "url": "https://www.youtube.com/watch?v=AVO0ifle-OU"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-sponsors', {'url': 'https://www.youtube.com/watch?v=AVO0ifle-OU'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-sponsors", {
  "url": "https://www.youtube.com/watch?v=AVO0ifle-OU"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-sponsors", sandbase.Params{
	"url": "https://www.youtube.com/watch?v=AVO0ifle-OU",
})
```

Same call via the path form: `POST /v1/api/youtube/video-sponsors` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | YouTube video or Short URL.  |
| `language` | string |  | 2-letter language code for transcript lookup (e.g. en, es, fr).  |

## Details

Detect suspected sponsors and paid promotions in a YouTube video by URL (sponsor names, websites, confidence).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-sponsors" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=AVO0ifle-OU"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | YouTube video or Short URL. |
| `language` | string | No | 2-letter language code for transcript lookup (e.g. en, es, fr). |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/video-sponsors.json`](../../../catalog/models/youtube/video-sponsors.json) · Store page: https://www.sandbase.ai/model/youtube/video-sponsors
