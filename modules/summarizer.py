from modules.openrouter_llm import ask_openrouter
from modules.utils import is_valid_policy_text
def generate_summary(policy_text: str) -> str:
    if not is_valid_policy_text(policy_text):
        return "⚠️ This document doesn't appear to be a valid insurance policy. Please upload a proper policy PDF."
    prompt = (
        "You are an expert assistant trained to simplify insurance documents for customers.\n\n"
        "Summarize the following policy in exactly 6 bullet points. Include:\n"
        "- Policy Type\n"
        "- Key Coverage\n"
        "- Major Exclusions\n"
        "- Waiting Period\n"
        "- Sum Insured (if present)\n"
        "- Any Co-pay, Room Rent Limits, or Lock-in Info\n\n"
        f"Policy Content:\n{policy_text[:3000]}"
    )
    return ask_openrouter(prompt)
