import os
from groq import Groq
from config.settings import GROQ_API_KEY
import re

class BaseAgent:
    def __init__(self, name, prompt_file, model):
        self.name = name
        self.model = model

        self.client = Groq(api_key=GROQ_API_KEY)

        # Load prompt
        prompt_path = os.path.join("prompts", prompt_file)
        with open(prompt_path, "r") as file:
            self.prompt = file.read()

    def run(self, task):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.prompt},
                    {"role": "user", "content": task}
                ]
            )

            output = response.choices[0].message.content

            # Remove thinking
            cleaned_output = re.sub(r"<think>.*?</think>", "", output, flags=re.DOTALL)

# REMOVE markdown blocks
            cleaned_output = re.sub(r"```[a-zA-Z]*", "", cleaned_output)
            cleaned_output = cleaned_output.replace("```", "")

            return cleaned_output.strip()

        except Exception as e:
            return f"Error in {self.name}: {str(e)}"