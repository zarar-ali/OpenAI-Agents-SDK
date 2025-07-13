# Global level

from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api # <- new line
from agents.extensions.visualization import draw_graph

gemini_api_key = userdata.get('GEMINI_API_KEY')
set_tracing_disabled(True)
set_default_openai_api("chat_completions") # <- new line

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)

import nest_asyncio
nest_asyncio.apply()

agent: Agent = Agent(
  name="Assistant",
  instructions="You are a helpful assistant",
  model="gemini-2.0-flash")

result = Runner.run_sync(agent, "Hello")

print(result.final_output)

# from agents import enable_verbose_stdout_logging

# enable_verbose_stdout_logging()

# agent: Agent = Agent(name="Assistant",
# instructions="You are a helpful assistant",
# model="gemini-2.0-flash")

# result = Runner.run_sync(agent, "Hi, My name is shahid")

# print(result.final_output)

# from agents import enable_verbose_stdout_logging, function_tool

# enable_verbose_stdout_logging()

# @function_tool
# def get_current_weather(city: str):
#   """Retruns weather for the city

#   Args:
#     city: City name

#   Retruns:
#     Weather: str
#     """
#   return f"The weather in {city} is sunny"

# agent: Agent = Agent(
#   name="Assistant",
#   instructions="You are a helpful assistant",
#   model="gemini-2.0-flash",
#   tools = [get_current_weather]
#   )

# result = Runner.run_sync(agent, "What is the weather in Karachi")

# print(result.final_output)

# from agents import enable_verbose_stdout_logging, function_tool

# enable_verbose_stdout_logging()

# @function_tool
# def get_current_news(industry: str) -> str:
#   """Retruns current news for a particular industry

#   Args:
#     industry: The industry to look in current News

#   Retruns:
#     news: str
#     """
#   return f"{industry} have new concept Agent Native Cloud"

# agent: Agent = Agent(name="Assistant",
#                      instructions="You are a helpful assistant",
#                      model="gemini-2.0-flash",
#                      tools = [get_current_weather, get_current_news]
#                      )

# result = Runner.run_sync(agent, "What is the weather in Karachi and share latest news in tech?")

# print(result.final_output)

# from agents import enable_verbose_stdout_logging, function_tool

# enable_verbose_stdout_logging()

# @function_tool
# def get_current_news(industry: str) -> str:
#   """Retruns current news for a particular industry

#   Args:
#     industry: The industry to look in current News

#   Retruns:
#     news: str
#     """
#   return f"{industry} have new concept Agent Native Cloud"

# panaversity_expert: Agent = Agent(name="Panaversity Assistant",
#                      instructions="You are a helpful panaversity assistant. you answer all about Panaversity",
#                      model="gemini-2.0-flash",
#                      handoff_description="Panaversity Expert"

#                      )

# agentic_ai_expert: Agent = Agent(name="Agentic AI Assistant",
#                      instructions="You are a helpful agentic ai expert. you answer all about AI Agents",
#                      model="gemini-2.0-flash",
#                      handoff_description="Agentic AI Expert"

#                      )

# triage_agent: Agent = Agent(
#     name="Triage Agent",
#     instructions="You are general chat assistant. you observe the communication with user and let relevant  agents answer back to user queries.",
#     model="gemini-2.0-flash",
#     handoffs=[panaversity_expert, agentic_ai_expert]
# )

# result = Runner.run_sync(triage_agent, "Who is the founder of PIAIC?")

# print(result.final_output)

# result.last_agent.name





# draw_graph(triage_agent)