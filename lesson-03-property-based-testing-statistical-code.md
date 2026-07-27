# Lesson 3: Property-Based Testing for Statistical Code

Date: Wednesday, July 22, 2026  
Module: Week 1 — Descriptive statistics, scaling, and lookup strategies  
Estimated time: 80 minutes  
Difficulty: Foundational graduate-prep bridge (implementation and verification)

## Overview

The score analyzer runs, but one successful sample is not strong evidence of correctness. Today you will turn mathematical facts into executable tests. An example checks one answer; a property checks a relationship that should hold across a class of inputs. Do not replace working code preemptively—let a failing test identify what needs attention.

## 1. Learning objectives

By the end, you should be able to:

- partition a function's input space into meaningful test classes;
- translate statistical invariants into Python assertions;
- prove that translating every observation leaves population variance unchanged;
- explain how transformation tests protect ML pipelines;
- analyze correctness and comparison counts for linear search;
- produce the missing verification evidence for Lesson 1.

## 2. Prerequisites

- Python functions, imports, exceptions, loops, and `assert`;
- mean, population variance, and linear search from Lessons 1–2;
- `math.isclose()` and `MSE(c) = Var(x) + (mu-c)^2`;
- `lesson-01-score-analyzer-starter.py`.

## 3. Retrieval warm-up

Without notes:

1. Why is exact equality often unsuitable for a computed decimal?
2. State one invariant of population variance.
3. What loop invariant justifies returning `-1` after linear search ends?
4. Which mean belongs in a held-out regression baseline: training or test?

## 4. Python: examples, properties, and partitions

An **example test** supplies a particular expected output. A **property test** checks a relationship among executions or outputs. This standalone example is executable:

```python
from math import isclose

def mean(values):
    if not values:
        raise ValueError("values must be non-empty")
    return sum(values) / len(values)

values = [1.0, 2.0, 7.0]
shift = 10.0
shifted = [x + shift for x in values]

assert isclose(mean(shifted), mean(values) + shift)
assert len(shifted) == len(values)
assert all(isclose(y - x, shift) for x, y in zip(values, shifted))
print("translation properties passed")
```

Expected output: `translation properties passed`.

Before testing, partition the input space. Useful classes here are ordinary data, a singleton, repeated equal values, negative/decimal values, target at either boundary, absent target, and invalid empty input. One representative from each class is more informative than many similar ordinary examples.

## 5. Mathematics: translation invariance of variance

For observations `x_1,...,x_n` with mean `mu`,

`Var(x) = (1/n) sum_i (x_i-mu)^2`.

Let `y_i = x_i + a`. Translation changes location but not spread. First derive the new mean:

`mu_y = (1/n) sum_i (x_i+a) = (1/n) sum_i x_i + na/n = mu+a`.

Then

`Var(y) = (1/n) sum_i (y_i-mu_y)^2`

`= (1/n) sum_i [(x_i+a)-(mu+a)]^2`

`= (1/n) sum_i (x_i-mu)^2 = Var(x)`.

For `[1,3,5]`, the mean is `3` and variance is `(4+0+4)/3 = 8/3`. Adding `10` gives mean `13`, but deviations remain `[-2,0,2]`, so variance is still `8/3`. This identity supplies a test oracle without hard-coding a variance.

## 6. Machine-learning connection

Pipelines routinely shift and scale features. Correct centering subtracts a mean learned from training data: it changes the training-feature mean to zero while preserving variance. Centering may improve numerical conditioning, and a linear-model intercept can often absorb a uniform shift. Fitting the centering value on test data, however, leaks held-out information.

Tests should check a transformation's **contract**, not just a few output numbers. Translation invariance can catch a transformer that accidentally alters spread when it should change only location. Z-score contracts will follow after the current work is verified.

## 7. Algorithms: linear-search comparison counts

At the start of iteration `i`, the loop invariant is: no index smaller than `i` contains the target. It is initially true, remains true after a mismatch, and proves that a found index is the first match or that `-1` is correct after termination.

For list length `n`, a target at zero-based index `k` costs `k+1` comparisons; an absent target costs `n`. If a successful target position is uniform,

`E[C] = (1/n) sum_(k=0)^(n-1)(k+1) = (1/n)(n(n+1)/2) = (n+1)/2 = Theta(n)`.

- Best-case time: `O(1)`
- Average/worst-case time: `O(n)`
- Auxiliary space: `O(1)`

A dictionary can provide average `O(1)` lookup after preprocessing, but costs memory and needs a duplicate-value policy. Preserve linear search's current contract for now.

## 8. Technical reading

Read Python's official documentation on [organizing test code](https://docs.python.org/3/library/unittest.html#organizing-test-code) and [skipping tests and expected failures](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures).

Guiding questions:

1. What belongs in `setUp()` rather than repeated in each test?
2. Why should every test method be independently runnable?
3. How does `assertRaises()` state an invalid-input contract?
4. Why is skipping a failing test different from fixing behavior?

Plain assertions remain acceptable today; this reading prepares you for structured suites.

## 9. Integrated coding exercise: verification harness

Create `test_lesson_01_score_analyzer.py` and import the four public functions from the existing implementation. Importing must not run its sample block.

Required groups:

1. **Known examples:** check mean, variance, and index for hand-computed data.
2. **Boundary partitions:** singleton, equal repeated values, first and last target, absent target, and empty statistical input.
3. **Report contract:** verify all eight report meanings, preserved input, and agreement between `found` and index. Match your implementation's exact key spelling.
4. **Properties:** within tolerance verify:
   - squared deviations sum to `n * population_variance`;
   - baseline MSE equals variance;
   - adding a constant changes mean by that constant;
   - adding a constant does not change variance.
5. **Evidence:** print a success message and save two report outputs, with present and absent targets.

Starter fragment (not a full solution):

```python
from math import isclose

# A hyphenated filename needs importlib or a careful rename. Document your choice.

def test_translation_invariance():
    values = [...]       # at least three unequal values
    shift = ...
    shifted = [...]

    original_mean = ...
    shifted_mean = ...
    original_variance = ...
    shifted_variance = ...

    assert isclose(..., ..., rel_tol=1e-9, abs_tol=1e-12)
    assert isclose(..., ..., rel_tol=1e-9, abs_tol=1e-12)
```

Hints:

- `importlib.util.spec_from_file_location()` can load a hyphenated filename.
- Use a helper to check expected exceptions if you keep plain assertions.
- Compare the key set once, then test relationships among values.
- Test behavior, not private helper structure.

### Acceptance criteria

- `python3 test_lesson_01_score_analyzer.py` exits successfully;
- tests call project functions rather than copied implementations;
- continuous results use `isclose()` with explicit tolerances;
- discrete outputs use exact comparisons;
- all required partitions and invalid input are covered;
- report invariants are asserted, not merely printed;
- two reports and passing terminal output are saved;
- your own translation-invariance derivation, reading answers, and quiz attempt are saved.

### Optional stretch goals

- Refactor into `unittest.TestCase` methods.
- Instrument a separate search demo to count comparisons without altering project code.
- Test shifts `[-100, -0.5, 0, 7, 1000]` deterministically.

## 10. Retrieval-practice quiz

1. How does an example test differ from a property test?
2. If `y_i=x_i+a`, what are `mu_y` and `Var(y)`?
3. Why compare shifted statistics with `isclose()`?
4. How many comparisons find a target at index `k`?
5. Why is centering on test data leakage?
6. Does one successful sample report establish general correctness?

<details>
<summary>Answers — open after attempting</summary>

1. An example checks one specified case; a property checks a relationship over a class of cases.
2. `mu_y=mu_x+a`; `Var(y)=Var(x)`.
3. Floating-point representations may differ slightly despite mathematical equality.
4. `k+1`.
5. It uses held-out information to define preprocessing, contaminating evaluation.
6. No; boundaries, invalid inputs, and invariant relationships remain unchecked.

</details>

## 11. Suggested 80-minute plan

- 0–7: retrieval warm-up.
- 7–17: run and explain the Python example.
- 17–30: reproduce the derivation by hand.
- 30–38: read documentation and answer questions.
- 38–65: implement and debug the harness.
- 65–73: run and save two reports.
- 73–80: quiz and error reflection.

## 12. Submission checklist

- `test_lesson_01_score_analyzer.py`;
- passing terminal output;
- present-target and absent-target report outputs;
- your translation-invariance derivation;
- four reading responses;
- quiz answers and a note on mistakes or sticking points.
