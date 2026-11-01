# Facebook Page Contact Info

`facebook/page-contact` · api · Facebook

Look up a Facebook Page's public contact details (email, phone, website, and address) by page URL or ID.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/page-contact", "page": "https://www.facebook.com/joesstonecrab"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/page-contact', {'page': 'https://www.facebook.com/joesstonecrab'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/page-contact", {
  "page": "https://www.facebook.com/joesstonecrab"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/page-contact", sandbase.Params{
	"page": "https://www.facebook.com/joesstonecrab",
})
```

Same call via the path form: `POST /v1/api/facebook/page-contact` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string | yes | Facebook Page URL or page ID to look up (e.g. https://www.facebook.com/nasa).  |
| `language` | string |  | Locale code for the returned data (e.g. en-US). default `"en-US"` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `createdUtc` or `adStatus`, and it is served only by a source that…  |

## Details

Look up a Facebook Page's public contact details (email, phone, website, and address) by page URL or ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/page-contact" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page": "https://www.facebook.com/joesstonecrab"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | string | Yes | Facebook Page URL or page ID to look up (e.g. https://www.facebook.com/nasa). |
| `language` | string | No | Locale code for the returned data (e.g. en-US). Default `"en-US"`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `createdUtc` or `adStatus`, and it is served only by a source that ret |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/page-contact.json`](../../../catalog/models/facebook/page-contact.json) · Store page: https://www.sandbase.ai/model/facebook/page-contact
