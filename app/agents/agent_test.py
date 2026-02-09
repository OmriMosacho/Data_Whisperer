# app/agents/agent_full_test.py
from app.agents.intent_agent import detect_intent
from app.agents.sql_planner_agent import plan_sql
from app.agents.sql_validator import validate_sql
from app.agents.execution_agent import execute_sql
from app.agents.explanation_agent import explain
from app.db.schema_loader import load_schema

question = "how many active combinations of item and location are there sold more than 100 units in may 2025 and what is their distribution to emr_abc_class?"

# Step 1: Detect intent
intent = detect_intent(question)

# Step 2: Load schema
schema = load_schema()
schema_text = "\n".join([f"{t}: {cols}" for t, cols in schema.items()])

# Step 3: Generate SQL
sql = plan_sql(intent, schema_text)

# Step 4: Validate
validate_sql(sql)

# Step 5: Execute
result = execute_sql(sql)

sql = result["sql"].replace("\n"," ")

# Step 6: Explain
explanation = explain(question, result)

print("Question:", question)
print("Intent:", intent)
print("SQL:", sql)
print("Result:", result)
print("Explanation:", explanation)
