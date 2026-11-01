# Instagram Media Transcript

`instagram/media-transcript` · api · Instagram

Get the spoken-audio transcript text for an Instagram post or reel by URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/media-transcript", "url": "https://www.instagram.com/reel/DHsD6HGqJhp/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/media-transcript', {'url': 'https://www.instagram.com/reel/DHsD6HGqJhp/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/media-transcript", {
  "url": "https://www.instagram.com/reel/DHsD6HGqJhp/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/media-transcript", sandbase.Params{
	"url": "https://www.instagram.com/reel/DHsD6HGqJhp/",
})
```

Same call via the path form: `POST /v1/api/instagram/media-transcript` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Instagram post or reel URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `durationSeconds`, and it is served only by a source that returns…  |

## Details

Get the spoken-audio transcript text for an Instagram post or reel by URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/media-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/reel/DHsD6HGqJhp/"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Instagram post or reel URL. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `durationSeconds`, and it is served only by a source that returns ever |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/media-transcript.json`](../../../catalog/models/instagram/media-transcript.json) · Store page: https://www.sandbase.ai/model/instagram/media-transcript
