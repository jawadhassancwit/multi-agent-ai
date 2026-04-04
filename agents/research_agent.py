from agents.base_agent import BaseAgent
from config.settings import RESEARCH_MODEL

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Research Agent",
            prompt_file="research.txt",
            model=RESEARCH_MODEL
        )

    def research(self, task):
        return self.run(task)