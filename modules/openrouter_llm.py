import streamlit as st
import requests

def ask_openrouter(prompt: str, model: str = "mistralai/mistral-7b-instruct") -> str:
    keys = st.secrets.get("OPENROUTER_KEYS", [])
    
    if not keys:
        return "[❌ Error] No OpenRouter API keys found in Streamlit secrets."

    headers_base = {
        "Referer": "https://policybuddy-cxne44tuvzb4g6fkvwpb8w.streamlit.app",
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

    for idx, key in enumerate(keys):
        headers = {
            **headers_base,
            "Authorization": f"Bearer {key}"
        }

        try:
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
            
            if response.status_code == 401:
                st.warning(f"🔁 Key {idx+1} unauthorized. Trying next...")
                continue  # Try the next key

            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip()
        
        except Exception as e:
            st.warning(f"⚠️ Key {idx+1} failed: {e}")
            continue

    return "[❌ API Error] All API keys failed or were unauthorized."
