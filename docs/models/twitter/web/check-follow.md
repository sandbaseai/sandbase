# Twitter Check follow API: pricing, parameters and code examples

`twitter/web/check-follow` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Check follow on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/check-follow", "user_name": "elonmusk", "follows": "NASA"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/check-follow', {'user_name': 'elonmusk', 'follows': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/check-follow", {
  "user_name": "elonmusk",
  "follows": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/check-follow", sandbase.Params{
	"user_name": "elonmusk",
	"follows": "NASA",
})
```

Same call via the path form: `POST /v1/api/twitter/web/check-follow` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `follows` | string | yes | Target Screen Name  |
| `user_name` | string | yes | Source Screen Name  |

## Details

Checks whether one Twitter account follows another. It needs two screen names: `user_name` (the source account) and `follows` (the target account). It returns a boolean and the source username.

### Use cases

- Verify that a customer or partner account follows your brand account before granting a reward.
- Check follow status between two accounts when you audit a giveaway or campaign.
- Confirm a relationship between two known accounts without paging through a full follower list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/check-follow" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_name": "elonmusk", "follows": "NASA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `follows` | string | Yes | Target Screen Name |
| `user_name` | string | Yes | Source Screen Name |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "is_follow": false,
  "username": "elonmusk"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `is_follow` | Boolean. `true` if the `user_name` account follows the `follows` account, `false` if it does not. The sample call for `elonmusk` and `NASA` returned `false`. |
| `username` | The source screen name the check was run for. It matches the `user_name` you sent. |

### Notes

- Pass screen names without the `@` sign, for example `elonmusk` and `NASA`.
- The check runs in one direction only. To test the reverse, swap the values of `user_name` and `follows`.
- To see the full list of accounts instead of one pair, use [Twitter (X) User Followings](/apis/twitter/web/user-followings) or [Twitter (X) User Followers](/apis/twitter/web/user-followers).
- To check a retweet instead of a follow, use [Twitter Check retweet](/apis/twitter/web/check-retweet).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/web/check-follow.json`](../../../../catalog/models/twitter/web/check-follow.json) · Store page: https://www.sandbase.ai/model/twitter/web/check-follow
