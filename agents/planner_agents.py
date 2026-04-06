class PlannerAgent:
    def plan(self, prompt):
        prompt = prompt.lower()
        steps = []

        if any(word in prompt for word in ["research", "explain", "what is", "history", "war"]):
            steps.append("research")
            steps.append("writer")   # 🔥 automatic writer after research

        elif any(word in prompt for word in ["write", "blog", "article"]):
            steps.append("writer")

        if any(word in prompt for word in ["code", "python", "program"]):
            steps.append("code")

        if any(word in prompt for word in ["image", "draw", "picture", "generate"]):
            steps.append("image")

        if "save" in prompt:
            steps.append("save")

        return steps

        print("Planner Steps:", steps)