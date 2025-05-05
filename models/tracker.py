def track_metrics(winner):
    with open("logs/performance.log", "a") as f:
        f.write(f"{winner}\n")
