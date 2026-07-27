# Lesson 7: Test Discovery and Detection Probability

Date: Sunday, July 26, 2026  
Current module: Week 1 — Descriptive statistics, scaling, and lookup strategies  
Estimated study time: 70–85 minutes  
Difficulty: Foundational graduate-prep reinforcement

## Overview

The latest test file is genuine progress: it imports the analyzer rather than shadowing it, and `pytest` finds five passing tests. However, the required command

```text
python3 -m unittest -v test_lesson_01_score_analyzer.py
```

reports `Ran 0 tests`. The functions use pytest-style discovery, while `unittest` normally discovers methods beginning with `test` inside a `unittest.TestCase` subclass. A passing runner and a zero-test runner are therefore both accurate descriptions of different discovery rules.

This lesson treats the **test runner contract** as part of correctness. You will convert the existing checks to discoverable `unittest` cases, measure whether intended cases were collected, and reason probabilistically about how additional independent cases increase fault-detection power.

## 1. Learning objectives

By the end, you should be able to:

- distinguish a test assertion from the runner that discovers and executes it;
- explain why “0 tests, OK” is not evidence that the analyzer is correct;
- organize tests as methods of a `unittest.TestCase` subclass;
- inspect the number of tests collected before trusting a green result;
- derive the probability that repeated independent cases detect a fault;
- connect test coverage to held-out ML evaluation;
- analyze depth-first traversal used to flatten a nested test suite.

## 2. Prerequisites

- imported-function boundaries and independent expected values from Lesson 6;
- basic classes and inheritance in Python;
- complements and multiplication of independent probabilities;
- the existing analyzer and `test_lesson_01_score_analyzer.py`.

## 3. Retrieval warm-up

Answer without running code:

1. What is the system under test in this project?
2. Why is importing `population_variance` safer than redefining it in the test file?
3. Which assertion style fits a floating-point variance?
4. If a runner executes zero tests and prints `OK`, what has actually been established?

## 4. Python: discovery is an executable contract

Run this example as a scratch file:

```python
import unittest


def is_even(value):
    return value % 2 == 0


class TestParity(unittest.TestCase):
    def test_even_value(self):
        self.assertTrue(is_even(8))

    def test_odd_value(self):
        self.assertFalse(is_even(7))


suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestParity)
print("collected:", suite.countTestCases())

if __name__ == "__main__":
    unittest.main(verbosity=2)
```

Expected first line: `collected: 2`. The loader creates a suite from methods whose names satisfy its discovery convention. The assertions matter only after the runner collects and calls them.

There are three separate contracts:

1. **Collection:** the intended tests are discoverable.
2. **Execution:** the collected tests actually run.
3. **Assertion:** observed behavior is compared with an independently specified expectation.

Your current file satisfies the third contract under pytest, but not the first under the required `unittest` runner.

## 5. Mathematics: probability of detecting a fault

Suppose a faulty implementation gives the wrong output on a fraction `p` of the input distribution. A randomly selected test misses the fault with probability

`P(miss once) = 1 - p`.

If `k` tests are independently sampled from that distribution, all `k` miss with probability

`P(miss all k) = (1 - p)^k`.

The event “detect at least once” is the complement:

`P(detect) = 1 - (1 - p)^k`.

### Worked calculation

If a bug affects `p = 0.20` of relevant inputs and you run `k = 5` independent cases,

`P(detect) = 1 - (1 - 0.20)^5`

`= 1 - 0.8^5`

`= 1 - 0.32768`

`= 0.67232`.

So five independent random cases detect the fault with probability about `67.2%`. With zero executed tests,

`P(detect) = 1 - (1-p)^0 = 1 - 1 = 0`.

### Important limitation

The formula assumes independence and a meaningful sampling distribution. Five copies of the same case are not five independent opportunities. Carefully chosen partitions—empty, singleton, constant, target present, and target absent—can be more useful than naive random repetition because they deliberately probe different behaviors.

## 6. Machine-learning connection: evaluation coverage

A test suite estimates whether code behaves correctly on a set of cases. A validation set estimates whether a learned model behaves well on unseen examples. Both estimates are trustworthy only when:

- examples are actually included and evaluated;
- the metric is computed as intended;
- the cases represent the behaviors or population you care about;
- repeated observations are not mistaken for independent evidence.

An empty validation loader can produce a misleading default, just as `unittest` can report `OK` after collecting zero tests. A validation set with duplicated or narrowly clustered examples can also overstate confidence. In both software testing and ML, always inspect the denominator: number of executed tests, evaluated examples, class counts, and important subgroups.

## 7. Algorithms: flattening a nested test suite

A `unittest` suite can contain individual test cases or other suites. A runner can traverse that nested structure using depth-first search:

```python
def count_leaves(node):
    if is_test_case(node):
        return 1

    total = 0
    for child in node:
        total += count_leaves(child)
    return total
```

Treat the nested suite as a tree with `V` nodes and `E` parent-child edges.

- Correctness invariant: after processing the first `j` children, `total` equals the number of test-case leaves in those `j` subtrees.
- Time complexity: `O(V + E)`, which is `O(V)` for a tree because `E = V - 1`.
- Auxiliary space: `O(h)` for recursion depth `h`; worst case `O(V)` for a chain, and `O(log V)` for a balanced tree.

The practical tradeoff is that recursive DFS closely matches nested suite structure, while an explicit stack avoids Python recursion-depth limits.

## 8. Technical reading

Read the “Basic example,” “Command-Line Interface,” and “Test Discovery” sections of the official Python [`unittest` documentation](https://docs.python.org/3/library/unittest.html#test-discovery).

Guiding questions:

1. What class must normal `unittest` test cases inherit from?
2. What naming convention identifies test methods?
3. What default filename pattern does discovery use?
4. How can you run one module verbosely?
5. Why can pytest collect the current top-level functions while `unittest` does not?

## 9. Integrated coding exercise: make collection measurable

Repair the existing `test_lesson_01_score_analyzer.py`. Do not change the analyzer merely to make a test pass, and do not create a second test file.

### Required work

1. Import `unittest`.
2. Put the five existing checks into a `TestScoreAnalyzer(unittest.TestCase)` class as methods beginning with `test_`.
3. Replace bare assertions with appropriate `self.assertEqual`, `self.assertTrue`, `self.assertAlmostEqual`, and `self.assertRaises` methods.
4. Add checks for:
   - one-element mean and variance;
   - `ValueError` from both empty statistical inputs;
   - approximate agreement between report variance and mean-baseline MSE;
   - all four Lesson 5 pairwise-oracle datasets.
5. Keep the pairwise oracle outside the class so it remains a helper, not an analyzer replacement.
6. Load the completed test class in a short collection audit and verify that its `countTestCases()` is at least six.
7. Run both:

```text
python3 -m unittest -v test_lesson_01_score_analyzer.py
python3 -m pytest -q test_lesson_01_score_analyzer.py
```

8. Save both outputs and explain why their executed-test counts should now agree.

### Scaffold

```python
import unittest

from lesson_01_score_analyzer_starter import (
    calc_mean,
    population_variance,
    linear_search,
    score_report,
)


def pairwise_population_variance(values):
    # Implement the independent Lesson 5 oracle.
    ...


class TestScoreAnalyzer(unittest.TestCase):
    def test_calc_mean(self):
        self.assertEqual(calc_mean([5, 2, 5]), 4)

    # Convert and extend the remaining tests.


class TestCollectionContract(unittest.TestCase):
    def test_expected_number_collected(self):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(
            TestScoreAnalyzer
        )
        self.assertGreaterEqual(suite.countTestCases(), 6)
```

### Acceptance criteria

- `unittest` discovers at least six analyzer tests plus the collection-contract test;
- pytest and unittest execute the same intended test methods;
- no analyzer function is redefined in the test file;
- exact, approximate, Boolean, and exception assertions are present;
- empty, singleton, constant, target-present, and target-absent partitions are covered;
- the independent pairwise oracle checks four datasets;
- a temporary fault in the analyzer produces at least one genuine failure and is then restored;
- passing output and deliberate-failure output are saved;
- the student explains why the earlier `0 tests / OK` result was not a pass.

### Optional stretch goals

- Use `subTest` to label each pairwise dataset.
- Add a command that runs exactly one test method by dotted name.
- Compute `1 - (1-p)^k` for `p` values from `0.05` to `0.50` and discuss why the calculation still does not replace partition design.

## 10. Retrieval-practice quiz

1. Name the three contracts between writing a test and trusting its result.
2. Why did pytest pass five tests while unittest ran zero?
3. If `p = 0.1` and `k = 3`, what is the probability of detecting the fault at least once?
4. What assumption makes `1 - (1-p)^k` potentially optimistic?
5. What should you inspect in an ML evaluation before trusting its aggregate metric?
6. Give the time and auxiliary-space complexity of recursive DFS over a suite tree.

<details>
<summary>Answers — open only after attempting</summary>

1. Collection, execution, and assertion.
2. Pytest collects suitable top-level `test_*` functions; ordinary unittest discovery expects test methods on `TestCase` instances.
3. `1 - 0.9^3 = 0.271`, or `27.1%`.
4. It assumes independent cases sampled from a meaningful distribution with fault probability `p`.
5. The number of evaluated examples and important class or subgroup counts, as well as the metric definition.
6. `O(V + E)` time, or `O(V)` for a tree, and `O(h)` recursive stack space.

</details>

## 11. Suggested 75-minute study plan

- 0–7 minutes: retrieval warm-up and reproduce both runner outputs.
- 7–17: run the collection example and identify its three contracts.
- 17–29: work the detection-probability derivation by hand.
- 29–38: read the official documentation and answer the questions.
- 38–60: convert and extend the test class.
- 60–67: run both frameworks and perform the temporary fault check.
- 67–72: attempt the quiz.
- 72–75: save outputs and write a two-sentence runner-mismatch explanation.

## 12. Submission checklist

- repaired `test_lesson_01_score_analyzer.py`;
- saved verbose unittest and concise pytest outputs;
- saved deliberate-failure output after temporary fault injection;
- detection-probability derivation and one additional `p, k` calculation;
- five reading responses;
- quiz attempt and correction notes;
- remaining report outputs and written responses from Lessons 2–6.
