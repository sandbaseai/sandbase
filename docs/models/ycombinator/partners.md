# Y Combinator Partners API: pricing, parameters and code examples

`ycombinator/partners` · data API · Y Combinator · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

List all current YC Partners. Returns partner profiles with name, slug, title, short bio, and photo URLs.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ycombinator/partners"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ycombinator/partners', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ycombinator/partners", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ycombinator/partners", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ycombinator/partners` with the body above minus `model`.

## Details

This API returns the list of current Y Combinator (YC) Partners. Each entry has a name, slug, title, short bio, and photo URLs. It takes no input.

### Use cases

- Build a directory of current YC Partners with photos and bios.
- Match a founder's background to the Partner whose bio and company history look closest.
- Track changes in the Partner roster by comparing `slug` values between calls.
- Fetch each Partner's `slug` to look up their full profile with a person detail call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ycombinator/partners" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "partners": [
      {
        "batchPhoto": "https://bookface-static.ycombinator.com/assets/ycdc/partners/garry-tan-batch-com…",
        "bio": "Co-founder of Posterous (acquired by Twitter) and Initialized Capital. Early eng…",
        "name": "Garry Tan",
        "photo": "https://bookface-static.ycombinator.com/assets/ycdc/partners/garry-tan-now-compr…",
        "slug": "garry-tan",
        "title": "Posterous, S08",
        "url": "/people/garry-tan"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.partners[].name` | Full name of the Partner. |
| `data.partners[].slug` | URL-style identifier for the Partner, such as `garry-tan`. Use it as a stable key. |
| `data.partners[].title` | The company and YC batch tied to the Partner, such as `Posterous, S08`. The format is company name, then batch code. |
| `data.partners[].bio` | Short text on the Partner's background, including past companies and roles. |
| `data.partners[].photo` | URL of the Partner's current photo. |
| `data.partners[].batchPhoto` | URL of a photo of the Partner from their own batch. |
| `data.partners[].url` | Relative path to the Partner's profile page on the YC site, such as `/people/garry-tan`. |

### Notes

- The call takes no parameters. Send an empty JSON object `{}`.
- The response returns all Partners in one list. There is no pagination.
- The `url` value is a relative path. The `slug` matches the last part of that path.
- For a fuller profile of one Partner, try [Y Combinator Person Detail](/apis/ycombinator/person-detail).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/ycombinator/partners.json`](../../../catalog/models/ycombinator/partners.json) · Store page: https://www.sandbase.ai/model/ycombinator/partners
