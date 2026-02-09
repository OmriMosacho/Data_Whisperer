import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

load_dotenv()

CHAT_GPT_API_KEY = os.getenv("CHAT_GPT_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=CHAT_GPT_API_KEY
)

memory = ConversationBufferMemory(
    memory_key="history",
    return_messages=True
)
