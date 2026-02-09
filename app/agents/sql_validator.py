# app/agents/sql_validator.py

FORBIDDEN = ["insert", "update", "delete", "drop", "alter"]

def validate_sql(sql: str):
    lowered = sql.lower()
    for word in FORBIDDEN:
        if word in lowered:
            raise ValueError(f"Forbidden SQL detected: {word}")

    if not lowered.strip().startswith("select"):
        raise ValueError("Only SELECT statements allowed")
    


    return True
