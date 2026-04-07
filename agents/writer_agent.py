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

    def clean_text(self, text):
        text = re.sub(r'#+', '', text)        # remove ###
        text = re.sub(r'\*+', '', text)       # remove ***
        text = re.sub(r'-{2,}', '', text)     # remove ---
        text = re.sub(r'\n\s*\n', '\n', text) # remove extra lines
        return text.strip()

    def write(self, task):
        result = self.run(task)
        result = self.clean_text(result)
        return result     

    def write(self, task):
        print("🔥 Writer agent running...")
        result = self.run(task)
        print("writer result:",result)
        result = self.clean_text(result)
        return result         

