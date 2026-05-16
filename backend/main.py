"""AgentStorefront — App Store for AI agents.

Run: uvicorn main:app --reload
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from db import init_db
from routes import agents, sellers, services, discover, subscribe

load_dotenv()

app = FastAPI(
    title="AgentStorefront",
    description="The App Store for AI agents. Devs list services. Agents discover, subscribe, pay.",
    version="0.1.0",
)

origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {
        "service": "AgentStorefront",
        "version": "0.1.0",
        "docs": "/docs",
        "github": "https://github.com/[FIDELE_GH]/agentstorefront",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(agents.router)
app.include_router(sellers.router)
app.include_router(services.router)
app.include_router(discover.router)
app.include_router(subscribe.router)
