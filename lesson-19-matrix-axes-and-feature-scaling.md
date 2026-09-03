# Lesson 19 — Matrix Axes and Feature-Wise Scaling

**Module:** Week 2 — Regression workflow and honest evaluation  
**Estimated time:** 75–90 minutes  
**Difficulty:** Introductory/intermediate NumPy

## Why this lesson is next

Your completed Lesson 10 program now has separate loading, analysis, and
presentation functions, returns a reusable report, applies an aligned mask,
standardizes without a Python arithmetic loop, rejects zero spread, and uses
`argmax` to recover `Emma 98`. That is enough evidence to advance from one
numeric variable to a matrix of variables.

The remaining Lesson 10 diagnostic ideas are not discarded. In this lesson,
shape, Boolean-mask, and `np.isclose` checks become required contracts for a
2-D matrix, where choosing the wrong axis can silently change the meaning of a
calculation.

## Learning objectives and prerequisites

By the end, you should be able to:

1. interpret rows, columns, shape, and axes in a 2-D NumPy array;
2. predict the output shape of an axis-wise reduction;
3. compute per-column and per-row summaries with the correct axis;
4. standardize feature columns and verify the result with `np.isclose`;
5. preserve identity while filtering rows and selecting a maximum; and
6. explain the time and memory costs of a matrix pipeline.

Prerequisites: Lesson 10's aligned 1-D arrays, Boolean masks, population
standard deviation, vectorized standardization, functions, and `argmax`.

## Retrieval warm-up

Before running code, answer these from memory:

1. Why must a mask have the same length as the array it indexes?
2. What does `argmax` return: a value or a position?
3. Why is `np.isclose(x, 0.0)` usually preferable to `x == 0.0` for a
   calculated floating-point result?
4. If five students each have two exam scores, what should the matrix shape be?

## Python instruction and executable example

Run:

```bash
python3 lesson-19-axis-contract-example.py
```

The central rule is: **the named axis is the one that disappears**.

For a score matrix with shape `(3, 2)`:

```python
exam_means = scores.mean(axis=0)     # shape (2,): one result per column
student_means = scores.mean(axis=1)  # shape (3,): one result per row
```

Column standardization uses one mean and one spread per feature:

```python
means = scores.mean(axis=0)
spreads = scores.std(axis=0, ddof=0)
standardized = (scores - means) / spreads
```

NumPy broadcasts the two-element vectors across all rows. Predict every shape
before printing it; shape reasoning is part of correctness, not merely
debugging.

## Mathematics: a worked axis derivation

Let a data matrix have `n` rows (observations) and `d` columns (features). The
entry in row `i`, column `j` is `x[i, j]`.

The mean of feature `j` is the sum down that column divided by the number of
rows:

```text
feature_mean[j] = (x[0,j] + x[1,j] + ... + x[n-1,j]) / n
```

For this matrix:

```text
80  90
70 100
90  80
```

the first column mean is `(80 + 70 + 90) / 3 = 80`, and the second is
`(90 + 100 + 80) / 3 = 90`. Therefore `mean(axis=0)` returns `[80, 90]`.

Now standardize the first entry in each column. The population spread of both
columns is approximately `8.165`:

```text
first standardized row = [(80 - 80)/8.165, (90 - 90)/8.165] = [0, 0]
```

Subtracting the column means centers each feature at zero. Dividing each
column by its own nonzero population spread makes each column's population
standard deviation one. That predicts these executable checks:

```python
np.allclose(standardized.mean(axis=0), 0.0)
np.allclose(standardized.std(axis=0, ddof=0), 1.0)
```

## Machine-learning theory connection

In a conventional design matrix, rows are samples and columns are features.
Feature scaling therefore operates down the rows, separately for each column.
Using `axis=1` would give every sample its own center and spread, mixing feature
meanings and changing model behavior.

This matters for distance-based models and gradient optimization: large-scale
features can dominate distance, while uneven scales can make optimization
poorly conditioned. In honest evaluation, fit column means and spreads on the
training set, then reuse them on validation and test rows. Recomputing them on
held-out data leaks information and changes the coordinate system.

## Algorithms and data structures: scanning an `n` by `d` matrix

A dense NumPy matrix stores `n*d` values, so its space cost is `O(nd)`.
Computing column means, column spreads, standardization, or a full Boolean mask
must inspect the matrix and takes `O(nd)` time. A fixed sequence of these full
passes remains `O(nd)`.

Computing `argmax` over the `n` student means takes `O(n)` time. Sorting those
means only to find the largest would take `O(n log n)` and is unnecessary.
Vectorization reduces Python interpreter overhead but does not change these
growth rates.

## Technical reading

Read NumPy's official sections on
[array axes and attributes](https://numpy.org/doc/stable/user/absolute_beginners.html#what-are-the-attributes-of-an-array)
and
[aggregation](https://numpy.org/doc/stable/user/absolute_beginners.html#more-useful-array-operations).

Guiding questions:

1. For shape `(5, 2)`, what does each dimension count?
2. What shapes result from `mean(axis=0)` and `mean(axis=1)`?
3. Why does an axis choice change meaning rather than just display format?
4. When might `keepdims=True` simplify later broadcasting?

## Integrated coding exercise: exam matrix pipeline

Create `lesson_11_exam_matrix.py` using the supplied `exams.csv`. Reuse the
architecture that worked in Lesson 10: loading, analysis, and presentation
must be separate responsibilities.

Your program must:

1. validate required columns `Name`, `Exam1`, and `Exam2`, nonempty data,
   nonblank names, integer scores, scores in `0..100`, and row widths;
2. include the physical row and rejected value in conversion errors;
3. build a 1-D names array and a 2-D score matrix with students as rows;
4. explicitly check `names.shape[0] == scores.shape[0]` and
   `scores.ndim == 2`;
5. report the score-matrix shape, dimensions, and dtype;
6. calculate exam means with `axis=0` and student means with `axis=1`;
7. use `argmax`, without sorting, to report the top student and mean;
8. create one Boolean row mask for student means at least 85, verify its dtype
   and shape, and apply it to both names and score rows;
9. column-standardize the matrix without a Python arithmetic loop, rejecting
   any zero-spread column;
10. verify standardized column means near zero and population spreads near one
    with `np.allclose`; and
11. return a structured report from analysis and print only in presentation.

### Acceptance criteria

- `python3 lesson_11_exam_matrix.py` succeeds on `exams.csv`.
- Key results are shape `(5, 2)`, exam means `[85.4, 88.0]`, student means
  `[89.5, 73.5, 97.0, 82.5, 91.0]`, top student `Sarah 97.0`, and qualifying
  names `Alice, Sarah, Emma`.
- Axis 0 produces two values; axis 1 produces five.
- The same verified row mask filters aligned names and matrix rows.
- Both standardized-column diagnostics pass.
- `lesson-11-reflection.md` records one valid and one malformed-input run.

### Optional stretch goals

- Add a third exam column without changing the aggregation logic.
- Report the best student on each exam with `argmax(axis=0)`.
- Separate `fit_scaler(training_scores)` from `apply_scaler(scores, params)`.
- Use `keepdims=True` and explain how it changes shapes but not values.

## Retrieval-practice quiz

1. What does shape `(5, 2)` mean in this program?
2. Which axis produces one mean per exam, and why?
3. Which axis produces one mean per student?
4. What shapes should the feature means and standardized matrix have?
5. Why must the same row mask index both names and scores?
6. Why are validation-set means unsuitable for fitting its scaler?
7. What are the time costs of standardizing an `n` by `d` matrix and sorting
   `n` student means?

## Quiz answers

1. Five student rows and two exam-feature columns.
2. `axis=0`; the row axis disappears, leaving one value per column.
3. `axis=1`.
4. `(2,)` and `(5, 2)` for the supplied data.
5. Each retained identity must remain paired with its original score row.
6. Held-out observations would influence preprocessing and leak information.
7. `O(nd)` and `O(n log n)`, respectively.

## Suggested 75–90 minute study plan

- 0–8 minutes: retrieval warm-up; predict all example shapes.
- 8–18 minutes: run and modify the executable example.
- 18–30 minutes: work the two column means and one standardized row by hand.
- 30–38 minutes: complete the reading and guiding questions.
- 38–70 minutes: implement loading, analysis, and presentation checkpoints.
- 70–80 minutes: run valid and malformed fixtures; inspect contracts.
- 80–90 minutes: answer the quiz and save `lesson-11-reflection.md`.

