# Grad School Prep

A cumulative graduate-school prep curriculum for AI, machine learning, data science, and applied math, combining Python, mathematics, algorithms, technical reading, and problem-first coding exercises.

## Purpose

This repository is a long-term study curriculum designed to prepare for graduate-level work in:

- artificial intelligence
- machine learning
- data science
- applied mathematics

The project emphasizes cumulative learning rather than isolated practice. Each lesson is meant to connect programming, mathematical reasoning, algorithmic thinking, and machine-learning theory.

The current pacing is three substantial assignments per week—Monday,
Wednesday, and Friday—with Tuesday and Thursday reserved for completion,
debugging, questions, and recovery.

**Current scheduling status:** Lesson 11 is the active curriculum lesson, and
the student began its CSV-loading stage on Thursday, September 3. Its published artifact
uses cumulative file number 19, but the student's course position is Lesson 11.
Its required whole-record minimum scan
is complete, and the main NumPy analyzer is now a working partial submission:
it validates and loads the valid CSV, preserves array alignment, masks above-
mean records, standardizes scores correctly, rejects zero spread, and recovers
the maximum identity with `argmax`. It now also has separate loading, analysis,
and presentation boundaries with a structured returned report. It still needs
explicit shape/mask and `np.isclose` checks, the rejected value in conversion
errors, and the reflection. Lesson 16 adds array
contracts, shared-mask invariants, incremental checks, and `argmax` identity
recovery while retaining the same Lesson 10 deliverable.
Lesson 9 is complete by the student's August 26 confirmation; its previously
listed contextual-validation and reflection items are no longer active gates.
Lesson 19 advances to 2-D matrix axes and feature-wise scaling while carrying
forward explicit shape, mask, contextual-error, and floating-point contracts.
Its integrated deliverable is `lesson_11_exam_matrix.py`. The loader now works
on the valid file and all six focused malformed fixtures; the NumPy analysis,
axis reductions, shared mask, feature scaling, report boundary, and reflection
remain to be completed.

The current near-term emphasis is coding fluency: repeated, cumulative practice
in core Python followed by NumPy, Pandas, and machine-learning libraries, with
one unfamiliar layer introduced at a time.

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
- [lesson-12-functions-validation-and-axis-reductions.md](lesson-12-functions-validation-and-axis-reductions.md): current reinforcement lesson on reliable function boundaries, validation, axes, and standardization
- [lesson-12-reliable-array-example.py](lesson-12-reliable-array-example.py): executable computation-boundary example
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
