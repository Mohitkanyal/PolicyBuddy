from modules.openrouter_llm import ask_openrouter

def detect_exclusions(policy_text: str) -> str:
    prompt = (
        "Review the following insurance policy text and identify any exclusions or conditions "
        "that could result in a claim being denied.\n\n"
        f"Policy:\n{policy_text[:3000].strip()}\n\n"
        "List and explain potential exclusions or risky terms in plain English."
    )

    return ask_openrouter(prompt, model="mistralai/mistral-7b-instruct")
