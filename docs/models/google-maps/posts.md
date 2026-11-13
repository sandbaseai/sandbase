# Google Maps Posts API: pricing, parameters and code examples

`google-maps/posts` · data API · Google Maps · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get the owner posts and updates published on a Google Maps place by data ID, with text, images, date and links.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-maps/posts", "data_id": "0x89c259a61c75684f:0x79d31adb123348d2"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-maps/posts', {'data_id': '0x89c259a61c75684f:0x79d31adb123348d2'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-maps/posts", {
  "data_id": "0x89c259a61c75684f:0x79d31adb123348d2"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-maps/posts", sandbase.Params{
	"data_id": "0x89c259a61c75684f:0x79d31adb123348d2",
})
```

Same call via the path form: `POST /v1/api/google-maps/posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `data_id` | string | yes | Parameter defines the Google Maps data ID. Find the data ID of a place using our Google Maps API.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `next_page_token` | string |  | Parameter defines the next page token. It is used for retrieving the next page results. `10` results are returned per page.  |

## Details

Get the owner posts and updates published on a Google Maps place by data ID, with text, images, date and links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-maps/posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"data_id": "0x89c259a61c75684f:0x79d31adb123348d2"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `data_id` | string | Yes | Parameter defines the Google Maps data ID. Find the data ID of a place using our Google Maps API. |
| `next_page_token` | string | No | Parameter defines the next page token. It is used for retrieving the next page results. `10` results are returned per page. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-maps/posts.json`](../../../catalog/models/google-maps/posts.json) · Store page: https://www.sandbase.ai/model/google-maps/posts
