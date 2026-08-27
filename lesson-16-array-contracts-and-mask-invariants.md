# Lesson 16 — Array Contracts and Mask Invariants

**Module:** Week 2 — From core Python pipelines to NumPy  
**Estimated time:** 75–90 minutes  
**Difficulty:** Introductory NumPy, intermediate program design

## Why this is the next lesson

The whole-record minimum scan from Lesson 10 is complete, but the main NumPy
program and reflection have not been submitted. This lesson therefore does not
advance to 2-D arrays or Pandas. It gives you a narrower implementation method
for the same `lesson_10_numpy_scores.py` deliverable: establish array contracts,
then add one verified transformation at a time.

## Learning objectives and prerequisites

By the end, you should be able to:

1. state and check a contract for two aligned one-dimensional arrays;
2. build one Boolean mask and apply it to every aligned array;
3. use `argmax` to recover the identity attached to an extreme value;
4. standardize a nonconstant array and verify its output invariants;
5. distinguish correctness checks from presentation code; and
6. analyze the time and auxiliary-space cost of masking and `argmax`.

Prerequisites: CSV parsing, functions, NumPy array creation, mean, population
standard deviation, and the Lesson 10 minimum-record scan.

## Retrieval warm-up

Without running code, answer:

1. If `names[i]` identifies `scores[i]`, what must remain true after filtering?
2. Does `np.argmax(scores)` return a score or a position?
3. Why should a zero standard deviation be rejected before division?

## Python instruction and executable example

Run `python3 lesson-16-mask-contract-example.py`.

The example checks an explicit boundary contract before doing array work:

```python
if names.ndim != 1 or values.ndim != 1:
    raise ValueError("names and values must be one-dimensional")
if names.shape != values.shape:
    raise ValueError("names and values must have matching shapes")
```

Then a single mask is created from the numeric array and reused:

```python
mask = values >= threshold
selected_names = names[mask]
selected_values = values[mask]
```

This is the core invariant: position `i` in both arrays refers to the same
observation. Never construct two independent filters and assume their outputs
will still line up.

Use incremental checkpoints: parse and validate ordinary Python records;
create the arrays and check their shapes; inspect the mask; apply it to both
arrays; standardize and verify its output; use `argmax` to recover identity;
and format output only after calculations are correct.

## Mathematics: invariants of standardization

Definition: a standardized value is the original value minus the mean, divided
by the population standard deviation.

```text
z = (x - mean) / population_standard_deviation
```

Worked check for `[2, 4, 6]`: the mean is `4`. The centered values are
`[-2, 0, 2]`; their sum is `0`, so their mean is `0`. Dividing every centered
value by the same nonzero standard deviation keeps the mean at `0`. The
population variance is divided by the original variance, giving `1`, so the
population standard deviation becomes `1`.

Intuition: centering changes the origin; scaling changes the unit. Neither
operation changes ordering when the divisor is positive. If the original
spread is zero, the new unit does not exist, so reject the operation.

For more detail, read Penn State STAT 200,
[Section 2.2.8 — z-scores](https://online.stat.psu.edu/stat200/lesson/2/2.2/2.2.8).

## Machine-learning connection

Feature preprocessing is a learned contract. Training data supplies the mean
and standard deviation; validation and test data must reuse them. Recomputing
them on test data leaks information into evaluation. Shape and alignment checks
matter for the same reason: a valid feature attached to the wrong identity or
label silently corrupts training.

K-nearest neighbors and k-means can be dominated by large-unit features.
Gradient-based optimization can be slower on badly mismatched scales. Trees
are usually less sensitive because they use ordered thresholds one feature at
a time.

## Algorithms and data structures: indexed extreme selection

`np.argmax(values)` scans all `n` values and returns the position of the first
maximum. Using that position to index both `names` and `values` preserves the
complete observation without sorting.

Correctness: after scanning position `i`, the stored position denotes the
largest value seen in `0..i`. Updating it only for a larger value preserves
that invariant. At the end it denotes a global maximum.

- `argmax`: `O(n)` time and `O(1)` auxiliary space.
- Boolean filtering: `O(n)` time and `O(n)` space for mask and results.
- Sorting: typically `O(n log n)` time and unnecessary for one extreme.

## Technical reading

Read NumPy's official documentation on
[Boolean array indexing](https://numpy.org/doc/stable/user/basics.indexing.html#boolean-array-indexing)
and [`numpy.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html).

Guiding questions:

1. What shape must a one-dimensional Boolean mask have here?
2. Does advanced Boolean indexing return a view or a copy?
3. What does `argmax` return when the maximum occurs more than once?
4. Why is one shared position safer than independent searches?

## Integrated coding exercise: finish the Lesson 10 analyzer

Continue the original deliverable: create `lesson_10_numpy_scores.py` from the
Lesson 10 behavioral specification. Do not create a second analyzer and do not
use a supplied starter or supplied tests.

1. Load `scores.csv` once. Reject missing columns, empty data, blank names,
   non-integer scores, and scores outside `0..100`. Include physical row number
   and bad value in row-specific errors.
2. Convert names and scores to separate 1-D arrays and reject shape mismatch.
3. Print `shape`, `size`, `ndim`, and `dtype` for scores.
4. Compute mean and population standard deviation with NumPy.
5. Create exactly one above-mean mask and apply it to both arrays.
6. Reject zero spread, then standardize without looping over the array.
7. Use `argmax` on standardized values and its position to print the matching
   name and raw score.
8. Keep loading, analysis, and presentation in at least three meaningful
   functions. Print only at the main/presentation boundary.

### Acceptance criteria

- `python3 lesson_10_numpy_scores.py` succeeds on a restored valid CSV.
- `names.ndim == scores.ndim == 1` and `names.shape == scores.shape`.
- The mask has Boolean dtype and the same shape as its source arrays.
- Above-mean names and scores remain paired and in input order.
- Standardized mean is approximately `0`; population standard deviation is
  approximately `1`.
- A constant-score file raises a deliberate zero-spread error.
- A malformed row reports its physical row number and offending value.
- No sorting or element-by-element transformation loop is used.

### Optional stretch goals

- Make the CSV path a command-line argument.
- Define and demonstrate a tie policy.
- Return a report dictionary reusable by a future model pipeline.

## Retrieval-practice quiz

1. State the alignment invariant for `names` and `scores`.
2. What type of array does `scores > scores.mean()` produce?
3. What value does `argmax` return?
4. What two properties should standardized training values have?
5. Why is a constant array invalid for standardization?
6. What are the time and space costs of Boolean filtering?
7. Why should test data not supply preprocessing statistics?

## Quiz answers

1. At every valid position `i`, `names[i]` identifies `scores[i]`.
2. A Boolean array with the same shape as `scores`.
3. The position of the first maximum value.
4. Mean approximately `0` and population standard deviation approximately `1`.
5. Its standard deviation is zero, so the formula divides by zero.
6. `O(n)` time and `O(n)` additional space.
7. That leaks evaluation information and makes performance estimates less
   honest.

## Suggested 75–90 minute study plan

- 0–8 minutes: retrieval warm-up and Lesson 10 specification review.
- 8–18 minutes: run and modify the executable example.
- 18–28 minutes: read the NumPy documentation.
- 28–38 minutes: sketch loading, analysis, and presentation boundaries.
- 38–68 minutes: implement checkpoint by checkpoint.
- 68–80 minutes: run valid, malformed, and constant-score cases.
- 80–90 minutes: complete the quiz and reflection.

## Submission checklist

Save `lesson_10_numpy_scores.py`, a valid terminal run, and
`lesson-10-reflection.md` containing one malformed run, one zero-spread run,
answers to the reading questions, quiz attempts, and a workload rating.

