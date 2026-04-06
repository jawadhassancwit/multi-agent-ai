import os
import requests
import uuid
import time

class ImageAgent:
    def __init__(self):
        self.api_url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0"

    def generate_image(self, prompt):
        headers = {
            "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {"prompt": prompt}

        response = requests.post(self.api_url, headers=headers, json=data)

        if response.status_code == 200:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            static_dir = os.path.join(base_dir, "static")

            if not os.path.exists(static_dir):
                os.makedirs(static_dir)

            filename = f"generated_{uuid.uuid4().hex}.png"
            image_path = os.path.join(static_dir, filename)

            with open(image_path, "wb") as f:
                f.write(response.content)

            print("Image saved at:", image_path)

            return f"https://web-production-7687b.up.railway.app/static/{filename}?t={int(time.time())}"
        else:
            print("Image API error:", response.text)
            return "Image generation failed"