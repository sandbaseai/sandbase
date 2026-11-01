# Reddit Post Transcript

`reddit/post-transcript` · api · Reddit

Extract the spoken transcript from a Reddit video post by URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/post-transcript", "url": "https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/post-transcript', {'url': 'https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/post-transcript", {
  "url": "https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/post-transcript", sandbase.Params{
	"url": "https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/",
})
```

Same call via the path form: `POST /v1/api/reddit/post-transcript` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Reddit post URL or direct v.redd.it video URL to transcribe.  |
| `language` | string |  | Optional two-letter language code (defaults to en).  |

## Details

Extract the spoken transcript from a Reddit video post by URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/post-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.reddit.com/r/youseeingthisshit/comments/1oiu9xm/"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Reddit post URL or direct v.redd.it video URL to transcribe. |
| `language` | string | No | Optional two-letter language code (defaults to en). |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/reddit/post-transcript.json`](../../../catalog/models/reddit/post-transcript.json) · Store page: https://www.sandbase.ai/model/reddit/post-transcript
