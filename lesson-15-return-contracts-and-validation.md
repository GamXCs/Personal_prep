# Lesson 15 — Return Contracts and Trustworthy Report Boundaries

**Module:** Week 2 — Regression workflow and honest evaluation  
**Estimated time:** 65–80 minutes  
**Difficulty:** Intermediate core Python reinforcement

## Why this lesson now

Your Lesson 9 program now reads and analyzes the real CSV correctly, including
preserving the entire highest-student record. Its remaining failure is at the
boundary: `report()` prints one field, implicitly returns `None`, and leaves the
other computed facts inaccessible. This Wednesday lesson completes that same
program. It is not a new project and does not advance to NumPy.

## Learning objectives and prerequisites

By the end, you should be able to:

1. distinguish a computation's return value from its printed presentation;
2. design a dictionary return contract whose shape is stable and inspectable;
3. attach CSV row numbers to conversion and validation failures;
4. explain why evaluation metrics must remain machine-readable;
5. reason about a linear best-record scan and its complexity.

Prerequisites: functions, dictionaries, loops, `csv.DictReader`, exceptions,
means, and the current `lesson_09_score_pipeline.py`.

## Retrieval review

Before reading further, answer from memory:

- What value does a Python function return when execution reaches the end
  without `return`?
- Why must the best-so-far variable remain a whole record dictionary?
- Which report field cannot be known until the final mean is available?

## Python instruction: compute, return, then format

Run the independent pattern example:

```bash
python3 lesson-15-contract-example.py
```

`summarize_runs()` returns structured data. `format_summary()` converts that
data to text. Only the main guard prints. This creates three useful boundaries:

- computation can be reused or checked without capturing terminal output;
- formatting can change without changing the arithmetic;
- an imported module has no accidental output.

A return contract should name every promised field. For your score report,
write the intended dictionary shape on paper before editing. Do not add a
`return` containing only variables that happen to be nearby; check it against
every required output in Lesson 9.

For contextual CSV errors, `enumerate(reader, start=2)` associates the first
data row with physical CSV line 2. Catch only the narrow conversion failure you
can explain, then raise a `ValueError` whose message includes the row number.
Range and blank-name checks should use the same context.

## Mathematics: a report as a vector of statistics

For scores \(x_1,\ldots,x_n\), define the report's numeric core as

\[
R(D) = \left(n,\; \bar{x},\; \max_i x_i,\; c_{90},c_{80},c_{70},c_{<70}\right),
\qquad \bar{x}=\frac{1}{n}\sum_{i=1}^n x_i.
\]

For scores `75, 90, 95`, the sum is `260`, so
\(\bar{x}=260/3=86.67\). The maximum is `95`, and the band-count tuple
from highest to lowest is `(2, 0, 1, 0)`. A returned dictionary is a named
software representation of this mathematical object; printing only the names
above the mean discards most of \(R(D)\).

## Machine-learning theory connection

An evaluation function should return structured metrics such as loss, sample
count, and the worst example. Training code can then compare runs, save results,
or choose a model. If the evaluator only prints, later code must scrape human
text, which is fragile. The sample count is part of the metric's meaning: two
equal mean losses based on 8 and 80,000 examples do not carry equal evidence.

Row-context validation also protects feature/target alignment. Rejecting a bad
row explicitly is safer than silently skipping one side of a future `(X, y)`
pair.

## Algorithms and data structures: best-record scan

Initialize `best` to the first valid record. After processing the first \(k\)
records, maintain this invariant: `best` is one of those records and no
processed record has a larger comparison field. The next record either replaces
`best` or leaves the invariant true. At termination, `best` is a maximum.

- time: \(O(n)\), because each record is compared once;
- auxiliary space: \(O(1)\), excluding the input and returned reference/copy;
- tradeoff: sorting also finds a maximum but costs \(O(n\log n)\) time and may
  disturb order unnecessarily.

Keeping the whole record preserves identity. Replacing `best` with only its
numeric field changes the variable's type and loses the associated name.

## Technical reading

Read Python's tutorial sections on
[`return` values](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
and [`raise`](https://docs.python.org/3/tutorial/errors.html#raising-exceptions).

Guiding questions:

1. What does falling off the end of a function return?
2. Why is an explicit return contract easier to reuse than printed output?
3. When should you raise a new `ValueError` rather than allow the raw conversion
   error to reach the user?
4. What information makes a data-validation error actionable?

## Integrated coding exercise: finish the existing Lesson 9 pipeline

Edit `lesson_09_score_pipeline.py`; do not create a second solution program.
Keep your current correct loading and maximum-record logic, then complete these
behaviors:

1. Make the analysis function return one dictionary containing every required
   report field. It must not print.
2. Add a separate presentation responsibility that formats or prints the
   returned report only when the file runs as a script.
3. Reject scores below `0` or above `100`.
4. Include the physical CSV row number in blank-name, invalid-integer, and
   out-of-range errors.
5. Run the normal file and at least one malformed file; save both commands and
   outputs in your reflection.

### Acceptance criteria

- `scores.csv` produces count `7`, mean `84.29`, highest `Emma (98)`, names
  above mean `Alice, Bob, Emma, Grace`, and band counts `2, 3, 1, 1`.
- `report(records)` returns structured data and produces no output itself.
- Loading, analysis, and presentation are separate meaningful responsibilities.
- Missing headers, empty data, blank names, invalid integers, and scores outside
  `0..100` raise clear errors; row-level errors identify the row.
- The file is opened once, input order is preserved, and the best candidate
  remains an entire record.
- The valid run no longer ends with `None`.

### Optional stretch goals

- Return copies of nested records/lists so callers cannot mutate internal data.
- Accept the CSV path from `sys.argv`.
- Define a deterministic tie policy for equal highest scores and document it.

## Retrieval-practice quiz

1. What is the implicit return value of a function with no `return`?
2. Why should the analysis function not print?
3. What invariant proves the best-record scan correct?
4. What are the scan's time and auxiliary-space complexities?
5. Why does an evaluation report need its sample count?

## Quiz answers

1. `None`.
2. Returning data makes it reusable and independently checkable; presentation
   belongs at a separate boundary.
3. After \(k\) items, `best` is a processed record with a comparison value at
   least as large as every other processed record.
4. \(O(n)\) time and \(O(1)\) auxiliary space.
5. A metric's evidential strength and interpretation depend on how many examples
   contributed to it.

## Suggested 65–80 minute study plan

- 0–7: retrieval review and run the example.
- 7–17: inspect the example's computation/presentation boundaries.
- 17–25: write the exact report dictionary contract.
- 25–55: edit the existing pipeline and validate the normal run.
- 55–65: create and run one malformed row case.
- 65–72: reading and quiz.
- 72–80: save outputs and reflection.

## Submission checklist

- completed `lesson_09_score_pipeline.py`;
- `lesson-09-reflection.md` with the valid and malformed commands/output;
- answers to the Lesson 15 quiz;
- one sentence stating the return contract of each meaningful function.
