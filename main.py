from fastapi import FastAPI, Request

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

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