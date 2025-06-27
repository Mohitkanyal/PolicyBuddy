def is_valid_policy_text(text):
    keywords = ["policy number", "sum insured", "coverage", "claim", "exclusion", "hospitalization", "premium"]
    match_count = sum(1 for kw in keywords if kw in text.lower())
    return match_count >= 2
