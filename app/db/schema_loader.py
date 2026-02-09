# app/db/schema_loader.py
from sqlalchemy import inspect
from app.db.connection import engine

# Existing function
def load_schema():
    inspector = inspect(engine)
    schema = {}
    for table in inspector.get_table_names():
        columns = inspector.get_columns(table)
        schema[table] = [c['name'] for c in columns]
    return schema

# Allowed tables pool
# ALLOWED_TABLES = [
#     "ds_matrix",
#     "ds_data",
#     "level",
#     "properties",
#     "audit",
#     "audit_data",
#     "maintenance_job_logs",
#     "logs",
#     "view",
#     "view_1_measure",
#     "view_2_measure",
#     "view_3_measure",
#     "view_4_measure",
#     "view_5_measure",
#     "users",
#     "sort",
#     "sort_user",
#     "users_view",
#     "calendar"
# ]


ALLOWED_TABLES = [
    "companies",
    "currency_rate",
    "customer_accounts",
    "customer_holdings",
    "customers",
    "discount_rules",
    "stock_prices",
    "trades",
    "users"
]


def load_allowed_schema():
    full_schema = load_schema()
    allowed_schema = {t: cols for t, cols in full_schema.items() if t in ALLOWED_TABLES}
    return allowed_schema
