import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

WRITER_MODEL = "qwen/qwen3-32b"
RESEARCH_MODEL = "qwen/qwen3-32b"
CODE_MODEL = "qwen/qwen3-32b"
ORCHESTRATOR_MODEL = "groq/compound-mini"

CLOUDFLARE_API_KEY = os.getenv("CLOUDFLARE_API_KEY")
CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")

GROQ_MODEL = "qwen/qwen3-32b"
CLOUDFLARE_IMAGE_MODEL = "@cf/stabilityai/stable-diffusion-xl-base-1.0"

TEMPERATURE = 0.7
MAX_TOKENS = 2000
DEBUG = True