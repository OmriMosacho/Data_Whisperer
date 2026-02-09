from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from ..config import llm, memory


class IntentResult(BaseModel):
    intent: str
    metric: str
    period: str


parser = PydanticOutputParser(pydantic_object=IntentResult)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a senior business analyst. "
        "You classify analytical business questions. "
        "Use the conversation history for context. "
        "Return ONLY valid JSON."
    ),
    (
        "human",
        """
Conversation history:
{history}

Question:
{question}

{format_instructions}
"""
    )
])


def detect_intent(question: str) -> IntentResult:

    history = memory.load_memory_variables({}).get("history", "")

    chain = prompt | llm | parser

    result = chain.invoke({
        "question": question,
        "history": history,
        "format_instructions": parser.get_format_instructions()
    })

    memory.save_context(
        {"input": question},
        {"output": result.json()}
    )

    return result
