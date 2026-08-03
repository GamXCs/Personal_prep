"""Small executable example for Lesson 12."""

from __future__ import annotations

import numpy as np


def summarize(scores: np.ndarray) -> dict[str, np.ndarray | int]:
    if scores.ndim != 2 or scores.shape[0] == 0:
        raise ValueError("scores must be a non-empty 2-D array")
    if not np.isfinite(scores).all():
        raise ValueError("scores must contain only finite numbers")

    column_means = scores.mean(axis=0)
    row_means = scores.mean(axis=1)
    return {
        "column_means": column_means,
        "row_means": row_means,
        "best_row": int(np.argmax(row_means)),
    }


def standardize_columns(scores: np.ndarray) -> np.ndarray:
    means = scores.mean(axis=0)
    standard_deviations = scores.std(axis=0)
    if np.any(standard_deviations == 0):
        raise ValueError("cannot standardize a constant column")
    return (scores - means) / standard_deviations


def main() -> None:
    names = np.array(["Ari", "Bo", "Cy"])
    scores = np.array([[80, 90], [70, 100], [90, 80]], dtype=float)
    if len(names) != scores.shape[0]:
        raise ValueError("names and score rows must stay aligned")

    summary = summarize(scores)
    standardized = standardize_columns(scores)
    best_row = summary["best_row"]

    print("Column means:", summary["column_means"])
    print("Row means:", summary["row_means"])
    print("Top row:", names[best_row], summary["row_means"][best_row])
    print("Standardized means:", standardized.mean(axis=0))
    print("Standardized stds:", standardized.std(axis=0))


if __name__ == "__main__":
    main()
