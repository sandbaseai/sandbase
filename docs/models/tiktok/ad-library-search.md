# TikTok Ad Library Search

`tiktok/ad-library-search` · api · TikTok

Search TikTok's public Ads Library by keyword or advertiser (advertiser, title, audience band, run dates, library link, and video).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ad-library-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ad-library-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ad-library-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ad-library-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/ad-library-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string |  | Keyword to search ad titles and content (e.g. spotify). Provide query or advertiserName, never both.  |
| `cursor` | string |  | Opaque cursor from a previous response's nextCursor. Omit it for the first page.  |
| `region` | string |  | Two-letter region code for TikTok's Commercial Content Library, such as DE, FR, GB or IT. Each region holds a different set of ads. Omit it to take the library's own default region, DE. Coverage is the EU and EEA; a…  |
| `advertiserName` | string |  | Advertiser name to list ads for (e.g. Spotify). Provide advertiserName or query, never both.  |

## Details

Search TikTok's public Ads Library by keyword or advertiser (advertiser, title, audience band, run dates, library link, and video).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ad-library-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "spotify"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `advertiserName` | string | No | Advertiser name to list ads for (e.g. Spotify). Provide advertiserName or query, never both. |
| `cursor` | string | No | Opaque cursor from a previous response's nextCursor. Omit it for the first page. |
| `query` | string | No | Keyword to search ad titles and content (e.g. spotify). Provide query or advertiserName, never both. |
| `region` | string | No | Two-letter region code for TikTok's Commercial Content Library, such as DE, FR, GB or IT. Each region holds a different set of ads. Omit it to take the library's own default region, DE. Coverage is the EU and EEA; a non- |

### Pricing

Billed at the actual cost of each call, usually $0.0008 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/ad-library-search.json`](../../../catalog/models/tiktok/ad-library-search.json) · Store page: https://www.sandbase.ai/model/tiktok/ad-library-search
