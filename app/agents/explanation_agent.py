# app/agents/explanation_agent.py
from app.config import llm
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system",
    #  "Explain SQL query results to a business user. Be concise, short and clear."
    #  "You are an expert demand planner at 'Emerson Electric Co' market."
    #     "If the user asks to 'Analyze' Explain the SQL results as a senior planner would, including:"
    #     "- Trends in the industrial equipment market"
    #     "- Seasonal effects"
    #     "- Stock & supply chain implications"
    #     "- Practical recommendations for business"
    #     "Use recent market trends when possible. Return a concise, actionable explanation."
        "Answer Shortly! If asked to analyze, only then,  you can elaborate"
     ),
    ("human", """
Question:
{question}

Result:
{result}

Explain the findings:
""")
])

def explain(question: str, result: dict):
    chain = prompt | llm
    return chain.invoke({
        "question": question,
        "result": result
    }).content
