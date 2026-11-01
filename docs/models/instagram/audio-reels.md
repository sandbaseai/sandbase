# Instagram Reels by Audio

`instagram/audio-reels` · api · Instagram

List Instagram reels that use a given audio track by audio id.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/audio-reels", "audioId": "1392969992841787"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/audio-reels', {'audioId': '1392969992841787'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/audio-reels", {
  "audioId": "1392969992841787"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/audio-reels", sandbase.Params{
	"audioId": "1392969992841787",
})
```

Same call via the path form: `POST /v1/api/instagram/audio-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor returned by a previous response.  |
| `audioId` | string | yes | Audio identifier from the Instagram audio page URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `reshares`, and it is served only by a source that returns every one…  |

## Details

List Instagram reels that use a given audio track by audio id.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/audio-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"audioId": "1392969992841787"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `audioId` | string | Yes | Audio identifier from the Instagram audio page URL. |
| `cursor` | string | No | Pagination cursor returned by a previous response. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `reshares`, and it is served only by a source that returns every one o |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/audio-reels.json`](../../../catalog/models/instagram/audio-reels.json) · Store page: https://www.sandbase.ai/model/instagram/audio-reels
