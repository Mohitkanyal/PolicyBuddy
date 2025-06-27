from modules.openrouter_llm import ask_openrouter
from modules.utils import is_valid_policy_text

def detect_exclusions(policy_text: str) -> str:
    if not is_valid_policy_text(policy_text):
        return "⚠️ This document doesn't appear to be a valid insurance policy. Please upload a proper policy PDF."
    prompt = (
        "Review the following insurance policy text and identify any exclusions or conditions "
        "that could result in a claim being denied.\n\n"
        f"Policy:\n{policy_text[:3000].strip()}\n\n"
        "List and explain potential exclusions or risky terms in plain English."
    )

    return ask_openrouter(prompt, model="mistralai/mistral-7b-instruct")
