# September 2026 Independent Checkpoint — Model Evaluation Table

**Module:** Python, NumPy, pandas, and SQL foundations  
**Checkpoint window:** September 28–October 2, 2026  
**Monday session:** 60–90 minutes  
**Difficulty:** Moderate, limited scaffolding

## Purpose

Build one small, reliable analysis of a fresh model-evaluation dataset. This
checkpoint asks you to reuse skills from Lessons 11–12 without a starter file
or prescribed function names. It introduces no new major concept.

The table contains predictions from two models on validation and test rows.
`Actual` is the known target and `Predicted` is the model output. The operational
error formula is:

```text
AbsoluteError = abs(Actual - Predicted)
```

A smaller mean absolute error (MAE) means predictions are closer to the known
targets on average. Model selection should use validation data; test data is a
final, less-biased check rather than a tuning resource.

## Monday focused support — November 9

No checkpoint program, partial code, output, or traceback was available after
Friday. Keep this checkpoint as the only active assignment. Do not begin Lesson
13, SQL, or another project.

Today's concept is **make the input boundary observable before transforming the
table**. Use 60–90 minutes, but stop as soon as this small result works:

1. Create and save `september_checkpoint_model_report.py` immediately.
2. Load `september-checkpoint-model-results.csv` with pandas.
3. Print the loaded object's type, shape, and ordered column labels. Confirm
   shape `(12, 5)`.
4. Select the complete source row whose `RunID` is `r06` and print `RunID`,
   `Model`, `Split`, `Actual`, and `Predicted`. Confirm `Actual = 94` and
   `Predicted = 84`.
5. Run and save after steps 2–3 and again after step 4.

If a run fails or the values differ, preserve the partial file plus the first
complete traceback or incorrect output. That is a valid submission. Only if
the source row works, create one vectorized `AbsoluteError` column with the
operational rule `abs(Actual - Predicted)` and confirm `r06 = 10`.

Acceptance criteria:

- the saved script loads the supplied CSV rather than recreating its rows;
- the inspection output exposes type, shape, and ordered labels;
- the Boolean condition is applied to the whole DataFrame, preserving the
  complete `r06` record;
- the submitted evidence is working output or the first complete failure.

Retrieval check: before running, predict whether the row selection returns a
Series or a DataFrame, then compare that prediction with `type(...)` and
`.shape`. For `n` rows, the Boolean scan is `O(n)` time and the mask is `O(n)`
space. It mirrors `WHERE RunID = 'r06'` in SQL and preserves the row identity
needed for AI error analysis. Read the pandas
[`read_csv` documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
only to identify what object is returned and how the file path is supplied.

The 12-row report, ordered-schema rejection, grouping, `idxmax`, threshold
filtering, additional validation, reflection, and SQL remain deferred.

## Friday project milestone — November 6

No checkpoint program, partial code, output, or traceback was available after
Wednesday. Keep this checkpoint as the only active assignment. Do not begin
Lesson 13, grouping, SQL, or another project.

Use 90–120 minutes in short run-and-save cycles, but keep one artifact:
`september_checkpoint_model_report.py`.

1. Without running code, write the expected `r06` values: `Actual = 94`,
   `Predicted = 84`, and `AbsoluteError = 10`.
2. Create and save the script immediately.
3. Load `september-checkpoint-model-results.csv`; run the script and inspect the
   DataFrame type, shape, and column labels.
4. Create and assign `AbsoluteError` with vectorized subtraction and `.abs()`;
   run again and inspect the Series type, length, and index.
5. Select the complete row whose `RunID` is `r06`, then print only `RunID`,
   `Actual`, `Predicted`, and `AbsoluteError`. Run and confirm `94`, `84`, `10`.

If a run fails or the values differ, stop adding features and preserve the
partial file plus the first complete traceback or incorrect output. That is a
valid Friday submission and gives the next review a concrete debugging target.

Only if the one-row result works, extend the same file to print all 12 rows with
`RunID`, `Actual`, `Predicted`, and `AbsoluteError`. Confirm `r01 = 4` and
`r12 = 5`. Do not add the ordered-schema check, grouping, `idxmax`, threshold
filter, additional validation, reflection, or SQL in this session.

Acceptance criteria:

- one saved script is the only project artifact;
- pandas loads the supplied table and creates `AbsoluteError` without a row
  loop;
- the Boolean mask is applied to the whole DataFrame so the selected values
  remain attached to the `r06` record;
- the submitted evidence is correct output or the first complete failure.

For `n` rows, both vectorized error calculation and Boolean selection are
`O(n)` time. The derived column and mask use `O(n)` auxiliary space. In database
terms, the mask is the pandas equivalent of `WHERE RunID = 'r06'`; in an AI
evaluation table, preserving the full row prevents a prediction error from
being detached from its model run and split.

## Wednesday independent/debugging milestone — November 4

No checkpoint program, partial code, output, or traceback was available after
Monday. Keep this checkpoint as the only active assignment. Do not begin Lesson
13, grouping, SQL, or another project.

Use 60–90 minutes, but stop when this one-row pipeline works:

1. Without running code, write the expected `r06` values: `Actual = 94`,
   `Predicted = 84`, and `AbsoluteError = 10`.
2. Create and save `september_checkpoint_model_report.py`.
3. Load `september-checkpoint-model-results.csv`; inspect the resulting
   object's type, shape, and column labels.
4. Create and assign `AbsoluteError` with vectorized subtraction and `.abs()`;
   inspect the resulting Series type, length, and index.
5. Select the complete row whose `RunID` is `r06`, then print only `RunID`,
   `Actual`, `Predicted`, and `AbsoluteError`.

Run and save after steps 3, 4, and 5. If a run fails or the values differ, do
not add another feature: preserve the partial file and the first complete
traceback or incorrect output. That is sufficient evidence for targeted code
review. If the row is correct, submit the script and its output; do not expand
the task today.

Acceptance criteria for this milestone:

- the script uses pandas to load the supplied file;
- `AbsoluteError` is a labeled, vectorized column rather than a row loop;
- the printed result is one complete `r06` row with values `94`, `84`, and
  `10`;
- the submitted evidence is either correct output or the first complete
  failure, not an unsaved description of the problem.

Retrieval check: explain in one sentence why applying the `RunID == "r06"`
Boolean mask to the whole DataFrame preserves all four requested fields from
the same model run. For `n` rows, both the vectorized error calculation and the
mask scan are `O(n)` time and use `O(n)` auxiliary space for the derived column
and mask. This mirrors a database `WHERE RunID = 'r06'` filter and preserves
the record identity needed in an AI error-analysis table.

## Friday project support milestone — October 23

No checkpoint program, partial implementation, traceback, saved output, or
reflection was available after Wednesday. Continue this checkpoint as the only
active project. Do not begin Lesson 13, the SQL translation, or a second
assignment.

Use 90–120 minutes in short run-and-save cycles:

1. From memory, calculate the absolute errors for `r01`, `r06`, and `r12`.
2. Create and save `september_checkpoint_model_report.py` immediately.
3. Load `september-checkpoint-model-results.csv` and print its shape and ordered
   column labels.
4. Reject the file unless its ordered labels are exactly `RunID`, `Model`,
   `Split`, `Actual`, and `Predicted`.
5. Create `AbsoluteError` with labeled Series subtraction and `.abs()`; assign
   the Series as one new DataFrame column.
6. Print only `RunID`, `Actual`, `Predicted`, and `AbsoluteError`. Confirm 12
   complete rows and the three hand-calculated values: `r01 = 4`, `r06 = 10`,
   and `r12 = 5`.

Run after steps 3, 4, and 6. If a run fails, stop adding features and save the
partial file plus the first complete traceback or incorrect output. That is
valid review evidence. If the 12-row table works, use the remaining time to add
the already-specified two-key `Model`/`Split` count-and-mean summary. Defer
`idxmax`, threshold filtering, additional validation, reflection, and SQL until
this artifact has been reviewed.

## Monday task: inspect, validate, and build the pandas result

Create `september_checkpoint_model_report.py` and use
`september-checkpoint-model-results.csv`.

Your program must:

1. Load the CSV with pandas.
2. Require exactly these columns in this order: `RunID`, `Model`, `Split`,
   `Actual`, `Predicted`.
3. Reject empty data, missing values, duplicate `RunID` values, blank model
   names, splits other than `validation` or `test`, and nonnumeric actual or
   predicted values.
4. Print the validated shape, column labels, and dtypes.
5. Add `AbsoluteError` with a vectorized expression.
6. Produce a summary grouped by both `Model` and `Split` containing row count
   and mean absolute error.
7. Recover the complete row with the largest absolute error without sorting the
   whole table.
8. Filter and display the complete validation rows whose absolute error is at
   least 5.

Choose your own program structure. Do not reuse the Lesson 12 file by renaming
columns; write the checkpoint independently.

## Expected facts for self-checking

- Validated shape before adding a column: `(12, 5)`.
- Each model/split group contains 3 rows.
- Validation MAE: `baseline = 6.0`, `tuned = 3.0`.
- Test MAE: `baseline = 6.0`, `tuned = 5.0`.
- The largest-error row is `r06`, from the baseline model on the test split,
  with absolute error `10`.
- The validation rows with absolute error at least 5 are `r02`, `r03`, and
  `r08`.

## Correctness and complexity

A Boolean Series has one decision per row and preserves complete-record
alignment when applied to the DataFrame. Grouping must use both `Model` and
`Split`; otherwise validation and test evidence are mixed.

For `n` rows, validation, error calculation, direct maximum lookup, filtering,
and grouping are each linear-time passes: `O(n)` time. The derived column and
masks require `O(n)` additional space. Sorting only to find one worst row would
cost `O(n log n)` and is unnecessary.

## Retrieval questions

Answer briefly from memory after the code runs:

1. Why must `Actual` and `Predicted` be selected explicitly before arithmetic?
2. Why does `idxmax` preserve the identity of the worst row?
3. What mistake occurs if the summary groups by `Model` but not `Split`?
4. Which split should guide model selection, and why should the test split stay
   out of repeated tuning?

## Reading

Read the pandas documentation for
[grouping by multiple columns](https://pandas.pydata.org/docs/user_guide/groupby.html#splitting-an-object-into-groups).
Focus on why the pair `(Model, Split)` forms the group key and how an aggregate
reduces several rows to one summary row.

## Monday acceptance criteria

- `python3 september_checkpoint_model_report.py` succeeds on the supplied CSV.
- All expected facts above are correct.
- `AbsoluteError` uses labeled, vectorized pandas operations rather than a row
  loop.
- The worst prediction and threshold filter retain complete rows.
- Validation and test results remain separate in the grouped summary.
- The input table is validated before analysis.

## Later checkpoint evidence

Wednesday will review this exact file, debug it independently, and add one
deliberate malformed-input run if needed. Friday will express the same grouped
summary and threshold filter as SQLite queries, then add a short
`september-checkpoint-reflection.md` comparing NumPy arrays, pandas tables, and
SQL result sets. Do not begin a separate project.

## Wednesday milestone — September 30

No checkpoint submission was available for review, so continue this same
assignment rather than opening a new one. Use 60–90 minutes to make the
valid-data path run in this order: load and check the ordered schema, calculate
`AbsoluteError`, build the two-key summary, recover the complete worst row, and
filter the complete validation rows. Run the program after each stage and fix
the first failure before adding another stage.

Once the valid report matches the expected facts, add the remaining input
checks and demonstrate one intentional rejection with a temporary malformed
copy of the data. Preserve the supplied CSV. If the valid path does not finish,
save the current program and the first traceback or incorrect output for
review. Do not begin the SQLite portion until the pandas result is reviewed.

## Friday milestone — October 2

No checkpoint program or reflection was available for review. Use today's
90–120 minute project session to finish the same pandas artifact; do not begin
the SQLite extension yet.

Work in this order:

1. Create `september_checkpoint_model_report.py` and make the supplied valid
   CSV run end to end.
2. Check the exact ordered schema before analysis.
3. Add vectorized `AbsoluteError`, then verify the four grouped MAEs.
4. Recover the complete `r06` row with `idxmax` and filter the complete `r02`,
   `r03`, and `r08` validation rows with one Boolean mask.
5. Only after those facts match, add the remaining validation rules and save
   one deliberate malformed-input rejection without changing the supplied
   dataset.
6. Answer the four retrieval questions in
   `september-checkpoint-reflection.md` if time remains.

Run after each stage and debug the first failure before adding more code. If
the program is unfinished when the session ends, preserve the partial file and
the first traceback or incorrect output for review. The minimum useful evidence
is one runnable valid-data report; SQL remains a later representation of this
same result after the pandas work is reviewed.

## Monday recovery milestone — October 5

No checkpoint code or debugging evidence was available for review, so continue
this checkpoint and do not start Lesson 13 or the October cycle. Today's one
focused concept is preserving the meaning of rows and columns while pandas
performs vectorized work.

Use 60–90 minutes, in this order:

1. Create `september_checkpoint_model_report.py` and load the supplied CSV.
2. Check that `list(dataframe.columns)` exactly equals the five required labels
   in the required order.
3. Create `AbsoluteError` by subtracting the labeled `Actual` and `Predicted`
   Series and taking the absolute value. Do not use a row loop.
4. Group by the pair `Model` and `Split`; calculate row count and mean
   `AbsoluteError`. Compare all four results with the expected facts above.

This working grouped report is today's minimum submission. If a step fails,
stop adding features and save the program plus the first traceback or
incorrect output; that is useful debugging evidence.

Only if the four group results are correct, add these two retrieval operations:

- use the index label from `AbsoluteError.idxmax()` to select the complete
  worst row (`r06`);
- build one Boolean mask for validation rows with error at least 5, and apply
  it to the whole DataFrame to retain `r02`, `r03`, and `r08` as complete rows.

Defer the remaining validation rules, deliberate malformed run, reflection,
and SQLite translation. Submit the runnable `.py` file and either its correct
grouped output or the first failure. Do not create a second assignment.

## Wednesday independent/debugging milestone — October 7

No program or failure evidence was available for review after Monday. Continue
this checkpoint without opening another lesson. Use 60–90 minutes, but stop
once the minimum report below works.

Retrieval first, without running code: write the four expected `(Model, Split)`
groups and their count and mean absolute error from the expected-facts section.
Then create `september_checkpoint_model_report.py` and build only this path:

1. Load `september-checkpoint-model-results.csv`.
2. Require the exact ordered labels `RunID`, `Model`, `Split`, `Actual`, and
   `Predicted`.
3. Create `AbsoluteError` with labeled Series arithmetic and `.abs()`; do not
   use a Python row loop.
4. Group by both `Model` and `Split`, then calculate count and mean error.
5. Print the summary and compare every value with the four results written
   before coding.

Debug independently after each step: inspect the object's type, shape, column
labels, or index as appropriate. Read the first traceback from its final line
upward and repair only that failure before continuing. If the expected values
do not match, inspect the grouping keys and the `AbsoluteError` Series before
changing multiple lines.

The minimum submission is the runnable `.py` file and its grouped output. If
blocked, submit the partial file plus the complete traceback or incorrect
output; that is valid review evidence. Only after the minimum report works may
you add complete-row `idxmax` recovery for `r06` and one Boolean mask for
validation rows `r02`, `r03`, and `r08`. Keep the remaining validation,
malformed-input demonstration, reflection, and SQL translation deferred.

## Friday project milestone — October 9

No program or failure evidence was available for review after Wednesday. Keep
this checkpoint as the only project and use 90–120 minutes to produce one
reviewable vertical slice.

Required deliverable:

1. Create `september_checkpoint_model_report.py` and load the supplied CSV.
2. Reject a column list that is not exactly `RunID`, `Model`, `Split`,
   `Actual`, `Predicted` in that order.
3. Add `AbsoluteError` with labeled, vectorized Series arithmetic.
4. Group by both `Model` and `Split` and print count and mean absolute error.
5. Compare all four groups with the expected facts above.

Run after every numbered step. If a step fails, preserve the file and the first
complete traceback or incorrect output rather than starting another feature.
That partial evidence is enough for the next review.

Only after the required deliverable works, use `idxmax` to recover the complete
`r06` row and one Boolean mask to retain complete validation rows `r02`, `r03`,
and `r08`. Defer additional validation, a malformed-input run, the reflection,
and SQLite. This remains the September checkpoint, not a new assignment.

## Monday focused support — October 12

No implementation or failure evidence was available for review after Friday,
so this checkpoint remains the only assignment. Use 60–90 minutes on one
focused concept: **the structure produced by grouping on two labeled columns**.

Create `september_checkpoint_model_report.py` and build this vertical slice:

1. Load `september-checkpoint-model-results.csv`.
2. Require the exact ordered labels `RunID`, `Model`, `Split`, `Actual`, and
   `Predicted`.
3. Create `AbsoluteError` with labeled Series subtraction and `.abs()`.
4. Group by both `Model` and `Split`; calculate count and mean absolute error.
5. Print the result, then inspect its type, shape, column labels, and index
   names before comparing the four values with the expected facts above.

Write one or two sentences explaining why two models crossed with two splits
produce four groups and why each group contains three rows. If anything fails,
save the partial file and the complete first traceback. That is valid review
evidence and is more useful than restarting.

Do not add `idxmax`, threshold filtering, more validation, the reflection, or
SQLite until this slice has been reviewed. This is support for the existing
independent checkpoint, not a new lesson.

## Friday project support — October 16

No checkpoint program, partial code, output, or traceback was available for
review after Monday. Continue this same checkpoint. Do not start Lesson 13,
SQL, or a separate exercise.

Use 90–120 minutes, but treat the first four steps as the complete required
milestone:

1. Create `september_checkpoint_model_report.py` and load
   `september-checkpoint-model-results.csv`.
2. Reject the input unless its ordered columns are exactly `RunID`, `Model`,
   `Split`, `Actual`, and `Predicted`.
3. Add `AbsoluteError` using labeled Series subtraction and `.abs()`.
4. Print only `RunID`, `Model`, `Split`, and `AbsoluteError`. Confirm that the
   table has 12 rows and that `r06` has error 10.

Run after each step. If a step fails, stop adding features and preserve the
partial file plus the complete traceback or incorrect output. That is valid
evidence for review.

Only after this 12-row error table is correct, group by both `Model` and
`Split` and calculate count and mean `AbsoluteError`. Compare the four groups
with the expected facts near the top of this file. Keep `idxmax`, threshold
filtering, additional validation, the reflection, and SQLite deferred until
the code above is reviewed.

Before finishing, answer these two retrieval prompts in a comment or separate
note:

- Why does selecting the four output columns retain row identity?
- Why must the summary use both `Model` and `Split` as keys?

## Monday focused support — October 19

No checkpoint program, partial code, output, traceback, or reflection was
available for review after Friday. Continue this checkpoint only; do not begin
Lesson 13, SQL, or another exercise.

Use 60–90 minutes on one concept: **pandas aligns labeled Series by index when
it creates a derived column**. That is why each absolute error stays attached
to its original `RunID`, model, and split.

Create `september_checkpoint_model_report.py` and stop after this path works:

1. Load `september-checkpoint-model-results.csv` with pandas.
2. Require the ordered column list to equal `RunID`, `Model`, `Split`, `Actual`,
   and `Predicted` exactly.
3. Subtract the labeled `Actual` and `Predicted` Series, call `.abs()`, and
   assign the result to a new `AbsoluteError` column. Do not write a row loop.
4. Print only `RunID`, `Actual`, `Predicted`, and `AbsoluteError`.
5. Confirm there are 12 rows and that `r06` has absolute error 10.

Run after loading, after the schema check, and after assigning the derived
column. If anything fails, stop and save the partial file plus the complete
first traceback or incorrect output. That is sufficient evidence for review.

Mathematical check: for row `r06`, `|94 - 84| = 10`. The operation is one
linear pass over `n` rows, so it takes `O(n)` time and stores one additional
length-`n` column. In ML terms, this is a per-example evaluation signal; the
later grouped mean will compare models without mixing validation and test
evidence.

Retrieval check, answered after the program runs:

- Why does assigning a Series with the same index preserve row identity?
- What information would be lost if only the error values were printed?

Keep grouping, `idxmax`, threshold filtering, additional validation, the
reflection, and SQL deferred until this small artifact is reviewed.

## Wednesday independent practice — October 21

No checkpoint program, partial code, output, traceback, or reflection was
available for review after Monday. Continue the same checkpoint only. This
session is independent practice and debugging of Monday's concept, not a new
lesson or a new project.

Use 60–90 minutes and stop when this reviewable vertical slice works:

1. Before running code, calculate the expected absolute errors for `r01`,
   `r06`, and `r12` directly from the CSV.
2. Create or continue `september_checkpoint_model_report.py` and load
   `september-checkpoint-model-results.csv`.
3. Require the ordered column list to equal `RunID`, `Model`, `Split`,
   `Actual`, and `Predicted` exactly.
4. Create `AbsoluteError` with labeled Series subtraction and `.abs()`; do not
   use a Python row loop.
5. Print `RunID`, `Actual`, `Predicted`, and `AbsoluteError` for all 12 rows.
6. Verify that the new Series index equals the DataFrame index and confirm that
   `r06` has error 10.

Run once after loading, once after the schema check, and once after assigning
the column. If a run fails, read the traceback from its final line upward,
repair only that failure, and rerun. If it remains blocked, preserve the
partial file and the first complete traceback or incorrect output; that is
sufficient evidence for the next review.

After it runs, answer from memory in a code comment or brief note:

- Why does Series assignment preserve the error-to-row relationship here?
- What bug could appear if two Series with different indexes were combined?
- Why is this operation `O(n)` rather than `O(n log n)`?

The minimum submission is the partial `.py` file plus its 12-row output or the
first complete failure. Keep grouping, `idxmax`, threshold filtering,
additional validation, the reflection, and SQL deferred until this artifact is
reviewed.

## Monday focused support — October 26

No checkpoint program, partial code, output, traceback, reflection, or new Git
commit was available for review after Friday. Continue this checkpoint only;
do not begin Lesson 13, SQL, or another exercise.

Use 60–90 minutes on one concept: **data lineage for a derived pandas column**.
Each calculated error must remain associated with the same `RunID`, model,
split, actual value, and prediction that produced it. Complete these as three
separate run-and-save checkpoints in `september_checkpoint_model_report.py`:

1. Load `september-checkpoint-model-results.csv`. Print the DataFrame shape and
   ordered columns. Stop and repair the load or schema problem if they are not
   `(12, 5)` and `RunID`, `Model`, `Split`, `Actual`, `Predicted`.
2. Calculate a vectorized absolute-error Series from the labeled `Actual` and
   `Predicted` columns. Before assigning it, print its index and the DataFrame
   index and verify that they match.
3. Assign the Series as `AbsoluteError`, then print all 12 rows using only
   `RunID`, `Actual`, `Predicted`, and `AbsoluteError`. Confirm `r01 = 4`,
   `r06 = 10`, and `r12 = 5`.

Do not use a row loop. The operational rule is `absolute error = |actual -
predicted|`; this is one `O(n)` pass plus one length-`n` output column. In ML,
the value is a per-example evaluation signal. In database terms, retaining
`RunID` is what lets the derived value be traced back to its source record.

After the last working run, answer briefly:

- What evidence shows that each error stayed attached to the intended row?
- Why is printing only an unlabeled list of errors insufficient for an audit?

The minimum review evidence is the partial `.py` file plus the output from the
last successful checkpoint or the first complete traceback. Preserve that
evidence even if the whole slice is unfinished. Keep grouping, `idxmax`,
filtering, additional validation, reflection, and SQL deferred until this
artifact is reviewed.

## Wednesday independent practice — October 28

No checkpoint program, partial code, output, traceback, reflection, or new Git
commit was available for review after Monday. Continue this checkpoint only;
do not begin Lesson 13, SQL, or another exercise.

Use 60–90 minutes, but stop as soon as this smallest reviewable run works:

1. Before coding, calculate the errors for `r01`, `r06`, and `r12` from the
   supplied CSV.
2. Create and save `september_checkpoint_model_report.py` immediately.
3. Load `september-checkpoint-model-results.csv` with pandas.
4. Create a vectorized Series using `Actual`, `Predicted`, subtraction, and
   `.abs()`, then assign it as the `AbsoluteError` column.
5. Select the complete rows whose `RunID` is `r01`, `r06`, or `r12` and print
   only `RunID`, `Actual`, `Predicted`, and `AbsoluteError`.
6. Confirm that the three errors are 4, 10, and 5, respectively.

Run and save after loading, after creating the Series, and after printing the
three rows. Do not use a Python row loop. If any step fails, read the final
traceback line first, repair only that failure, and rerun. If still blocked,
preserve the partial file and the first complete traceback or incorrect output;
that is sufficient evidence for review.

After it runs, answer aloud or in one short code comment: why does selecting
complete rows preserve the connection between an error and its `RunID`? This
operation is `O(n)` because pandas scans the rows once; sorting would add work
without helping this task. In ML terms, each error remains an auditable
per-example result, and in database terms `RunID` remains the record key.

The minimum submission is the partial `.py` file plus the three-row output or
the first complete failure. Defer the full 12-row display, ordered-schema check,
grouping, `idxmax`, threshold filtering, additional validation, reflection,
and SQL until this artifact is reviewed.

## Friday project support — October 30

No checkpoint program, partial code, output, traceback, reflection, or new Git
commit was available for review after Wednesday. Continue this checkpoint as
the only project; do not begin Lesson 13, SQL, or a second assignment.

Use 90–120 minutes, but make one small runnable artifact the required result:

1. Create and save `september_checkpoint_model_report.py` before adding later
   features.
2. Load `september-checkpoint-model-results.csv` with pandas.
3. Calculate `AbsoluteError` with labeled vectorized subtraction and `.abs()`;
   do not use a Python row loop.
4. Select the complete rows for `r01`, `r06`, and `r12`, then print only
   `RunID`, `Actual`, `Predicted`, and `AbsoluteError`.
5. Confirm the errors are 4, 10, and 5. Save and rerun this version.

Only after that output is correct, require the exact ordered input columns
`RunID`, `Model`, `Split`, `Actual`, and `Predicted`, then replace the
three-record display with all 12 complete identity/error rows. Confirm the
output still includes `r06` with error 10.

If the program fails, stop adding features. Preserve the partial file and the
first complete traceback or incorrect output; that is useful submission
evidence. Keep the two-key grouped summary, `idxmax`, threshold filtering,
additional validation, reflection, and SQL deferred until this file is
reviewed.

Retrieval check before coding: compute `|70 - 74|`, `|94 - 84|`, and
`|94 - 89|` by hand. After running, explain in one or two sentences why
filtering the whole DataFrame retains the `RunID` attached to each error.
Creating the derived column and scanning the rows are `O(n)` time and require
an `O(n)` result column; sorting would add unnecessary `O(n log n)` work. In
ML terms these are auditable per-example errors, and in database terms `RunID`
is the record key that preserves lineage.

Suggested work blocks: 10 minutes retrieval and file creation, 25 minutes for
the three-row result, 15 minutes to debug the first failure, 20 minutes for the
schema check and full display if the minimum works, and the remaining time to
save output and explain row identity. Submit the `.py` file plus correct output
or the first complete failure.

## Monday focused support — November 2

No checkpoint program, partial code, output, traceback, reflection, or new Git
commit was available for review after Friday. Continue this checkpoint only;
do not begin Lesson 13, SQL, or another assignment.

Use 60–90 minutes on one focused concept: a pandas pipeline should be runnable
and inspectable after each operation. Build only this read-transform-select
slice in `september_checkpoint_model_report.py`:

1. Create and save the file, load `september-checkpoint-model-results.csv`, and
   print the table's shape. Run it; the shape must be `(12, 5)`.
2. Derive `AbsoluteError` with labeled vectorized subtraction and `.abs()`,
   assign the new column, and run again. Do not use a Python row loop.
3. Select the complete row whose `RunID` is `r06`. Print only `RunID`, `Actual`,
   `Predicted`, and `AbsoluteError`; verify `94`, `84`, and `10` stay together.

Stop when that one-row result works. If an operation fails, preserve the file
and the first complete traceback or incorrect output instead of adding more
features. That evidence is sufficient for review.

Retrieval before coding: calculate `|94 - 84|` by hand. After running, explain
in one or two sentences why selecting the complete row is safer for an ML error
audit than printing the error value alone. Both deriving the column and finding
`r06` require linear scans, so the pipeline is `O(n)` time; the new column uses
`O(n)` space. In database terms, `RunID` acts as the record key that preserves
lineage.

Suggested plan: 10 minutes retrieval and file creation, 15 minutes loading and
running, 20 minutes deriving the column, 15 minutes selecting and checking the
row, and the remaining time for one-failure-at-a-time debugging and saving the
evidence. Defer the other rows, ordered-schema validation, grouping, `idxmax`,
threshold filtering, additional validation, reflection, and SQL until this
artifact is reviewed.
