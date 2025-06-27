from modules.openrouter_llm import ask_openrouter

def simulate_claim(policy_text: str, claim_scenario: str) -> str:
    prompt = (
        "You are a helpful insurance assistant.\n\n"
        f"Here is an insurance policy document:\n{policy_text[:3000].strip()}\n\n"
        f"A user wants to make the following claim:\n\"\"\"{claim_scenario.strip()}\"\"\"\n\n"
        "Tell if the claim is likely to be ACCEPTED or REJECTED. Also provide a short reason.\n\n"
        "Respond in this format:\n- Status: Accepted / Rejected\n- Reason:"
    )

    return ask_openrouter(prompt, model="mistralai/mistral-7b-instruct")
