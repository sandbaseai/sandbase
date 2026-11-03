# WeChat Channels User Collections API: pricing, parameters and code examples

`wechat-channels/v2/user-collections` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns the video collections displayed on a creator homepage by username. Includes collection metadata and identifiers used to look up collection videos.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/user-collections", "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/user-collections', {'username': 'v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/user-collections", {
  "username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/user-collections", sandbase.Params{
	"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/user-collections` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure.  |
| `username` | string | yes | WeChat Channels finder username (`v2_…@finder` format). E.g. `v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder` (People's Daily).  |

## Details

Returns the video collections shown on a WeChat Channels creator homepage. It needs the creator's finder `username` (format `v2_…@finder`). Each collection includes its name, cover image, video count and identifiers.

### Use cases

- List every collection a creator has published, with the video count of each.
- Collect `categoryId` and `collectionTopicId` values to look up the videos inside a collection.
- Sort a creator's collections by `lastUpdateTime` to see which series were updated most recently.
- Compare how different creator accounts organize their content into series.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/user-collections" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | WeChat Channels finder username (`v2_…@finder` format). E.g. `v2_060000231003b20faec8c6e4811dc1d4c602ee30b0771bbcf220c67926bb76ab7702ac335a53@finder` (People's Daily). |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified parsed structure. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "collectionCount": 7,
  "collectionInfo": [
    {
      "businessType": 0,
      "categoryId": "nfccid-14566193340220246217",
      "collectionBuffer": "",
      "collectionDesc": "",
      "collectionEnterType": 0,
      "collectionName": "习语",
      "collectionTopicBuffer": "",
      "collectionTopicId": 14566193340220246217,
      "collectionTopicIdStr": "",
      "collectionTopicType": 16,
      "collectionType": 1,
      "collectionTypeWording": ""
    }
  ],
  "debug_id": "7363a780",
  "debug_info": "gAAAAABq6ZEnBTcr8zbeDChUPRfoCE30pdi5gcf_eRfqmHzDu1qERb_xwThPiduf6y8tpuW9k5mhUM2T…",
  "lastBuffer": "",
  "pbRequestMsgInfo": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `collectionCount` | Total number of collections on the creator homepage. |
| `collectionInfo[]` | One entry per collection. The response may list only some of the collections counted in `collectionCount`. |
| `collectionInfo[].collectionName` | Display name of the collection. |
| `collectionInfo[].categoryId` | Collection identifier as a string, in the form `nfccid-<digits>`. |
| `collectionInfo[].collectionTopicId` | Numeric topic identifier of the collection. It matches the digits in `categoryId`. |
| `collectionInfo[].feedCount` | Number of videos in the collection. |
| `collectionInfo[].lastUpdateTime` | Time the collection was last updated, as a 10-digit Unix timestamp. |
| `collectionInfo[].coverImgUrl` | URL of the collection cover image. |
| `collectionInfo[].collectionDesc` | Collection description text. It is an empty string for the collections shown here. |
| `lastBuffer` | Cursor-style string at the end of the response. It is empty in this response. |

### Notes

- Get the `username` from a creator's Channel ID with [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username).
- Pass a collection's `categoryId` to [WeChat Channels Collection Videos](/apis/wechat-channels/v2/collection-videos) to list its videos.
- Set `raw` to `false` to get a simplified parsed structure instead of the raw response shown here.
- The response also contains `debug_id` and `debug_info`, which describe the request and not the creator.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Collection Videos](/apis/wechat-channels/v2/collection-videos): Returns videos contained within a WeChat Channels collection using a collection ID.

---
Machine-readable: [`catalog/models/wechat-channels/v2/user-collections.json`](../../../../catalog/models/wechat-channels/v2/user-collections.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/user-collections
