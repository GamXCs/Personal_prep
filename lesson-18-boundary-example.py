import numpy as np


def summarize(labels, values):
    labels = np.asarray(labels)
    values = np.asarray(values, dtype=float)
    if labels.ndim != 1 or values.ndim != 1 or labels.shape != values.shape:
        raise ValueError("labels and values must be aligned 1-D arrays")
    if values.size == 0:
        raise ValueError("values cannot be empty")

    mean = values.mean()
    spread = values.std(ddof=0)
    if np.isclose(spread, 0.0):
        raise ValueError("values must not be constant")

    mask = values > mean
    if mask.shape != values.shape or not np.issubdtype(mask.dtype, np.bool_):
        raise AssertionError("mask contract failed")

    standardized = (values - mean) / spread
    if not np.isclose(standardized.mean(), 0.0):
        raise AssertionError("standardized mean contract failed")
    if not np.isclose(standardized.std(ddof=0), 1.0):
        raise AssertionError("standardized spread contract failed")

    largest_index = int(np.argmax(standardized))
    return {
        "mean": float(mean),
        "above_mean_labels": labels[mask],
        "largest_label": str(labels[largest_index]),
        "largest_value": float(values[largest_index]),
    }


def format_report(report):
    above = ", ".join(str(label) for label in report["above_mean_labels"])
    return (
        f"Mean: {report['mean']:.2f}\n"
        f"Above mean: {above}\n"
        f"Largest: {report['largest_label']} ({report['largest_value']:.1f})"
    )


if __name__ == "__main__":
    experiment_ids = np.array(["run-a", "run-b", "run-c", "run-d"])
    validation_scores = np.array([72.0, 81.0, 78.0, 89.0])
    print(format_report(summarize(experiment_ids, validation_scores)))
