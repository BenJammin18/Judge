import json
from datetime import datetime

def save_verdict(prompt, responses, winner, reason=None, mode="judy"):
    verdict = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "responses": responses,
        "winner": winner,
        "reason": reason,
        "mode": mode
    }
    with open("logs/verdicts.jsonl", "a") as f:
        f.write(json.dumps(verdict) + "\n")
