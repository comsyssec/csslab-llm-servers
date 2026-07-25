import requests
from app.config import MODEL_SERVERS

def chat(model, prompt):
    info = MODEL_SERVERS[model]
    payload = {
            "model": info["model"],
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        }

    r = requests.post(
            info["url"]+"/api/chat",
            json=payload,
            timeout=300
        )

    r.raise_for_status()

    return r.json()["message"]["content"]
