import os
from groq import Groq
from config.settings import GROQ_API_KEY
import re

class BaseAgent:
    def __init__(self, name, prompt_file, model):
        self.name = name
        self.model = model

        self.client = Groq(api_key=GROQ_API_KEY)

        # Load prompt file
        prompt_path = os.path.join("prompts", prompt_file)
        with open(prompt_path, "r") as file:
            self.prompt = file.read()

    def clean_text(self, text):
        if not isinstance(text, str):
            return text

        # Remove <think> blocks
        text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)

        # Remove markdown blocks
        text = re.sub(r"```[a-zA-Z]*\n?", "", text)
        text = text.replace("```", "")

        # Remove ALL HTML tags
        text = re.sub(r"<[^>]+>", "", text)

        return text.strip()

    def run(self, task):
        try:
            print(f" {self.name} running...")

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.prompt},
                    {"role": "user", "content": task}
                ]
            )

            output = response.choices[0].message.content

            print(f" RAW OUTPUT ({self.name}):", output)

            cleaned_output = self.clean_text(output)

            print(f" CLEAN OUTPUT ({self.name}):", cleaned_output)

            return cleaned_output

        except Exception as e:
            error_msg = f" Error in {self.name}: {str(e)}"
            print(error_msg)
            return error_msg
