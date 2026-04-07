from memory.long_memory import LongMemory
from memory.vector_store import VectorStore
from memory.short_memory import ShortMemory
from agents.writer_agent import WriterAgent
from agents.research_agent import ResearchAgent
from agents.code_agent import CodeAgent
from agents.image_agent import ImageAgent
from agents.planner_agents import PlannerAgent
from tools.file_tool import FileTool


class Orchestrator:
    def __init__(self):
        self.writer = WriterAgent()
        self.research = ResearchAgent()
        self.code = CodeAgent()
        self.image = ImageAgent()
        self.planner = PlannerAgent()
        self.memory = ShortMemory()
        self.file_tool = FileTool()
        self.vector_store = VectorStore()
        self.long_memory = LongMemory(self.vector_store)

    def handle_request(self, prompt):
        print("\n New Request:", prompt)

        self.memory.add("user", prompt)

        response = {}

        #  Long memory search
        past_info = self.long_memory.search(prompt)
        if past_info:
            print(" Memory found")
            response["memory_search"] = past_info

        #  Planning
        steps = self.planner.plan(prompt)

        # Ensure list
        if isinstance(steps, str):
            steps = [steps]

        print(" Planned Steps:", steps)

        #  Execute steps
        for step in steps:
            print(" Running step:", step)

            if step == "research":
                result = self.research.research(prompt)
                print(" Research Result:", result)
                response["research"] = result

            elif step == "write" or step == "writer":
                research_text = response.get("research") or prompt
                result = self.writer.write(research_text)
                print(" Writer Result:", result)
                response["write"] = result

            elif step == "code":
                result = self.code.generate_code(prompt)
                print(" Code Result:", result)
                response["code"] = result

            elif step == "image":
                result = self.image.generate_image(prompt)
                print(" Image Result:", result)
                response["image"] = result

            elif step == "save":
                self.file_tool.save_to_file("output.txt", str(response))
                response["tool"] = "Saved to output.txt"

        #  Save last output to memory
        if response:
            last_value = list(response.values())[-1]
            self.memory.add("assistant", str(last_value))

        #  FINAL RETURN (ROBUST FIX)
        if not response:
            return {"type": "text", "content": "No response generated"}

        last_key = list(response.keys())[-1]
        last_value = response[last_key]

        print(f"FINAL OUTPUT: {last_key} => {last_value}")

        # If image → return dict
        if last_key == "image":
            return {
                "type":"image",
                "image":last_value
            }

        # Otherwise return text
        return {
            "type":"text",
            "content": last_value
        }