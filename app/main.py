from fastapi import FastAPI
from app.api.ask import router as ask_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Data Whisperer",
    version="0.1.0"
)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ask_router, prefix="/ask")
