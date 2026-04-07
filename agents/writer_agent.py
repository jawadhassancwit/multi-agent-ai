from agents.base_agent import BaseAgent
from config.settings import WRITER_MODEL
import re

class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Writer Agent",
            prompt_file="writer.txt",
            model=WRITER_MODEL
        )

    def write(self, task):
        print(" Writer agent executing...")

        result = self.run(task)

        print(" Writer final output:", result)

        return result        

