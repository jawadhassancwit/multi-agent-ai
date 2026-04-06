import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")

print("ACCOUNT ID:", CLOUDFLARE_ACCOUNT_ID)
print("TOKEN:", CLOUDFLARE_API_TOKEN[:10])

class ImageAgent:
    def __init__(self):
        self.api_url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0"

    def generate_image(self, prompt):
        headers = {
            "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "prompt": prompt
        }

        response = requests.post(self.api_url, headers=headers, json=data)

        if response.status_code == 200:
            # Absolute path to static folder
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            image_path = os.path.join(base_dir, "static", "generated_image.png")

            with open(image_path, "wb") as f:
                f.write(response.content)

            image_url = "https://web-production-7687b.up.railway.app/static/generated_image.png"
            return image_url
        else:
            return response.text             