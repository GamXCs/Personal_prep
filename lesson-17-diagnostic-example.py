"""Executable vectorization and diagnostic-check example for Lesson 17."""

import numpy as np


def standardized_report(labels, values):
    """Return aligned selections and verified standardized values."""
    if labels.ndim != 1 or values.ndim != 1:
        raise ValueError("labels and values must be one-dimensional")
    if labels.shape != values.shape or values.size == 0:
        raise ValueError("labels and values must be aligned and nonempty")

    mean = values.mean()
    spread = values.std(ddof=0)
    if np.isclose(spread, 0.0):
        raise ValueError("cannot standardize values with zero spread")

    standardized = (values - mean) / spread
    if not np.isclose(standardized.mean(), 0.0):
        raise AssertionError("standardized mean contract failed")
    if not np.isclose(standardized.std(ddof=0), 1.0):
        raise AssertionError("standardized spread contract failed")

    mask = values > mean
    best_position = int(np.argmax(standardized))
    return {
        "selected_labels": labels[mask],
        "selected_values": values[mask],
        "standardized": standardized,
        "best_label": labels[best_position],
        "best_value": values[best_position],
    }


def main():
    experiment_ids = np.array(["exp-a", "exp-b", "exp-c", "exp-d"])
    accuracies = np.array([0.72, 0.78, 0.75, 0.83])
    report = standardized_report(experiment_ids, accuracies)

    print("above mean:", report["selected_labels"], report["selected_values"])
    print("standardized:", np.round(report["standardized"], 3))
    print("best:", report["best_label"], report["best_value"])


if __name__ == "__main__":
    main()
