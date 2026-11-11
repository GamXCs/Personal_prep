# Grad School Prep

A cumulative graduate-school prep curriculum for AI, machine learning, data science, and applied math, combining Python, mathematics, algorithms, technical reading, and problem-first coding exercises.

## Purpose

This repository is a long-term study curriculum designed to prepare for graduate-level work in:

- artificial intelligence
- machine learning
- data science
- applied mathematics

The project emphasizes cumulative learning rather than isolated practice. Each lesson is meant to connect programming, mathematical reasoning, algorithmic thinking, and machine-learning theory.

The current rhythm is Monday focused learning (60–90 minutes), Wednesday
independent practice/debugging/review (60–90 minutes), and Friday application
to the ongoing project (90–120 minutes). Work is organized around monthly
objectives, with every fourth week used as an independent checkpoint.

**Current scheduling status:** Lesson 12's core pandas work was completed and
reviewed on September 27. Lesson 11's valid NumPy pipeline is complete: it performs both axis
reductions, aligned filtering, top-student identity recovery, column
standardization, invariant checks, and formatted presentation. Lesson 12 now
translates the familiar exam analysis into pandas DataFrames, labeled
selection, derived columns, validation, and grouped performance summaries.
The submitted program now validates the exam table, derives `StudentMean`,
recovers Sarah's complete `idxmax` row, filters complete qualifying rows,
assigns performance bands, and produces the expected grouped counts and means.
At the student's request, presentation formatting, function decomposition, a
saved malformed run, and the reflection are optional cleanup rather than
advancement blockers. The unnumbered September independent checkpoint is now
active. It uses a fresh model-evaluation table to assess validation, vectorized
error, two-key grouping, direct worst-row lookup, and complete-row filtering
before the same result is expressed in SQL. No later numbered lesson has been
opened.
Lesson 11's companion artifact uses cumulative file number 19, but the
student's current course position is Lesson 12.
Historical Lessons 16–18 are Lesson 10 reinforcement records, not separate
student advancement. Lesson 19 is Lesson 11 companion material. The curriculum
tracker, not the largest filename, is the canonical course position.

The curriculum path is Python/NumPy/pandas/SQL, then statistics and classical
ML, APIs/Docker/AWS, deep learning, evaluated AI applications, and finally
specialization plus portfolio development. Current assignments connect to AI
and database coursework through feature matrices, evaluation, schemas,
aggregation, and SQL-style data reasoning.

## How The Curriculum Works

- Lessons build on prior work and do not assume mastery without evidence.
- Coding assignments are problem-first: you attempt them before seeing a full solution.
- Mathematics is treated as part of implementation, not separate from it.
- Progress is tracked through lesson artifacts, notes, derivations, and completed exercises.

## Repository Structure

- [advisor-instructions.md](advisor-instructions.md): teaching and curriculum rules
- [student-profile.md](student-profile.md): durable context about background, pacing, and preferences
- [curriculum-progress.md](curriculum-progress.md): current position, mastery status, and next-step guidance
- [lesson-01-descriptive-statistics-linear-search-loss.md](lesson-01-descriptive-statistics-linear-search-loss.md): current lesson
- [lesson-01-score-analyzer-starter.py](lesson-01-score-analyzer-starter.py): starter scaffold for the current coding exercise
- [lesson-02-verifying-statistical-code-and-invariants.md](lesson-02-verifying-statistical-code-and-invariants.md): current reinforcement lesson on testing and correctness
- [lesson-03-property-based-testing-statistical-code.md](lesson-03-property-based-testing-statistical-code.md): current implementation lesson on property-based verification
- [lesson-04-test-adequacy-affine-invariants.md](lesson-04-test-adequacy-affine-invariants.md): current review lesson on fault detection and affine invariants
- [lesson-05-independent-oracles-pairwise-variance.md](lesson-05-independent-oracles-pairwise-variance.md): flex-day checkpoint on independent variance verification
- [lesson-06-testing-boundaries-and-expected-values.md](lesson-06-testing-boundaries-and-expected-values.md): targeted reinforcement on testing the imported analyzer rather than local copies
- [lesson-07-test-discovery-and-detection-probability.md](lesson-07-test-discovery-and-detection-probability.md): current lesson on unittest discovery, collection counts, and detection probability
- [lesson-08-coding-prediction-evaluator.md](lesson-08-coding-prediction-evaluator.md): current coding-first prediction-evaluator project
- [lesson-08-transformation-example.py](lesson-08-transformation-example.py): complete loop-transformation pattern
- [lesson-08-prediction-evaluator-starter.py](lesson-08-prediction-evaluator-starter.py): four-checkpoint coding scaffold
- [lesson-08-student-data.csv](lesson-08-student-data.csv): input data for the active pipeline assignment
- `lesson_08_student_pipeline_starter.py` and
  `test_lesson_08_student_pipeline.py`: retired support artifacts; use only if
  the student explicitly requests scaffolding
- [lesson-09-single-pass-csv-pipelines.md](lesson-09-single-pass-csv-pipelines.md): current lesson on structured, single-pass CSV programs
- [lesson-09-streaming-example.py](lesson-09-streaming-example.py): executable aggregation and presentation example
- [lesson-10-numpy-arrays-and-boolean-masks.md](lesson-10-numpy-arrays-and-boolean-masks.md): current NumPy lesson on arrays, masks, alignment, and standardization
- [lesson-10-array-example.py](lesson-10-array-example.py): executable NumPy masking and standardization example
- [lesson-11-2d-arrays-axes-and-argmax.md](lesson-11-2d-arrays-axes-and-argmax.md): current lesson on 2-D axes, reductions, and record identity
- [lesson-11-axis-example.py](lesson-11-axis-example.py): executable row-wise and column-wise aggregation example
- [lesson-12-functions-validation-and-axis-reductions.md](lesson-12-functions-validation-and-axis-reductions.md): active pandas lesson on labeled tabular analysis and grouped summaries
- [lesson-12-reliable-array-example.py](lesson-12-reliable-array-example.py): executable pandas DataFrame and filtering example
- [lesson-13-schema-driven-csv-and-residual-bias.md](lesson-13-schema-driven-csv-and-residual-bias.md): current core-Python lesson on schema parsing, validation, and residual bias
- [lesson-13-schema-example.py](lesson-13-schema-example.py): executable parser-dispatch example
- [lesson-14-pipeline-state-and-invariants.md](lesson-14-pipeline-state-and-invariants.md): active reinforcement on accumulator design and loop invariants
- [lesson-14-state-example.py](lesson-14-state-example.py): executable state-update example
- [lesson-15-return-contracts-and-validation.md](lesson-15-return-contracts-and-validation.md): active reinforcement on structured returns, presentation boundaries, and contextual validation
- [lesson-15-contract-example.py](lesson-15-contract-example.py): executable computation-versus-presentation example
- [lesson-16-array-contracts-and-mask-invariants.md](lesson-16-array-contracts-and-mask-invariants.md): focused reinforcement on aligned arrays, masks, and indexed extreme selection
- [lesson-16-mask-contract-example.py](lesson-16-mask-contract-example.py): executable shared-mask contract example
- [lesson-17-vectorized-transformations-and-diagnostic-checks.md](lesson-17-vectorized-transformations-and-diagnostic-checks.md): active reinforcement on broadcasting, standardization, and diagnostic checks
- [lesson-17-diagnostic-example.py](lesson-17-diagnostic-example.py): executable vectorization and invariant-check example
- [lesson-18-array-pipeline-boundaries.md](lesson-18-array-pipeline-boundaries.md): active reinforcement on reusable NumPy pipeline boundaries
- [lesson-18-boundary-example.py](lesson-18-boundary-example.py): executable structured-analysis example
- [lesson-19-matrix-axes-and-feature-scaling.md](lesson-19-matrix-axes-and-feature-scaling.md): active lesson on 2-D axes and feature-wise scaling
- [lesson-19-axis-contract-example.py](lesson-19-axis-contract-example.py): executable axis and matrix-contract example

## Current Status

As of Monday, November 9, 2026:

- No checkpoint code, output, traceback, reflection, or commit appeared after
  Friday. The unnumbered September checkpoint remains the only active work;
  Lesson 13, SQL, and a new cycle remain closed. Monday's 60–90 minute focused
  support makes the CSV-loading boundary observable: create
  `september_checkpoint_model_report.py`, load the supplied CSV, print its
  type, `(12, 5)` shape, and ordered labels, then select and print the complete
  source row `r06` with `Actual = 94` and `Predicted = 84`. Submit the working
  output or the partial script and first complete failure. Add vectorized
  `AbsoluteError` and confirm `10` only if that source-row result works; all
  later checkpoint features remain deferred.

As of Friday, November 6, 2026:

- No checkpoint code, output, traceback, reflection, or commit appeared after
  Wednesday. The unnumbered September checkpoint remains the only active work;
  Lesson 13, SQL, and a new cycle remain closed. Friday's 90–120 minute project
  block keeps one artifact: create `september_checkpoint_model_report.py`, load
  the supplied CSV, assign vectorized `AbsoluteError`, and print the complete
  `r06` row with values `94`, `84`, and `10`. Run and save after each operation.
  Submit the working script and output, or the partial script and first complete
  failure. Only after that row works, extend the same file to the full 12-row
  identity/error table and confirm `r01 = 4` and `r12 = 5`; all later checkpoint
  features remain deferred.

As of Wednesday, November 4, 2026:

- No checkpoint code, output, traceback, reflection, or commit appeared after
  Monday. The unnumbered September checkpoint remains the only active work;
  Lesson 13, SQL, and a new cycle remain closed. Wednesday's 60–90 minute
  independent practice keeps Monday's smallest runnable pandas pipeline:
  retrieve the expected `r06` values, load the CSV, assign vectorized
  `AbsoluteError`, and print the complete `r06` row with values `94`, `84`, and
  `10`. Submit the script and output, or preserve the partial file and first
  complete failure for review. All later checkpoint features remain deferred.

As of Wednesday, October 28, 2026:

- No checkpoint code, debugging evidence, reflection, or commit appeared after
  Monday. The unnumbered September checkpoint remains the only active work;
  Lesson 13, SQL, and the October cycle remain closed. Wednesday's 60–90 minute
  independent practice is the smallest runnable pandas slice: create
  `september_checkpoint_model_report.py`, load the supplied CSV, derive and
  assign vectorized `AbsoluteError`, and print only complete rows `r01`, `r06`,
  and `r12`. Confirm errors 4, 10, and 5, or preserve the partial file and first
  complete failure. The full report and later checkpoint features remain
  deferred pending review.

As of Monday, October 26, 2026:

- No checkpoint code, debugging evidence, reflection, or commit appeared after
  Friday. The unnumbered September checkpoint remains the only active work;
  Lesson 13, SQL, and the October cycle remain closed. Monday's 60–90 minute
  focused support session uses three saved checkpoints to establish derived-
  column data lineage: load and inspect the 12-row table, compare the
  vectorized error Series index with the DataFrame index, then assign and print
  all 12 labeled identity/error rows. Confirm `r01 = 4`, `r06 = 10`, and
  `r12 = 5`, or preserve the last working output and first complete failure.
  All grouped and later checkpoint features remain deferred pending review.

As of Friday, October 23, 2026:

- No checkpoint code or debugging evidence appeared after Wednesday. The
  unnumbered September checkpoint remains the only active work; Lesson 13,
  SQL, and the October cycle remain closed. Friday's 90–120 minute project
  block requires one saved `september_checkpoint_model_report.py`: load the
  checkpoint CSV, check the exact ordered schema, create vectorized
  `AbsoluteError`, and print the 12 complete identity/error rows. Confirm
  `r01 = 4`, `r06 = 10`, and `r12 = 5`, or preserve the partial file and first
  complete failure. Add the two-key grouped summary only after this table
  works; all later checkpoint features remain deferred.

As of Wednesday, October 21, 2026:

- No checkpoint code or debugging evidence appeared after Monday. The
  unnumbered September checkpoint remains the only active work; Lesson 13,
  SQL, and the October cycle remain closed. Wednesday's 60–90 minute
  independent practice repeats the same bounded artifact: first predict the
  errors for `r01`, `r06`, and `r12`, then load the checkpoint CSV, check its
  exact ordered schema, create vectorized `AbsoluteError`, and print the
  12-row identity/error table. Verify index alignment and `r06` error 10, or
  preserve the partial file and first complete traceback. All later checkpoint
  features remain deferred until this evidence is reviewed.

As of Monday, October 19, 2026:

- No checkpoint code or debugging evidence appeared after Friday. The
  unnumbered September checkpoint remains the only active work; Lesson 13,
  SQL, and the October cycle remain closed. Monday's 60–90 minute focused
  support target is labeled Series alignment: load the checkpoint CSV, require
  its exact ordered schema, create vectorized `AbsoluteError`, and print the
  12-row `RunID`/`Actual`/`Predicted`/`AbsoluteError` table. Confirm `r06` has
  error 10, or preserve the partial file and first complete traceback. All
  grouping and later checkpoint work remains deferred until this slice is
  reviewed.

As of Friday, October 16, 2026:

- No checkpoint code or debugging evidence appeared after Monday. The
  unnumbered September checkpoint remains the only active work; Lesson 13,
  SQL, and the October cycle remain closed. Friday's 90–120 minute project
  support target is a smaller load-and-error table in
  `september_checkpoint_model_report.py`: load the supplied CSV, require the
  exact ordered schema, create vectorized `AbsoluteError`, and print 12
  complete identity/error rows, including error 10 for `r06`. Add the two-key
  grouped summary only if that table works. Preserve the first full failure if
  blocked; all later checkpoint features remain deferred.

As of Monday, October 12, 2026:

- No checkpoint code or debugging evidence appeared after Friday. The
  unnumbered September checkpoint remains the only active work; no Lesson 13,
  SQL extension, or October cycle was opened. Monday's 60–90 minute support
  target focuses on the structure of a two-key pandas `groupby`: create
  `september_checkpoint_model_report.py`, check the exact ordered schema,
  derive vectorized `AbsoluteError`, and print count and mean grouped by
  `Model` and `Split`. Inspect the result's type, shape, columns, and index
  names, then explain why it contains four groups. A partial file plus output
  or the first complete traceback is sufficient review evidence. Defer
  `idxmax`, filtering, further validation, reflection, and SQL.

As of Friday, October 9, 2026:

- No checkpoint code or debugging evidence appeared after Wednesday, so the
  unnumbered September checkpoint remains the only active work. No Lesson 13,
  SQL extension, or October cycle was opened. Friday's 90–120 minute target is
  one runnable `september_checkpoint_model_report.py` containing the ordered
  schema check, vectorized `AbsoluteError`, and four `Model`/`Split`
  count-and-mean results. Run after each operation and preserve the first full
  failure if blocked. Add complete-row `idxmax` and threshold filtering only
  after the grouped report matches the supplied facts; defer all other
  checkpoint requirements.

As of Wednesday, October 7, 2026:

- No checkpoint implementation or debugging evidence appeared after Monday.
  The unnumbered September checkpoint therefore remains the only active work;
  no new lesson or SQL task was added. Today's 60–90 minute independent target
  is the smallest runnable pandas report in
  `september_checkpoint_model_report.py`: ordered-schema check, vectorized
  `AbsoluteError`, and the four `Model`/`Split` count-and-mean results. Inspect
  intermediate type/shape/index information and save the complete first error
  or incorrect output if blocked. Add `idxmax`, threshold filtering, further
  validation, reflection, and SQL only after that minimum report works.

As of Monday, October 5, 2026:

- No checkpoint implementation or debugging evidence has appeared, so the
  September independent checkpoint remains the sole active assignment and the
  October cycle is deferred. Monday's 60–90 minute recovery target is one thin
  valid pandas path in `september_checkpoint_model_report.py`: load the data,
  verify the ordered schema, create vectorized `AbsoluteError`, and produce the
  four `Model`/`Split` count-and-mean results. Add complete-row `idxmax` recovery
  and the validation threshold mask only if that grouped report works. Save the
  first failure if blocked; remaining validation, malformed evidence,
  reflection, SQL, and Lesson 13 stay closed pending review.

As of Friday, October 2, 2026:

- No checkpoint program, reflection, saved output, or malformed-data evidence
  has appeared, so the unnumbered September checkpoint remains the only active
  assignment. Friday's 90–120 minute project session is narrowed to completing
  `september_checkpoint_model_report.py`: ordered-schema validation,
  vectorized `AbsoluteError`, the two-key `Model`/`Split` summary, complete
  `idxmax` worst-row recovery, and complete validation-row filtering. Add the
  remaining validation, one deliberate rejected run, and retrieval answers
  only after the valid report works. SQLite and the October cycle stay deferred
  until this checkpoint evidence is reviewed; no Lesson 13 was opened.

As of Wednesday, September 30, 2026:

- No checkpoint submission has appeared since Monday, so the unnumbered
  September checkpoint remains the only active assignment and no Lesson 13 was
  opened. Wednesday's 60–90 minute independent/debugging target is one
  runnable pandas report in `september_checkpoint_model_report.py`: exact
  ordered-schema check, vectorized `AbsoluteError`, two-key `Model`/`Split`
  summary, complete worst-row recovery with `idxmax`, and complete validation
  rows meeting the threshold. Add the remaining input checks and one deliberate
  malformed run only after the valid path works. Friday's SQLite representation
  waits until this pandas evidence is reviewed.

As of Monday, September 28, 2026:

- The fourth-week independent checkpoint is active; no Lesson 13 was opened.
  Monday's 60–90 minute task is to implement the pandas portion in
  `september_checkpoint_model_report.py` from the behavioral specification in
  `september-2026-independent-checkpoint.md`, using the supplied fresh model
  results. Wednesday will review/debug the same artifact, and Friday will add
  its SQL representation and comparison reflection. The next monthly cycle
  begins only after checkpoint evidence is reviewed.

As of Sunday, September 27, 2026:

- The core Lesson 12 submission compiles and runs with correct validation,
  labeled selection, row-wise means, label-preserving maximum lookup,
  complete-row filtering, performance bands, and grouped counts/means. The
  student elected to defer formatting, decomposition, saved malformed-output,
  and reflection work; those are recorded as optional cleanup rather than
  blockers. No Sunday lesson was added. The next scheduled decision belongs to
  the September 28 independent-checkpoint week.

As of Friday, September 25, 2026:

- The Lesson 12 program and reflection are still absent, so advancement is not
  supported. The independent pandas example and completed Lesson 11 report
  compile, and the example runs successfully. Friday's 90–120 minute project
  session is an end-to-end valid-data report through schema/value validation,
  labeled exam selection, `StudentMean`, Sarah's complete top row, complete-row
  filtering, performance bands, and grouped counts/means. Save the successful
  output before adding malformed-input evidence and reflection. No new lesson,
  SQL extension, or separate checkpoint project was opened.

As of Wednesday, September 23, 2026:

- No student-authored artifact changed after Monday, and the expected Lesson 12
  program and reflection remain absent. The pandas example and completed
  Lesson 11 report compile and run successfully. Lesson 12 remains the only
  active assignment. Wednesday's independent practice is narrowed to creating
  and debugging the valid-data slice through `StudentMean` and Sarah's complete
  `idxmax` row, followed by the complete qualifying rows only if time permits.
  The seven repository-wide pytest failures come from a retired, intentionally
  unfinished Lesson 8 starter and do not block the active curriculum.

As of Monday, September 21, 2026:

- No student-authored file changed after Friday, and the expected Lesson 12
  program and reflection remain absent. The pandas example still runs and the
  completed Lesson 11 program compiles. Lesson 12 remains the only active
  assignment. Monday's single concept is label-safe vectorized row analysis:
  explicit exam-column selection, `mean(axis=1)`, `idxmax`, and one aligned
  Boolean Series applied to complete rows. Complete that valid-data path first;
  add performance bands and grouping only if time remains. No new numbered
  lesson or parallel SQL task was added.

As of Friday, September 18, 2026:

- No student-authored file changed after Wednesday, and the expected Lesson 12
  program and reflection are still absent. The pandas example runs successfully
  under pandas 2.3.1, and the completed Lesson 11 submission still compiles.
  Lesson 12 remains the only active assignment. Friday's 90–120 minute project
  session should first produce a runnable valid-data path with deliberate
  schema/value checks, explicit exam-column selection, `StudentMean`, Sarah's
  complete top row, and the complete qualifying rows for Alice, Sarah, and
  Emma. Add performance bands, the grouped summary, one malformed-input run,
  and reflection evidence only after that vertical slice works. No new lesson,
  SQL extension, or parallel backlog was added.

As of Friday, September 11, 2026:

- Lesson 11 remains active because its code and completion evidence have not
  changed since Wednesday, and `lesson-11-reflection.md` is still absent. The
  valid and edge-case runs continue to confirm that the core NumPy analysis is
  sound. Friday's 90–120 minute project session is a bounded finish: correct
  the qualifying-row report value, implement and call `format_output`, add the
  rejected score text to conversion errors, and save valid, malformed, and
  constant-column evidence plus the assigned reading and retrieval responses.
  The new `insertion_sort.c` file is preserved as separate coursework and does
  not change the active data-curriculum lesson. No new lesson or pandas backlog
  was added.

As of Wednesday, September 9, 2026:

- No student-authored files changed after the September 7 review. Lesson 11
  remains active; no new lesson or pandas assignment was added. The valid run,
  six malformed fixtures, and an independent constant-column check still
  confirm the completed NumPy analysis and validation behavior. Wednesday's
  bounded completion milestone is to correct the qualifying-row report field,
  implement and call `format_output`, add rejected score text to conversion
  errors, and save valid/malformed/constant evidence plus retrieval answers in
  `lesson-11-reflection.md`.

As of Sunday, September 7, 2026:

- The committed Lesson 11 analysis now completes successfully with correct
  feature-wise standardization and explicit matrix, alignment, mask, and
  `np.allclose` contracts. All six malformed loader fixtures still fail at the
  intended boundaries. Only the presentation function, rejected-value error
  context, saved edge-case evidence, and reflection remain. Sunday is outside
  the active assignment cadence, so no new lesson was added.

As of Saturday, September 5, 2026:

- No student-authored artifact changed after Friday's review. The Lesson 11
  program still compiles and runs, and all six malformed loader fixtures still
  reach their intended checks. Its next coding checkpoint is unchanged: use
  score axis `0` for row alignment, then return a structured analysis result
  before adding the remaining reductions, mask, scaling, and diagnostics.
  Saturday is outside the active lesson cadence, so no new assignment was
  added.

As of Friday, September 4, 2026:

- `lesson_11_exam_matrix.py` now converts the valid loader output into aligned
  NumPy arrays with the correct visible shapes. The next correction is to
  compare the name count with score axis `0`, not axis `1`; the latter is the
  feature count. The loader still rejects all six malformed fixtures. Friday
  remains catch-up, so no new lesson was added. Continue with both axis means,
  `argmax`, a shared row mask, column-wise standardization, explicit diagnostics,
  a structured returned report, and the reflection.

As of Thursday, September 3, 2026:

- `lesson_11_exam_matrix.py` now has a working CSV loader with physical-row
  validation. Its valid run returns all five aligned records, and each supplied
  malformed fixture reaches its intended validation check. No new lesson was
  added on this completion day. Finish the existing Lesson 11 matrix-analysis
  requirements and `lesson-11-reflection.md` before advancing.

As of Wednesday, September 2, 2026:

- The student confirmed that Lesson 11 is current and will begin it on
  September 3. Do not publish another lesson until that work is reviewed or the
  student reports completion. The Lesson 19 filename is only the cumulative
  publication number for the Lesson 11 matrix topic.

- Lesson 10's committed implementation is sufficient to advance. Lesson 19 is
  now active, with a new 2-D exam-matrix exercise that requires explicit axis,
  alignment, mask, and column-standardization contracts. The next evidence is
  `lesson_11_exam_matrix.py`, valid and malformed output, and
  `lesson-11-reflection.md`.

As of Tuesday, September 1, 2026:

- The Lesson 10 analyzer now satisfies Lesson 18's three-boundary refactoring
  requirement and preserves all valid-output facts. Temporary malformed and
  constant-score checks both fail as intended. Tuesday remains a completion
  day: add the explicit array/mask and floating-point checks, include rejected
  score text in conversion errors, and save `lesson-10-reflection.md`; no new
  assignment was added.

As of Monday, August 31, 2026:

- New analyzer work now rejects zero spread and uses `argmax` to recover
  `Emma 98`. Lesson 18 targets the remaining function-boundary, explicit
  invariant, contextual-error, and saved-evidence requirements without adding
  a second integrated assignment.

- No student-authored artifact changed after the August 29 checkpoint. The
  analyzer and Lesson 17 diagnostic example both compile and run successfully,
  and no new Sunday assignment was added. Lesson 17 remains the active
  self-contained completion route; Monday should review the same outstanding
  Lesson 10 evidence before advancing.

- No student-authored artifact changed after the August 27 review. The current
  analyzer was rerun successfully, and Lesson 17 remains the self-contained
  teaching and completion route for the active Lesson 10 deliverable.
- Saturday is outside the active Monday/Wednesday/Friday assignment cadence, so
  no Lesson 18 or second integrated exercise was added.

- `lesson_10_numpy_scores.py` is a meaningful partial submission. Its valid run
  produces the expected metadata, four aligned above-mean records, and correct
  standardization diagnostics. Remaining work is function decomposition,
  explicit invariant checks, zero-spread rejection, `argmax` identity recovery,
  malformed/constant-data evidence, and `lesson-10-reflection.md`.
- Thursday remains a completion/support day, so no Lesson 18 was added.

- No new Lesson 10 submission evidence appeared. Lesson 17 continues the same
  analyzer with broadcasting, vectorized standardization, and `np.isclose`
  diagnostics. The current malformed CSV row is retained as validation evidence;
  2-D arrays and Pandas remain deferred.

- No new Lesson 10 implementation evidence appeared. Lesson 16 now provides a
  narrower checkpoint-based path through the same analyzer assignment; 2-D
  arrays and Pandas remain deferred.
- Tuesday's checkpoint found the analyzer and reflection still absent. No
  Lesson 17 was published because Tuesday is an implementation/debugging day.

- Lesson 9 is complete by explicit student confirmation. Loading, computation,
  and presentation are separated, and the required report facts print
  correctly. Do not block Lesson 10 on additional Lesson 9 evidence.
- Lesson 10 is active. The separate minimum-record scan is complete and returns
  the full model record correctly. The next evidence to review is
  `lesson_10_numpy_scores.py`, its valid/edge-case output, and the Lesson 10
  reflection.
- No Sunday assignment was added; the existing Lesson 10 already provides a
  self-contained 80–90 minute lesson. The NumPy program and reflection remain
  absent, so Monday's decision should begin with another evidence review.

- Week 1 has begun.
- Lesson 1 covers descriptive statistics, mean baselines, and linear search.
- The analyzer functions and integrated report are present, but the verification evidence remains incomplete.
- The test file now calls the imported analyzer and contains five checks that pass under pytest.
- The required unittest command still discovers zero tests because those checks are top-level functions.
- The required testing sequence has been retired after student feedback; its
  useful concepts remain available when a future project needs them.
- Lesson 8 was recalibrated twice from direct feedback: the original ML workflow
  was too advanced, while the first simplification repeated already-understood
  mean/MSE work.
- The current Lesson 8 is a coding-first mini-project. The math is supplied;
  the student implements data extraction, prediction generation, report
  construction, validation, and a linear maximum scan.
- The initial two functions were completed in about three minutes and now count
  only as a warm-up. The active assignment is a larger core-Python CSV pipeline
  given as a behavioral specification. The student chooses the architecture;
  scaffolding and tests are withheld until requested.
- The unscaffolded Lesson 8 CSV evaluator is now complete. Its iterative,
  assignment-first debugging process is the preferred model for future coding
  practice.
- `lesson_2_csv.py` now demonstrates successful basic CSV extraction,
  conversion, and filtering. Lesson 9 builds directly on that evidence with
  functions, validation, and single-pass aggregation.
- The updated CSV script now reads once and computes several statistics, while
  `lesson_3_numpy_intro.py` demonstrates basic array construction and mean
  calculation. Lesson 10 introduces one NumPy layer—metadata, elementwise
  operations, Boolean masks, and standardization—without assuming the missing
  Lesson 9 validation work is complete.
- `lesson_4_numpy.py` now demonstrates correct simple and compound Boolean
  masks, and `lesson_3_numpy_intro.py` constructs and inspects a 2-D array.
  Lesson 11 builds narrowly on that evidence with axes, row/column reductions,
  `argmax`, and aligned row filtering.
- `lesson_4_numpy_asgn.py` is now a runnable partial Lesson 11 submission. It
  loads the supplied exam data into a `(5, 2)` array, uses aligned Boolean
  masks, and reports correct descriptive statistics. Axis-based row means,
  `argmax`, standardization, validation, and function decomposition remain.
- July 31 is intentionally a flex/recovery day, so Lesson 12 is deferred until
  the Monday review of the remaining Lesson 9–11 evidence.
- The Monday review found a new partial CSV submission that fails when `Hours`
  contains `3.5`, plus the still-present syntax error and incomplete function,
  validation, axis, `argmax`, and standardization work. Lesson 12 reinforces
  those exact gaps before Pandas.
- The August 2 review found no newer completion evidence. Lesson 13 builds
  directly on the failing CSV attempt with a parser-function schema,
  `DictReader`, contextual validation, and fixed-rule prediction evaluation.
  Lesson 12 remains active for the unfinished NumPy refactor; Pandas is still
  deferred.

## Suggested Workflow

1. Read the current lesson file.
2. Work the math by hand first.
3. Complete the Python exercise in the starter file.
4. Save your outputs, derivations, and notes.
5. Use those artifacts to decide whether to reinforce or advance.

## Current Focus

The curriculum is currently working on:

- translating function contracts into Python
- transforming lists of dictionaries
- maintaining alignment between records and predictions
- constructing evaluation reports without mutating inputs
- validation and linear maximum scans
- NumPy array metadata and homogeneous numeric data
- elementwise transformations and Boolean-mask filtering
- aligned names and scores
- feature standardization and zero-variance handling
- 2-D row/column semantics and axis-wise aggregation
- indexed maximum reductions that preserve record identity
