from django.conf import settings

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from pydantic import BaseModel, Field

class SupportResponse(BaseModel):

    suggested_response: str = Field(
        description="Professional response to the support ticket"
    )

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
    """
You are a professional customer support assistant.

Create a helpful and professional response for the following support ticket.

TICKET TITLE:
{title}

TICKET DESCRIPTION:
{description}

CATEGORY:
{category}

PRIORITY:
{priority}

STATUS:
{status}

REQUIREMENTS:
1. Be polite and professional.
2. Clearly acknowledge the customer's issue.
3. Do not invent information.
4. Do not promise anything that is not confirmed.
5. Keep the response concise.
6. Return only the requested structured output.
"""
)

structured_llm = llm.with_structured_output(
    SupportResponse
)

ai_chain = prompt | structured_llm

def generate_support_response(ticket):

    result = ai_chain.invoke(
        {
            "title": ticket.title,
            "description": ticket.description,
            "category": ticket.category,
            "priority": ticket.priority,
            "status": ticket.status,
        }
    )

    return result