# X / Twitter Article

`twitter/article` · api · X (Twitter)

Get a public X long-form article from its wrapper post URL, including its author, engagement, cover image, and structured content blocks.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00054**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/article", "url": "https://x.com/Decentralisedco/status/1905545699552375179"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/article', {'url': 'https://x.com/Decentralisedco/status/1905545699552375179'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/article", {
  "url": "https://x.com/Decentralisedco/status/1905545699552375179"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/article", sandbase.Params{
	"url": "https://x.com/Decentralisedco/status/1905545699552375179",
})
```

Same call via the path form: `POST /v1/api/twitter/article` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Canonical x.com or twitter.com URL of the public wrapper post for an X Article.  |

## Details

Get a public X long-form article from its wrapper post URL, including its author, engagement, cover image, and structured content blocks.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/article" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://x.com/Decentralisedco/status/1905545699552375179"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Canonical x.com or twitter.com URL of the public wrapper post for an X Article. |

### Pricing

Billed at the actual cost of each call, usually $0.00054 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/twitter/article.json`](../../../catalog/models/twitter/article.json) · Store page: https://www.sandbase.ai/model/twitter/article
