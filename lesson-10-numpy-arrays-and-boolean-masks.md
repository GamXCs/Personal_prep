# Lesson 10 — NumPy Arrays and Boolean Masks

**Module:** Week 2 — From core Python data pipelines to NumPy  
**Estimated time:** 75–90 minutes  
**Difficulty:** Introductory NumPy, intermediate Python

## Why this is the next lesson

Your updated `lesson_2_csv.py` now reads the file once and computes several
statistics, and `lesson_3_numpy_intro.py` correctly creates an array and checks
that `temperatures.mean()` agrees with a manual mean. That is enough evidence
to introduce one new layer: NumPy array operations.

Lesson 9's structured pipeline submission and malformed-input handling are
still incomplete. This lesson does not pretend those skills are mastered. It
reuses CSV loading, but concentrates on what changes after numeric values enter
an array.

## Learning objectives

By the end of this lesson, you should be able to:

1. create a one-dimensional numeric `ndarray` and inspect its `shape`, `size`,
   `ndim`, and `dtype`;
2. distinguish elementwise array arithmetic from Python list behavior;
3. construct and apply a Boolean mask without breaking name/value alignment;
4. standardize values with a mean and standard deviation;
5. explain how feature scale affects distance-based and gradient-based models;
6. compare a vectorized scan with a Python loop using asymptotic complexity.

## Prerequisites

- Python lists, loops, functions, and comparisons
- reading and converting CSV values
- mean and population standard deviation
- maintaining alignment between names and scores

## Retrieval warm-up

Before running any code, answer:

1. Why is `score = int(row[1])` necessary after reading a CSV?
2. What state is sufficient to find a maximum in one pass?
3. What problem occurs if names are filtered separately from scores?

## Python instruction and executable example

Run:

```bash
python3 lesson-10-array-example.py
```

The central difference is that NumPy operations act element by element:

```python
temperatures = np.array([72.0, 74.0, 71.0])
fahrenheit_offset = temperatures + 2
```

The result is `[74., 76., 73.]`. With a Python list,
`temperatures_list + [2]` would concatenate rather than add 2 to every item.

A comparison also acts element by element:

```python
mask = temperatures > temperatures.mean()
```

The mask is an array of `True` and `False` values. Indexing with it selects
values at the `True` positions. If two aligned arrays use the same mask, their
pairing is preserved:

```python
names[mask]
temperatures[mask]
```

Inspect array metadata whenever a result surprises you:

- `ndim`: number of axes;
- `shape`: length along each axis;
- `size`: total element count;
- `dtype`: the common stored data type.

## Mathematics: standardization

For observations \(x_1,\ldots,x_n\), define the population mean and standard
deviation:

\[
\mu=\frac{1}{n}\sum_{i=1}^n x_i,\qquad
\sigma=\sqrt{\frac{1}{n}\sum_{i=1}^n(x_i-\mu)^2}.
\]

The standardized value is:

\[
z_i=\frac{x_i-\mu}{\sigma}.
\]

For the small array \([2,4,6]\), \(\mu=4\). The squared deviations are
\(4,0,4\), so:

\[
\sigma=\sqrt{\frac{8}{3}}\approx1.633.
\]

Therefore the standardized array is approximately:

\[
[-1.225,\ 0,\ 1.225].
\]

Its mean is approximately zero. Its population standard deviation is
approximately one:

\[
\frac{1}{n}\sum_i z_i
=\frac{1}{n\sigma}\sum_i(x_i-\mu)=0.
\]

This derivation also exposes an edge case: if every value is equal, then
\(\sigma=0\), and division by zero makes standardization undefined. Production
code must choose an explicit behavior instead of silently accepting `nan`.

## Machine-learning connection

Many ML methods treat a row as a vector of numeric features. If one feature is
measured in dollars and another in years, their raw numeric scales can be very
different.

- In k-nearest neighbors and k-means, a large-scale feature can dominate
  Euclidean distance.
- In gradient-based optimization, badly mismatched scales can make the loss
  surface elongated, which can slow or destabilize learning.
- Tree-based models split one feature at a time and are generally much less
  sensitive to monotonic rescaling.

Standardization does not make data “better” automatically. It changes the
representation so that scale-sensitive algorithms do not interpret units as
importance. In a real ML workflow, calculate \(\mu\) and \(\sigma\) from the
training set only, then reuse them on validation and test data; otherwise
evaluation information leaks into preprocessing.

## Algorithms and data structures: vectorized filtering

For an array of \(n\) scores, `scores > scores.mean()` requires:

1. a reduction over \(n\) values to compute the mean;
2. a comparison of each of the \(n\) values;
3. storage for an \(n\)-element Boolean mask.

Therefore the operation is \(O(n)\) time and \(O(n)\) additional space for the
mask. A carefully written Python loop can also be \(O(n)\); vectorization does
not change the Big-O class. It often improves constant factors because the loop
over homogeneous numeric data runs in compiled NumPy code.

**Correctness argument:** mask position \(i\) is `True` exactly when
`scores[i] > mean`. Applying that same mask to both `names` and `scores`
selects exactly the above-mean records while preserving their original order
and pairing.

Tradeoff: a mask is clear and reusable, but it consumes memory. For data too
large to fit in memory, a streaming loop may be the correct design.

## Technical reading

Read the NumPy manual sections on
[array fundamentals and attributes](https://numpy.org/doc/stable/user/absolute_beginners.html#array-fundamentals)
and
[basic array operations](https://numpy.org/doc/stable/user/absolute_beginners.html#basic-array-operations).

Guiding questions:

1. Why must ordinary NumPy array elements usually share one data type?
2. How are `shape`, `size`, and `ndim` different for a two-dimensional array?
3. What does a comparison such as `scores >= 80` return?
4. Why can a NumPy slice unexpectedly change its original array?
5. When might a Python list be a better container than an `ndarray`?

## Integrated coding exercise: NumPy score analysis

Create `lesson_10_numpy_scores.py`. Do not use a supplied starter, function
signatures, TODOs, or tests. Choose the program structure yourself.

### Input

Use the existing `scores.csv`, whose required columns are `Name` and `Score`.
Open and parse it once. Convert the aligned names and scores into NumPy arrays
after parsing.

### Required behavior

Your program must:

1. reject a missing required column, empty data, blank name, non-integer score,
   and score outside `0` through `100` with a clear error;
2. print the score array's `shape`, `size`, `ndim`, and `dtype`;
3. compute the mean and population standard deviation using NumPy;
4. use one Boolean mask to print above-mean names and their scores in input
   order;
5. compute a standardized score array without a Python loop;
6. reject standardization when the standard deviation is zero;
7. print the name and score whose standardized value is largest;
8. place substantial logic in at least three meaningful functions;
9. print output only when executed as a program.

For the supplied data, the output must include:

```text
Shape: (7,)
Size: 7
Dimensions: 1
Mean: 84.29
Population standard deviation: 9.25
Above mean: Alice 87, Bob 92, Emma 98, Grace 88
Largest standardized score: Emma 98
```

Also print the standardized values rounded to three decimal places. Their mean
should be approximately `0.0`, and their population standard deviation should
be approximately `1.0`.

### Implementation constraints

- Do not manually loop over the NumPy arrays to add, compare, filter, or
  standardize values.
- Do not sort to find the largest standardized value.
- Do not independently filter names and scores.
- Do not overwrite `lesson_2_csv.py` or `lesson_3_numpy_intro.py`.
- A loop during CSV parsing is allowed and expected.

### Acceptance criteria

- `python3 lesson_10_numpy_scores.py` succeeds on the supplied CSV.
- All facts in the expected output are correct.
- `names.shape == scores.shape` before any aligned filtering.
- The same Boolean mask selects both above-mean names and scores.
- Standardization is elementwise and handles zero variance deliberately.
- Valid reordered rows preserve each name/score pair.
- At least one malformed-input run is saved in the reflection.
- The implementation is your own architecture, not copied from a full
  solution.

### Optional stretch goals

- Use masks to report score bands without a Python loop.
- Add command-line selection of the input path.
- Compare population standard deviation (`ddof=0`) with sample standard
  deviation (`ddof=1`) and explain the denominator difference.
- Time a Python-loop transformation and a NumPy transformation on one million
  generated values; explain why one timing does not prove a universal rule.

## Retrieval-practice quiz

1. What do `shape`, `size`, `ndim`, and `dtype` describe?
2. What is returned by `scores > scores.mean()`?
3. Why must the same mask be applied to aligned names and scores?
4. State the standardization formula.
5. What happens mathematically when \(\sigma=0\)?
6. Does vectorization change this filtering problem from \(O(n)\) to \(O(1)\)?
7. Why must an ML test set not determine the standardization mean?

## Quiz answers

1. Axis lengths, total elements, number of axes, and stored element type.
2. A Boolean array with one truth value per score.
3. It preserves the identity of each selected record.
4. \(z=(x-\mu)/\sigma\).
5. Division by zero is undefined, so the program needs an explicit policy.
6. No. It remains \(O(n)\), though compiled operations can reduce overhead.
7. That would leak evaluation-set information into preprocessing and make the
   evaluation less honest.

## Suggested 75–90 minute study plan

- 0–8 minutes: answer the retrieval warm-up.
- 8–20 minutes: run and modify the executable example.
- 20–30 minutes: read the NumPy sections and inspect array metadata.
- 30–38 minutes: sketch the program's data flow and responsibilities.
- 38–70 minutes: implement the integrated exercise.
- 70–78 minutes: check the expected valid output.
- 78–84 minutes: run one malformed case and one zero-variance case.
- 84–90 minutes: complete the quiz and reflection.

## Submission checklist

Save:

- `lesson_10_numpy_scores.py`;
- valid terminal output;
- `lesson-10-reflection.md` containing:
  1. one malformed-input run and its output;
  2. the zero-variance behavior;
  3. an explanation of how the mask preserves alignment;
  4. answers to the five reading questions;
  5. whether the coding workload felt too short, appropriate, or too long.

