# Yahoo Trends API: pricing, parameters and code examples

`yahoo/trends` · data API · Yahoo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

List trending searches on Yahoo right now, with topic, related links and videos.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo/trends"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo/trends', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo/trends", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo/trends", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/yahoo/trends` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `next_page_token` | string |  | Parameter defines the next page token. It is used for retrieving the next page of results. Leave it unset for the first page. Up to `100` results are returned per page; Yahoo! may return fewer. The next page token can…  |
| `full_video_links` | string |  | Parameter defines whether to include playable video links. It can be set to `true` to include a `full_video_link` for each topic video, or `false` (default) to skip them. Enabling it performs an additional request to…  |

## Details

List trending searches on Yahoo right now, with topic, related links and videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo/trends" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `next_page_token` | string | No | Parameter defines the next page token. It is used for retrieving the next page of results. Leave it unset for the first page. Up to `100` results are returned per page; Yahoo! may return fewer. The next page token can be found in the the AP |
| `full_video_links` | string | No | Parameter defines whether to include playable video links. It can be set to `true` to include a `full_video_link` for each topic video, or `false` (default) to skip them. Enabling it performs an additional request to Yahoo!, which may incre |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo/trends.json`](../../../catalog/models/yahoo/trends.json) · Store page: https://www.sandbase.ai/model/yahoo/trends
