# LinkedIn Group API: pricing, parameters and code examples

`linkedin/group` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0013 per call · **Modes:** sync

Fetch one LinkedIn group by URL or id: name, description, rules, member count, logo and cover image, creation date, visibility and join settings, and its admins.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0013**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/group"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/group', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/group", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/group", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/linkedin/group` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | LinkedIn group URL (e.g. https://www.linkedin.com/groups/1898033). Send this or groupId.  |
| `groupId` | string |  | Numeric LinkedIn group id (e.g. 1898033), the number in the group URL. Send this or url.  |

## Details

Fetch one LinkedIn group by URL or id: name, description, rules, member count, logo and cover image, creation date, visibility and join settings, and its admins.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/group" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/groups/1898033"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `groupId` | string | No | Numeric LinkedIn group id (e.g. 1898033), the number in the group URL. Send this or url. |
| `url` | string | No | LinkedIn group URL (e.g. https://www.linkedin.com/groups/1898033). Send this or groupId. |

### Pricing

Billed at the actual cost of each call, usually $0.0013 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/group.json`](../../../catalog/models/linkedin/group.json) · Store page: https://www.sandbase.ai/model/linkedin/group
