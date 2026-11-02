<p align="center">
  <a href="https://www.sandbase.ai"><img src=".github/social-preview.png" alt="SandBase：一个 Key 用上模型、数据 API、沙箱和 Agent" width="100%"></a>
</p>

<p align="center">
  <b>一个 API Key，打造你的个人 Agent。</b>
</p>

<p align="center">
  <!-- counts:zh --><b>2,000+ 个模型和 API</b> · 400+ 个 AI 模型 · 1,700+ 个数据 API，来自 100+ 个平台<br><b>每天 100 次免费 API 调用</b> · <b>沙箱免费</b> · <b>Agent 免费</b><!-- /counts:zh -->
</p>

<p align="center">
  <a href="https://www.sandbase.ai/console"><b>获取 API Key</b></a> ·
  <a href="docs/INDEX.md">全部模型和 API</a> ·
  <a href="docs/platforms/README.md">按平台浏览</a> ·
  <a href="https://www.sandbase.ai/docs/">文档</a> ·
  <a href="README.md">English</a>
</p>

---

## 一次调用，拥有你的个人 Agent

创建一个 Agent，交给它任务，拿到结果。每个 Agent 都能自己找到并调用 SandBase 上的 2,000+ 模型和 API，在自己的沙箱里干活。Agent 和沙箱免费，只为 Agent 用到的模型和 API 付费。

```python
# pip install "git+https://github.com/sandbaseai/sandbase#subdirectory=sdk/python"
from sandbase import SandBase

sb = SandBase()  # 读取 SANDBASE_API_KEY

agent = sb.create_agent(
    "deepseek/deepseek-v4-flash",
    instructions="你是我的研究助理，需要实时数据时使用 SandBase 工具。",
)

reply = sb.run_agent(agent["id"], "今天 X 上大家怎么讨论 AI Agent？")
print(reply["output"])
```

实测中，Agent 自己找到了 X 的 API，读取了 schema 和价格，调用后返回三条真实帖子和链接。全程 45 秒，除了 key 不需要任何配置。

新建的 Agent 默认自带 SandBase 工具（discover、inspect、run），不需要配置。如果自己设置 `mcp_connections`，这个列表会替换默认值：要保留 SandBase 工具，就把 `{"connection_id": "builtin:sandbase", "server_label": "sandbase_builtin"}` 一起写进去；只想要纯对话、不带工具，就传 `[]`。

用 `sb.send(reply["session_id"], "...")` 继续对话。调好之后可以部署成 HTTP Service 或定时任务。Agent 兼容 OpenAI Agents API，也可以直接用 OpenAI 官方 SDK。

| | 你的 Agent 得到什么 | 价格 |
|---|---|---|
| 🧰 **工具箱** | 2,000+ 模型和 API：LLM、图像、视频、音频，以及 100+ 平台的社媒、搜索、SEO、电商、金融数据 | 按量付费 · **每天 100 次免费 API 调用** |
| 📦 **工作环境** | 隔离沙箱，可以运行代码、执行命令、读写文件，兼容 E2B SDK | **免费** |
| 🤖 **任务** | 基于 OpenAgentCore 运行时的 Session、HTTP Service、定时任务，通过 OpenAI Agents API 调用 | **免费** |

## 选择你的场景

| 你是 | 从这里开始 |
|---|---|
| **打造个人 Agent** | 上面的示例 |
| **在应用里直接调用模型或 API** | 下面的「快速开始」，以及 [Python](sdk/python) · [TypeScript](sdk/typescript) · [Go](sdk/go) 客户端 |
| **运营中转平台或网关**（new-api、one-api、LiteLLM） | [中转接入指南](docs/guides/relay-platforms.md)（英文）和可直接导入的[价格文件](exports/) |
| **使用 AI 编程工具**（Claude Code、Codex、Cursor） | [SandBase CLI / MCP](https://github.com/sandbaseai/cli) |
| **API 提供方** | 通过 PR [接入你的 API](integrations/README.md) |

## 快速开始

在 [sandbase.ai/console](https://www.sandbase.ai/console) 获取 key 后，就可以调用任意模型或 API：

```bash
export SANDBASE_API_KEY=sk-...

curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "exa/search", "query": "AI agents"}'
```

安装 Python 客户端：

```bash
pip install "git+https://github.com/sandbaseai/sandbase#subdirectory=sdk/python"
```

```python
from sandbase import SandBase

sb = SandBase()

# 数据 API（同步）
sb.run("exa/search", query="AI agents")

# 视频模型（异步，run() 会自动等待结果）
sb.run(
    "bytedance/seedance/2.5/text-to-video",
    prompt="a cat surfing",
    duration=4,
)
```

TypeScript 和 Go 的用法一样，见 [`sdk/typescript`](sdk/typescript) 和 [`sdk/go`](sdk/go)。调用 LLM 时直接用 OpenAI 官方 SDK，把 `base_url` 设为 `https://api.sandbase.ai/v1` 即可。

## 包含哪些

<!-- inside:zh -->
| | 数量 | 包括 |
|---|---|---|
| **AI 模型** | 400+ | LLM 100+、视频 150+、图像 100+、音频 30+：Alibaba, Google, OpenAI, Kling, ByteDance, MiniMax, Black Forest Labs, xAI 等 |
| 社媒与内容 | 1,100+ | Douyin, TikTok, Instagram, Weibo, Xiaohongshu, YouTube, Zhihu, Bilibili, Kuaishou, LinkedIn 等 |
| 搜索、SEO 与网页数据 | 200+ | DataForSEO, Similarweb, Brave, Google, Firecrawl, Artificial Analysis, Exa, Scholar, Tavily, Ahrefs 等 |
| 电商、应用与点评 | 100+ | 1688, GetApp, TikTok Shop, Amazon, Clutch, Trustpilot, G2, JD.com, Taobao, Zillow 等 |
| 金融、加密与市场 | 150+ | Polymarket, FRED, CoinGecko, Financial Datasets, Nasdaq, MarketBeat, SECForm4, StockAnalysis, Yahoo Finance, Kalshi 等 |
| 公司、人物与招聘 | 40+ | Web3.career, Apollo, Levels.fyi, Y Combinator, Wellfound, Crunchbase, Hunter, Built In, Indeed 等 |
| 更多 | 30+ | IMDb, AAA, IQAir, AccuWeather, Weather Underground 等 |
<!-- /inside:zh -->

每个模型和 API 都有一页文档，写明 schema、价格，并附四种语言的示例。完整列表见[全部模型和 API](docs/INDEX.md)，也可以[按平台浏览](docs/platforms/README.md)：[抖音](docs/platforms/douyin.md) · [小红书](docs/platforms/xiaohongshu.md) · [TikTok](docs/platforms/tiktok.md) · [Instagram](docs/platforms/instagram.md) · [YouTube](docs/platforms/youtube.md) · [微博](docs/platforms/weibo.md) · [知乎](docs/platforms/zhihu.md) · [B 站](docs/platforms/bilibili.md) · [OpenAI](docs/platforms/openai.md) · [可灵](docs/platforms/kwaivgi.md)

## 沙箱

沙箱免费，兼容 E2B 协议。继续用 E2B 官方 SDK，把它指向 SandBase 就行：

```python
# pip install e2b
import os
from e2b import Sandbox

os.environ["E2B_API_KEY"] = os.environ["SANDBASE_API_KEY"]
os.environ["E2B_API_URL"] = "https://sandbox.sandbase.ai"
os.environ["E2B_DOMAIN"] = "sandbox.sandbase.ai"

sbx = Sandbox.create("tpl_...", timeout=120)  # 模板 ID 见 catalog/sandbox.json
print(sbx.commands.run("python3 -c 'print(40 + 2)'").stdout)
sbx.kill()
```

## Agent

Agent 免费，Agent 调用的模型和 API 照常计费。

```python
agent = sb.create_agent(
    "deepseek/deepseek-v4-flash",
    instructions="用一句话回答。",
)

reply = sb.run_agent(agent["id"], "2+2 等于几？")
print(reply["output"])

# 在同一个 Session 里追问
sb.send(reply["session_id"], "再乘以 10？")
```

也可以直接用 OpenAI 官方 SDK 的 `client.beta.agents`，示例见 [`examples/agents`](examples/agents)。

## 价格

- **免费**：沙箱、Agent，以及每个组织每天 100 次数据 API 调用（UTC 0 点重置）。
- **按量付费**：其他调用都按目录里的美元标价计费，调用失败不收费。
- **调用前算价格**：价格随参数变化的模型，附有 `price_examples` 价格表。例如 gpt-image-2.5-flare 分 15 档，从 $0.01 到 $1。
- **查实际费用**：用 `sb.cost(id)` 查询某次调用的实际扣费。目录每天刷新，`git log -p catalog/` 可以看到每一次改价。

## 接入你的 API

API 提供方可以在 [`integrations/`](integrations/README.md) 下提交 PR 申请接入。CI 会自动校验，维护者审核通过后自动上线，上线后所有 SandBase key 都能调用。Issue 和 PR 请使用英文。

<details>
<summary><b>常见问题</b></summary>

- **兼容 OpenAI 吗？** 兼容。Chat Completions、Responses 和 Agents API 都可以直接用 OpenAI 官方 SDK，Anthropic 和 Gemini 格式也支持。
- **E2B 代码能直接用吗？** 能，只需要改三个环境变量。
- **怎么调用抖音、小红书、TikTok、YouTube 的数据？** 在[平台页](docs/platforms/README.md)找到对应接口，用 `POST /v1/run` 加上它的 `model` 名称调用，不需要分别注册这些平台的账号。
- **AI 编程工具能用吗？** 能。[SandBase CLI / MCP](https://github.com/sandbaseai/cli) 支持 Claude Code、Codex、Cursor 等 25 个客户端。
</details>

代码采用 [Apache-2.0](LICENSE) 许可。目录数据的使用说明见 [NOTICE.md](NOTICE.md)。如果这个项目对你有帮助，欢迎点个 ⭐。
