from dotenv import load_dotenv
import os
import nest_asyncio
nest_asyncio.apply()
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from openai import AsyncOpenAI
import asyncio

load_dotenv()

MODEL = os.getenv("MODEL")

set_tracing_disabled(disabled=True) # Open AI Tracing == Disable

client = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("BASE_URL"),
)

set_tracing_disabled(disabled=True)


async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="You only respond in english.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = await Runner.run(
        agent, # starting agent
        "What is your name?.", # request
    )
    print(result.final_output)


asyncio.run(main())
