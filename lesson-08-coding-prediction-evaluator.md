# Lesson 8 — Code a Prediction Evaluator

**Module:** Week 2 — Python problem solving for machine learning  
**Estimated time:** 70–90 minutes  
**Difficulty:** Intermediate Python, gentle ML

## Why this lesson

You already understand mean and mean squared error. This lesson supplies those
calculations and puts the challenge where you want it: turning requirements into
working Python.

You will build a small prediction-evaluation program using functions, loops,
lists, dictionaries, validation, and a linear scan. No Pandas, NumPy,
scikit-learn, or model fitting is required.

## Learning objectives

By the end, you should be able to:

1. translate a written function contract into code;
2. traverse a list of dictionaries safely;
3. produce a new list without changing the input;
4. combine related values into report dictionaries;
5. validate parallel lists and raise useful errors;
6. find a maximum item with a linear scan;
7. explain how the resulting code supports ML evaluation.

## Prerequisites

- functions, parameters, return values
- `for` loops and conditionals
- lists and dictionaries
- `append`, `len`, and `range`
- basic understanding of prediction error and MSE

## Retrieval warm-up

Predict the output before running this:

```python
records = [{"name": "A", "score": 70}, {"name": "B", "score": 82}]
results = []

for record in records:
    results.append(record["score"] + 5)

print(results)
print(records)
```

Questions:

1. Why does `records` remain unchanged?
2. What type is `record` during each iteration?
3. What would happen if one dictionary lacked `"score"`?

## The mini-project

The starter contains these records:

```python
STUDENTS = [
    {"name": "Amina", "hours": 1, "actual_score": 55},
    {"name": "Ben", "hours": 2, "actual_score": 60},
    {"name": "Chen", "hours": 3, "actual_score": 68},
    {"name": "Dalia", "hours": 4, "actual_score": 74},
    {"name": "Eli", "hours": 5, "actual_score": 82},
    {"name": "Fatima", "hours": 6, "actual_score": 88},
]
```

The supplied prediction rule is:

```python
predicted_score = 48 + 7 * hours
```

The rule is intentionally fixed. Your job is to build the surrounding evaluation
software, not derive or train a model.

## Python instruction: transform one collection into another

Many data-science programs follow this pattern:

```python
output = []
for item in input_items:
    new_item = ...  # compute something from item
    output.append(new_item)
return output
```

Run the small pattern example:

```bash
python3 lesson-08-transformation-example.py
```

It demonstrates the pattern on temperatures, not student predictions, so it
does not solve your assignment.

Before coding each function, write:

- the type and meaning of each input;
- the exact return type;
- one hand-worked example;
- one condition that should cause an error.

## Mathematics supplied to you

For each observation:

\[
\text{error}=\text{actual}-\text{predicted}
\]

and

\[
\text{squared error}=(\text{actual}-\text{predicted})^2.
\]

The starter already provides a complete MSE function. You do not need to
reimplement it.

Worked example: if the actual score is `68` and the prediction is `69`, the
error is `-1` and the squared error is `1`.

## Machine-learning connection

Training produces a prediction rule. Evaluation code answers questions about
that rule:

- What did it predict for each observation?
- How wrong was each prediction?
- What is the average squared error?
- Which observation had the largest error?

Reliable evaluation depends on matching each prediction with the correct actual
value. A length check is therefore not cosmetic: silently dropping or
misaligning values can produce a believable but false metric.

## Algorithms: finding the worst prediction

To find the report row with the largest `"squared_error"`, scan once while
remembering the best candidate seen so far.

Loop invariant: after processing the first \(k\) rows, `worst` refers to a row
with the largest squared error among those \(k\) rows.

- Time: \(O(n)\)
- Extra space: \(O(1)\)

Sorting all rows would take \(O(n\log n)\) time and is unnecessary when you need
only one maximum.

## Technical reading

Read the Python tutorial sections on
[looping through dictionaries](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)
and the short Google explanation of
[prediction loss](https://developers.google.com/machine-learning/crash-course/linear-regression/loss).

Guiding questions:

1. When are `.items()` and `enumerate()` useful?
2. Why must actual and predicted values stay paired?
3. Why does squared error emphasize a large miss?

## Integrated coding assignment

Open `lesson-08-prediction-evaluator-starter.py`. The math helper and printing
code are provided. Implement four functions in order.

### Checkpoint 1 — `extract_values`

Contract:

```python
extract_values(records, key) -> list
```

Return the value associated with `key` from every record, in original order.
Do not modify `records`.

Example:

```python
extract_values([{"x": 2}, {"x": 5}], "x")  # [2, 5]
```

### Checkpoint 2 — `make_predictions`

Contract:

```python
make_predictions(records, intercept, hourly_gain) -> list
```

For each record, calculate:

```python
intercept + hourly_gain * record["hours"]
```

Return the predictions in the same order as the records.

### Checkpoint 3 — `build_evaluation_rows`

Contract:

```python
build_evaluation_rows(records, predictions) -> list[dict]
```

First raise `ValueError` if the lengths differ. Then create one new dictionary
per student containing exactly:

```python
{
    "name": ...,
    "actual": ...,
    "predicted": ...,
    "error": ...,
    "squared_error": ...,
}
```

Do not add fields to the original student dictionaries.

### Checkpoint 4 — `find_worst_prediction`

Contract:

```python
find_worst_prediction(evaluation_rows) -> dict
```

Raise `ValueError` for an empty list. Otherwise, use a linear scan to return the
row with the largest `"squared_error"`. Do not use `sorted`.

### Acceptance criteria

- All four functions satisfy their contracts.
- Input records remain unchanged.
- A prediction is produced for every record, in the same order.
- Mismatched lengths raise `ValueError`.
- Empty input to `find_worst_prediction` raises `ValueError`.
- The program runs with:

```bash
python3 lesson-08-prediction-evaluator-starter.py
```

- It prints six detailed evaluation rows, MSE, and the worst prediction.
- Save a short `lesson-08-reflection.md` answering:
  1. Which function was hardest to implement, and why?
  2. How did you decide what variables to keep inside your loop?
  3. Why is the worst-item scan \(O(n)\)?

### Built-in hints

Use these only when stuck:

1. `extract_values`: start with an empty result list.
2. `make_predictions`: calculate one prediction inside each loop iteration.
3. `build_evaluation_rows`: use an index to access both `records[i]` and
   `predictions[i]`.
4. `find_worst_prediction`: initialize the candidate from the first row, then
   compare each remaining row.

### Reduced path

If four functions are too much, submit Checkpoints 1 and 2 only. They form a
complete first coding block; the next lesson can continue from them.

### Stretch goals

- Add `validate_records` to check required keys and numeric values.
- Add `find_top_k_errors` without changing the core functions.
- Write assertion tests for each contract and error case.

## Retrieval quiz

1. Why should output order match input order?
2. Why check list lengths before pairing actual values and predictions?
3. What should `find_worst_prediction([])` do?
4. State the loop invariant for the worst-item scan.
5. Why is a single scan preferable to sorting when only one maximum is needed?

<details>
<summary>Answers</summary>

1. So each prediction stays aligned with its original observation.
2. A missing value would misalign or omit comparisons and corrupt evaluation.
3. Raise `ValueError`.
4. After \(k\) rows, the candidate is a maximum among those \(k\) rows.
5. A scan is \(O(n)\); sorting is \(O(n\log n)\).

</details>

## Suggested 70–90 minute plan

- 0–8: warm-up and run the transformation example
- 8–18: write contracts and hand-worked examples
- 18–30: Checkpoint 1
- 30–42: Checkpoint 2 and run partial checks
- 42–60: Checkpoint 3
- 60–72: Checkpoint 4
- 72–80: run the whole program and debug
- 80–90: reading, quiz, and reflection

## Submit

- `lesson-08-prediction-evaluator-starter.py`
- terminal output from the completed or reduced path
- `lesson-08-reflection.md`

