import time
import random

def run_juror_models(prompt, models):
    results = {}
    for model in models:
        time.sleep(random.uniform(0.2, 0.5))  # simulate latency
        results[model] = f"{model} responds: I believe the answer to '{prompt}' is nuanced and insightful."
    return results
