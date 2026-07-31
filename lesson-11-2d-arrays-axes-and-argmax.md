# Lesson 11 — 2-D NumPy Arrays, Axes, and `argmax`

**Module:** Week 2 — From core Python data pipelines to NumPy  
**Estimated time:** 70–85 minutes  
**Difficulty:** Introductory/intermediate NumPy  

## Why this lesson is next

Your new `lesson_4_numpy.py` correctly uses simple and compound Boolean masks.
Your updated `lesson_3_numpy_intro.py` also constructs a 2-D array and correctly
reports its shape, dtype, and number of dimensions. That is enough evidence to
move from inspecting a matrix to computing along its axes.

The larger Lesson 10 program and its validation evidence are not present, so
this lesson keeps the data small and the coding target narrow. It does not yet
introduce Pandas or model fitting.

## Learning objectives

By the end, you should be able to:

1. interpret rows, columns, shape, and axes in a 2-D NumPy array;
2. compute column-wise and row-wise statistics with `axis`;
3. use `argmax` to recover the position associated with an extreme value;
4. apply a row mask without breaking alignment with a names array;
5. explain why feature columns must remain semantically aligned in ML;
6. analyze full scans and explain why vectorization does not change Big-O.

## Prerequisites

- 1-D NumPy arrays, metadata, and Boolean masks
- CSV parsing and numeric conversion
- arithmetic mean
- aligned names and numeric observations

## Retrieval warm-up

Answer before running code:

1. What array does `(scores >= 80) & (scores <= 90)` produce?
2. Why must NumPy conditions use `&` here instead of Python's `and`?
3. For a matrix with 5 students and 2 exams, what should its shape be?
4. Which metadata attribute tells you the number of axes?

## Python instruction and executable example

Run:

```bash
python3 lesson-11-axis-example.py
```

For this matrix:

```python
scores = np.array([
    [88, 91],
    [72, 75],
    [96, 98],
])
```

- `scores.shape` is `(3, 2)`: three rows and two columns.
- `scores.mean(axis=0)` collapses the row axis and returns one mean per column.
- `scores.mean(axis=1)` collapses the column axis and returns one mean per row.

A useful verbal rule is: **the named axis is the one that disappears**.

`np.argmax(values)` returns a position, not the value itself. If `averages`
contains one value per student, then:

```python
best_index = np.argmax(averages)
best_name = names[best_index]
best_average = averages[best_index]
```

This is the array version of preserving record identity during a maximum scan.

## Mathematics: averaging by axis

Let \(X\in\mathbb{R}^{n\times d}\), where row \(i\) is one observation and
column \(j\) is one feature. Define \(x_{ij}\) as the value in row \(i\),
column \(j\).

The mean of feature \(j\) is

\[
\mu_j=\frac{1}{n}\sum_{i=1}^{n}x_{ij}.
\]

This fixes a column and averages down its rows, corresponding to
`X.mean(axis=0)`.

For

\[
X=\begin{bmatrix}80&90\\70&100\\90&80\end{bmatrix},
\]

the column means are

\[
\mu_1=(80+70+90)/3=80,\qquad
\mu_2=(90+100+80)/3=90.
\]

The mean of row \(i\) is

\[
\bar{x}_i=\frac{1}{d}\sum_{j=1}^{d}x_{ij},
\]

which corresponds to `X.mean(axis=1)`. The row means above are \(85,85,85\).
The same numbers can therefore produce different outputs depending on which
index is held fixed.

## Machine-learning connection

In the usual supervised-learning design matrix, rows are samples and columns
are features. Column-wise means and standard deviations are used to scale each
feature. Row-wise averaging instead mixes different features within each
sample, usually changing the meaning of the data.

This distinction affects model behavior:

- scaling with the wrong axis gives every sample its own transformation rather
  than putting each feature on a comparable training-set scale;
- swapping columns changes which learned coefficient or split corresponds to
  which feature;
- removing rows from `X` without applying the same mask to target array `y`
  pairs features with the wrong outcomes.

In a later fitted workflow, training data must determine column statistics;
validation and test rows reuse those statistics to prevent leakage.

## Algorithms and data structures: maximum with its index

Finding the largest value in an unsorted length-\(n\) array requires inspecting
all \(n\) values in the worst case. `np.argmax` therefore takes \(O(n)\) time
and \(O(1)\) auxiliary space conceptually for the running best position (apart
from library-level details). Sorting first would take \(O(n\log n)\) time and
is unnecessary when only one maximum is needed.

**Correctness invariant:** after inspecting positions `0` through `k`, the
stored best index points to a maximum among exactly those positions. Comparing
position `k + 1` either preserves that index or replaces it with the new
maximum. At termination it points to a maximum of the entire array.

NumPy performs the scan in compiled code, but the asymptotic cost remains
\(O(n)\).

## Technical reading

Read NumPy's sections on
[array axes](https://numpy.org/doc/stable/user/absolute_beginners.html#what-are-the-attributes-of-an-array)
and
[aggregation](https://numpy.org/doc/stable/user/absolute_beginners.html#more-useful-array-operations).

Guiding questions:

1. For shape `(5, 2)`, what does each dimension count?
2. What output shapes result from `mean(axis=0)` and `mean(axis=1)`?
3. Why does specifying `axis` change the meaning, not merely the format?
4. What does `argmax` return?
5. When would `keepdims=True` make later broadcasting easier?

## Integrated coding exercise: exam matrix report

Create `lesson_11_exam_matrix.py`. Choose the program structure yourself; no
starter or tests are supplied.

### Input

Use `exams.csv`, with required columns `Name`, `Exam1`, and `Exam2`. Parse the
file once, then create:

- one 1-D array of names;
- one 2-D numeric array with one student per row and one exam per column.

### Required behavior

Your program must:

1. reject missing columns, empty data, blank names, non-integer scores, scores
   outside 0–100, and malformed row widths with a clear error;
2. verify that the number of names equals the number of matrix rows;
3. print the matrix shape, dimensions, and dtype;
4. compute and print the mean of each exam with `axis=0`;
5. compute and print each student's mean with `axis=1`;
6. use `argmax`, without sorting, to print the top student's name and mean;
7. construct one row mask for students whose mean is at least 85 and apply it
   to both names and score rows;
8. compute column-standardized exam scores without Python loops over the
   matrix, rejecting any zero-variance exam column;
9. place substantial logic in at least three meaningful functions;
10. print only when the file is run as a program.

For the supplied data, key results are:

```text
Shape: (5, 2)
Exam means: [85.4 88. ]
Student means: [89.5 73.5 97.  82.5 91. ]
Top student: Sarah 97.0
At least 85: Alice, Sarah, Emma
```

### Acceptance criteria

- `python3 lesson_11_exam_matrix.py` succeeds on `exams.csv`.
- The valid results above are present and correct.
- The score matrix has shape `(5, 2)`, not `(2, 5)`.
- Axis 0 produces two exam means; axis 1 produces five student means.
- One mask filters aligned names and rows.
- Column-standardized values have column means near 0 and population standard
  deviations near 1.
- A saved malformed-input run demonstrates deliberate validation.
- No sorting or manual matrix loop is used for the maximum, aggregation,
  filtering, or standardization.

### Optional stretch goals

- Add a third exam column without changing the aggregation logic.
- Report the best student on each individual exam using `argmax(axis=0)`.
- Accept an input path using `argparse`.
- Compare `keepdims=False` and `keepdims=True` during standardization.

## Retrieval-practice quiz

1. What does shape `(5, 2)` mean?
2. Which axis gives one mean per exam?
3. Which axis gives one mean per student?
4. What does `argmax` return?
5. Why must a student mask be applied to both names and matrix rows?
6. What are the time complexities of `argmax` and sorting?
7. In ML, what do rows and columns conventionally represent?

## Quiz answers

1. Five rows and two columns.
2. `axis=0`.
3. `axis=1`.
4. The position of a maximum value.
5. To preserve each name's association with the correct score row.
6. \(O(n)\) and \(O(n\log n)\), respectively.
7. Samples and features, respectively.

## Suggested 70–85 minute study plan

- 0–8 minutes: retrieval warm-up.
- 8–20 minutes: run and modify the example; predict shapes before printing.
- 20–30 minutes: work the two axis calculations by hand.
- 30–38 minutes: complete the reading and guiding questions.
- 38–68 minutes: implement the exam matrix report.
- 68–76 minutes: verify valid output and one malformed case.
- 76–85 minutes: quiz and short reflection.

## Submission checklist

Save:

- `lesson_11_exam_matrix.py`;
- valid terminal output;
- `lesson-11-reflection.md` containing one malformed-input run, answers to the
  five reading questions, an explanation of the axis rule, quiz attempts, and
  whether the workload felt too short, appropriate, or too long.
