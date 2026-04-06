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