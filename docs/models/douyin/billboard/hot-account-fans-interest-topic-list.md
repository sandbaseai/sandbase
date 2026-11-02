# Douyin Account Fan Interest Topics API: pricing, parameters and code examples

`douyin/billboard/hot-account-fans-interest-topic-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the top ten topics that an account's followers were interested in over the last three days based on a specified user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-account-fans-interest-topic-list", "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-account-fans-interest-topic-list', {'sec_uid': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-account-fans-interest-topic-list", {
  "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-account-fans-interest-topic-list", sandbase.Params{
	"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-account-fans-interest-topic-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_uid` | string | yes | User sec_id  |

## Details

Look up recent follower interests by querying top topics for an account using its `sec_uid`.

### Use cases

- Analyze recent content interests among an account's follower base.
- Identify trending topics relevant to a specific Douyin creator.
- Tailor video production themes to match audience engagement patterns.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-fans-interest-topic-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_id |

### Notes

- Requires the target account's `sec_uid` string.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-fans-interest-topic-list.json`](../../../../catalog/models/douyin/billboard/hot-account-fans-interest-topic-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-fans-interest-topic-list
