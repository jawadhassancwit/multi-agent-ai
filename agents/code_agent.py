from agents.base_agent import BaseAgent
from config.settings import CODE_MODEL

class CodeAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Code Agent",
            prompt_file="code.txt",
            model=CODE_MODEL
        )

    def generate_code(self, task):
        return self.run(task)