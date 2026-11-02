# DataForSEO Bing Search Volume History API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/bing/search_volume_history/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.09 per call · **Modes:** sync

Get monthly Bing search volume history for up to 1000 keywords. Bing Ads search volume history for a keyword list.

## Pricing

- **$0.09 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/bing/search_volume_history/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/bing/search_volume_history/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/bing/search_volume_history/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/bing/search_volume_history/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/bing/search_volume_history/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | List of keywords (up to 100 per call).  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Get monthly Bing search volume history for up to 1000 keywords.

Request fields follow the official DataForSEO `/v3/keywords_data/bing/search_volume_history/live` task schema (one task per call; send `{"tasks": [...]}` for several). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/bing/search_volume_history/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `keywords` | List of keywords (up to 100 per call). |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Reference

- Official docs: https://docs.dataforseo.com/v3/keywords_data/bing/search_volume_history/live/

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/bing/search_volume_history/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/bing/search_volume_history/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/bing/search_volume_history/live
