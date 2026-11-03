# Brave Rich Search API: pricing, parameters and code examples

`brave/web-rich` · data API · Brave · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Rich Search from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/web-rich", "callback_key": "9a186935547145e29271648369eeec01"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/web-rich', {'callback_key': '9a186935547145e29271648369eeec01'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/web-rich", {
  "callback_key": "9a186935547145e29271648369eeec01"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/web-rich", sandbase.Params{
	"callback_key": "9a186935547145e29271648369eeec01",
})
```

Same call via the path form: `POST /v1/api/brave/web-rich` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `callback_key` | string | yes | The callback key to use for the rich header  |

## Details

Returns the rich result data for a Brave web search. You pass a `callback_key` and get back a `type` and a `results` list.

### Use cases

- Fetch the rich result block (such as weather or other enhanced answers) that Brave flags in a web search response.
- Complete a two-step search flow by resolving the rich header from a web search into its full data.
- Check whether a given search produced any rich data by testing if `results` is empty.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/web-rich" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"callback_key": "9a186935547145e29271648369eeec01"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `callback_key` | string | Yes | The callback key to use for the rich header |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "results": [],
  "type": "rich"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `type` | Response type. The value is `rich` for this API. |
| `results` | List of rich result items for the callback key. It is an empty list when Brave has no rich data for the key. |

### Notes

- Get `callback_key` from the rich header in the response of [Brave Web Search](/apis/brave/web). Send that value unchanged.
- The sample response has an empty `results` list, so a key can return no rich data.
- For other result types, see [Brave News Search](/apis/brave/news) or [Brave Image Search](/apis/brave/images).

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/brave/web-rich.json`](../../../catalog/models/brave/web-rich.json) · Store page: https://www.sandbase.ai/model/brave/web-rich
