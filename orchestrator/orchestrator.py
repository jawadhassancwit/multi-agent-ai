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
        self.memory.add("user", prompt)

        response = {}

        past_info = self.long_memory.search(prompt)
        if past_info:
            response["memory_search"] = past_info

        steps = self.planner.plan(prompt)

        i = 0
        while i < len(steps):
            step = steps[i]
            print("Running:", step)

            if step == "research":
                result = self.research.research(prompt)
                response["research"] = result

            elif step == "writer":
                result = self.writer.write(prompt)
                response["writer"] = result

            elif step == "code":
                result = self.code.generate_code(prompt)
                response["code"] = result

            elif step == "image":
                result = self.image.generate_image(prompt)
                response["image"] = result

            elif step == "save":
                self.file_tool.save_to_file("output.txt", str(response))
                response["tool"] = "Saved to output.txt"

            self.memory.add("assistant", str(response))
            i += 1

        return response