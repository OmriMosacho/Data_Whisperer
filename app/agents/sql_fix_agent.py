from app.config import llm

def fix_sql_with_llm(sql_error, sql):
    prompt = f"""
The following SQL caused an error:

{sql}

Error:
{sql_error}

Rewrite the SQL so it is valid in PostgreSQL.
Return only the corrected SQL.
"""
    corrected = llm(prompt)
    return corrected.content.replace("```sql","").replace("```","")