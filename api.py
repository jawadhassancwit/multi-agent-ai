from fastapi import FastAPI
from orchestrator.orchestrator import Orchestrator

app = FastAPI()
orchestrator = Orchestrator()

@app.get("/")
def home():
    return {"message": "Multi-Agent AI Running"}

@app.get("/chat")
@app.post("/chat")
def chat(prompt: str):
    result = orchestrator.handle_request(prompt)
    return {"response": result}