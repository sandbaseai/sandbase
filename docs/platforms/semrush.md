# Semrush API: 19 endpoints with pricing and code examples

Call 19 Semrush endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`semrush/backlink-anchors`](../models/semrush/backlink-anchors.md) | Anchor texts used in backlinks to a domain or URL, with backlink counts per anchor. | about $0.08 per call |
| [`semrush/backlink-competitors`](../models/semrush/backlink-competitors.md) | Domains with a backlink profile similar to the target, ranked by similarity. | about $0.08 per call |
| [`semrush/backlinks`](../models/semrush/backlinks.md) | Backlinks pointing to a domain or URL, with source URL, target URL and anchor text. | about $0.08 per call |
| [`semrush/backlinks-overview`](../models/semrush/backlinks-overview.md) | Backlink summary for a domain or URL: Authority Score, total backlinks, referring domains, URLs and IPs. | $0.004 per call (free daily quota) |
| [`semrush/broad-match-keywords`](../models/semrush/broad-match-keywords.md) | Broad-match keyword ideas for a seed phrase with search volume, CPC and competition, from a regional database. | about $0.04 per call |
| [`semrush/domain-organic-competitors`](../models/semrush/domain-organic-competitors.md) | Domains competing with the target in Google organic results, with relevance and common keywords. | about $0.08 per call |
| [`semrush/domain-organic-keywords`](../models/semrush/domain-organic-keywords.md) | Keywords a domain ranks for in Google organic search, with position, search volume, CPC and URL. | about $0.02 per call |
| [`semrush/domain-overview`](../models/semrush/domain-overview.md) | Semrush rank, organic keywords, organic traffic, traffic cost and paid keywords for a domain. | $0.001 per call (free daily quota) |
| [`semrush/domain-paid-keywords`](../models/semrush/domain-paid-keywords.md) | Keywords a domain bids on in Google Ads, with ad position, search volume, CPC and landing URL. | about $0.04 per call |
| [`semrush/domain-rank-history`](../models/semrush/domain-rank-history.md) | Monthly history of a domain's Semrush rank, organic keywords, organic traffic and traffic cost. | about $0.02 per call |
| [`semrush/domain-vs-domain`](../models/semrush/domain-vs-domain.md) | Keyword gap between domains: shared and unique keywords with each domain's ranking position. | about $0.16 per call |
| [`semrush/indexed-pages`](../models/semrush/indexed-pages.md) | Pages of a domain that receive backlinks, with the backlink count of each page. | about $0.08 per call |
| [`semrush/keyword-difficulty`](../models/semrush/keyword-difficulty.md) | Keyword difficulty score (0-100) for a phrase in a regional Semrush database. | about $0.005 per call |
| [`semrush/keyword-organic-results`](../models/semrush/keyword-organic-results.md) | Domains and URLs ranking in Google organic results for a keyword, by position. | about $0.02 per call |
| [`semrush/keyword-overview`](../models/semrush/keyword-overview.md) | Search volume, CPC, competition and number of results for a keyword in a regional database. | $0.001 per call (free daily quota) |
| [`semrush/keyword-paid-results`](../models/semrush/keyword-paid-results.md) | Advertisers bidding on a keyword in Google Ads, with ad position and landing URL. | about $0.04 per call |
| [`semrush/question-keywords`](../models/semrush/question-keywords.md) | Question-form keyword ideas for a seed phrase, with search volume, CPC and competition. | about $0.08 per call |
| [`semrush/referring-domains`](../models/semrush/referring-domains.md) | Domains linking to the target, with the number of backlinks from each domain. | about $0.08 per call |
| [`semrush/url-organic-keywords`](../models/semrush/url-organic-keywords.md) | Keywords a single URL ranks for in Google organic search, with position, search volume and CPC. | about $0.02 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/backlink-anchors", "target": "nike.com", "target_type": "root_domain"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
