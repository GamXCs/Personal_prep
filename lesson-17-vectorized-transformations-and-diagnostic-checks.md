# Lesson 17 — Vectorized Transformations and Diagnostic Checks

**Module:** Week 2 — From core Python pipelines to NumPy  
**Estimated time:** 70–85 minutes  
**Difficulty:** Introductory NumPy, intermediate debugging

## Why this is the next lesson

No Lesson 10 analyzer or reflection has appeared yet, so there is not enough
evidence to move to 2-D arrays or Pandas. This Wednesday lesson keeps the same
`lesson_10_numpy_scores.py` deliverable and concentrates on the point where a
valid CSV becomes aligned arrays, a vectorized transformation, and useful
diagnostic checks. It is reinforcement, not a second project.

## Learning objectives and prerequisites

By the end, you should be able to:

1. convert validated records into aligned one-dimensional NumPy arrays;
2. explain broadcasting by a scalar in a vectorized expression;
3. distinguish a transformation from a check of its result;
4. use `np.isclose` and shape assertions as diagnostic evidence;
5. preserve identity while selecting a largest transformed value; and
6. analyze the work and memory used by a vectorized pipeline.

Prerequisites: CSV parsing, lists of dictionaries, NumPy array creation,
`mean`, population standard deviation, Boolean masks, and `argmax`.

## Retrieval warm-up

Before running code, predict the shape of each result when `scores.shape` is
`(7,)`: `scores.mean()`, `scores - scores.mean()`, and
`scores > scores.mean()`. Which result can index the aligned `names` array?

## Python instruction and executable example

Run:

```bash
python3 lesson-17-diagnostic-example.py
```

The example separates three responsibilities:

- verify the input contract;
- compute a vectorized transformation;
- verify properties that should hold afterward.

In this expression, NumPy broadcasts the scalar mean and standard deviation
across the one-dimensional array:

```python
standardized = (values - mean) / spread
```

The computation still examines every element, but Python does not execute an
element-by-element loop that you wrote. Checks such as these make silent errors
visible near their source:

```python
if not np.isclose(standardized.mean(), 0.0):
    raise AssertionError("standardized mean contract failed")
if not np.isclose(standardized.std(ddof=0), 1.0):
    raise AssertionError("standardized spread contract failed")
```

Use `np.isclose` because floating-point arithmetic often produces values very
near, rather than exactly equal to, the mathematical target.

## Mathematics: why the standardized spread is one

Definition: population variance is the average squared distance from the
mean. Population standard deviation is the square root of that variance.

For values `2, 4, 6`, the mean is `4`. The centered values are `-2, 0, 2`, so
the population variance is `(4 + 0 + 4) / 3 = 8/3`. Let the population standard
deviation be `s = sqrt(8/3)`.

After standardizing, every centered value is divided by `s`. Therefore every
squared distance is divided by `s squared`. The new population variance is:

```text
old variance / s squared = (8/3) / (8/3) = 1
```

The new population standard deviation is therefore `sqrt(1) = 1`. This
derivation requires `s` to be nonzero; a constant array must be rejected.

Intuition: subtraction moves the center to zero, while division measures each
distance in units of one original standard deviation.

## Machine-learning theory connection

Many models consume a numeric feature matrix whose columns may use different
units. Standardization can keep a large-unit feature from dominating Euclidean
distance and can make gradient-based optimization better conditioned. The
model behavior is only trustworthy if preprocessing parameters come from the
training data and are then reused for validation and test data.

Diagnostic checks protect this behavior. A mean far from zero may indicate the
wrong mean was used; a spread far from one may indicate a wrong `ddof`, an
incorrect divisor, or a constant feature. A shape mismatch can indicate that
features and identities were filtered separately.

## Algorithms and data structures: transformation pipelines

For `n` scores, mean, standard deviation, standardization, mask construction,
and `argmax` are each linear scans. A fixed number of linear passes is still
`O(n)` time. Materialized centered values, standardized values, a Boolean mask,
and filtered arrays require `O(n)` additional space.

NumPy vectorization reduces interpreter overhead; it does not turn a linear
operation into `O(1)`. Sorting only to find one maximum would cost
`O(n log n)` time, so `argmax` is the appropriate reduction.

## Technical reading

Read the official NumPy documentation for
[`numpy.isclose`](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html)
and the short broadcasting overview in
[NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html).

Guiding questions:

1. Why is `isclose` asymmetric in its default equation?
2. In `(scores - mean) / spread`, which operands are scalars?
3. What compatibility rule allows a scalar to operate with shape `(n,)`?
4. Why do successful diagnostic checks support correctness without proving the
   entire CSV program correct?

## Integrated coding exercise: complete the existing analyzer

Continue `lesson_10_numpy_scores.py`; do not create another analyzer. Begin
from the behavioral specification in Lesson 10 and use Lesson 16's boundary
contracts. The repository's current `scores.csv` contains the deliberate bad
row `Gam,eight`, so preserve that failure as malformed-input evidence and use a
valid copy with that row removed for the successful run.

Implement a program that:

1. loads the CSV once and gives physical row number plus bad value for row
   errors;
2. creates aligned one-dimensional `names` and integer `scores` arrays;
3. rejects mismatched shapes and empty data;
4. reports score metadata, mean, and population standard deviation;
5. uses one shared above-mean mask for names and scores;
6. rejects zero spread and standardizes with one vectorized expression;
7. checks the standardized mean and population standard deviation with
   `np.isclose`;
8. uses `argmax` to recover the matching name and raw score; and
9. separates loading, analysis, and presentation into at least three meaningful
   functions, printing only at the presentation boundary.

Do not use a Python loop for array arithmetic, filtering, or standardization;
do not sort to find the largest value. A CSV-parsing loop is expected.

### Acceptance criteria

- A valid copy produces the Lesson 10 expected facts: shape `(7,)`, mean
  `84.29`, population standard deviation `9.25`, the four aligned above-mean
  records, and `Emma 98` as the largest standardized score.
- `names.shape == scores.shape == mask.shape`, and the mask dtype is Boolean.
- The standardized mean is close to zero and its `ddof=0` standard deviation is
  close to one.
- The current malformed row is rejected with physical row number and
  `eight` in the error message.
- A nonempty constant-score file reaches a deliberate zero-spread error.
- Valid output and both failure runs are saved in `lesson-10-reflection.md`.

### Optional stretch goals

- Accept the CSV path as a command-line argument so fixtures are easy to run.
- Return tolerances and diagnostic results in a reusable report dictionary.
- Add a closest-to-mean scan that keeps the entire name/score identity without
  sorting.

## Retrieval-practice quiz

1. What does scalar broadcasting do in `scores - scores.mean()`?
2. Why should floating-point invariants use `np.isclose`?
3. Which `std` setting represents population standard deviation?
4. What does `argmax` return, and how does it recover identity?
5. Why is a sequence of five `O(n)` passes still `O(n)`?
6. Name one model behavior affected by badly scaled features.
7. Why must the deliberate malformed row be tested before array construction?

## Quiz answers

1. It subtracts the same scalar mean from every score.
2. Binary floating-point results can be slightly different from exact real
   arithmetic.
3. `ddof=0`.
4. It returns a position; use that same position to index aligned names and raw
   scores.
5. Constant factors are omitted in asymptotic growth: `5n` is `O(n)`.
6. Distance can be dominated by a large-unit feature, or gradient optimization
   can converge poorly.
7. Parsing and validation establish a homogeneous numeric boundary; otherwise
   array dtype or conversion failures obscure the bad source record.

## Suggested 70–85 minute study plan

- 0–7 minutes: retrieval warm-up and reread the Lesson 10 output contract.
- 7–17 minutes: run the example and alter one value to inspect diagnostics.
- 17–27 minutes: read the two NumPy documentation sections.
- 27–35 minutes: sketch loading, analysis, and presentation responsibilities.
- 35–65 minutes: implement the valid pipeline checkpoint by checkpoint.
- 65–77 minutes: run the malformed and constant-score cases.
- 77–85 minutes: answer the quiz and finish the reflection.

## Submission checklist

Save `lesson_10_numpy_scores.py` and `lesson-10-reflection.md`. The reflection
must include valid output, malformed-row output, zero-spread output, reading
answers, quiz attempts, and whether the implementation time felt appropriate.
