// SandBase client for Node 18+, Deno, Bun and browsers (global fetch). No dependencies.
//
//   import { SandBase } from "@sandbaseai/sdk";
//   const sb = new SandBase();                               // SANDBASE_API_KEY
//   const r = await sb.run("exa/search", { query: "AI agents" });

export const VERSION = "0.1.0";
export const DEFAULT_BASE_URL = "https://api.sandbase.ai";
const TERMINAL = new Set(["completed", "succeeded", "failed", "cancelled", "canceled"]);

export interface RunResult {
  id: string;
  model?: string;
  status: string;
  output?: unknown;
  outputs?: Array<Record<string, unknown>>;
  error?: string | { type?: string; message?: string };
}

export interface SubmitOptions {
  /** Only values listed in the model's catalog record ("sync" | "async"). */
  mode?: string;
  /** Async image/video/audio only. */
  webhookUrl?: string;
}

export interface WaitOptions {
  timeoutMs?: number;
  intervalMs?: number;
  maxIntervalMs?: number;
}

export class SandBaseError extends Error {
  constructor(message: string, public status?: number, public body?: unknown) {
    super(message);
    this.name = "SandBaseError";
  }
}

export interface ClientOptions {
  apiKey?: string;
  baseUrl?: string;
  fetch?: typeof fetch;
}

const env = (k: string): string | undefined =>
  (globalThis as { process?: { env?: Record<string, string | undefined> } }).process?.env?.[k];

export class SandBase {
  readonly apiKey: string;
  readonly baseUrl: string;
  private readonly fetchImpl: typeof fetch;

  constructor(opts: ClientOptions = {}) {
    const key = opts.apiKey ?? env("SANDBASE_API_KEY");
    if (!key) throw new SandBaseError("missing API key: pass apiKey or set SANDBASE_API_KEY");
    this.apiKey = key;
    this.baseUrl = (opts.baseUrl ?? env("SANDBASE_BASE_URL") ?? DEFAULT_BASE_URL).replace(/\/+$/, "");
    this.fetchImpl = opts.fetch ?? fetch;
  }

  /** Call any endpoint, e.g. request("POST", "/v1/chat/completions", {...}). */
  async request<T = unknown>(method: string, path: string, body?: unknown, headers: Record<string, string> = {}): Promise<T> {
    const res = await this.fetchImpl(this.baseUrl + path, {
      method,
      headers: { Authorization: `Bearer ${this.apiKey}`, "Content-Type": "application/json", ...headers },
      body: body === undefined ? undefined : JSON.stringify(body),
    });
    const text = await res.text();
    let parsed: unknown = text;
    try {
      parsed = text ? JSON.parse(text) : undefined;
    } catch {
      /* keep text */
    }
    if (!res.ok) throw new SandBaseError(`HTTP ${res.status}: ${text.slice(0, 500)}`, res.status, parsed);
    return parsed as T;
  }

  /** POST /v1/run. Sync capabilities return the finished run; async ones return {id, status: "pending"}. */
  submit(model: string, params: Record<string, unknown> = {}, opts: SubmitOptions = {}): Promise<RunResult> {
    return this.request<RunResult>("POST", "/v1/run", {
      model,
      ...params,
      ...(opts.mode ? { mode: opts.mode } : {}),
      ...(opts.webhookUrl ? { webhook_url: opts.webhookUrl } : {}),
    });
  }

  get(id: string): Promise<RunResult> {
    return this.request<RunResult>("GET", `/v1/run/${encodeURIComponent(id)}`);
  }

  /** Poll GET /v1/run/{id} with backoff until the run is terminal. */
  async wait(id: string, opts: WaitOptions = {}): Promise<RunResult> {
    const deadline = Date.now() + (opts.timeoutMs ?? 900_000);
    let interval = opts.intervalMs ?? 2000;
    for (;;) {
      const run = await this.get(id);
      if (TERMINAL.has(run.status)) return run;
      if (Date.now() > deadline) throw new SandBaseError(`run ${id} still ${run.status}`, undefined, run);
      await new Promise((r) => setTimeout(r, interval));
      interval = Math.min(interval * 1.5, opts.maxIntervalMs ?? 15_000);
    }
  }

  /** Run any capability and resolve with the finished result, sync or async. Rejects if the run failed. */
  async run(model: string, params: Record<string, unknown> = {}, opts: WaitOptions = {}): Promise<RunResult> {
    let run = await this.submit(model, params);
    if (!TERMINAL.has(run.status)) run = await this.wait(run.id, opts);
    if (run.status === "failed") throw new SandBaseError(`run ${run.id} failed`, undefined, run);
    return run;
  }

  /** Billed amount of a run: GET /v1/tasks/{id}/cost. */
  cost(id: string): Promise<Record<string, unknown>> {
    return this.request("GET", `/v1/tasks/${encodeURIComponent(id)}/cost`);
  }

  /** OpenAI-compatible chat completion. For streaming use the openai SDK with baseURL. */
  chat(model: string, messages: Array<Record<string, unknown>>, extra: Record<string, unknown> = {}) {
    return this.request<Record<string, unknown>>("POST", "/v1/chat/completions", { model, messages, ...extra });
  }

  // ---------------------------------------------------------------- Agents

  /** POST /v1/agents, then wait until the version can start Sessions. */
  async createAgent(fields: { model: string; instructions?: string; name?: string; [k: string]: unknown }, idempotencyKey?: string): Promise<Agent> {
    const agent = await this.request<Agent>("POST", "/v1/agents", fields, { "Idempotency-Key": idempotencyKey ?? key() });
    return this.waitAgentReady(agent);
  }

  /** Start a Session with `input` and wait for the turn. */
  async runAgent(agentId: string, input: string, opts: WaitOptions = {}): Promise<AgentTurnResult> {
    const session = await this.request<{ id: string }>("POST", "/v1/agents/sessions", { agent_id: agentId, input }, { "Idempotency-Key": key() });
    return this.finishTurn(session.id, 0, opts);
  }

  /** Send a follow-up message to a Session and wait for its turn. */
  async send(sessionId: string, input: string, opts: WaitOptions = {}): Promise<AgentTurnResult> {
    const previous = (await this.turns(sessionId)).length;
    await this.request("POST", `/v1/agents/sessions/${sessionId}/events`, { input }, { "Idempotency-Key": key() });
    return this.finishTurn(sessionId, previous, opts);
  }

  /** Invoke a Service and wait for its Run; `output` is the Session's final assistant text. */
  async invokeService(serviceId: string, input?: string, opts: WaitOptions & { idempotencyKey?: string } = {}) {
    let run = await this.request<ServiceRun>("POST", `/v1/services/${serviceId}/invoke`, input ? { input } : {}, {
      "Idempotency-Key": opts.idempotencyKey ?? key(),
    });
    const deadline = Date.now() + (opts.timeoutMs ?? 900_000);
    let interval = opts.intervalMs ?? 2000;
    while (!["succeeded", "failed", "cancelled", "canceled"].includes(run.status)) {
      if (Date.now() > deadline) throw new SandBaseError(`service run ${run.id} still ${run.status}`, undefined, run);
      await sleep(interval);
      interval = Math.min(interval * 1.5, 15_000);
      run = await this.request<ServiceRun>("GET", `/v1/services/${serviceId}/runs/${run.id}`);
    }
    if (run.session_id) run.output = await this.latestOutput(run.session_id);
    return run;
  }

  private async waitAgentReady(agent: Agent, timeoutMs = 120_000): Promise<Agent> {
    const deadline = Date.now() + timeoutMs;
    while (agent.projection_status && agent.projection_status !== "ready") {
      if (agent.projection_status === "failed" || Date.now() > deadline)
        throw new SandBaseError(`agent ${agent.id} projection ${agent.projection_status}`, undefined, agent);
      await sleep(2000);
      agent = await this.request<Agent>("GET", `/v1/agents/${agent.id}`);
    }
    return agent;
  }

  private async turns(sessionId: string): Promise<Array<{ id: string; status: string; error?: unknown }>> {
    return (await this.request<{ data: Array<{ id: string; status: string }> }>("GET", `/v1/agents/sessions/${sessionId}/turns`)).data ?? [];
  }

  private async finishTurn(sessionId: string, previousTurns: number, opts: WaitOptions): Promise<AgentTurnResult> {
    const deadline = Date.now() + (opts.timeoutMs ?? 900_000);
    let interval = opts.intervalMs ?? 2000;
    for (;;) {
      const turns = await this.turns(sessionId); // newest first
      if (turns.length > previousTurns && TURN_TERMINAL.has(turns[0].status)) {
        const turn = turns[0];
        if (turn.status !== "completed") throw new SandBaseError(`turn ${turn.id} ${turn.status}`, undefined, turn);
        return { sessionId, status: turn.status, output: await this.latestOutput(sessionId), turn };
      }
      const session = await this.request<{ status: string; failure?: unknown }>("GET", `/v1/agents/sessions/${sessionId}`);
      if (session.status === "failed") throw new SandBaseError(`session ${sessionId} failed`, undefined, session);
      if (Date.now() > deadline) throw new SandBaseError(`session ${sessionId} turn not finished`, undefined, session);
      await sleep(interval);
      interval = Math.min(interval * 1.5, 10_000);
    }
  }

  private async latestOutput(sessionId: string): Promise<string> {
    const items = (await this.request<{ data: SessionItem[] }>("GET", `/v1/agents/sessions/${sessionId}/items?order=desc&limit=50`)).data ?? [];
    const texts: string[] = [];
    for (const item of items) {
      if (item.type === "message" && item.role === "user") break;
      if (item.type === "message" && item.role === "assistant")
        for (const part of item.content ?? []) if (part.type === "output_text") texts.unshift(part.text ?? "");
    }
    return texts.join("\n");
  }
}

export interface Agent {
  id: string;
  name?: string;
  model?: string;
  version?: number;
  projection_status?: string;
  [k: string]: unknown;
}

export interface AgentTurnResult {
  sessionId: string;
  status: string;
  output: string;
  turn: { id: string; status: string; [k: string]: unknown };
}

export interface ServiceRun {
  id: string;
  status: string;
  session_id?: string;
  output?: string;
  [k: string]: unknown;
}

interface SessionItem {
  type?: string;
  role?: string;
  content?: Array<{ type?: string; text?: string }>;
}

const TURN_TERMINAL = new Set(["completed", "failed", "cancelled", "canceled", "incomplete", "expired"]);
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));
const key = () => `sdk-${globalThis.crypto?.randomUUID?.() ?? `${Date.now()}-${Math.random().toString(16).slice(2)}`}`;

export default SandBase;
