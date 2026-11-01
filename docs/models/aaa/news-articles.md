# AAA News Articles

`aaa/news-articles` · api · AAA

Returns recent AAA gas price news articles with pagination support. Results include article title, publication date, excerpt, slug, and link.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/news-articles"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/news-articles', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/news-articles", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/news-articles", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/news-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. range -9007199254740991–9007199254740991 |
| `limit` | integer |  | Maximum number of articles per page. range -9007199254740991–9007199254740991 |

## Details

Returns recent AAA gas price news articles with pagination support. Results include article title, publication date, excerpt, slug, and link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/news-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of articles per page. |
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/aaa/news-articles.json`](../../../catalog/models/aaa/news-articles.json) · Store page: https://www.sandbase.ai/model/aaa/news-articles
