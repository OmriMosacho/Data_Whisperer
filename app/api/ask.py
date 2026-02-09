from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.intent_agent import detect_intent
from app.agents.sql_planner_agent import plan_sql
from app.agents.execution_agent import execute_sql
from app.agents.explanation_agent import explain
from app.db.schema_loader import load_allowed_schema

router = APIRouter()


class AskRequest(BaseModel):
    question: str


@router.post("/")
def ask(req: AskRequest):
    # 1. Detect intent
    intent = detect_intent(req.question)

    # 2. Load schema (restricted)
    schema = load_allowed_schema()

    # 3. Plan SQL
    sql = plan_sql(intent, schema)

    # 4. Execute SQL
    result = execute_sql(sql)

    # 5. Explain
    explanation = explain(req.question, result)

    return {
        "intent": intent,
        "sql": sql,
        "data": result,
        "explanation": explanation
    }
