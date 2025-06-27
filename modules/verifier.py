from modules.openrouter_llm import ask_openrouter
from modules.utils import is_valid_policy_text

def verify_explanation(policy_text: str, agent_text: str) -> str:
    if not is_valid_policy_text(policy_text):
        return "⚠️ This document doesn't appear to be a valid insurance policy. Please upload a proper policy PDF."
    prompt = (
        "You are an insurance compliance assistant.\n\n"
        "Compare the following:\n\n"
        "Agent Explanation:\n"
        f"{agent_text.strip()}\n\n"
        "Policy Document:\n"
        f"{policy_text[:3000].strip()}\n\n"
        "Your Task:\n"
        "- Identify if the agent explanation contains any misleading claims.\n"
        "- Point out any missing or contradictory information.\n"
        "- If the explanation is accurate and complete, state that clearly.\n"
        "Keep your response short, direct, and easy to understand."
    )

    return ask_openrouter(prompt)
