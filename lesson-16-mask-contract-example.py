"""Executable alignment-contract example for Lesson 16."""

import numpy as np


def select_at_or_above(names, values, threshold):
    """Return aligned identity/value arrays selected by one shared mask."""
    if names.ndim != 1 or values.ndim != 1:
        raise ValueError("names and values must be one-dimensional")
    if names.shape != values.shape:
        raise ValueError("names and values must have matching shapes")

    mask = values >= threshold
    return names[mask], values[mask], mask


def main():
    run_ids = np.array(["run-a", "run-b", "run-c", "run-d"])
    accuracies = np.array([0.81, 0.88, 0.84, 0.91])
    selected_ids, selected_values, mask = select_at_or_above(
        run_ids, accuracies, threshold=0.85
    )
    best_position = int(np.argmax(accuracies))

    print("mask:", mask)
    print("selected ids:", selected_ids)
    print("selected accuracies:", selected_values)
    print("best run:", run_ids[best_position], accuracies[best_position])


if __name__ == "__main__":
    main()
