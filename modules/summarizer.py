from modules.openrouter_llm import ask_openrouter

def generate_summary(policy_text: str) -> str:
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
