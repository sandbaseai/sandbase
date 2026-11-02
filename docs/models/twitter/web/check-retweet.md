# Twitter Check retweet API: pricing, parameters and code examples

`twitter/web/check-retweet` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Check retweet on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/check-retweet", "screen_name": "elonmusk", "tweet_id": "1808168603721650364"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/check-retweet', {'screen_name': 'elonmusk', 'tweet_id': '1808168603721650364'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/check-retweet", {
  "screen_name": "elonmusk",
  "tweet_id": "1808168603721650364"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/check-retweet", sandbase.Params{
	"screen_name": "elonmusk",
	"tweet_id": "1808168603721650364",
})
```

Same call via the path form: `POST /v1/api/twitter/web/check-retweet` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tweet_id` | string | yes | Tweet ID  |
| `screen_name` | string | yes | Screen Name  |

## Details

Check retweet on Twitter. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/check-retweet" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "elonmusk", "tweet_id": "1808168603721650364"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `screen_name` | string | Yes | Screen Name |
| `tweet_id` | string | Yes | Tweet ID |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/twitter/web/check-retweet.json`](../../../../catalog/models/twitter/web/check-retweet.json) · Store page: https://www.sandbase.ai/model/twitter/web/check-retweet
