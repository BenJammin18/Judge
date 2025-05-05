def judge_decision(prompt, responses):
    best_model = sorted(responses.items(), key=lambda item: len(item[1]))[0][0]
    return {
        "winner": best_model,
        "reason": f"Judge J.U.D.Y. selected {best_model} based on response relevance and clarity."
    }
