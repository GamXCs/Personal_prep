"""Executable axis and feature-scaling example for Lesson 19."""

import numpy as np


def analyze(names, scores):
    names = np.asarray(names)
    scores = np.asarray(scores, dtype=float)

    if scores.ndim != 2 or names.ndim != 1:
        raise ValueError("expected 1-D names and a 2-D score matrix")
    if names.shape[0] != scores.shape[0]:
        raise ValueError("each score row must have one aligned name")

    exam_means = scores.mean(axis=0)
    student_means = scores.mean(axis=1)
    spreads = scores.std(axis=0, ddof=0)
    if np.any(np.isclose(spreads, 0.0)):
        raise ValueError("every exam column must have nonzero spread")

    standardized = (scores - exam_means) / spreads
    if not np.allclose(standardized.mean(axis=0), 0.0):
        raise AssertionError("standardized column means are not zero")
    if not np.allclose(standardized.std(axis=0, ddof=0), 1.0):
        raise AssertionError("standardized column spreads are not one")

    qualifying = student_means >= 85.0
    if qualifying.shape != names.shape or qualifying.dtype != np.bool_:
        raise AssertionError("row-mask contract failed")

    best = int(np.argmax(student_means))
    return exam_means, student_means, names[qualifying], names[best]


if __name__ == "__main__":
    student_names = np.array(["Ada", "Lin", "Mira"])
    score_matrix = np.array([[80, 90], [70, 100], [90, 80]])
    results = analyze(student_names, score_matrix)
    print("matrix shape:", score_matrix.shape)
    print("exam means:", results[0], "shape:", results[0].shape)
    print("student means:", results[1], "shape:", results[1].shape)
    print("qualifying:", results[2])
    print("best:", results[3])

