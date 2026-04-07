from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from orchestrator.orchestrator import Orchestrator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
orchestrator = Orchestrator()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve images and static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Chat API
@app.post("/chat")
def chat(prompt: str):
    result = orchestrator.handle_request(prompt)

    # If agent returned image
    if isinstance(result, dict) and "image" in result:
        return {
            "response": {
                "type": "image",
                "image": result["image"]
            }
        }

    # Otherwise text response
    return {
        "response": {
            "type": "text",
            "content": str(result)
        }
    }