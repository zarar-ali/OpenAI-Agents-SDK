# Async Function
import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

# Load environment variables from .env
load_dotenv()

# Disable tracing
set_tracing_disabled(disabled=True)

# Get environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("MODEL")

# Check if API key is present
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Define tool
@function_tool
def get_weather(city: str) -> str:
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."

# Create Agents
weather_agent = Agent(
    name="WeatherAssistant",
    instructions="You will answer weather relevent questions only karachi city",
    model=LitellmModel(model=MODEL, api_key=GEMINI_API_KEY),
    tools=[get_weather],
    handoff_description="Weather Assistant is specialized for All Weather Queries"
)

giaic_agent = Agent(
    name="GIAIC Assistant",
    instructions="You will answer GIAIC relevent questions, GIAIC is the governor iniative for artificial intelligenne and cloud computing",
    model=LitellmModel(model=MODEL, api_key=GEMINI_API_KEY),
    handoff_description=(
        "GIAIC Assistant is trained to answer questions only related to the Governor Initiative for Artificial Intelligence and Cloud Computing (GIAIC), "
        "including its courses, instructors, assignments, and events."
    )
)

triage_agent = Agent(
    name="GeneralAssistant",
    instructions="You will chat with user for general questions and handoff to Specialized Assistants when needed i.e: WeatherAssistant for weather queries and GIAIC Assistant for All Governor Initiative for Artificial Intelligence and Cloud Computing",
    model=LitellmModel(model=MODEL, api_key=GEMINI_API_KEY),
    handoffs=[weather_agent, giaic_agent]
)

# Wrap in async function
async def main():
    result = await Runner.run(triage_agent, "Hi")
    print(result.final_output)

# Call the async function properly
asyncio.run(main())
