from agents.writer_agent import WriterAgent
from agents.research_agent import ResearchAgent
from agents.code_agent import CodeAgent
from agents.image_agent import ImageAgent

writer = WriterAgent()
researcher = ResearchAgent()
coder = CodeAgent()
image_agent = ImageAgent()

print("\n=== WRITER ===\n")
print(writer.write("Write a short blog about AI"))

print("\n=== RESEARCH ===\n")
print(researcher.research("Explain Machine Learning"))

print("\n=== CODE ===\n")
print(coder.generate_code("Write a Python function to calculate factorial"))

print("\n=== IMAGE ===\n")
print(image_agent.generate_image("A futuristic AI robot"))