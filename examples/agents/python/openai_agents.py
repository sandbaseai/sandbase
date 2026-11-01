#!/usr/bin/env python3
"""Create and run a SandBase Agent with the official OpenAI SDK (pip install openai).

    export SANDBASE_API_KEY=sk-...
    python openai_agents.py "What are three uses of a vector database?"

SandBase implements the OpenAI Agents API: point base_url at SandBase and use your SandBase key.
The Agent runtime is free; you pay only for the model and API calls the Agent makes.
"""
import os
import sys
import threading
import time

from openai import OpenAI

client = OpenAI(api_key=os.environ["SANDBASE_API_KEY"], base_url="https://api.sandbase.ai/v1")
question = sys.argv[1] if len(sys.argv) > 1 else "What is 2+2?"

agent = client.beta.agents.create(
    name="OpenAI SDK example",
    model="deepseek/deepseek-v4-flash",          # any LLM in catalog/index.json
    instructions="Answer briefly and clearly.",
)
while client.beta.agents.retrieve(agent.id).model_extra.get("projection_status") not in (None, "ready"):
    time.sleep(2)                                # the new version is being prepared

session = client.beta.agents.sessions.create(
    agent_id=agent.id,
    environment={"type": "openai_hosted"},       # required by the SDK; SandBase always runs Sessions in its cloud
)


def send_input():
    client.beta.agents.sessions.events.create(
        session.id,
        events=[{
            "type": "agent.session.input.message",
            "input": [{"role": "user", "content": [{"type": "input_text", "text": question}]}],
        }],
    )


# The event stream is live-only: open it first, then send the input.
with client.beta.agents.sessions.events.stream(session.id) as stream:
    threading.Thread(target=send_input).start()
    for event in stream:
        if event.type in ("agent.session.turn.completed", "agent.session.turn.failed", "agent.session.turn.cancelled"):
            print("turn:", event.type.rsplit(".", 1)[-1])
            break

for item in client.beta.agents.sessions.items.list(session.id, order="asc"):
    if getattr(item, "role", None) == "assistant":
        print("".join(part.text for part in item.content if getattr(part, "type", "") == "output_text"))

# Keep the Agent to reuse it (Sessions, Services, Schedules). This example archives both.
client.beta.agents.sessions.delete(session.id)
client.beta.agents.delete(agent.id)
