# Xiaohongshu Pugongying Note Performance Metrics API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/data-v3-notes-rate` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Xiaohongshu Pugongying aggregate note performance metrics for a creator with business, note-type, date-range, and advertisement filters. Use it to compare content performance across selected scopes.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/data-v3-notes-rate", "userId": "5a73c5fa4eacab4c4ccc9778"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/data-v3-notes-rate', {'userId': '5a73c5fa4eacab4c4ccc9778'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/data-v3-notes-rate", {
  "userId": "5a73c5fa4eacab4c4ccc9778"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/data-v3-notes-rate", sandbase.Params{
	"userId": "5a73c5fa4eacab4c4ccc9778",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/data-v3-notes-rate` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |
| `business` | string |  | Business type. one of: `DAILY_NOTE`, `COOPERATE_NOTE`; default `"DAILY_NOTE"` |
| `dateType` | string |  | Time range for data. one of: `DAY_30`, `DAY_90`; default `"DAY_30"` |
| `noteType` | string |  | Type of note. one of: `PHOTO_TEXT_AND_VIDEO`, `PHOTO_TEXT`, `VIDEO`; default `"PHOTO_TEXT_AND_VIDEO"` |
| `advertiseSwitch` | string |  | Advertisement filter. one of: `ALL`, `ORGANIC_ONLY`; default `"ALL"` |

## Details

Returns aggregate note performance metrics for one Xiaohongshu Pugongying creator, such as median reads, impressions and interactions, traffic source shares, and a short list of recent notes. It needs the creator's `userId`. You can narrow the data by business type, note type, date range and advertisement filter.

### Use cases

- Compare a creator's median reads and interactions for organic notes against all notes by switching `advertiseSwitch`.
- Check whether a creator's cooperation notes earn more long-term reads than their daily notes.
- Find which traffic sources, such as home feed, search or follow page, bring the most reads to a creator's notes.
- Screen creators for a campaign by their read and interaction rankings against other creators (the `...BeyondRate` fields).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/data-v3-notes-rate" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5a73c5fa4eacab4c4ccc9778"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |
| `advertiseSwitch` | string | No | Advertisement filter. |
| `business` | string | No | Business type. |
| `dateType` | string | No | Time range for data. |
| `noteType` | string | No | Type of note. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "collectMedian": 20580,
  "commentMedian": 23809,
  "hundredLikePercent": "100.0",
  "impMedian": 7498187,
  "impMedianBeyondRate": "99.4",
  "interactionBeyondRate": "98.9",
  "interactionMedian": 285434,
  "interactionRate": "17.7",
  "likeMedian": 241045,
  "longTermCommonNoteVo": {
    "endPublishTime": "2026-05-07",
    "longTermFindPagePercent": "7.1",
    "longTermFollowPagePercent": "29.8",
    "longTermKolHomePagePercent": "42.4",
    "longTermOtherPagePercent": "9.3",
    "longTermReadBeyondRate": "98.3",
    "longTermReadNum": 450929,
    "longTermSearchPagePercent": "11.3",
    "noteNumber": 14,
    "recentFindPagePercent": "68.9",
    "recentFollowPagePercent": "17.0",
    "recentKolHomePagePercent": "9.4"
  },
  "longTermCooperateNoteVo": {
    "endPublishTime": "2026-05-07",
    "longTermFindPagePercent": "0.6",
    "longTermFollowPagePercent": "40.2",
    "longTermKolHomePagePercent": "39.5",
    "longTermOtherPagePercent": "2.9",
    "longTermReadBeyondRate": "99.0",
    "longTermReadNum": 407086,
    "longTermSearchPagePercent": "16.8",
    "noteNumber": 5,
    "recentFindPagePercent": "34.4",
    "recentFollowPagePercent": "38.3",
    "recentKolHomePagePercent": "21.2"
  },
  "mEngagementNum": 299081
}
```

### Response fields

| Field | Meaning |
|---|---|
| `readMedian / impMedian / interactionMedian` | Median reads, impressions and interactions across the notes in the selected scope. |
| `likeMedian / collectMedian / commentMedian / shareMedian` | Median likes, collects, comments and shares per note. |
| `interactionRate` | Interaction rate as a percentage string, for example `17.7`. |
| `readMedianBeyondRate / impMedianBeyondRate / interactionBeyondRate` | Percentage strings that show how the creator's median compares with other creators. A higher value means a better standing. |
| `hundredLikePercent / thousandLikePercent` | Percentage strings for notes that reach the 100-like and 1000-like levels. |
| `noteNumber / videoNoteNumber` | Count of notes and count of video notes in the selected scope. |
| `noteType[].contentTag / noteType[].percent` | Content tags used by the creator and the share of notes under each tag. |
| `pagePercentVo.readHomefeedPercent / readSearchPercent / readFollowPercent / readDetailPercent / readNearbyPercent` | Share of reads from each source, written as a fraction of 1. The `imp...Percent` fields give the same split for impressions. |
| `longTermCommonNoteVo / longTermCooperateNoteVo` | Recent and long-term read counts, read rankings and page source shares for daily notes and cooperation notes. Each block has `startPublishTime`, `endPublishTime` and `noteNumber`. |
| `notes[].noteId / notes[].title / notes[].publishTime` | ID, title and publish date of each listed note. Use `notes[].readNum`, `impNum`, `likeNum`, `collectNum` and `interactionNum` for its counts. |

### Notes

- Only `userId` is required. The defaults are `business` `DAILY_NOTE`, `noteType` `PHOTO_TEXT_AND_VIDEO`, `dateType` `DAY_30` and `advertiseSwitch` `ALL`.
- Use `dateType` `DAY_90` for a longer window, and `advertiseSwitch` `ORGANIC_ONLY` to leave out advertised notes.
- Fields like `mEngagementNum` and `mengagementNum` appear twice with the same value, as do `mFollowCnt` and `mfollowCnt`.
- Use [Xiaohongshu Pugongying Creator Note List](/apis/xiaohongshu/pgy-v2/data-v2-notes-detail) for the full note list, and [Xiaohongshu Pugongying Note Details](/apis/xiaohongshu/pgy-v2/note-id-detail) to look up a single `noteId`.

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/data-v3-notes-rate.json`](../../../../catalog/models/xiaohongshu/pgy-v2/data-v3-notes-rate.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/data-v3-notes-rate
