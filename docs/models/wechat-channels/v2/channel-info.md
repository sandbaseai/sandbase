# WeChat Channels Account Info API: pricing, parameters and code examples

`wechat-channels/v2/channel-info` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service category and license numbers.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/channel-info", "raw": false, "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/channel-info', {'raw': False, 'username': 'v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/channel-info", {
  "raw": false,
  "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/channel-info", sandbase.Params{
	"raw": false,
	"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/channel-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure.  |
| `username` | string | yes | WeChat Channels finder username (`v2_…@finder` format), e.g. `v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder` (People's Daily).  |

## Details

Returns the public "More info" panel of a WeChat Channels account: its Channel ID, IP and profile location, and verification details such as entity type, service unit and license number. It needs the account's finder username in `v2_…@finder` format.

### Use cases

- Check which organization and entity type stand behind a Channels account before a media partnership.
- Read the news service license number of an official media account for compliance records.
- Store the Channel ID and location of accounts in an internal creator directory.
- Map a finder username back to its public Channel ID to match records from other sources.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/channel-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder", "raw": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | WeChat Channels finder username (`v2_…@finder` format), e.g. `v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder` (People's Daily). |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified parsed structure. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel_id": null,
  "debug_id": "d5953921",
  "debug_info": "gAAAAABq6ZEgJFp75BVW0Qp9McV-keALwAbI5bKK1MWYdkOpd00m_UoF9XVOKT9eh3GsseHxU_WVPl2q…",
  "finder_username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@…",
  "info": {
    "Channels ID": "sphi9BjV8GK0Zsl",
    "IP归属地": "Beijing",
    "主体类型": "互联网新闻信息服务单位",
    "互联网新闻信息服务许可证编号": "10120180018",
    "服务单位": "人民日报社",
    "服务类别": "互联网新闻信息采编发布服务、传播平台服务、采编发布服务、传播平台服务、采编发布服务、传播平台服务",
    "认证时间": "Completed WeChat Verification on 2022年1月26日. Tencent and a third-party verificat…",
    "资料所在地": "Beijing"
  },
  "sections": [
    {
      "items": [
        {
          "content": "Beijing",
          "title": "IP归属地"
        }
      ],
      "title": "基础信息"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `finder_username` | The finder username you sent in the request. |
| `sections[].title` | The name of a panel group, such as `基础信息` (basic info) or `认证信息` (verification info). |
| `sections[].items[].title / sections[].items[].content` | The label and value of each row in a group. Rows include the Channel ID (a short ID that starts with `sph`), the IP location, the profile location, the service unit, the entity type and the license number. |
| `info.主体类型` | The entity type of the verified account. Here it is an internet news information service unit. |
| `info.服务单位` | The name of the organization that runs the account. |
| `info.互联网新闻信息服务许可证编号` | The internet news information service license number. |
| `info.服务类别` | The verified service categories, as one text string. Entries can repeat. |
| `info.认证时间` | Text that gives the date the account completed WeChat verification. |
| `info.资料所在地` | The profile location shown on the panel. It is `Beijing` in this example. |
| `channel_id` | A top-level Channel ID field. It is `null` in this response. |

### Notes

- The top-level `channel_id` was `null` in this response. Read the Channel ID from the `sections` row whose `title` is `Channels ID`, or from the matching key in `info`.
- The `info` object uses the panel labels as keys, so most keys are in Chinese and one is in English. Accounts with fewer verification details may return fewer keys.
- If you only have a Channel ID, call [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username) first to get the `v2_…@finder` username.
- To list the account's videos next, use [WeChat Channels User Videos](/apis/wechat-channels/v2/user-videos).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels User Videos](/apis/wechat-channels/v2/user-videos): Get the videos on a WeChat Channels account's homepage with descriptions, publish time, like, comment, share and favorite counts, and media download info, with…
- [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail): Get the full detail of a WeChat Channels video: description, author, engagement counts and the media URL with decode key for download.

---
Machine-readable: [`catalog/models/wechat-channels/v2/channel-info.json`](../../../../catalog/models/wechat-channels/v2/channel-info.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/channel-info
