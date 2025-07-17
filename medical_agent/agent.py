from google.adk.agents import Agent
import os
from . import prompt

# Import general medical agent
from .sub_agents.sub_agent_coordinator import sub_agent_coordinator


# --- Define the Coordinator Agent ---
root_agent = Agent(
    name="medical_agent",
    description="The main agent that delegates medical questions to sub agents coordinator and handles other queries.",
    model="gemini-2.0-flash",
    instruction=prompt.MEDICAL_AGENT_PROMPT,
    sub_agents=[sub_agent_coordinator],
)