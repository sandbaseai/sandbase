# WeChat MP Account Basic Info API: pricing, parameters and code examples

`wechat-mp/account-basic-info` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.142857 per call · **Modes:** sync

Get basic profile information for a WeChat Official Account by account name. Use it to identify or enrich a known account before article, ownership, or publishing research.

## Pricing

- **$0.142857 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/account-basic-info", "name": "人民日报"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/account-basic-info', {'name': '人民日报'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/account-basic-info", {
  "name": "人民日报"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/account-basic-info", sandbase.Params{
	"name": "人民日报",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/account-basic-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `name` | string | yes | WeChat Official Account name used to fetch basic profile information.  |

## Details

Returns the basic public profile of a WeChat Official Account: its name, description, avatar, account type, WeChat ID and `biz` identifier. It needs one input, the account name in `name`.

### Use cases

- Confirm that an Official Account name maps to a real account and read its `wxid` before further research.
- Collect the `biz` value of an account so you can match it against article links.
- Fill in an account list with the avatar, description and account type for each name.
- Check whether an account is a subscription account or another type before you plan article collection.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/account-basic-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "人民日报"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | WeChat Official Account name used to fetch basic profile information. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatar": "http://mmbiz.qpic.cn/mmbiz_png/xrFYciaHL08D1hiaVU0brP9YwQH1wFm9D9AG7oAVaNE8RzGia…",
    "biz": "MjM5MjAxNDM4MA==",
    "desc": "参与、沟通、记录时代。",
    "name": "人民日报",
    "type": "订阅号",
    "wxid": "rmrbwx"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name` | The display name of the Official Account. |
| `data.wxid` | The WeChat ID of the account, for example `rmrbwx`. |
| `data.biz` | The `biz` identifier of the account. The value looks like a Base64 string, for example `MjM5MjAxNDM4MA==`. |
| `data.desc` | The account's profile description, as the account owner wrote it. |
| `data.type` | The account type as a text label. The sample value `订阅号` means subscription account. |
| `data.avatar` | URL of the account's avatar image. |

### Notes

- Pass the exact account name in `name`. The sample request uses `人民日报`.
- Keep `biz` and `wxid` from the response to identify the account in later calls.
- To read the account's posts next, try [WeChat MP Account Articles](/apis/wechat-mp/v2/account-articles) or [WeChat MP Account Historical Articles](/apis/wechat-mp/account-history-articles).
- For a fuller account record, see [WeChat MP Account Profile](/apis/wechat-mp/v2/account-profile).

### Pricing

$0.142857 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/account-basic-info.json`](../../../catalog/models/wechat-mp/account-basic-info.json) · Store page: https://www.sandbase.ai/model/wechat-mp/account-basic-info
