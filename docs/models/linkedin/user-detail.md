# LinkedIn User Profile API: pricing, parameters and code examples

`linkedin/user-detail` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get a LinkedIn profile by username, including documented core profile fields such as name and headline. Use it to inspect a person's professional background or before requesting published posts.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/user-detail", "username": "williamhgates"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/user-detail', {'username': 'williamhgates'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/user-detail", {
  "username": "williamhgates"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/user-detail", sandbase.Params{
	"username": "williamhgates",
})
```

Same call via the path form: `POST /v1/api/linkedin/user-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | LinkedIn username from the profile URL, for example jack from linkedin.com/in/jack.  |

## Details

Get a LinkedIn profile by username, including documented core profile fields such as name and headline. Use it to inspect a person's professional background or before requesting published posts.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/user-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "williamhgates"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | LinkedIn username from the profile URL, for example jack from linkedin.com/in/jack. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/linkedin/user-detail.json`](../../../catalog/models/linkedin/user-detail.json) · Store page: https://www.sandbase.ai/model/linkedin/user-detail
