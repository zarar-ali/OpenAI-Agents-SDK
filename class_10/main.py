from dotenv import load_dotenv
import nest_asyncio
import requests
import json
import os

nest_asyncio.apply()
load_dotenv()


# 1. Using the OpenRouter API directly

# BASE_URL = "https://openrouter.ai/api/v1"
# MODEL = "deepseek/deepseek-r1-0528-qwen3-8b:free"

# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# response = requests.post(
#   url=f"{BASE_URL}/chat/completions",
#   headers={
#     "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#   },
#   data=json.dumps({
#     "model": MODEL,
#     "messages": [
#       {
#         "role": "user",
#         "content": "hello, how are you?"
#       }
#     ]
#   })
# )

# print(response.json())

# data = response.json()
# data['choices'][0]['message']['content']

# 2. Using OpenAI Agents SDK

import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

MODEL = os.getenv("MODEL")

client = AsyncOpenAI(
    api_key= os.getenv("OPENROUTER_API_KEY"),
    base_url= os.getenv("BASE_URL"),
   
)

set_tracing_disabled(disabled=True)

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = await Runner.run(
        agent,
        "Tell me about recursion in programming.",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())