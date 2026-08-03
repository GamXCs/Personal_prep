# Lesson 12 — From a Working Array Script to a Reliable Data Function

**Module:** Week 3 — Reliable NumPy data pipelines  
**Estimated time:** 75–90 minutes  
**Difficulty:** Introductory/intermediate

## Why this lesson is next

Your exam script already loads a `(5, 2)` array, preserves name alignment, and
computes correct per-exam summaries. That is real progress. Two current failure
modes identify the next useful step: `lesson_8_csv_code.py` tries to parse the
decimal value `3.5` with `int`, and `lesson_3_numpy_intro.py` contains a stray
`-` that prevents compilation. The exam script also keeps all work at module
level and has not yet used `axis`, `argmax`, or explicit validation.

This lesson does not introduce Pandas. It turns the NumPy work you already have
into a small, reliable pipeline with clear function boundaries.

## Learning objectives and prerequisites

By the end, you should be able to:

1. separate loading, validation, computation, and presentation;
2. choose `int` versus `float` from a data contract rather than by guesswork;
3. use `mean(axis=0)`, `mean(axis=1)`, and `argmax` correctly;
4. validate shape and alignment before computing;
5. standardize each feature column and verify the result;
6. explain the time and space costs of a single-pass validation scan.

Prerequisites: CSV iteration, functions, exceptions, 2-D NumPy arrays, Boolean
masks, arithmetic mean, and population standard deviation.

## Python instruction and executable example

Run:

```bash
python3 lesson-12-reliable-array-example.py
```

The example demonstrates a useful boundary: a computation function accepts
already numeric arrays and either returns a result or raises a clear error. It
does not open a file or print. The `main` function coordinates the program.

Notice these parsing contracts:

```python
hours = float(text)       # accepts "3.5"
exam_score = int(text)    # appropriate only if whole numbers are required
```

Conversion success is not enough. After conversion, validate the permitted
range and reject non-finite floating-point values with `np.isfinite`.

## Mathematics: column standardization

For matrix \(X\in\mathbb{R}^{n\times d}\), define the mean and population
standard deviation of column \(j\) by

\[
\mu_j=\frac{1}{n}\sum_{i=1}^n x_{ij},\qquad
\sigma_j=\sqrt{\frac{1}{n}\sum_{i=1}^n(x_{ij}-\mu_j)^2}.
\]

The standardized entry is \(z_{ij}=(x_{ij}-\mu_j)/\sigma_j\). Its column mean
is

\[
\frac{1}{n}\sum_i z_{ij}
=\frac{1}{n\sigma_j}\sum_i(x_{ij}-\mu_j)
=\frac{n\mu_j-n\mu_j}{n\sigma_j}=0.
\]

Also,

\[
\frac{1}{n}\sum_i z_{ij}^2
=\frac{1}{n\sigma_j^2}\sum_i(x_{ij}-\mu_j)^2=1,
\]

so its population standard deviation is 1. This derivation assumes
\(\sigma_j>0\); a constant column must be rejected or handled by an explicit
policy.

Intuition: centering moves each feature's balance point to zero; dividing by
its spread expresses values in comparable “standard deviation” units.

## Machine-learning connection

An ML design matrix conventionally stores observations in rows and features in
columns. Column standardization prevents a large-unit feature from dominating
distance calculations or gradient updates merely because of its units.

The pipeline boundary matters too. If malformed rows silently shift or drop
values, features can become paired with the wrong target. If means and standard
deviations are later computed using test data, evaluation leaks information.
For this exercise use the whole educational dataset; in a fitted workflow,
learn preprocessing statistics from the training split only.

## Algorithms and data structures: validation scan

A validator can scan \(n\) rows with \(d\) numeric fields per row. It checks
each field once, so its time complexity is \(O(nd)\). If it validates an
already-built array in place, its auxiliary space is \(O(1)\). Building the
array itself stores \(nd\) values and therefore uses \(O(nd)\) space.

**Loop invariant:** after validating the first \(k\) rows, every accepted row
among those \(k\) has the required width, numeric types, and ranges. Checking
row \(k+1\) either preserves the invariant or raises an error. At termination,
all rows satisfy the contract.

`argmax` similarly scans an unsorted length-\(n\) vector in \(O(n)\) time.
Sorting would cost \(O(n\log n)\) and is unnecessary for one maximum.

## Technical reading

Read NumPy's accessible introductions to
[array aggregation](https://numpy.org/doc/stable/user/absolute_beginners.html#more-useful-array-operations)
and [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html).

Guiding questions:

1. In a shape `(5, 2)` matrix, which axis disappears under `mean(axis=0)`?
2. Why can vectors of shape `(2,)` be subtracted from a `(5, 2)` matrix?
3. What output does `argmax` return: a value or a position?
4. Which shape mismatch should your validator reject before NumPy computes?

## Integrated coding exercise: reliable exam analyzer

Refactor your existing `lesson_4_numpy_asgn.py`; do not rename it and do not
discard working code. You choose the function names and architecture.

Required behavior:

1. Remove the stray `-` from `lesson_3_numpy_intro.py`, then confirm both files
   compile.
2. Divide the exam analyzer into at least three meaningful functions covering
   loading/validation, computation, and presentation.
3. Require exactly `Name,Exam1,Exam2`; reject malformed widths, blank names,
   empty data, non-integers, and scores outside 0–100 with clear errors.
4. Return aligned name and score arrays, with scores shaped `(n, 2)`.
5. Use `mean(axis=0)` for exam means and `mean(axis=1)` for student means.
6. Use `argmax` on student means to recover the top student's name and score.
7. Use one shared row mask to select names and rows with mean at least 85.
8. Standardize columns without looping over matrix entries; reject a
   zero-standard-deviation column.
9. Keep printing behind `if __name__ == "__main__":`.
10. Save a brief `lesson-12-reflection.md` containing one successful run, one
    deliberate malformed-input error, and answers to the reading questions.

Acceptance criteria:

- `python3 -m py_compile lesson_3_numpy_intro.py lesson_4_numpy_asgn.py` passes.
- `python3 lesson_4_numpy_asgn.py` reports exam means `[85.4 88. ]`, student
  means `[89.5 73.5 97.  82.5 91. ]`, and top student `Sarah` with `97.0`.
- The at-least-85 selection contains Alice, Sarah, and Emma, with aligned rows.
- Standardized column means are near 0 and population standard deviations near
  1, checked with `np.allclose`.
- A malformed file causes a clear error rather than a partial report.
- Loading/computation functions return data and do not print.

Optional stretch goals:

- Generalize validation and standardization to any positive number of exam
  columns.
- Add one small `unittest` for a valid matrix and one for a constant column.
- Repair `lesson_8_csv_code.py` by giving each field an explicit type contract;
  `Hours` must accept decimals such as `3.5`.

## Retrieval-practice quiz

1. What does `scores.mean(axis=1)` return for a `(5, 2)` matrix?
2. Why is `float("3.5")` valid while `int("3.5")` fails?
3. What condition makes z-score standardization undefined?
4. Why use `argmax` rather than sorting to find one top student?
5. Why should computation functions normally return rather than print results?

## Quiz answers

1. Five values: one mean per row/student.
2. `3.5` is a valid floating-point literal but not an integer literal.
3. A standard deviation of zero, caused by a constant column.
4. `argmax` preserves the index in `O(n)` time; sorting costs `O(n log n)`.
5. Returned values can be tested and reused independently of presentation.

## Suggested 80-minute study plan

- **0–8 min:** retrieval warm-up and predict the current failure points.
- **8–20 min:** run the example and read its function contracts.
- **20–32 min:** work the standardization derivation and axis shapes by hand.
- **32–62 min:** refactor the analyzer and implement axis/`argmax` operations.
- **62–72 min:** add validation and deliberately trigger one failure.
- **72–80 min:** run acceptance checks and write the reflection.

