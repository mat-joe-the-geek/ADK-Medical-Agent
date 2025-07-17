from google.adk.agents import Agent
import os
from . import prompt

# Import general medical agent
from ..general_medical_agent import general_medical_related_agent

# Import your specialized medical agents
from ..cardiology_agent import cardiology_related_agent
from ..dermatology_agent import dermatology_related_agent
from ..neurology_agent import neurology_related_agent
from ..orthology_agent import orthology_related_agent
from ..pediatrics_agent import pediatrics_related_agent
from ..psychiatry_agent import psychiatry_related_agent


# --- Define the Coordinator Agent ---
sub_agent_coordinator = Agent(
    name="sub_agent_coordinator",
    description="A coordinator agent that delegates medical questions to specialized agents and handles other queries.",
    model="gemini-2.0-flash",
    instruction=prompt.SUB_AGENT_COORDINATOR_PROMPT,
    sub_agents=[
        general_medical_related_agent,
        cardiology_related_agent,
        dermatology_related_agent,
        neurology_related_agent,
        orthology_related_agent,
        pediatrics_related_agent,
        psychiatry_related_agent,
    ],
)

