# Import necessary classes and functions from the agents library
from agents import Agent, OpenAIChatCompletionsModel, RunConfig, Runner, AsyncOpenAI, set_tracing_disabled

# Import os to access environment variables
import os

# Import load_dotenv to manage environment variables
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Disable tracing if needed
set_tracing_disabled(disabled=True)


# Get the Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")


# Ensure the API key is available
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")


# Step 1 client
# Initialize the AsyncOpenAI client with the Gemini API key and base URL
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Step 2 model
# Initialize the OpenAIChatCompletionsModel with the desired Gemini model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # or "gemini-1.5-pro"
    openai_client=client,
)


# Step 3 run config
# Create a RunConfig with the specified model
run_config = RunConfig(
    model=model,
)


# Step 4 agent
# Create an Agent with a name and instructions
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant that greets the user.",
)

# Step 5 run
# Run the agent with a sample input and the run configuration
result = Runner.run_sync(agent, "Hello, how are you?", run_config=run_config)

# Print the final output from the agent
print(result.final_output)