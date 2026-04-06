import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from orchestrator.orchestrator import Orchestrator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
orchestrator = Orchestrator()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Absolute path for static folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def home():
    return {"message": "Multi-Agent AI Running"}

@app.get("/chat")
@app.post("/chat")
def chat(prompt: str):
    result = orchestrator.handle_request(prompt)
    return {"response": result}