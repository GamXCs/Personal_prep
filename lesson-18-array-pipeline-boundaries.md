# Lesson 18 — From a Working NumPy Script to a Reusable Pipeline

**Module:** Week 2 — From core Python pipelines to NumPy  
**Estimated time:** 70–85 minutes  
**Difficulty:** Introductory NumPy, intermediate program design

## Why this is the next lesson

The current analyzer now runs successfully, rejects zero spread, and uses
`argmax` to recover the highest student's identity. Those are meaningful new
results. The remaining weakness is architectural: parsing, analysis, checking,
and printing still happen at top level, so edge cases are awkward to run and
the computed facts cannot be reused by a later ML workflow.

This Monday lesson keeps `lesson_10_numpy_scores.py` as the only integrated
assignment. It does not start the 2-D array lesson yet.

## Learning objectives and prerequisites

By the end, you should be able to:

1. give loading, analysis, and presentation separate function contracts;
2. return a structured analysis result instead of printing during computation;
3. encode array alignment and floating-point invariants as checks;
4. include the physical row and bad value in a conversion error;
5. explain why reusable preprocessing reduces train/test inconsistency; and
6. analyze the time and space cost of the complete pipeline.

Prerequisites: CSV `DictReader`, functions and dictionaries, one-dimensional
NumPy arrays, Boolean masks, standardization, `np.isclose`, and `argmax`.

## Retrieval warm-up

Without running the program, name the input and output of each responsibility:
loading, analysis, and presentation. Which one should know the CSV path? Which
one should know how many decimal places to print?

## Python instruction and executable example

Run `python3 lesson-18-boundary-example.py`.

The example demonstrates this direction of dependency:

```text
raw rows -> numeric arrays -> report dictionary -> formatted text
```

The analysis function returns data rather than printing it. The presentation
function consumes only that report. This makes the analysis callable from a
terminal program, test, notebook, or future ML pipeline. Function boundaries
are contracts: each has a defined input, output, and set of failures.

## Mathematics: invariants as operational checks

An invariant is a property expected to remain true at a defined point. For
aligned arrays and a mask:

```text
names length = scores length = mask length
```

For standardized nonconstant scores:

```text
standardized mean is close to 0
population standard deviation is close to 1
```

Worked check: if scores have mean `10` and population standard deviation `2`,
score `14` becomes `(14 - 10) / 2 = 2`, or two standard deviations above the
mean. If every score is `10`, the divisor is zero and no valid standardized
value exists.

For review, revisit Penn State STAT 200's
[z-score section](https://online.stat.psu.edu/stat200/lesson/2/2.2/2.2.8).
Ask which two summaries determine every standardized value and why they must
come only from training data in an evaluated ML system.

## Machine-learning theory connection

A fitted preprocessing step is part of a model pipeline. If training and
prediction code independently implement scaling, they may use different
statistics, degrees of freedom, column order, or validation rules. A reusable
analysis boundary makes those choices explicit.

Fit mean and spread on training data, then reuse them on validation or test
data. Recomputing them on held-out data leaks information and changes the
coordinate system seen by the model. Shape and finite-value checks catch
pipeline failures before model fitting.

## Algorithms and data structures: staged linear pipelines

Loading `n` rows is `O(n)` time and stores `O(n)` data. Mean, standard
deviation, mask construction, standardization, and `argmax` are each linear
passes, so a fixed number of stages remains `O(n)` time. Arrays, the mask, and
standardized values require `O(n)` space. A report dictionary gives expected
`O(1)` field lookup.

Correctness follows stage by stage: validated rows create aligned arrays; one
shared mask preserves positions; nonzero spread permits standardization; and
one `argmax` index selects corresponding entries from both aligned arrays.

## Technical reading

Read the official Python tutorial on
[defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
and NumPy's [`isclose`](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html).

Guiding questions:

1. What is the difference between printing and returning a value?
2. Why should the formatter depend on a report instead of global arrays?
3. Which tolerance does `isclose` scale relative to its reference argument?
4. What useful failure would a shape check expose before masking?

## Integrated coding exercise: refactor the existing analyzer

Continue `lesson_10_numpy_scores.py`. Preserve its correct output and logic
while reorganizing it into at least three meaningful functions:

- a loading boundary that accepts a CSV path and returns validated data;
- an analysis boundary that returns a structured report without printing; and
- a presentation boundary that accepts only the report and prints it.

Add explicit checks that aligned arrays and the Boolean mask have equal shapes,
that the mask dtype is Boolean, and that standardized mean/spread satisfy their
contracts with `np.isclose`. Update integer-conversion failures to include both
the physical row number and rejected value. Choose the exact report structure
yourself; do not create a second analyzer.

### Acceptance criteria

- The valid run still reports shape `(7,)`, mean `84.29`, population standard
  deviation about `9.25`, four above-mean records, and `Emma 98`.
- Loading, analysis, and presentation are separate meaningful functions.
- Analysis returns a structured value and contains no `print` calls.
- Presentation uses its argument rather than global names or scores.
- Shape equality, Boolean mask dtype, and both `np.isclose` diagnostics are
  checked explicitly.
- A malformed score error includes its physical row and rejected text.
- A constant-score fixture raises the deliberate zero-spread error.
- `lesson-10-reflection.md` contains valid, malformed, and constant-score runs,
  plus brief reading and quiz answers.

### Optional stretch goals

- Accept the input path with `argparse`.
- Separate fitted scaling parameters from the function that applies them.
- Return the whole name/score record closest to the mean in `O(n)` time without
  sorting.

## Retrieval-practice quiz

1. Why is returning a report more reusable than printing inside analysis?
2. What belongs in a useful CSV conversion error?
3. Why must names, scores, and a mask have equal shapes?
4. Why use `np.isclose` for standardized diagnostics?
5. What is the asymptotic time of six sequential linear passes?
6. Why are test-set scaling statistics a form of leakage?

## Quiz answers

1. A caller can test, format, serialize, or reuse returned data.
2. At minimum, the physical row, field, and rejected value.
3. Each mask position must refer to the same record in both arrays.
4. Floating-point results can be extremely near but not exactly equal to the
   mathematical target.
5. `O(n)`; a fixed number of passes does not change the growth class.
6. Held-out observations influence preprocessing used for evaluation.

## Suggested 70–85 minute study plan

- 0–8 minutes: retrieval warm-up and inspect top-level statements.
- 8–18 minutes: run the example and identify each contract.
- 18–28 minutes: complete the readings.
- 28–38 minutes: sketch inputs, outputs, and errors for three functions.
- 38–65 minutes: refactor, rerunning after each boundary is extracted.
- 65–77 minutes: run valid, malformed, and constant-score fixtures.
- 77–85 minutes: save evidence, reading answers, and quiz attempts.

## Submission checklist

Save `lesson_10_numpy_scores.py` and `lesson-10-reflection.md`. The reflection
must contain the three runs, reading answers, quiz attempts, actual
implementation time, and the hardest remaining step.
