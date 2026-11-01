<h1 align="center">SandBase</h1>

<p align="center"><b>AI 模型、数据 API、沙箱和 Agent。一个 Key，按量付费。</b></p>

<p align="center"><!-- counts:zh -->**2,000+ 个模型和 API** · 400+ 个 AI 模型 · 1,700+ 个数据 API，来自 100+ 个平台<br>**每天 100 次免费 API 调用** · **沙箱免费** · **Agent 免费**<!-- /counts:zh --><br>HTTP · curl · Python · TypeScript · Go · OpenAPI 3.1 · E2B SDK · OpenAI SDK</p>

---

大多数平台只做其中一层：LLM 网关、媒体生成 API、沙箱，或者工具目录。SandBase 把这四层都放在**同一个 key、同一份余额、同一张账单**下，而且四层之间可以互相调用：你在 SandBase 定义的 Agent 能调用目录里的任何模型和数据 API，代码在 SandBase 的沙箱里运行。

| 层 | 内容 | 价格 | 调用方式 |
|---|---|---|---|
| **模型** | LLM、图像、视频、音频、Embedding | 按次或按 token，价格见目录 | OpenAI、Anthropic、Gemini 官方 SDK，或 `POST /v1/run` |
| **API** | 搜索、抓取、社媒、电商、SEO、金融等数据 API | **每天 100 次免费**，超出后按次计费 | `POST /v1/run` 或 `POST /v1/api/<name>` |
| **沙箱** | 隔离的机器，可以执行命令、读写文件、运行代码 | **免费** | 官方 **E2B SDK**：只改地址和 key，代码不用动 |
| **Agent** | 带版本的 Agent、Session、HTTP Service、定时任务、Skill、MCP | **免费**，Agent 调用的模型和 API 照常计费 | 官方 **OpenAI SDK**（`client.beta.agents`），或本仓库的客户端 |

## 包含哪些

<!-- inside:zh -->
| | 数量 | 包括 |
|---|---|---|
| **AI 模型** | 400+ | LLM 100+、视频 150+、图像 100+、音频 30+：Alibaba, Google, OpenAI, KwaiVGI, Bytedance, MiniMax, BFL, xAI 等 |
| 社媒与内容 | 1,100+ | Douyin, TikTok, Instagram, Weibo, Xiaohongshu, YouTube, Zhihu, Bilibili, Kuaishou, LinkedIn 等 |
| 搜索、SEO 与网页数据 | 200+ | DataForSEO, Similarweb, Brave, Google, Firecrawl, Artificial Analysis, Exa, Scholar, Tavily, Ahrefs 等 |
| 电商、应用与点评 | 100+ | 1688, GetApp, TikTok Shop, Amazon, Clutch, Trustpilot, G2, JD.com, Taobao, Zillow 等 |
| 金融、加密与市场 | 150+ | Polymarket, FRED, CoinGecko, Financial Datasets, Nasdaq, MarketBeat, SECForm4, StockAnalysis, Yahoo Finance, Kalshi 等 |
| 公司、人物与招聘 | 40+ | Web3.career, Apollo, Levels.fyi, Y Combinator, Wellfound, Crunchbase, Hunter, Built In, Indeed 等 |
| 更多 | 30+ | IMDb, AAA, IQAir, AccuWeather, Weather Underground 等 |
<!-- /inside:zh -->

完整列表和每个能力的精确价格见 `catalog/index.json` 和 `docs/INDEX.md`。

## 快速上手

```bash
export SANDBASE_API_KEY=sk-...
```

```python
from sandbase import SandBase        # pip install "git+https://github.com/sandbaseai/sandbase#subdirectory=sdk/python"
sb = SandBase()

sb.run("exa/search", query="AI agents")                                             # 数据 API，同步调用
sb.run("bytedance/seedance/2.5/text-to-video", prompt="a cat surfing", duration=4)  # 视频，异步，会自动等待结果

agent = sb.create_agent("deepseek/deepseek-v4-flash", "用一句话回答。")
r = sb.run_agent(agent["id"], "2+2 等于几？")                                         # 运行一次 Agent
print(r["output"], sb.send(r["session_id"], "再乘以 10？")["output"])
```

Agent：直接用 OpenAI 官方 SDK，把 `base_url` 设为 `https://api.sandbase.ai/v1`，示例见 `examples/agents/python/openai_agents.py`。

沙箱：保留 E2B 官方 SDK，只需设置这三个环境变量：`E2B_API_KEY=$SANDBASE_API_KEY`、`E2B_API_URL=https://sandbox.sandbase.ai`、`E2B_DOMAIN=sandbox.sandbase.ai`。完整示例在 `examples/sandbox/`。

TypeScript 和 Go 的用法和 Python 一样，见 `sdk/typescript` 和 `sdk/go`。

## 调用前就知道价格

每个模型都有结构化的价格字段。价格随参数变化的模型附带 `price_examples` 价格表，例如 gpt-image-2.5-flare 分 15 档，从 $0.01 到 $1。目录每天刷新，`git log -p catalog/` 可以看到每一次改价。实际扣费用 `sb.cost(id)` 查询，账户折扣在计费时扣减。

## 仓库内容

- `catalog/`：每个模型和 API 的说明、schema、价格；另有 Skill 和沙箱模板。
- `docs/`：按模型生成的文档页，每页带 curl、Python、TypeScript、Go 示例。
- `openapi/`：OpenAPI 3.1 文件，可以导入 Postman、Apifox、API 网关或你自己的平台。
- `sdk/`：Python、TypeScript、Go 三个客户端，覆盖模型、API 和 Agent。
- `examples/`：`.http`、curl、沙箱（E2B）、Agent（OpenAI SDK）示例。

AI Agent 客户端（Claude Code、Codex、Cursor 等 25 个）可以用 [SandBase CLI / MCP](https://github.com/sandbaseai/cli) 接入。

## 接入你的 API

API 提供方可以在 [`integrations/`](integrations/README.md) 下提交 PR 来申请接入。CI 会自动校验提交的文件，维护者审核后会和你联系，确认 API 访问方式。PR 合并后自动进入上线流程，上线后会出现在目录里，所有 SandBase key 都能直接调用。Issue 和 PR 请用英文。
