# Lesson 9 — From a Working Script to a Single-Pass CSV Pipeline

**Module:** Week 2 — Python problem solving for machine learning  
**Estimated time:** 75–90 minutes  
**Difficulty:** Intermediate core Python

## Why this is the next lesson

Your `lesson_2_csv.py` is valid completion evidence: it reads `scores.csv`,
converts score strings to integers, extracts names, and filters high scores.
The next skill is not another CSV syntax exercise. It is turning repeated
top-level code into a program whose parts can be reused, reasoned about, and
changed independently.

Do not modify `lesson_2_csv.py`; keep it as a before-refactoring artifact.

## Learning objectives

By the end of this lesson, you should be able to:

1. separate file loading, computation, and presentation;
2. use `csv.DictReader` to access columns by header name;
3. validate a row before using its values;
4. compute several summary quantities during one traversal;
5. explain why a one-pass maximum scan is correct and \(O(n)\);
6. connect clean data pipelines to reliable ML feature and label construction.

## Prerequisites

- opening a file with `with`
- `csv.reader`, loops, lists, dictionaries, and functions
- numeric conversion with `int` or `float`
- arithmetic mean and comparison operators

## Python instruction and executable example

A useful pipeline separates three responsibilities:

```text
load and validate -> transform or summarize -> format and print
```

Run:

```bash
python3 lesson-09-streaming-example.py
```

The example analyzes inventory records rather than student scores, so it
demonstrates the pattern without supplying the assignment solution. Notice that
the summarizer receives ordinary Python records and knows nothing about files.
That separation makes it possible to reuse it with records from a CSV file,
database, API, or test case.

`csv.reader` returns positional rows such as `["Alice", "87"]`.
`csv.DictReader` returns rows such as `{"Name": "Alice", "Score": "87"}`.
Header-based access is usually clearer and is less fragile if column order
changes. CSV values are still strings, so conversion remains your
responsibility.

## Mathematics: online aggregation

For values \(x_1,\ldots,x_n\), define the running count and sum after \(k\)
observations:

\[
n_k=k,\qquad S_k=\sum_{i=1}^{k}x_i.
\]

When a new value \(x_{k+1}\) arrives:

\[
n_{k+1}=n_k+1,\qquad S_{k+1}=S_k+x_{k+1}.
\]

The mean is computed after the scan:

\[
\bar{x}=\frac{S_n}{n}.
\]

Worked derivation for scores \(87,92,75\):

\[
S_1=87,\quad S_2=87+92=179,\quad S_3=179+75=254,
\]

\[
\bar{x}=\frac{254}{3}\approx84.67.
\]

Intuition: the complete list is not mathematically necessary for count, sum,
mean, minimum, or maximum. A small amount of state can summarize everything
seen so far. For this lesson, keep the records because the report also needs
names and filtered results, but recognize which metrics could be streamed.

## Machine-learning connection

An ML pipeline eventually converts raw rows into:

- **features**, the input values used to make predictions;
- **labels**, the outcomes the model should predict;
- **metadata**, such as a name or identifier used for reporting but not
  necessarily for training.

CSV parsing mistakes change model behavior before training even begins. Reading
the wrong column, leaving numbers as strings, silently skipping malformed rows,
or separating names from scores inconsistently can corrupt features, labels, or
their alignment. A loader with a clear contract creates a trustworthy boundary
between raw data and later modeling code.

The mean score also acts as a constant prediction baseline. A more complex
model is useful only if its honest evaluation improves on an appropriate
baseline; a clean pipeline is therefore part of model evaluation, not merely
file-handling boilerplate.

## Algorithms and data structures: a one-pass maximum

To find the highest-scoring record, maintain one candidate.

**Loop invariant:** after processing \(k\) valid records, the candidate has a
score at least as large as every score among those \(k\) records.

Initialization is true after the first record. On each later record, replace
the candidate only if the new score is larger. The invariant is preserved, so
after all \(n\) records the candidate is a maximum.

- time: \(O(n)\)
- extra space for the candidate: \(O(1)\)
- sorting instead: \(O(n\log n)\) time

A dictionary is a natural record structure because `"Name"` and `"Score"`
identify fields by meaning. Dictionary lookup is \(O(1)\) expected time.

## Technical reading

Read the Python documentation for
[`csv.reader` and `csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader),
especially the descriptions of returned row types and numeric conversion.
Then skim Google’s explanation of
[numerical features and feature vectors](https://developers.google.com/machine-learning/crash-course/numerical-data/feature-vectors).

Guiding questions:

1. Why should a CSV file be opened with `newline=""`?
2. Does `DictReader` automatically convert `"87"` into `87`?
3. What advantage does a field name have over `row[1]`?
4. Which value in `scores.csv` could be a feature, a label, or metadata in
   different ML problems?

## Integrated coding exercise: score-report refactor

Create a new file named `lesson_09_score_pipeline.py`. Do not begin from a
provided starter, signatures, TODO list, or supplied tests. Choose your own
functions and control flow.

Input: the existing `scores.csv`.

Required behavior:

1. Open the CSV only once.
2. Use `csv.DictReader`.
3. Require the columns `Name` and `Score`.
4. Convert every score to an integer.
5. Reject an empty data file with a clear error.
6. Reject a missing/blank name or a non-integer score with a message that
   identifies the data row.
7. Produce a report containing:
   - number of valid students;
   - mean score, rounded to two decimal places;
   - highest-scoring student's name and score;
   - names of students scoring strictly above the mean, in input order;
   - counts in these bands: `90–100`, `80–89`, `70–79`, and `below 70`.
8. Put the substantial logic in at least three meaningful functions.
9. Print the report only when the file is run as a program.

For the supplied data, your report must contain these facts (format is your
choice):

```text
Count: 7
Mean: 84.29
Highest: Emma (98)
Above mean: Alice, Bob, Emma, Grace
90-100: 2
80-89: 3
70-79: 1
Below 70: 1
```

### Acceptance criteria

- `python3 lesson_09_score_pipeline.py` exits successfully on `scores.csv`.
- The report contains all expected facts above.
- The file is opened once; no second parsing pass is used.
- Changing the CSV row order does not break name/score pairing.
- Scores below `0` or above `100` are rejected clearly.
- An empty file, missing column, blank name, and invalid score are handled.
- Computation functions return values; they do not depend on global mutable
  lists.
- Existing Lesson 8 and earlier artifacts are not overwritten.

### Optional stretch goals

- Accept the CSV path from `sys.argv`.
- Add a median score; explain why this requires different state or sorting.
- Write a second valid CSV with reordered columns and demonstrate that the
  program still works.
- After finishing, ask for acceptance tests and compare them with your design.

## Retrieval-practice quiz

1. Why are the score values from a CSV initially strings?
2. State the running-sum update equations.
3. Why does a maximum scan not require sorting?
4. What is the expected time for dictionary lookup?
5. Give one way a parsing bug can change an ML model's apparent quality.
6. Why put printing outside the main computation functions?

## Quiz answers

1. CSV is a text format, and the standard reader does not infer ordinary
   numeric types.
2. \(n_{k+1}=n_k+1\) and \(S_{k+1}=S_k+x_{k+1}\).
3. Keeping the largest item seen so far finds one maximum in \(O(n)\).
4. \(O(1)\) expected.
5. It can change a feature or label, skip observations, or misalign inputs and
   outcomes, producing a misleading metric.
6. Separation makes computation reusable and easier to inspect independently
   of the terminal format.

## Suggested 75–90 minute study plan

- 0–8 minutes: run and predict the executable example.
- 8–18 minutes: read the specification and inspect `scores.csv`.
- 18–25 minutes: sketch inputs, outputs, and responsibilities on paper.
- 25–60 minutes: implement the pipeline independently.
- 60–72 minutes: run it and debug against the expected facts.
- 72–80 minutes: manually create and try one malformed CSV case.
- 80–86 minutes: complete the reading and guiding questions.
- 86–90 minutes: answer the retrieval quiz and write a short reflection.

## Submission

Save:

- `lesson_09_score_pipeline.py`;
- terminal output from the valid dataset;
- `lesson-09-reflection.md` with:
  1. the hardest design or debugging decision;
  2. why the original script opened the file three times and how the new design
     avoids that repetition;
  3. one malformed-input case you ran and its output;
  4. whether the implementation time felt too short, appropriate, or too long.

