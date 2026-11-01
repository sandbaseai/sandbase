# Google Play Movies

`google-play/movies` · api · Google Play

Search or browse movies, TV shows, episodes, categories, and charts on Google Play.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-play/movies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-play/movies', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-play/movies", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-play/movies", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/google-play/movies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Search query, 1-2,048 bytes. Excludes category and chart; omit it to browse the storefront.  |
| `gl` | string |  | Two-letter country code. Default 'us'.  |
| `hl` | string |  | Storefront language, such as 'en', 'de', or 'zh-TW'. Default 'en'.  |
| `age` | string |  | Children's age range. Requires movies_category 'FAMILY'. one of: `AGE_RANGE1`, `AGE_RANGE2`, `AGE_RANGE3` |
| `chart` | string |  | Chart identifier such as 'topselling_free', 'topselling_paid', or 'topgrossing'. Excludes q and the pagination tokens.  |
| `see_more_token` | string |  | Open a result collection with its returned token and the same parameters.  |
| `movies_category` | string |  | Native category identifier, such as 'FAMILY'. Excludes q.  |
| `next_page_token` | string |  | Continue the listing with the returned next_page_token and the same parameters.  |
| `section_page_token` | string |  | Continue one result group with its returned token and the same parameters.  |

## Details

Search or browse movies, TV shows, episodes, categories, and charts on Google Play.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-play/movies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `age` | string | No | Children's age range. Requires movies_category 'FAMILY'. One of: `AGE_RANGE1`, `AGE_RANGE2`, `AGE_RANGE3`. |
| `chart` | string | No | Chart identifier such as 'topselling_free', 'topselling_paid', or 'topgrossing'. Excludes q and the pagination tokens. |
| `gl` | string | No | Two-letter country code. Default 'us'. |
| `hl` | string | No | Storefront language, such as 'en', 'de', or 'zh-TW'. Default 'en'. |
| `movies_category` | string | No | Native category identifier, such as 'FAMILY'. Excludes q. |
| `next_page_token` | string | No | Continue the listing with the returned next_page_token and the same parameters. |
| `q` | string | No | Search query, 1-2,048 bytes. Excludes category and chart; omit it to browse the storefront. |
| `section_page_token` | string | No | Continue one result group with its returned token and the same parameters. |
| `see_more_token` | string | No | Open a result collection with its returned token and the same parameters. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-play/movies.json`](../../../catalog/models/google-play/movies.json) · Store page: https://www.sandbase.ai/model/google-play/movies
