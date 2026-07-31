"""Small 2-D NumPy example for Lesson 11; not the assignment solution."""

import numpy as np


def main():
    names = np.array(["Ada", "Lin", "Mira"])
    scores = np.array([
        [80.0, 90.0],
        [70.0, 100.0],
        [90.0, 80.0],
    ])

    exam_means = scores.mean(axis=0)
    student_means = scores.mean(axis=1)
    best_index = int(np.argmax(student_means))
    qualifying_mask = student_means >= 85

    print("shape:", scores.shape)
    print("exam means (axis 0):", exam_means)
    print("student means (axis 1):", student_means)
    print("best:", names[best_index], student_means[best_index])
    print("qualifying names:", names[qualifying_mask])
    print("qualifying rows:\n", scores[qualifying_mask])


if __name__ == "__main__":
    main()
