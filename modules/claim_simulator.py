from modules.openrouter_llm import ask_openrouter
from modules.utils import is_valid_policy_text

def simulate_claim(policy_text: str, claim_scenario: str) -> str:
    if not is_valid_policy_text(policy_text):
        return "⚠️ This document doesn't appear to be a valid insurance policy. Please upload a proper policy PDF."
    prompt = (
        "You are a helpful insurance assistant.\n\n"
        f"Here is an insurance policy document:\n{policy_text[:3000].strip()}\n\n"
        f"A user wants to make the following claim:\n\"\"\"{claim_scenario.strip()}\"\"\"\n\n"
        "Tell if the claim is likely to be ACCEPTED or REJECTED. Also provide a short reason.\n\n"
        "Respond in this format:\n- Status: Accepted / Rejected\n- Reason:"
    )

    return ask_openrouter(prompt, model="mistralai/mistral-7b-instruct")
