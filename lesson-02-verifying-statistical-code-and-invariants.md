# Lesson 2: Verifying Statistical Code with Invariants

Date: Tuesday, July 21, 2026  
Current module: Week 1 - Descriptive statistics, scaling, and lookup strategies  
Estimated study time: 75 minutes  
Difficulty: Foundational graduate-prep bridge (reinforcement)

This is a continuation of Lesson 1, not an advance to new scaling material. The project contains implementations of `calc_mean`, `population_variance`, and `linear_search`, but the integrated report, required tests, derivation, and reading responses are not present. Today turns the partial implementation into evidence that can be reviewed.

## 1. Learning objectives

By the end of this lesson, you should be able to:

- test numerical Python functions with tolerances instead of fragile exact equality,
- state and use invariants for mean, variance, and linear search,
- derive the squared-error decomposition around the mean,
- explain why a trained regression model should be compared with a mean baseline,
- complete and test the Lesson 1 score analyzer without duplicating helper logic.

## 2. Prerequisites

- Python functions, loops, lists, dictionaries, `assert`, and exceptions.
- Mean and population variance from Lesson 1.
- The purpose and `O(n)` complexity of linear search.
- The existing [`lesson-01-score-analyzer-starter.py`](</Users/gamlielibn/Documents/Grad School Prep/lesson-01-score-analyzer-starter.py>).

## 3. Retrieval warm-up

Without looking back, write short answers:

1. What constant minimizes mean squared error on a fixed set of targets?
2. What must linear search have established after it checks indices `0` through `k - 1` without returning?
3. Why is variance never negative?
4. What should `linear_search([], 7)` return under the current function contract?

## 4. Python instruction: assertions and floating-point tolerance

An executable example:

```python
def approximately_equal(actual, expected, tolerance=1e-9):
    return abs(actual - expected) <= tolerance


def mean(values):
    if not values:
        raise ValueError("values must be non-empty")
    return sum(values) / len(values)


result = mean([0.1, 0.2])
assert approximately_equal(result, 0.15)
assert mean([5, 5, 5]) == 5

try:
    mean([])
except ValueError:
    print("empty-input test passed")
else:
    raise AssertionError("mean([]) should raise ValueError")

print("numeric tests passed")
```

Run it by saving it temporarily or entering it in Python. Expected output:

```text
empty-input test passed
numeric tests passed
```

Use exact equality for discrete outputs such as an index or Boolean. Use a tolerance for calculated decimal values. A good test suite also checks boundaries: empty input, one element, repeated values, a missing target, and a target at either end.

## 5. Mathematics: invariants and squared-error decomposition

### Definitions

For values `x_1, ..., x_n`, let

`mu = (1/n) sum_i x_i`

and let the mean squared error of a constant `c` be

`MSE(c) = (1/n) sum_i (x_i - c)^2`.

An **invariant** is a property that must remain true for every valid input or at a specified point in an algorithm. Useful statistical invariants include:

- `sum_i (x_i - mu) = 0`,
- `Var(x) >= 0`,
- adding a constant to every observation does not change variance,
- `MSE(mu) = Var(x)` when population variance is used.

### Worked derivation

Write each error around an arbitrary constant `c` as

`x_i - c = (x_i - mu) + (mu - c)`.

Square and average:

`MSE(c) = (1/n) sum_i [(x_i - mu) + (mu - c)]^2`

`= (1/n) sum_i (x_i - mu)^2`

`  + (2(mu - c)/n) sum_i (x_i - mu)`

`  + (1/n) sum_i (mu - c)^2`.

The middle term is zero because deviations from the mean sum to zero. The last term repeats the same constant `n` times. Therefore

`MSE(c) = Var(x) + (mu - c)^2`.

This identity is stronger than merely finding a zero derivative: it shows exactly how much extra error any other constant incurs.

For `[2, 4, 6, 8]`, `mu = 5` and `Var(x) = 5`. If `c = 7`, then

`MSE(7) = 5 + (5 - 7)^2 = 9`.

Direct check: squared errors are `25, 9, 1, 1`; their mean is `36/4 = 9`.

## 6. Machine-learning connection

For regression trained with squared loss, predicting the training-target mean is the feature-free baseline. The decomposition above says every other constant predictor has baseline error plus a nonnegative penalty.

This leads to a verification rule: if a fitted model evaluated on the same training data has MSE worse than the mean predictor, either the model is constrained or poorly optimized, regularization changes the objective, or the implementation deserves inspection. On held-out data, compute the baseline using the **training** target mean; using the test mean leaks information from the evaluation set.

Later, the coefficient of determination will formalize this comparison: a negative test `R^2` means the model performed worse than the chosen mean baseline.

## 7. Algorithms: loop invariants for linear search

At the start of iteration `i`, a suitable loop invariant is:

> The target does not occur at any index smaller than `i`.

- **Initialization:** before `i = 0`, there are no smaller indices, so the statement is true.
- **Maintenance:** if `values[i]` is not the target, advancing to `i + 1` makes the statement true for all indices through `i`.
- **Termination:** returning `i` is correct when equality is found. If the loop ends, every valid index has been ruled out, so `-1` is correct.

Complexity for a list of length `n`:

- best-case time: `O(1)`,
- worst- and average-case time: `O(n)`,
- auxiliary space: `O(1)`.

Early return changes how much work many inputs require, but it does not change worst-case `O(n)` time.

## 8. Technical reading

Read the official Python documentation section [Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html), through the discussion of `math.isclose()`.

Guiding questions:

1. Why can a decimal such as `0.1` fail to have an exact binary floating-point representation?
2. Why does rounding displayed output not change the stored value?
3. When is `math.isclose(a, b)` preferable to `a == b`?
4. Which outputs in the score analyzer should be compared exactly, and which approximately?

## 9. Integrated coding exercise: finish and verify the score analyzer

Continue in [`lesson-01-score-analyzer-starter.py`](</Users/gamlielibn/Documents/Grad School Prep/lesson-01-score-analyzer-starter.py>). Do not replace your existing functions unless a test exposes a problem.

### Part A: complete `score_report`

Return a dictionary containing every field required in Lesson 1. Use the helper functions rather than reimplementing mean, variance, or search. Define the spread-label thresholds in your own code and document them; there is no single statistically universal threshold.

### Part B: add tests

Create `test_lesson_01_score_analyzer.py` using plain `assert` statements. It must test:

- the suggested score list with target `76`,
- an absent target,
- a one-element list,
- repeated equal values (variance must be zero),
- empty input behavior for both statistical functions,
- `mean_baseline_mse` approximately equals population variance,
- squared deviations sum to `n * population_variance` within tolerance.

Run with:

```bash
python3 test_lesson_01_score_analyzer.py
```

### Acceptance criteria

- both Python files execute without external libraries,
- all required report keys are present and values have sensible types,
- `score_report` calls the existing helpers and does not duplicate their algorithms,
- floating-point quantities are tested with `math.isclose()` or an explicit tolerance,
- exact outputs such as indices and Booleans use exact comparisons,
- present, absent, boundary, repeated-value, and invalid-input cases are covered,
- the program prints or saves output from at least two report runs,
- the submission includes the hand derivation from Section 5 in your own words.

### Hints

- Build squared deviations with a loop or list comprehension after calculating the mean once.
- The target index determines both `found` and `target_index`.
- Use `try`/`except` to verify an expected exception without a testing framework.

### Optional stretch goals

- Write a test that verifies variance is unchanged after adding `10` to every score.
- Count comparisons in linear search and demonstrate best versus worst case.
- Refactor tests into small named functions without using `pytest` yet.

## 10. Retrieval-practice quiz

1. State the squared-error decomposition for an arbitrary constant `c`.
2. Which term in the derivation vanishes, and why?
3. Does early return make linear search worst-case `O(1)`?
4. Why should decimal statistical results usually be compared with a tolerance?
5. On test data, should a legitimate mean baseline use the training-target mean or test-target mean?

<details>
<summary>Answers — open only after attempting the quiz</summary>

1. `MSE(c) = Var(x) + (mu - c)^2`.
2. The cross term vanishes because `sum_i (x_i - mu) = 0`.
3. No. An absent or last-position target still requires `n` comparisons, so worst-case time is `O(n)`.
4. Many decimal values are approximated in binary floating point, so mathematically equal computations may differ by a tiny representation error.
5. The training-target mean; the test-target mean leaks evaluation information.

</details>

## 11. Suggested 75-minute study plan

- 0-8 minutes: retrieval warm-up without notes.
- 8-20 minutes: run the assertion example and read the floating-point article.
- 20-35 minutes: reproduce the decomposition by hand and verify the `[2, 4, 6, 8]` example.
- 35-60 minutes: complete `score_report` and write tests.
- 60-68 minutes: run tests, debug, and record two report outputs.
- 68-75 minutes: take the quiz and write brief reading responses.

## 12. Submission checklist

Return these artifacts for review before Lesson 3:

- completed `lesson-01-score-analyzer-starter.py`,
- `test_lesson_01_score_analyzer.py` with passing output,
- output from at least two report runs,
- your hand-worked squared-error decomposition,
- answers to the four reading questions,
- quiz answers plus notes on any mistakes or sticking points.
