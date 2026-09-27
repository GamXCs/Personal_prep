"""Independent pandas example: labeled response-time analysis."""

import pandas as pd


def build_report():
    runs = pd.DataFrame(
        {
            "Request": ["r-101", "r-102", "r-103", "r-104"],
            "Service": ["search", "billing", "search", "billing"],
            "LatencyMs": [120, 185, 95, 140],
        }
    )
    runs["Slow"] = runs["LatencyMs"] >= 140
    slow_runs = runs.loc[runs["Slow"], ["Request", "Service", "LatencyMs"]]
    service_means = runs.groupby("Service")["LatencyMs"].mean()
    return runs, slow_runs, service_means


if __name__ == "__main__":
    table, selected, means = build_report()
    print("Table:")
    print(table)
    print("\nSlow requests:")
    print(selected)
    print("\nMean latency by service:")
    print(means)
