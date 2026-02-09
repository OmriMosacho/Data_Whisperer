from app.config import llm
from langchain_core.prompts import ChatPromptTemplate
from app.db.schema_loader import load_allowed_schema


# Format schema nicely for LLM
def format_schema(schema: dict) -> str:
    output = []
    for table, cols in schema.items():
        output.append(f"Table {table}:")
        for col in cols:
            output.append(f"  - {col}")
    return "\n".join(output)


prompt = ChatPromptTemplate.from_messages([
    ("system",
    #  "If asked: active combination is demand_valid = true in ds_matrix"
    #  "If asked: sales data can be found in ds_data table in final_history column"
    #  "If asked: ds_data and ds_matrix can be join using item_id and location_id"
    #  "If asked: combination counts and similar have to be distincted or groupped by item_id and location_id"
    #  "If asked: categories and all kinds of data segmentation exist in ds_matrix (emr_abc_class, emr_demantra_segment)"
    #  "If asked: the data is weekly if there is a need to sum the month's sold units, aggregate it"
     "Generate safe SELECT/S SQL query only. "
     "Never modify data. Use standard SQL."
     "Create the query ONLY on what you have been asked to search in the following question!"),
    ("human",
     """
Intent:
{intent}

Database schema:
{schema}

Write the SQL query:
""")
])

def plan_sql(intent, schema):

    allowed_schema = load_allowed_schema()
    final_schema = format_schema(allowed_schema)

    chain = prompt | llm
    return chain.invoke({
        "intent": intent,
        "schema": final_schema
    }).content.replace("```sql","").replace("```","")
