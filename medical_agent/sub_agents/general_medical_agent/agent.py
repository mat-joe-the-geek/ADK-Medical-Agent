from google.adk.agents import Agent
from google.adk.agents import LlmAgent
import os
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True" 
# async def create_agent() :
#     agent_instance = Agent(
#         name="medical_agent_bot",
#         description="A medical agent that suggests possible disease based on symptoms and suggests medicines",
#         model="gemini-2.0-flash",
#         instruction=(
#             "You are a medical agent who suggests possible disease based on symptoms."
#             "Always show a disclaimer stating that you are an agent and any prescription should be taken only given by medical professionals."
#         ),
#     )
#     return agent_instance
# root_agent = create_agent()

general_medical_related_agent =LlmAgent(
    name="general_medical_agent",
    description="A medical agent that suggests possible disease based on symptoms and suggests medicines",
    model="gemini-2.0-flash",
    instruction=(
        "You are a general medical agent. Your primary role is to suggest possible diseases or conditions based on the symptoms provided, covering a wide range of medical areas that are not specific to a single specialty."
        "You should also be able to suggest common medications or general management strategies relevant to overall health."
        "When a symptom is provided, consider common ailments and general health principles."
        "You are an agent, and any prescription or medical advice should only be taken when given by qualified medical professionals."
        "\n\n**Disclaimer:** Always consult a healthcare professional for diagnosis and treatment. This information is for educational purposes only and not a substitute for professional medical"
        "Do not try to shorten the response, rather explain in points so its easier for people to read"
    ),
    output_key="general_medical_output",
) 