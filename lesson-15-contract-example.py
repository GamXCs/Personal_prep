"""Small example of separating computation from presentation."""


def summarize_runs(runs):
    if not runs:
        raise ValueError("runs cannot be empty")

    total_ms = 0
    slowest = runs[0]
    for run in runs:
        total_ms += run["latency_ms"]
        if run["latency_ms"] > slowest["latency_ms"]:
            slowest = run

    return {
        "count": len(runs),
        "mean_latency_ms": total_ms / len(runs),
        "slowest": slowest.copy(),
    }


def format_summary(summary):
    slowest = summary["slowest"]
    return (
        f"count: {summary['count']}\n"
        f"mean latency: {summary['mean_latency_ms']:.2f} ms\n"
        f"slowest: {slowest['request_id']} ({slowest['latency_ms']} ms)"
    )


if __name__ == "__main__":
    sample = [
        {"request_id": "r-101", "latency_ms": 120},
        {"request_id": "r-102", "latency_ms": 185},
        {"request_id": "r-103", "latency_ms": 95},
    ]
    print(format_summary(summarize_runs(sample)))
