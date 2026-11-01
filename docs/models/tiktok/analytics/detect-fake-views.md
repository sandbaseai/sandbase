# Detect fake views in video

`tiktok/analytics/detect-fake-views` · api · TikTok

Check whether a TikTok video has fake views. Paste a video ID and get a fake-view score, the estimated share of inflated views, and a risk level, based on engagement ratios, follower growth, creator credibility and TikTok's traffic-pool tiers. Built for creators, MCN agencies and brands vetting influencers.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/analytics/detect-fake-views", "content_category": "default", "item_id": "7460937381265411370"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/analytics/detect-fake-views', {'content_category': 'default', 'item_id': '7460937381265411370'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/analytics/detect-fake-views", {
  "content_category": "default",
  "item_id": "7460937381265411370"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/analytics/detect-fake-views", sandbase.Params{
	"content_category": "default",
	"item_id": "7460937381265411370",
})
```

Same call via the path form: `POST /v1/api/tiktok/analytics/detect-fake-views` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | TikTok video ID: the number after /video/ in the video URL. For https://www.tiktok.com/@tiktok/video/7460937381265411370 the ID is 7460937381265411370.  |
| `content_category` | string |  | Content category used to pick engagement-rate benchmarks. Use verified_large for verified accounts with very large followings. one of: `default`, `entertainment`, `education`, `product`, `verified_large`; default `"default"` |

## Details

Find out whether a TikTok video's views are real. Give this API a video ID and it returns a **fake-view score**, the **estimated number and percentage of fake views**, a **risk level**, and the specific signals that look suspicious.

### Who it is for

- **Brands and agencies** vetting influencers before signing a sponsorship deal.
- **MCN agencies** monitoring the traffic quality of the creators they manage.
- **Creators** checking whether a sudden spike in views is organic.

### How to use it

1. Copy the TikTok video URL, e.g. `https://www.tiktok.com/@tiktok/video/7460937381265411370`.
2. Take the number after `/video/`. That is the `item_id`: `7460937381265411370`.
3. Optionally set `content_category` (`default`, `entertainment`, `education`, `product`, `verified_large`) so engagement is compared against the right benchmark.
4. Run it in the playground above, or call the API:

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/analytics/detect-fake-views" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7460937381265411370"}'
```

### What the report checks

The score combines eight dimensions and 20+ metrics:

| Dimension | What it looks at |
|---|---|
| Engagement health | Like, comment, share and favorite ratios against category benchmarks |
| Follower correlation | Views compared with what an account of this follower tier usually gets |
| Fan growth | Follower milestones and abnormal daily growth |
| Creator credibility | Account age, verification and trust score |
| Content authenticity | AI-generated or heavily edited content flags |
| Traffic pool | Current vs. expected TikTok traffic-pool tier (level 1 to 8) |
| Distribution and consistency | How views and engagement are spread and whether they move together |
| Statistical anomalies | Outliers that point to bought or bot traffic |

### Example result

Real output for the video above (trimmed):

```json
{
  "fake_view_analysis": {
    "fake_score": 4.34,
    "fake_view_percentage": 5.0,
    "estimated_fake_views": 8102490,
    "is_suspicious": false,
    "confidence_level": "Minimal"
  },
  "traffic_pool": {
    "current_tier_name": "8th-Level Traffic Pool",
    "expected_tier_name": "8th-Level Traffic Pool",
    "current_views_range": "30M+"
  },
  "suspicious_features": [
    "Suspicious: Account gaining 22670 followers per day on average"
  ],
  "recommendations": {
    "risk_level": "low",
    "action": "no_action",
    "suggested_steps": ["No immediate action required", "Include in routine monitoring"]
  }
}
```

### How to read the result

- `fake_view_analysis.fake_score`: overall suspicion score; higher means more likely to be inflated.
- `fake_view_analysis.is_suspicious`: quick yes/no verdict.
- `fake_view_analysis.fake_view_percentage` and `estimated_fake_views`: how much of the view count is likely fake.
- `suspicious_features`: plain-language reasons behind the score.
- `recommendations.risk_level` and `suggested_steps`: what to do next.
- `mcn_report`: business impact summary (brand safety, estimated revenue impact) for agency reports.

The result is a statistical estimate, not a verdict from TikTok. Use it to screen and prioritize, and combine it with your own review for high-stakes decisions.

### Related TikTok analytics APIs

- [Get video metrics](/model/tiktok/analytics/video-metrics): views, likes and engagement trends for a video.
- [Get creator info and milestones](/model/tiktok/analytics/creator-info-and-milestones): follower milestones and creator profile.
- [Get comment keywords analysis](/model/tiktok/analytics/comment-keywords): what viewers are saying in the comments.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/tiktok/analytics/detect-fake-views.json`](../../../../catalog/models/tiktok/analytics/detect-fake-views.json) · Store page: https://www.sandbase.ai/model/tiktok/analytics/detect-fake-views
