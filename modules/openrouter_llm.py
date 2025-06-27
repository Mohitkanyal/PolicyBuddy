import os
import requests
from dotenv import load_dotenv

load_dotenv()

def ask_openrouter(prompt: str, model: str = "mistralai/mistral-7b-instruct") -> str:
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return "[❌ Error] OPENROUTER_API_KEY is not set in your environment."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "PolicyBuddy+",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful insurance assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[❌ API Error] {e}"
