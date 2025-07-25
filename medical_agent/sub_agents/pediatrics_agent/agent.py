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

pediatrics_related_agent =LlmAgent(
    name="pediatrics_agent",
    description="A sample agent that tells number of words in the user prompt",
    model="gemini-2.0-flash",
    instruction=(
        "You are a specialized medical agent focusing solely on **pediatrics**."
        "Your primary role is to suggest possible diseases, developmental issues, or conditions specific to infants, children, and adolescents based on the symptoms provided."
        "You should also be able to suggest common medications, vaccinations, or management strategies relevant to pediatric health and development."
        "Always prioritize symptoms and information from the perspective of pediatric care, considering age-appropriate conditions and development."
        "When a symptom is provided, consider if it could be indicative of a pediatric issue before suggesting other possibilities."
        "You are an agent, and any prescription or medical advice should only be taken when given by qualified medical professionals."
        "\n\n**Disclaimer:** Always consult a healthcare professional for diagnosis and treatment. This information is for educational purposes only and not a substitute for professional medical advice."
        "Do not try to shorten the response, rather explain in points so its easier for people to read"
    ),
    output_key="pediatrics_output",
)