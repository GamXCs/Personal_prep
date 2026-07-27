# Lesson 4: Test Adequacy with Affine Invariants

Date: Thursday, July 23, 2026  
Current module: Week 1 — Descriptive statistics, scaling, and lookup strategies  
Estimated study time: 80 minutes  
Difficulty: Foundational graduate-prep bridge (review and debugging)

## Overview

The analyzer produces a plausible report, but the repository still has no verification harness or written reasoning. This lesson does not advance to z-scores. Instead, it asks a stronger question: would your tests reject a plausible but incorrect implementation? You will use affine transformations, deliberate fault injection, and coverage bookkeeping to turn “the sample worked” into evidence.

## 1. Learning objectives

By the end, you should be able to:

- distinguish code coverage from fault-detection evidence;
- derive and test `Var(aX+b) = a^2 Var(X)`;
- use deliberate, temporary faults to evaluate a test suite;
- explain why feature units can change distance-based and gradient-based model behavior;
- use a set to track test partitions, with time and space analysis;
- complete the still-missing verification submission without receiving a full solution.

## 2. Prerequisites

- Lessons 1–3: mean, population variance, squared loss, `math.isclose()`, input partitions, and translation invariance;
- Python functions, assertions, exceptions, imports, and set literals;
- the working `lesson-01-score-analyzer-starter.py`;
- the identity `MSE(c) = Var(X) + (mu-c)^2`.

## 3. Retrieval warm-up

Without notes:

1. State two properties of population variance.
2. Why is one passing example weaker than a property test?
3. What are the time and auxiliary-space complexities of linear search?
4. Which data must determine preprocessing parameters for a held-out evaluation?

## 4. Python: test whether a test can fail

A **test oracle** decides whether observed behavior is acceptable. A test that executes a line but would also accept a common bug is weak evidence. This executable example deliberately compares a correct function with a plausible faulty one:

```python
from math import isclose

def population_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

def faulty_variance(values):
    mean = sum(values) / len(values)
    return sum(abs(x - mean) for x in values) / len(values)

def obeys_scaling_property(variance_fn, values, scale):
    original = variance_fn(values)
    scaled = variance_fn([scale * x for x in values])
    return isclose(scaled, scale**2 * original,
                   rel_tol=1e-9, abs_tol=1e-12)

values = [1.0, 2.0, 6.0]
assert obeys_scaling_property(population_variance, values, 3.0)
assert not obeys_scaling_property(faulty_variance, values, 3.0)
print("the property accepts the implementation and rejects the fault")
```

Expected output:

```text
the property accepts the implementation and rejects the fault
```

The faulty function measures mean absolute deviation, so it scales by `|a|`, not `a^2`. Notice that the property supplies an oracle without requiring a hard-coded variance value.

## 5. Mathematics: affine transformations of variance

An **affine transformation** has the form

`Y = aX + b`,

where `a` changes scale (and may reverse direction) and `b` changes location.

For observations `x_1,...,x_n` with mean `mu_X`, the transformed mean is

`mu_Y = (1/n) sum_i (a x_i+b) = a mu_X+b`.

Now derive the transformed variance:

`Var(Y) = (1/n) sum_i [(a x_i+b)-(a mu_X+b)]^2`

`= (1/n) sum_i [a(x_i-mu_X)]^2`

`= a^2 (1/n) sum_i (x_i-mu_X)^2`

`= a^2 Var(X)`.

Thus, translation by `b` disappears from deviations, while scaling by `a` is squared. A negative scale reverses order but variance remains nonnegative.

Worked check: for `X=[1,3,5]`, `mu_X=3` and `Var(X)=8/3`. Let `Y=-2X+10=[8,4,0]`. Then `mu_Y=4` and

`Var(Y) = (16+0+16)/3 = 32/3 = (-2)^2(8/3)`.

## 6. Machine-learning connection

Feature transformations can preserve information while changing model behavior. Multiplying one feature by `1000` makes its squared contribution to Euclidean distance one million times larger. Nearest-neighbor and clustering methods can then be dominated by that feature's units.

Scaling also changes the geometry of an optimization problem: gradient descent may move efficiently along one direction and oscillate or crawl along another when feature scales are very different. A preprocessing test should therefore verify its mathematical contract and confirm that its parameters are learned from training data only. This lesson establishes the scaling law needed for z-scores later; it does not yet assume z-score mastery.

## 7. Data structures: sets for coverage bookkeeping

A set stores unique hashable values. Use one to record which input partitions actually ran:

```python
covered = set()
covered.add("singleton")
covered.add("target-absent")
covered.add("singleton")
assert covered == {"singleton", "target-absent"}
```

For `p` partition labels:

- average insertion and membership: `O(1)` each;
- checking all required labels: `O(p)`;
- space: `O(p)`;
- duplicates: removed automatically.

A list also preserves labels, but membership is `O(p)`, so repeatedly checking `p` requirements can take `O(p^2)`. Sets do not preserve a semantic test order and hash operations have worst-case `O(p)` behavior, so use them for membership and uniqueness—not ordered reporting.

Correctness argument: after each test group, add its label only if that group finishes. At termination, `required <= covered` is true exactly when every required category has been recorded.

## 8. Technical reading

Read Python's official `unittest` documentation on [distinguishing test iterations using subtests](https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests).

Guiding questions:

1. What problem does `subTest()` solve when several cases share one test structure?
2. Which case-specific information should you pass to `subTest()`?
3. Why is seeing every failed case more useful than stopping at the first case?
4. Would subtests replace the need to choose meaningful input partitions? Why or why not?

You may keep plain assertions for the required exercise; the reading shows a structured next step.

## 9. Integrated coding exercise: adequacy audit

Create or finish `test_lesson_01_score_analyzer.py`. Reuse the requirements from Lesson 3, then add an adequacy audit.

### Required work

1. Test the known examples, boundary partitions, invalid inputs, and all report relationships from Lesson 3.
2. Add an affine-property helper that checks, within tolerance:
   - `mean(aX+b) = a mean(X)+b`;
   - `Var(aX+b) = a^2 Var(X)`.
3. Run the helper for at least three `(a,b)` pairs, including a negative `a` and `a=0`.
4. Maintain a `covered` set with at least:
   - `ordinary`,
   - `singleton`,
   - `constant`,
   - `negative-decimal`,
   - `target-first`,
   - `target-last`,
   - `target-absent`,
   - `empty-invalid`,
   - `affine-property`.
5. Assert that every required partition was covered.
6. Perform a **temporary mutation audit**: locally change one variance operation or one search return value, confirm at least one test fails, record the failure, and immediately restore the working code.

Do not leave a deliberate fault in the project. Do not copy the implementation into the test file.

Starter structure—not a solution:

```python
REQUIRED = {
    "ordinary", "singleton", "constant", "negative-decimal",
    "target-first", "target-last", "target-absent",
    "empty-invalid", "affine-property",
}
covered = set()

def check_affine_property(values, scale, shift):
    transformed = [...]
    # Call the imported project functions.
    assert isclose(..., ..., rel_tol=1e-9, abs_tol=1e-12)
    assert isclose(..., ..., rel_tol=1e-9, abs_tol=1e-12)

# Add a label only after its assertions pass.
assert REQUIRED <= covered
```

### Acceptance criteria

- `python3 test_lesson_01_score_analyzer.py` exits successfully after restoration;
- importing the analyzer does not execute its sample block;
- tests call project functions rather than copied implementations;
- all nine required partition labels are recorded and checked;
- floating-point assertions use explicit tolerances;
- all three affine cases pass, including negative and zero scale;
- the temporary fault produces a saved failure and the restored code produces saved passing output;
- present-target and absent-target reports are saved;
- the affine derivation, reading answers, and quiz attempt are saved in your own words.

### Optional stretch goals

- Convert repeated affine cases to `unittest` subtests.
- Write a tiny comparison-counting search wrapper and verify `k+1` versus `n`.
- Add deterministic affine cases with very small and very large magnitudes, then explain any tolerance issues.

## 10. Retrieval-practice quiz

1. What is the difference between executing code and demonstrating that a test detects a fault?
2. If `Y=aX+b`, what are `E[Y]` (or the sample mean analogue) and `Var(Y)`?
3. Why does a negative `a` not make variance negative?
4. What fault in the executable example is exposed by the scaling property?
5. What are average set insertion and membership complexities?
6. Why can unscaled features distort nearest-neighbor behavior?

<details>
<summary>Answers — open after attempting</summary>

1. Execution shows reachability; fault detection shows the oracle rejects at least one relevant incorrect behavior.
2. The mean is `a mu_X+b`; the variance is `a^2 Var(X)`.
3. The scale factor is squared.
4. Mean absolute deviation scales by `|a|`, unlike variance, which scales by `a^2`.
5. Average `O(1)` for each; a set storing `p` labels uses `O(p)` space.
6. A large numerical scale can dominate the distance even when it is not more informative.

</details>

## 11. Suggested 80-minute study plan

- 0–7 minutes: retrieval warm-up.
- 7–17: run and explain the fault-detection example.
- 17–30: reproduce the affine derivation and worked check.
- 30–37: complete the reading and guiding questions.
- 37–62: build or finish the verification harness.
- 62–70: perform, record, and restore the temporary mutation.
- 70–75: save passing output and two reports.
- 75–80: quiz and brief error reflection.

## 12. Submission checklist

- `test_lesson_01_score_analyzer.py`;
- one saved failing run from the temporary mutation;
- one saved passing run after restoration;
- present-target and absent-target report outputs;
- affine-variance derivation in your own words;
- four reading responses;
- quiz answers and a note on mistakes or sticking points.
