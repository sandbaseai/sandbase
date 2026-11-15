# Eastmoney Community Posts API: pricing, parameters and code examples

`eastmoney/community-posts` · data API · Eastmoney · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get stock community discussion posts from EastMoney's Guba forum related to the stock screening topic (znxg). Returns posts with title, content, author, and publish time. Paginated by page/page_size.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "eastmoney/community-posts"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('eastmoney/community-posts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("eastmoney/community-posts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "eastmoney/community-posts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/eastmoney/community-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for results pagination. default `1` |
| `page_size` | integer |  | Number of posts per page. default `15` |

## Details

Get stock community discussion posts from EastMoney's Guba forum related to the stock screening topic (znxg). Returns posts with title, content, author, and publish time. Paginated by page/page_size.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "eastmoney/community-posts", "page": 1, "page_size": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number for results pagination. |
| `page_size` | integer | No | Number of posts per page. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/eastmoney/community-posts.json`](../../../catalog/models/eastmoney/community-posts.json) · Store page: https://www.sandbase.ai/model/eastmoney/community-posts
