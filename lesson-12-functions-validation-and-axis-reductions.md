# Lesson 12 — From NumPy Matrices to pandas DataFrames

**Module:** Foundation path — Python, NumPy, pandas, and SQL

**Estimated time:** 75–90 minutes

**Difficulty:** Introductory pandas, intermediate data reasoning

## Why this lesson is next

You completed Lesson 11's central matrix pipeline: two-dimensional data,
axis-wise means, aligned filtering, `argmax`, and feature-wise standardization.
Lesson 12 keeps the familiar `exams.csv` facts but introduces one new
representation: a pandas `DataFrame` with labeled rows and columns.

The assignment remains problem-first. No starter architecture, function
signatures, solution, or tests are supplied.

## Learning objectives and prerequisites

By the end, you should be able to:

1. load a CSV into a `DataFrame` and inspect shape, columns, and dtypes;
2. distinguish a two-dimensional `DataFrame` from a one-dimensional `Series`;
3. select numeric columns by label and reduce across columns or rows;
4. create derived columns and filter complete rows with a Boolean Series;
5. recover a complete extreme row while retaining its labels;
6. validate schema, missing values, numeric types, ranges, and uniqueness;
7. relate pandas filtering to NumPy masks and SQL `WHERE`.

Prerequisites: Lesson 11, Python functions and dictionaries, CSV validation,
and the meaning of rows, columns, means, and standardization.

## Retrieval review

1. What did rows and columns represent in the Lesson 11 matrix?
2. Why did one Boolean mask preserve name/score alignment?
3. What did `axis=0` and `axis=1` compute?
4. What did `argmax` return, and why was that position useful?

## Python/pandas instruction and executable example

Run:

```bash
python3 lesson-12-reliable-array-example.py
```

The independent response-time example demonstrates the new objects:

- a `DataFrame` is a labeled two-dimensional table;
- selecting one column normally returns a `Series`;
- comparing a Series produces an index-aligned Boolean Series;
- filtering the DataFrame keeps complete rows together;
- `groupby` performs split–apply–combine aggregation.

Unlike parallel NumPy arrays, a DataFrame can store names and numeric columns
in one table. Labels clarify intent, but you must still inspect `.shape`,
`.columns`, `.dtypes`, missing values, and row identity.

## Mathematics: familiar reductions with labels

pandas does not change the mathematics. For Alice, the row mean remains
`(88 + 91) / 2 = 89.5`. The complete student-mean sequence remains:

```text
89.5, 73.5, 97.0, 82.5, 91.0
```

Reducing down rows produces one statistic per selected column. Reducing across
selected columns produces one statistic per row. Explicitly name the numeric
columns so an identifier such as `Name` is never included in arithmetic.

## Machine-learning connection

A DataFrame commonly stages data before creating feature matrix `X` and target
vector `y`. Labels document feature meaning, but they do not prevent leakage.
A derived column built from a future outcome could make evaluation look
excellent while being unavailable at prediction time. Before fitting, separate
identifiers, features, targets, and post-outcome data deliberately. Learn
scaling or imputation parameters from training data only.

## Algorithms and data structures

A DataFrame combines column labels, an index, and column arrays. Filtering `n`
rows remains `O(n)` time and uses an `O(n)` Boolean mask. Correctness requires
one mask decision per row; applying the aligned mask to the whole DataFrame
returns precisely the qualifying complete records. Sorting all rows for one
maximum costs `O(n log n)`; a direct maximum-index scan is `O(n)`.

## Technical reading

Read the official pandas tutorials:

- [What kind of data does pandas handle?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)
- [How do I select a subset of a DataFrame?](https://pandas.p/pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html)

Guiding questions:

1. What is the difference between a `Series` and a `DataFrame`?
2. What does selecting a single column return?
3. Why must a Boolean filter have one decision per row?
4. How do column labels reduce—but not remove—alignment mistakes?
5. Which inspection output reveals that numeric data loaded as text?

## Integrated coding exercise: pandas exam report

Create `lesson_12_pandas_exam_report.py` using `exams.csv`. Design the program
yourself; do not copy Lesson 11's architecture automatically.

### Required behavior

1. Load with pandas and require exactly `Name`, `Exam1`, and `Exam2`.
2. Reject empty data, blank/missing names, missing or nonnumeric exams,
   duplicate names, and scores outside `0..100` with clear errors.
3. Display shape, column labels, and dtypes after validation.
4. Compute the two exam means using labeled column selection.
5. Create `StudentMean` from Exam1 and Exam2 without a Python row loop.
6. Identify the complete top-student row without sorting the entire table.
7. Filter complete rows whose `StudentMean` is at least 85.
8. Create `PerformanceBand`: `Excellent` for at least 90, `Strong` for at
   least 85 but below 90, and `Developing` below 85.
9. Produce a band summary with student count and mean `StudentMean` per band.
10. Separate loading/validation, analysis, and presentation meaningfully; print
    only when executed as a program.

Do not use a Python loop for row means, filtering, band assignment, or the top
student. A short schema-validation or presentation loop is acceptable.

### Expected facts

```text
Shape immediately after loading: (5, 3)
Exam means: Exam1 85.4, Exam2 88.0
Top student: Sarah 97.0
At least 85: Alice, Sarah, Emma
Bands: Excellent 2, Strong 1, Developing 2
```

The analyzed table has five columns after adding `StudentMean` and
`PerformanceBand`.

### Acceptance criteria

- `python3 lesson_12_pandas_exam_report.py` succeeds on `exams.csv`.
- All expected facts above are correct.
- Numeric calculations explicitly select `Exam1` and `Exam2`.
- The qualifying result contains complete rows, not independently filtered
  columns.
- The top row retains Sarah's name and both original scores.
- The band summary has exactly three rows and correct counts.
- Analysis does not mutate a caller's input DataFrame.
- One malformed-input run demonstrates deliberate validation.

### Optional stretch goals

- Reproduce the at-least-85 filter as a SQLite query.
- Compare label-preserving maximum lookup with NumPy `argmax`.
- Add `Exam3` and identify which operations generalize automatically.

## Retrieval-practice quiz

1. What does selecting one DataFrame column normally return?
2. Why select exam columns explicitly before calculating a mean?
3. What is the pandas analogue of a NumPy Boolean row mask?
4. Why is sorting unnecessary for one maximum row?
5. How can a derived column cause ML leakage?

## Quiz answers

1. A one-dimensional `Series`.
2. To exclude identifiers and unrelated columns and preserve meaning.
3. An index-aligned Boolean Series.
4. Direct maximum-index lookup is `O(n)` rather than `O(n log n)` sorting.
5. It may encode target or post-outcome information unavailable at prediction
   time.

## Suggested 75–90 minute study plan

- 0–10: retrieval review and run the example.
- 10–22: inspect DataFrame, Series, labels, dtypes, and filtering.
- 22–32: reading and guiding questions.
- 32–65: implement the valid report independently.
- 65–75: add validation and run one malformed case.
- 75–90: quiz, reflection, and NumPy-versus-pandas comparison.

## Submission checklist

- `lesson_12_pandas_exam_report.py`;
- valid terminal output;
- one saved malformed-input command and error;
- `lesson-12-reflection.md` with reading answers, quiz attempts, and a short
  comparison of NumPy arrays with pandas DataFrames.
