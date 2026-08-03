# Lesson 13 — Schema-Driven CSV Parsing and Residual Bias

**Module:** Reliable Python data pipelines  
**Estimated time:** 75–90 minutes  
**Difficulty:** Introductory/intermediate

## Why this lesson is next

Your new `lesson_8_csv_code.py` reaches the first data row, but stops at
`int("3.5")`. The useful next step is not another tour of CSV syntax: it is to
encode each column's contract once, parse rows by header name, and finish a
small prediction-evaluation pipeline. Lesson 12's NumPy refactor remains active;
this lesson gives you a separate core-Python route to practice functions and
validation without introducing Pandas.

## Learning objectives and prerequisites

By the end, you should be able to:

1. explain why numeric text must be parsed according to a field contract;
2. use `csv.DictReader` without depending on column positions;
3. store parser functions in a dictionary and look them up by field name;
4. validate a complete row before adding it to the dataset;
5. compute predictions, residuals, MSE, and mean residual without losing alignment;
6. find the largest-error record with one linear scan.

Prerequisites: functions, dictionaries, exceptions, CSV iteration, arithmetic
mean, and squared error. You do not need NumPy for this lesson.

## Python instruction and executable example

Run:

```bash
python3 lesson-13-schema-example.py
```

The central pattern is a schema dictionary:

```python
PARSERS = {"hours": float, "attendance": int, "actual_score": int}
```

`PARSERS[field](text)` first looks up the correct conversion function, then
calls it. This accepts decimal hours while retaining whole-number contracts for
attendance and scores. Parsing and range validation are different operations:
`float("-2.5")` succeeds, but a nonnegative-hours rule should still reject it.

Catch a conversion error only where you can add useful context such as the row
number and field name. Do not catch every exception and silently continue.

## Mathematics: residual bias

For actual value \(y_i\) and prediction \(\hat y_i\), define the residual

\[
r_i = y_i-\hat y_i.
\]

The mean residual is \(\bar r=\frac1n\sum_i r_i\). A positive value means the
model underpredicts on average; a negative value means it overpredicts on
average, under this sign convention.

Suppose every prediction is corrected by the same constant \(c\):
\(\hat y_i'=\hat y_i+c\). Then

\[
r_i'=y_i-(\hat y_i+c)=r_i-c,
\qquad
\bar r'=\frac1n\sum_i(r_i-c)=\bar r-c.
\]

Choosing \(c=\bar r\) makes the corrected mean residual zero. For example, if
residuals are \([-2,1,-2]\), then \(\bar r=-1\). Subtracting 1 from every
prediction is the same as adding \(c=-1\), producing residuals \([-1,2,-1]\)
whose mean is zero.

This does **not** prove the model is accurate: positive and negative errors can
cancel. Report MSE alongside mean residual because MSE measures error magnitude
after squaring.

## Machine-learning theory connection

The supplied rule

\[
\hat y = 30 + 6(\text{hours}) + 0.25(\text{attendance})
\]

is a linear model with fixed coefficients. A one-unit increase in hours changes
the prediction by 6 points when attendance is held fixed. A one-point increase
in attendance changes it by 0.25 points when hours are held fixed.

Reliable parsing affects model behavior directly. Parsing `3.5` incorrectly,
truncating it to `3`, or skipping that row changes both its prediction and the
evaluation denominator. A metric can be numerically correct for the wrong data,
which is why validation belongs before evaluation.

## Algorithms and data structures: schema lookup and maximum scan

A dictionary maps each required header to its parser. With \(d\) required
fields, validating the header set costs \(O(d)\). Each dictionary lookup is
average-case \(O(1)\), so parsing \(n\) rows and \(d\) fields costs \(O(nd)\)
time. Storing all records costs \(O(nd)\) space.

To find the record with the largest squared error, keep one `worst` record and
scan the results once. The invariant is: after processing \(k\) records,
`worst` has the largest squared error among those \(k\). This costs \(O(n)\)
time and \(O(1)\) auxiliary space; sorting would unnecessarily cost
\(O(n\log n)\).

## Technical reading

Read the Python documentation for
[`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader)
and the Google Machine Learning Crash Course section on
[linear regression](https://developers.google.com/machine-learning/crash-course/linear-regression).

Guiding questions:

1. Where does `DictReader` obtain dictionary keys?
2. What happens when a row contains more fields than the header?
3. In the supplied prediction rule, which values are features and which are parameters?
4. Why can mean residual be near zero while MSE is large?

## Integrated coding exercise: finish the prediction evaluator

Continue your existing `lesson_8_csv_code.py`; do not create a replacement
just to avoid the current error. Choose your own function names and structure.

Required behavior:

1. Use `csv.DictReader` and require exactly `name`, `hours`, `attendance`, and
   `actual_score` (order need not matter).
2. Use a dictionary that maps numeric field names to parser functions.
3. Accept decimal hours, including `3.5` and `4.5`; require integer attendance
   and actual scores.
4. Reject blank names, negative or non-finite hours, attendance outside 0–100,
   scores outside 0–100, missing/extra cells, empty data, and invalid numbers.
5. Separate loading, evaluation, and presentation into at least three
   meaningful functions. Loading and evaluation return values rather than print.
6. Compute each prediction using `30 + 6 * hours + 0.25 * attendance`.
7. Preserve each student's name with the prediction, residual, and squared error.
8. Report count, MSE, mean residual, within-five count, and the name of the
   largest-squared-error record.
9. Put execution behind `if __name__ == "__main__":`.
10. Save `lesson-13-reflection.md` with one valid run, one deliberate malformed
    run, reading answers, and a two-sentence explanation of the residual sign.

### Acceptance criteria

- `python3 -m py_compile lesson_8_csv_code.py` passes.
- The valid run prints eight aligned student rows.
- Summary values are: count `8`, MSE `4.234375`, mean residual `-1.75`,
  within-five count `8`, and worst record `Ben`.
- Grace's prediction is `71.25`; Hugo's prediction is `80.5`.
- A malformed file raises a clear error containing useful row/field context.
- No Pandas, NumPy, or scikit-learn is used.

Optional stretch goals:

- Allow a caller to supply a different schema dictionary.
- Stream the summary using running totals instead of retaining all result rows.
- Write one small test for decimal hours and one for a missing field.

## Retrieval-practice quiz

1. Why does `int("3.5")` fail while `float("3.5")` succeeds?
2. What is the residual sign when an actual value is below its prediction?
3. What does a negative mean residual suggest under \(y-\hat y\)?
4. Why is a parser dictionary preferable to repeating a long field-name conditional?
5. What is the complexity of parsing \(n\) rows with \(d\) required fields?

## Quiz answers

1. `3.5` is valid floating-point syntax but not integer syntax.
2. Negative.
3. The model overpredicts on average.
4. It centralizes the contract and provides average \(O(1)\) parser lookup.
5. \(O(nd)\) time.

## Suggested 85-minute study plan

- **0–8 min:** reproduce the current error and predict its cause.
- **8–20 min:** run the example and read the two documentation sections.
- **20–32 min:** work the residual-correction derivation and two residuals by hand.
- **32–62 min:** refactor loading and implement the evaluator.
- **62–75 min:** add validation and trigger one deliberate failure.
- **75–85 min:** check exact acceptance values and write the reflection.
