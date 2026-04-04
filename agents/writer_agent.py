from agents.base_agent import BaseAgent
from config.settings import WRITER_MODEL

class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Writer Agent",
            prompt_file="writer.txt",
            model=WRITER_MODEL
        )

    def write(self, task):
        return self.run(task)