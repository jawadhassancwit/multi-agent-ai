import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from orchestrator.orchestrator import Orchestrator
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request

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

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

    if not prompt:
        return {"response": {"type": "text", "content": "No prompt provided"}}

    result = orchestrator.handle_request(prompt)

    if isinstance(result, dict) and "image" in result:
        return {
            "response": {
                "type": "image",
                "image": result["image"]
            }
        }

    return {
        "response": result
    }