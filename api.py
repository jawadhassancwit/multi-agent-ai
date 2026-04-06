from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from orchestrator.orchestrator import Orchestrator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
orchestrator = Orchestrator()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (images)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return {"message": "Multi-Agent AI Running"}

@app.get("/chat")
@app.post("/chat")
def chat(prompt: str):
    result = orchestrator.handle_request(prompt)
    return {"response": result}