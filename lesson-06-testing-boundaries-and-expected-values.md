# Lesson 6: Testing Boundaries and Expected Values

Date: Saturday, July 25, 2026  
Current module: Week 1 — Descriptive statistics, scaling, and lookup strategies  
Estimated study time: 70–80 minutes  
Difficulty: Foundational graduate-prep reinforcement

## Overview

Your new `test_lesson_01_score_analyzer.py` shows a useful intermediate step: you identified the required cases and imported the project functions. However, the file then redefines functions with the same names and contains no assertions. In Python, each later `def` replaces the imported name in that module. A “test” would therefore call the copy in the test file, not the analyzer you intended to test.

This lesson repairs that testing boundary. You will test the actual analyzer against expected values derived by hand, while preserving the cumulative variance-oracle work from Lessons 2–5.

## 1. Learning objectives

By the end, you should be able to:

- explain how name binding can accidentally replace an imported function;
- distinguish the **system under test** from test inputs and expected results;
- write executable `unittest` cases for exact values, approximate values, and exceptions;
- derive expected mean, variance, and search results independently;
- connect test independence to trustworthy ML evaluation;
- analyze hash-table-backed sets used to track test coverage.

## 2. Prerequisites

- the analyzer functions from Lesson 1;
- floating-point tolerances and invariants from Lessons 2–4;
- the pairwise variance identity from Lesson 5;
- Python imports, functions, exceptions, and dictionaries.

## 3. Retrieval warm-up

Answer before running code:

1. If a module imports `population_variance` and later executes `def population_variance(...):`, which object does that name refer to afterward?
2. What is the population variance of `[2, 2, 2]`?
3. What should linear search return when a target is absent?
4. Why is copying production logic into a test risky?

## 4. Python: test behavior without replacing it

The **system under test (SUT)** is the code whose behavior you are checking. Keep its definition in the analyzer module and import it into the test module. Do not redefine it there.

This small example is executable:

```python
import unittest

from lesson_01_score_analyzer_starter import calc_mean


class TestCalcMeanExample(unittest.TestCase):
    def test_three_values(self):
        self.assertAlmostEqual(calc_mean([1.0, 2.0, 6.0]), 3.0)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            calc_mean([])


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

Save it temporarily or type it into a scratch file, then run it. Notice the three roles:

- input: `[1.0, 2.0, 6.0]`;
- observed value: the result returned by the imported function;
- expected value: `3.0`, computed independently.

`assertAlmostEqual` is appropriate for floating-point results. `assertEqual` is better for discrete results such as an index or Boolean. `assertRaises` verifies an error contract.

## 5. Mathematics: derive an expected value before testing

For `x = [2, 4, 8]`, the population mean is

`mu = (2 + 4 + 8) / 3 = 14/3`.

The population variance is

`Var(x) = (1/3) sum_i (x_i - mu)^2`.

Substitute the values:

`Var(x) = (1/3)[(2-14/3)^2 + (4-14/3)^2 + (8-14/3)^2]`

`= (1/3)[(-8/3)^2 + (-2/3)^2 + (10/3)^2]`

`= (1/3)[64/9 + 4/9 + 100/9]`

`= (1/3)(168/9) = 56/9`.

Thus a test can compare the analyzer's result with `56/9`. This expected value does not reuse the analyzer's loop.

### Why independence matters

Let the implementation and a copied test both contain the same mistaken rule, represented by error `e`. Then both may return

`true_value + e`.

Their equality proves only that the copies agree, not that either is correct. A hand-derived result or a structurally different oracle reduces this **correlated-error** risk.

## 6. Machine-learning connection: evaluation must be independent

The same boundary applies in ML. Training code fits parameters using training data; evaluation code estimates behavior on data that did not influence those parameters. If preprocessing, target statistics, or hand-written evaluation logic leaks information from the test set, the reported score may agree with an optimistic story without measuring generalization.

Unit tests and held-out evaluation answer parallel questions:

- Did independently specified behavior match the implementation?
- Did behavior measured on independent data match the desired objective?

Neither guarantee is useful when the “independent” side silently duplicates or depends on the object being evaluated.

## 7. Data structures: a set as a coverage ledger

A coverage set records which behavioral partitions have been exercised:

```python
covered = set()
covered.add("target-present")
covered.add("target-absent")
covered.add("constant-values")

required = {"target-present", "target-absent", "constant-values", "empty-input"}
missing = required - covered
print(missing)
```

A Python set is implemented using hashing. Under ordinary assumptions:

- insertion and membership: expected `O(1)` time each;
- set difference: expected `O(len(required))` when checking a small ledger against `covered`;
- space: `O(k)` for `k` distinct labels.

Correctness invariant: after each passing test adds its label, `covered` contains exactly the partitions that the executed checks have established. A label is evidence only if it is added after the relevant assertion succeeds.

## 8. Technical reading

Read the “Basic example” and command-line discussion in the official Python [`unittest` documentation](https://docs.python.org/3/library/unittest.html#basic-example).

Guiding questions:

1. How does the runner recognize a test method?
2. What is the difference between a test failure and a test error?
3. Why use `assertRaises` instead of merely calling code that should fail?
4. What command runs this project’s test file verbosely?

## 9. Integrated coding exercise: repair the real test boundary

Edit the existing `test_lesson_01_score_analyzer.py`; do not create another analyzer.

### Required work

1. Keep the import of `calc_mean`, `population_variance`, `linear_search`, and `score_report`.
2. Delete every redefinition of those four imported names from the test file.
3. Create a `unittest.TestCase` subclass with test methods for:
   - the sample list with target `76`;
   - a missing target;
   - a one-element list;
   - repeated equal values with variance zero;
   - empty inputs for `calc_mean` and `population_variance`;
   - agreement between report variance and mean-baseline MSE.
4. Add a separate `pairwise_population_variance` helper. It may compute an expected value with nested pairwise differences because it is structurally independent of the analyzer.
5. Compare the pairwise oracle with `population_variance` on the four Lesson 5 datasets.
6. Maintain a coverage set and assert at the end that no required labels are missing.
7. Run `python3 -m unittest -v test_lesson_01_score_analyzer.py` and save the output in your notes.

Scaffold, intentionally incomplete:

```python
import unittest
from lesson_01_score_analyzer_starter import (
    calc_mean,
    population_variance,
    linear_search,
    score_report,
)


def pairwise_population_variance(values):
    # Implement the independent Lesson 5 oracle here.
    ...


class TestScoreAnalyzer(unittest.TestCase):
    def test_sample_target_present(self):
        scores = [88, 91, 91, 76, 84, 95]
        # Call the imported functions and assert expected behavior.
        ...


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

### Acceptance criteria

- the test file defines none of the four analyzer functions;
- the verbose command discovers and runs at least six named tests;
- exact assertions check indices and Booleans;
- approximate assertions check means, variances, and MSE values;
- both empty statistical inputs are verified with `assertRaises(ValueError)`;
- the pairwise oracle checks all four Lesson 5 datasets;
- every required coverage label is present;
- the unmodified analyzer passes;
- one deliberately introduced analyzer fault causes a failure, after which the fault is restored;
- passing and deliberate-failure outputs are saved.

### Optional stretch goals

- Use `subTest(values=values)` for the four oracle datasets.
- Add a test proving that the report preserves the original score order.
- Explain why checking only `report["Population Variance"] == report["Mean Baseline MSE"]` could allow both fields to be wrong.

## 10. Retrieval-practice quiz

1. What happens when a local `def` uses the same name as an earlier import?
2. Identify the SUT in this lesson.
3. When should you use an exact assertion rather than an approximate one?
4. What is the variance of `[2, 4, 8]`?
5. Why can two equal outputs still both be wrong?
6. Give the expected time and space complexity of a coverage set containing `k` labels.

<details>
<summary>Answers — open only after attempting</summary>

1. The later definition rebinds the name, hiding the imported object.
2. The functions in `lesson_01_score_analyzer_starter.py`.
3. For discrete or exactly represented contracts such as an integer index, Boolean, or string.
4. `56/9`.
5. They may share the same logic or error; agreement is not independent evidence of correctness.
6. Expected `O(1)` insertion/membership and `O(k)` space.

</details>

## 11. Suggested 75-minute study plan

- 0–7 minutes: retrieval warm-up and inspect current name bindings.
- 7–17: run and annotate the small `unittest` example.
- 17–29: reproduce the `[2,4,8]` variance derivation.
- 29–37: read the official documentation and answer its questions.
- 37–60: repair the cumulative test file and add assertions.
- 60–67: run passing tests, inject one temporary fault, and restore it.
- 67–72: attempt the quiz.
- 72–75: save outputs and record one remaining uncertainty.

## 12. Submission checklist

- repaired `test_lesson_01_score_analyzer.py`;
- saved verbose passing output and one mutation-failure output;
- hand derivation for `[2,4,8]`;
- four reading responses;
- quiz attempt and correction notes;
- remaining Lessons 2–5 written responses and report outputs.
