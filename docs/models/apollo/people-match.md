# Apollo People Enrichment API: pricing, parameters and code examples

`apollo/people-match` · data API · Apollo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01975 per call · **Modes:** sync

Enrich one person: give whatever identifiers you have and get back Apollo's full record for them. Send identifiers in the JSON request body, not the query string.

## Pricing

- **$0.01975 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/people-match"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/people-match', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/people-match", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/people-match", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/apollo/people-match` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | The Apollo ID for the person. Each person in the Apollo database is assigned a unique ID. To find IDs, call the People API Search endpoint and identify the values for person_id. Example: 587cf802f65125cad923a266  |
| `name` | string |  | The full name of the person. This will typically be a first name and last name separated by a space. If you use this parameter, you do not need to use the first_name and last_name parameters. Example: tim zheng  |
| `email` | string |  | The email address of the person. Example: example@email.com  |
| `domain` | string |  | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. Example: apollo.io or microsoft.com  |
| `last_name` | string |  | The last name of the person. This is typically used in combination with the first_name parameter. Example: zheng  |
| `first_name` | string |  | The first name of the person. This is typically used in combination with the last_name parameter. Example: tim  |
| `hashed_email` | string |  | The hashed email of the person. The email should adhere to either the MD5 or SHA-256 hash format. Example: 8d935115b9ff4489f2d1f9249503cadf (MD5) or 97817c0c49994eb500ad0a5e7e2d8aed51977b26424d508f66e4e8887746a152…  |
| `linkedin_url` | string |  | The URL for the person's LinkedIn profile. Example: http://www.linkedin.com/in/tim-zheng-677ba010  |
| `organization_name` | string |  | The name of the person's employer. This can be the current employer or a previous employer. Example: apollo  |

## Details

Enrich one person: give whatever identifiers you have and get back Apollo's full record for them. Send identifiers in the JSON request body, not the query string.

The response is the official Apollo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/people-match" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Patrick", "last_name": "Collison", "domain": "stripe.com"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | No | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. Example: apol |
| `email` | string | No | The email address of the person. Example: example@email.com |
| `first_name` | string | No | The first name of the person. This is typically used in combination with the last_name parameter. Example: tim |
| `hashed_email` | string | No | The hashed email of the person. The email should adhere to either the MD5 or SHA-256 hash format. Example: 8d935115b9ff4489f2d1f9249503cadf (MD5) or 97817c0c499 |
| `id` | string | No | The Apollo ID for the person. Each person in the Apollo database is assigned a unique ID. To find IDs, call the People API Search endpoint and identify the valu |
| `last_name` | string | No | The last name of the person. This is typically used in combination with the first_name parameter. Example: zheng |
| `linkedin_url` | string | No | The URL for the person's LinkedIn profile. Example: http://www.linkedin.com/in/tim-zheng-677ba010 |
| `name` | string | No | The full name of the person. This will typically be a first name and last name separated by a space. If you use this parameter, you do not need to use the first |
| `organization_name` | string | No | The name of the person's employer. This can be the current employer or a previous employer. Example: apollo |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/people-match.json`](../../../catalog/models/apollo/people-match.json) · Store page: https://www.sandbase.ai/model/apollo/people-match
