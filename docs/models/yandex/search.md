# Yandex Search API: pricing, parameters and code examples

`yandex/search` · data API · Yandex · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Yandex web results for a query with organic results and pagination, localized by Yandex domain, region and language.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yandex/search", "text": "best coffee grinder"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yandex/search', {'text': 'best coffee grinder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yandex/search", {
  "text": "best coffee grinder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yandex/search", sandbase.Params{
	"text": "best coffee grinder",
})
```

Same call via the path form: `POST /v1/api/yandex/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `p` | string |  | Parameter defines page number. Pagination starts from 0.  |
| `lr` | string |  | Parameter defines country or region ID to limit the search results to. Head to the Yandex locations for a full list of supported Yandex locations. If parameter is not set - the matching location of selected…  |
| `lang` | string |  | Parameter defines the language to use for the Yandex search. Head to the Yandex languages for a full list of supported Yandex languages. It defaults to `en` when `yandex_domain` is `yandex.com`.  |
| `text` | string | yes | Parameter defines the search query. You can use anything that you would use in a regular Yandex search. It can be 400 characters at maximum. Yandex usually accepts first 40 words of the query.  |
| `period` | string |  | Parameter defines the time period for search results. It can be set to: `all` - all time (Default) `day` - last day `last_two_weeks` - last two weeks `month` - last month  |
| `fix_typo` | string |  | Parameter enables or disables automatic spelling correction. It can be set to: `true` - `false`. It defaults to `true`.  |
| `sort_mode` | string |  | Parameter defines the sorting mode of search results. It can be set to: `relevance` - by relevance (default) `date` - by date.  |
| `family_mode` | string |  | Parameter enables or disables Family Mode (safe search). It can be set to: - Off(`0`) - Moderate(`1`) - Strict(`2`). It defaults to Moderate(`1`).  |
| `yandex_domain` | string |  | Parameter defines the Yandex domain to use. It defaults to `yandex.com`. Head to the Yandex domains for a full list of supported Yandex domains. A default&nbsp;`lr` is used for each&nbsp;`yandex_domain`. Example:…  |
| `groups_on_page` | string |  | Parameter defines the maximum number of groups displayed on a single results page. It defaults to `20`.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Yandex web results for a query with organic results and pagination, localized by Yandex domain, region and language.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yandex/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "best coffee grinder"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `text` | string | Yes | Parameter defines the search query. You can use anything that you would use in a regular Yandex search. It can be 400 characters at maximum. Yandex usually accepts first 40 words of the query. |
| `yandex_domain` | string | No | Parameter defines the Yandex domain to use. It defaults to `yandex.com`. Head to the Yandex domains for a full list of supported Yandex domains. A default&nbsp;`lr` is used for each&nbsp;`yandex_domain`. Example: `84`(US) for `yandex.com` A |
| `lang` | string | No | Parameter defines the language to use for the Yandex search. Head to the Yandex languages for a full list of supported Yandex languages. It defaults to `en` when `yandex_domain` is `yandex.com`. |
| `lr` | string | No | Parameter defines country or region ID to limit the search results to. Head to the Yandex locations for a full list of supported Yandex locations. If parameter is not set - the matching location of selected `yandex_domain` is used, e.g. `84 |
| `family_mode` | string | No | Parameter enables or disables Family Mode (safe search). It can be set to: - Off(`0`) - Moderate(`1`) - Strict(`2`). It defaults to Moderate(`1`). |
| `fix_typo` | string | No | Parameter enables or disables automatic spelling correction. It can be set to: `true` - `false`. It defaults to `true`. |
| `groups_on_page` | string | No | Parameter defines the maximum number of groups displayed on a single results page. It defaults to `20`. |
| `sort_mode` | string | No | Parameter defines the sorting mode of search results. It can be set to: `relevance` - by relevance (default) `date` - by date. |
| `period` | string | No | Parameter defines the time period for search results. It can be set to: `all` - all time (Default) `day` - last day `last_two_weeks` - last two weeks `month` - last month |
| `p` | string | No | Parameter defines page number. Pagination starts from 0. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yandex/search.json`](../../../catalog/models/yandex/search.json) · Store page: https://www.sandbase.ai/model/yandex/search
