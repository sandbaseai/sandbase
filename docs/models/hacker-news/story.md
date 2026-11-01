# Hacker News Story

`hacker-news/story` · api · Hacker News

Get a Hacker News story by id - title, link, author, points, and comment count as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hacker-news/story", "id": "47340079"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hacker-news/story', {'id': '47340079'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hacker-news/story", {
  "id": "47340079"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hacker-news/story", sandbase.Params{
	"id": "47340079",
})
```

Same call via the path form: `POST /v1/api/hacker-news/story` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Hacker News story id, e.g. "47340079".  |

## Details

Get a Hacker News story by id - title, link, author, points, and comment count as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hacker-news/story" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "47340079"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Hacker News story id, e.g. "47340079". |

### Pricing

Billed at the actual cost of each call, usually $0.0015 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/hacker-news/story.json`](../../../catalog/models/hacker-news/story.json) · Store page: https://www.sandbase.ai/model/hacker-news/story
