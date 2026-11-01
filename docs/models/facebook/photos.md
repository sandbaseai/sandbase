# Facebook Page Photos

`facebook/photos` · api · Facebook

Fetch recent photos posted by any public Facebook page or profile (image URLs, captions, and dimensions) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/photos", "url": "https://www.facebook.com/Spurs"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/photos', {'url': 'https://www.facebook.com/Spurs'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/photos", {
  "url": "https://www.facebook.com/Spurs"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/photos", sandbase.Params{
	"url": "https://www.facebook.com/Spurs",
})
```

Same call via the path form: `POST /v1/api/facebook/photos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | URL of the public Facebook page or profile to fetch photos from (e.g. https://www.facebook.com/Spurs).  |
| `cursor` | string |  | Pagination cursor from a previous response to fetch the next page.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `imageWidth`, and it is served only by a source that returns every…  |

## Details

Fetch recent photos posted by any public Facebook page or profile (image URLs, captions, and dimensions) as normalized JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/photos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/Spurs"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | URL of the public Facebook page or profile to fetch photos from (e.g. https://www.facebook.com/Spurs). |
| `cursor` | string | No | Pagination cursor from a previous response to fetch the next page. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `imageWidth`, and it is served only by a source that returns every one |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/photos.json`](../../../catalog/models/facebook/photos.json) · Store page: https://www.sandbase.ai/model/facebook/photos
