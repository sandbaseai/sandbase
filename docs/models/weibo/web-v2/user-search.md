# Weibo User Search API: pricing, parameters and code examples

`weibo/web-v2/user-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Weibo users using keywords or profile attributes such as company, school, tags, gender, age range, and verification type.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-search"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `age` |  |  | Age bucket 18y/22y/29y/39y/40y (optional)  |
| `tag` |  |  | Tag filter (optional)  |
| `auth` |  |  | Auth type org_vip/per_vip/ord (optional)  |
| `page` | integer |  | Page number (default 1) default `1` |
| `work` |  |  | Company filter (optional)  |
| `query` |  |  | Search keyword (optional)  |
| `gender` |  |  | Gender man/women (optional)  |
| `region` |  |  | Region code from /fetch_city_list (optional)  |
| `school` |  |  | School filter (optional)  |
| `nickname` |  |  | Nickname filter (optional)  |

## Details

Returns Weibo users that match a keyword or profile filters such as company, school, tag, gender, age bucket, region, and verification type. You must send at least one of `query`, `region`, `auth`, `gender`, `age`, `nickname`, `tag`, `school`, or `work`.

### Use cases

- Find verified organization accounts by sending `auth` as `org_vip` together with a `tag` or `query`.
- Look for people who list a given company by sending `work`.
- Look for people from a given school by sending `school`.
- Build a list of users in one age bucket and gender by sending `age` and `gender`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `age` | string | No | Age bucket 18y/22y/29y/39y/40y (optional) |
| `auth` | string | No | Auth type org_vip/per_vip/ord (optional) |
| `gender` | string | No | Gender man/women (optional) |
| `nickname` | string | No | Nickname filter (optional) |
| `page` | integer | No | Page number (default 1) |
| `query` | string | No | Search keyword (optional) |
| `region` | string | No | Region code from /fetch_city_list (optional) |
| `school` | string | No | School filter (optional) |
| `tag` | string | No | Tag filter (optional) |
| `work` | string | No | Company filter (optional) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "message": "Invalid query. Pass at least one of: query, region, auth, gender, age, nickname,…",
  "message_zh": "query 非法。请至少传入以下一项：query, region, auth, gender, age, nickname, tag, school, work…",
  "ok": 0,
  "param": "query"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `ok` | Status flag. `0` means the request failed, as in the response to an empty request. |
| `message` | English error text. It says the query is invalid and lists the parameters you can send; at least one is required. |
| `message_zh` | The same error text in Chinese. |
| `param` | Name of the parameter the error refers to. An empty request returns `query`, even though any one of the listed filters is enough. |

### Notes

- An empty request body returns `ok` as `0` with the error message. Send at least one search or filter parameter.
- Use `page` to move through results. It starts at `1`.
- Get a `region` code from [Weibo Region City List](/apis/weibo/web-v2/city-list).
- To see more about a user you found, call [Weibo User Profile Details (Web V2)](/apis/weibo/web-v2/user-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-search.json`](../../../../catalog/models/weibo/web-v2/user-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-search
