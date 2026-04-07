from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from orchestrator.orchestrator import Orchestrator

app = FastAPI()
orchestrator = Orchestrator()

app.mount("/static", StaticFiles(directory="static"), name="static")

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
        "response": {
            "type": "text",
            "content": str(result)
        }
    }