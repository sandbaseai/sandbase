<h1 align="center">SandBase</h1>

<p align="center"><b>AI models, data APIs, sandboxes and agents. One key. Pay as you go.</b></p>

<p align="center">
<!-- counts:en -->**2,000+ models and APIs** · 400+ AI models · 1,700+ data APIs from 100+ platforms<br>**100 free API calls every day** · **Sandboxes free** · **Agents free**<!-- /counts:en -->
</p>

<p align="center">HTTP · curl · Python · TypeScript · Go · OpenAPI 3.1 · OpenAI SDK · E2B SDK</p>

<p align="center">
<a href="https://www.sandbase.ai/console">Get a key</a> ·
<a href="docs/INDEX.md">Models &amp; APIs</a> ·
<a href="docs/SKILLS.md">Skills</a> ·
<a href="catalog/index.json">catalog.json</a> ·
<a href="openapi/sandbase.openapi.json">OpenAPI</a> ·
<a href="README.zh-CN.md">中文</a>
</p>

---

Most platforms cover one layer: an LLM gateway, a media API, a sandbox, or a tool catalog. SandBase gives you all four layers behind **one key, one balance and one bill**, and they work together. An Agent you define here can call any model or data API in the catalog and runs its code in a SandBase sandbox.

| Layer | What you get | Price | How you call it |
|---|---|---|---|
| **Models** | LLM, image, video, audio, embedding | Per call or per token, listed in the catalog | OpenAI / Anthropic / Gemini SDKs, or `POST /v1/run` |
| **APIs** | Search, scraping, social, e-commerce, SEO, finance and other data APIs | **100 free calls a day**, then per call | `POST /v1/run` or `POST /v1/api/<name>` |
| **Sandboxes** | Isolated machines for commands, files and code | **Free** | The official **E2B SDK**: change the URL and the key, keep your code |
| **Agents** | Versioned Agents, Sessions, HTTP Services, Schedules, Skills, MCP | **Free**; the models and APIs an Agent calls are billed as usual | The official **OpenAI SDK** (`client.beta.agents`), or the clients here |

## What's inside

<!-- inside:en -->
| | Count | Includes |
|---|---|---|
| **AI models** | 400+ | 100+ LLMs, 150+ video, 100+ image, 30+ audio: Alibaba, Google, OpenAI, KwaiVGI, Bytedance, MiniMax, BFL, xAI, … |
| Social & content | 1,100+ | Douyin, TikTok, Instagram, Weibo, Xiaohongshu, YouTube, Zhihu, Bilibili, Kuaishou, LinkedIn, … |
| Search, SEO & web data | 200+ | DataForSEO, Similarweb, Brave, Google, Firecrawl, Artificial Analysis, Exa, Scholar, Tavily, Ahrefs, … |
| E-commerce, apps & reviews | 100+ | 1688, GetApp, TikTok Shop, Amazon, Clutch, Trustpilot, G2, JD.com, Taobao, Zillow, … |
| Finance, crypto & markets | 150+ | Polymarket, FRED, CoinGecko, Financial Datasets, Nasdaq, MarketBeat, SECForm4, StockAnalysis, Yahoo Finance, Kalshi, … |
| Companies, people & jobs | 40+ | Web3.career, Apollo, Levels.fyi, Y Combinator, Wellfound, Crunchbase, Hunter, Built In, Indeed, … |
| More | 30+ | IMDb, AAA, IQAir, AccuWeather, Weather Underground, … |
<!-- /inside:en -->

Every entry is in [`catalog/index.json`](catalog/index.json) and [`docs/INDEX.md`](docs/INDEX.md), with its exact price.

This repository is where integration starts:

- **The catalog as data.** Each model and API has a JSON record with its description, input JSON Schema, output shape, sync/async mode and price. The repository also lists public Skills and sandbox templates. Everything refreshes daily from the live API.
- **Dependency-free clients** for Python, TypeScript and Go, plus `.http`, curl and E2B examples.
- **A model page per capability** with ready-to-run curl, Python, TypeScript and Go snippets.

```bash
export SANDBASE_API_KEY=sk-...
```

## Models and APIs

Every non-LLM capability uses the same call. `run()` returns the finished result whether the capability is sync or async.

<table>
<tr><td><b>curl</b></td><td>

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "exa/search", "query": "AI agents", "numResults": 3}'
```
</td></tr>
<tr><td><b>Python</b></td><td>

```python
from sandbase import SandBase   # pip install "git+https://github.com/sandbaseai/sandbase#subdirectory=sdk/python"

sb = SandBase()
sb.run("exa/search", query="AI agents", numResults=3)
sb.run("bytedance/seedance/2.5/text-to-video", prompt="a cat surfing", duration=4)   # async, waits
```
</td></tr>
<tr><td><b>TypeScript</b></td><td>

```ts
import { SandBase } from "@sandbaseai/sdk";   // sdk/typescript, one file, no dependencies

const sb = new SandBase();
await sb.run("exa/search", { query: "AI agents", numResults: 3 });
```
</td></tr>
<tr><td><b>Go</b></td><td>

```go
import sandbase "github.com/sandbaseai/sandbase/sdk/go"

c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "exa/search", sandbase.Params{"query": "AI agents", "numResults": 3})
```
</td></tr>
<tr><td><b>LLMs</b></td><td>

Use the official OpenAI, Anthropic or Gemini SDK and set the base URL to `https://api.sandbase.ai/v1`.
</td></tr>
</table>

Find a capability with [`docs/INDEX.md`](docs/INDEX.md) or `jq`:

```bash
curl -s https://raw.githubusercontent.com/sandbaseai/sandbase/main/catalog/index.json \
  | jq '.models[] | select(.type=="video") | {name, price}'
```

## Sandboxes

Sandboxes are free. SandBase speaks the E2B protocol. Keep the official E2B SDK and your existing code. Change three environment variables:

```bash
export E2B_API_KEY="$SANDBASE_API_KEY"
export E2B_API_URL="https://sandbox.sandbase.ai"
export E2B_DOMAIN="sandbox.sandbase.ai"
```

```python
from e2b import Sandbox   # pip install e2b

sbx = Sandbox.create("tpl_...", timeout=120)          # public templates: catalog/sandbox.json
print(sbx.commands.run("python3 -c 'print(40+2)'").stdout)
sbx.kill()
```

Complete examples: [`examples/sandbox/python`](examples/sandbox/python/hello_sandbox.py) and [`examples/sandbox/typescript`](examples/sandbox/typescript/hello-sandbox.mjs). Both pick a ready template, run a command, write and read a file, and delete the sandbox.

## Agents

Agents are free to create and run. You pay only for the models and APIs they call. SandBase implements the OpenAI Agents API, so the official OpenAI SDK works as-is:

```python
from openai import OpenAI   # pip install openai

client = OpenAI(api_key=os.environ["SANDBASE_API_KEY"], base_url="https://api.sandbase.ai/v1")
agent = client.beta.agents.create(model="deepseek/deepseek-v4-flash", instructions="Answer briefly.")
session = client.beta.agents.sessions.create(agent_id=agent.id, environment={"type": "openai_hosted"})
# open client.beta.agents.sessions.events.stream(session.id), then send input with sessions.events.create(...)
```

The full streaming example is [`examples/agents/python/openai_agents.py`](examples/agents/python/openai_agents.py). Agents can use any LLM in the catalog, the [Skills](docs/SKILLS.md), and SandBase's built-in tools.

If you only want the answer, the clients in this repository wrap the same API in one call:

<table>
<tr><td><b>Python</b></td><td>

```python
agent = sb.create_agent("deepseek/deepseek-v4-flash", "Answer in one short sentence.")
r = sb.run_agent(agent["id"], "What is 2+2?")       # creates a Session and waits for the turn
print(r["output"])                                   # "2 + 2 = 4."
print(sb.send(r["session_id"], "And times 10?")["output"])
print(sb.invoke_service("svc_...", "What is 7+7?")["output"])   # an Agent deployed as an HTTP Service
```
</td></tr>
<tr><td><b>TypeScript</b></td><td>

```ts
const agent = await sb.createAgent({ model: "deepseek/deepseek-v4-flash", instructions: "Answer briefly." });
const r = await sb.runAgent(agent.id, "What is 2+2?");
console.log(r.output, (await sb.send(r.sessionId, "And times 10?")).output);
```
</td></tr>
<tr><td><b>Go</b></td><td>

```go
a, _ := c.CreateAgent(ctx, sandbase.Params{"model": "deepseek/deepseek-v4-flash", "instructions": "Answer briefly."})
res, err := c.RunAgent(ctx, a.ID, "What is 2+2?")
fmt.Println(res.Output)
```
</td></tr>
</table>

## Price before you call

Every model record carries a structured price. For parameter-dependent prices, `price_examples` is precomputed over the allowed values:

```jsonc
// catalog/models/openai/gpt-image-2.5-flare.json → pricing.price_examples
{ "params": { "quality": "low",  "resolution": "1k" }, "usd": 0.01 }
{ "params": { "quality": "high", "resolution": "2k" }, "usd": 0.15 }
{ "params": { "quality": "max",  "resolution": "4k" }, "usd": 1 }
```

| `pricing.model` | Meaning |
|---|---|
| `per_call` | Flat price per successful call (`per_call`) |
| `per_token` | `per_million_tokens.input / output`, plus cache multipliers |
| `formula` | Depends on parameters; see `price_examples`, `formula`, `reference_price` |
| `usage_based` | Metered by the provider per call; `reference_price` is typical |
| `free` | No charge |

Prices are SandBase list prices in USD. Sandboxes and Agents are free; Agents are billed only for the models and APIs they call. Account discounts apply at billing time. `sb.cost(id)` (`GET /v1/tasks/{id}/cost`) returns what a run actually cost. The catalog refreshes daily, so `git log -p catalog/` shows every price change. Every organization gets **100 free data-API calls a day**, shared across the APIs marked `pricing.free_quota` (most data APIs). The quota resets at 00:00 UTC.

## Sync and async

- **sync**: `POST /v1/run` returns `200` with `status: "completed"` and `output` / `outputs`.
- **async**: `POST /v1/run` returns `{"id", "status": "pending"}`. Poll `GET /v1/run/{id}`, or pass `webhook_url` (image, video and audio).
- Only send a `mode` listed in the record. Unsupported modes return `400`.
- Errors: `400` invalid input (checked against `input_schema` before any charge), `401` bad key, `402` insufficient balance, `429` rate or free-quota limit.

## Repository layout

| Path | Contents |
|---|---|
| `catalog/index.json` | Every model and API: name, type, modes, endpoint, price summary |
| `catalog/models/<name>.json` | Full record: description, `input_schema`, output/response schema, modes, endpoints, pricing, examples, docs |
| `catalog/skills.json`, `catalog/sandbox.json` | Public Skills, sandbox connection settings and templates |
| `docs/` | `INDEX.md`, `SKILLS.md`, and one page per model with snippets |
| `openapi/sandbase.openapi.json` | OpenAPI 3.1 for `/v1/run`, `/v1/run/{id}` and `/v1/api/<name>`. Import into Postman, Apifox, gateways or SDK generators |
| `sdk/python`, `sdk/typescript`, `sdk/go` | Clients covering models, APIs and Agents |
| `examples/` | `.http`, curl, sandbox (E2B), Agents (OpenAI SDK) and catalog-import examples |

## Other ways in

- **AI agents** (Claude Code, Codex, Cursor and 22 more): [SandBase CLI / MCP](https://github.com/sandbaseai/cli) lets them discover and run these capabilities at run time.
- **Docs**: [sandbase.ai/docs](https://www.sandbase.ai/docs/)

## Add your API

API owners can propose an integration with a pull request under [`integrations/`](integrations/README.md). CI validates the proposal. A maintainer reviews it and arranges access with you. Merging starts an automated rollout, and the API then appears in this catalog and is callable with every SandBase key.

## Contributing

Found a wrong field or price? Open a [catalog issue](../../issues/new?template=catalog-issue.yml). The catalog files are generated, so we fix the source and the next daily refresh picks up the fix. SDK and example improvements are welcome as pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Code: Apache-2.0. Catalog data: see [NOTICE.md](NOTICE.md).
