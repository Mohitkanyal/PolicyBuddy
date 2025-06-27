from modules.openrouter_llm import ask_openrouter

def verify_explanation(policy_text: str, agent_text: str) -> str:
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
