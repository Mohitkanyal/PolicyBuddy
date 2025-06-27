from modules.openrouter_llm import ask_openrouter
from modules.utils import is_valid_policy_text

def ask_question(policy_text: str, question: str) -> str:
    if not is_valid_policy_text(policy_text):
        return "⚠️ This document doesn't appear to be a valid insurance policy. Please upload a proper policy PDF."
    prompt = (
        "You are an expert insurance assistant.\n\n"
        "The following is the content of an insurance policy:\n"
        f"{policy_text[:3000].strip()}\n\n"
        f"User's Question: {question.strip()}\n\n"
        "Please answer in a clear, friendly, and accurate manner. Avoid technical jargon unless needed."
    )

    return ask_openrouter(prompt, model="mistralai/mistral-7b-instruct")
