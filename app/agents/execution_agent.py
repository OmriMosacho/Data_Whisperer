from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.db.connection import engine
from app.agents.sql_fix_agent import fix_sql_with_llm


def execute_sql(sql: str, max_attempts: int = 3):
    last_error = None

    for attempt in range(max_attempts):
        try:
            with engine.connect() as conn:
                result = conn.execute(text(sql))

                columns = list(result.keys())
                rows = [list(row) for row in result.fetchall()]

                return {
                    "sql": sql,
                    "columns": columns,
                    "rows": rows
                }

        except SQLAlchemyError as e:
            last_error = str(e)
            sql = fix_sql_with_llm(last_error, sql)

    raise RuntimeError(f"SQL failed after {max_attempts} attempts: {last_error}")
