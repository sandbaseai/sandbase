# OpenTable Reviews API: pricing, parameters and code examples

`opentable/reviews` · data API · OpenTable · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get diner reviews for a restaurant on OpenTable by restaurant ID, with overall and sub-ratings, text, date and diner info.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "opentable/reviews", "rid": "r/central-park-boathouse-new-york-2"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('opentable/reviews', {'rid': 'r/central-park-boathouse-new-york-2'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("opentable/reviews", {
  "rid": "r/central-park-boathouse-new-york-2"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "opentable/reviews", sandbase.Params{
	"rid": "r/central-park-boathouse-new-york-2",
})
```

Same call via the path form: `POST /v1/api/opentable/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `rid` | string | yes | Parameter defines the OpenTable Restaurant ID. This identifier can be found in the URL of the restaurant's page, it's the path of the URL (the part after the first singular `/`). For example, in the URL…  |
| `page` | string |  | Parameter defines the page number. `1` (default) is the first page of 10 results, `2` is the 2nd page, etc.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get diner reviews for a restaurant on OpenTable by restaurant ID, with overall and sub-ratings, text, date and diner info.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/opentable/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"rid": "r/central-park-boathouse-new-york-2"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `rid` | string | Yes | Parameter defines the OpenTable Restaurant ID. This identifier can be found in the URL of the restaurant's page, it's the path of the URL (the part after the first singular `/`). For example, in the URL `https://www.opentable.com/r/central- |
| `page` | string | No | Parameter defines the page number. `1` (default) is the first page of 10 results, `2` is the 2nd page, etc. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/opentable/reviews.json`](../../../catalog/models/opentable/reviews.json) · Store page: https://www.sandbase.ai/model/opentable/reviews
