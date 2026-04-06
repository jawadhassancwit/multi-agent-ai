class PlannerAgent:
    def plan(self, prompt):
    prompt = prompt.lower()

    if "image" in prompt or "picture" in prompt or "draw" in prompt or "generate image" in prompt:
        return "image"

    elif "code" in prompt or "program" in prompt:
        return "code"

    elif "research" in prompt or "information" in prompt:
        return "research"

    else:
        return "write"