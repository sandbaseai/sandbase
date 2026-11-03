# DataForSEO Google Business Questions and Answers API: pricing, parameters and code examples

`dataforseo/v3/business_data/google/questions_and_answers/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0054 per call · **Modes:** sync

Questions and answers posted on a Google Business Profile, found by business name or place id.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0054**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/business_data/google/questions_and_answers/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/business_data/google/questions_and_answers/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/business_data/google/questions_and_answers/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/business_data/google/questions_and_answers/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/business_data/google/questions_and_answers/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Business name, or "cid:<id>" / "place_id:<id>".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns the questions and answers posted on a Google Business Profile. Send a business name, or a `cid:<id>` or `place_id:<id>` value, as `keyword`, together with a `location_code` and a `language_code`.

### Use cases

- Pull the questions visitors ask about a landmark or store to find gaps in its listing information.
- Track which questions have no answer yet so a business can reply to them.
- Collect answer text from many locations to compare what customers ask across branches.
- Read who answered each question to separate owner replies from visitor replies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/business_data/google/questions_and_answers/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "Empire State Building", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Business name, or "cid:<id>" / "place_id:<id>". |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "business_data",
        "device": "desktop",
        "function": "questions_and_answers",
        "keyword": "Empire State Building",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "google"
      },
      "id": "11030828-2190-0578-0000-e1057ac5c994",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.google.com/maps/place/data=!4m3!3m2!1s0x0:0xd134e199a405a163!10e4?hl…",
          "cid": "15074921902713971043",
          "datetime": "2026-11-03 08:29:06 +00:00",
          "feature_id": "0x0:0xd134e199a405a163",
          "item_types": [
            "google_business_question_item"
          ],
          "items": [
            {
              "items": [
                {
                  "answer_id": "8@1:CAESGUNWX0J6VVpFX0lOOTBSaW9PRFNBQWZ1eGc|",
                  "answer_text": "Yes",
                  "original_answer_text": null,
                  "profile_image_url": "https://lh3.googleusercontent.com/a-/ALV-UjVUYetmCHBLqyjcXerRKBZ6Jmx95DLJ7V0AM-g…",
                  "profile_name": "Marcelo Quinde",
                  "profile_url": "https://www.google.com/maps/contrib/113388248075047475338?hl=en-GB",
                  "time_ago": "9 years ago",
                  "timestamp": "2017-11-03 08:29:05 +00:00"
                }
              ],
              "original_question_text": null,
              "profile_image_url": "https://lh3.googleusercontent.com/a-/ALV-UjUXmLeUaeJFEuosq8vyRvyvIP6OUE0Kp7C2gYf…",
              "profile_name": "Federico Picapietra",
              "profile_url": "https://www.google.com/maps/contrib/103767993357197415632?hl=en-GB",
              "question_id": "8@1:CAESGUNWX0FBVkJVVFFPTnhWaW4tOVRBQVZEa3c|",
              "question_text": "Ir os open  from 8 pm till 2 am?",
              "rank_absolute": 1
            }
          ],
          "items_count": 20,
          "items_without_answers": [
            {
              "items": null,
              "original_question_text": null,
              "profile_image_url": "https://lh3.googleusercontent.com/a-/ALV-UjXn_uHGmorOWySo9DPkswMH4pyisT4_FXWQZt5…",
              "profile_name": "Pastel Milk",
              "profile_url": "https://www.google.com/maps/contrib/102252461306156041986?hl=en-GB",
              "question_id": "8@1:CAESGUNWX0NtUFJSVkVNYU9WaXBJMnFBQWVYWmc|",
              "question_text": "How long did it take? 24 hours or more I’m pretty sure 😂",
              "rank_absolute": 0
            }
          ]
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "18.2704 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "18.2843 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].cid / feature_id` | Identifiers of the matched Google business. `cid` is a numeric string and `feature_id` is a hex pair. |
| `tasks[].result[].items_count` | Number of question items reported for the business. |
| `tasks[].result[].items[].question_text` | Text of a question that has at least one answer. `original_question_text` holds the source-language text when the question was translated, and is `null` otherwise. |
| `tasks[].result[].items[].question_id` | Identifier of the question. |
| `tasks[].result[].items[].profile_name / profile_url` | Name and Google Maps profile link of the person who asked the question. |
| `tasks[].result[].items[].items[].answer_text` | Text of one answer to the question. |
| `tasks[].result[].items[].items[].profile_name / profile_url` | Name and profile link of the person who answered. `profile_url` is `null` for the business owner reply. |
| `tasks[].result[].items[].items[].timestamp / time_ago` | Time of the answer as a UTC timestamp, and the same time in relative words such as `a year ago`. |
| `tasks[].result[].items_without_answers[].question_text` | Text of a question that has no answers yet. The `items` field for these questions is `null`. |
| `tasks[].result[].check_url` | Google Maps URL for the business, which you can open to check the result. |

### Notes

- For an exact match, pass `place_id:<id>` or `cid:<id>` as `keyword` instead of the business name.
- Questions with answers are in `items[]`, and questions without answers are in `items_without_answers[]`.
- Timestamps use the format `YYYY-MM-DD HH:MM:SS +00:00`.
- Results sit in `tasks[].result`, and `tasks[].id` is the task ID.

### Pricing

Billed at the actual cost of each call, about $0.0054 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/business_data/google/questions_and_answers/live.json`](../../../../../../../catalog/models/dataforseo/v3/business_data/google/questions_and_answers/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/business_data/google/questions_and_answers/live
