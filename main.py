from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from orchestrator.orchestrator import Orchestrator

app = FastAPI()
orchestrator = Orchestrator()

# Serve images and static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Chat API
@app.post("/chat")
def chat(prompt: str):
    result = orchestrator.handle_request(prompt)
    return {"response": result}