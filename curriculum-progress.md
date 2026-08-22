# AI/Data Science Grad School Prep Progress Log

Last updated: 2026-08-21

## Current module

- Week 2 - Regression workflow and honest evaluation

## Schedule policy

- As of August 12, 2026, the active cadence is three substantial assignments per
  week: Monday, Wednesday, and Friday.
- Tuesday and Thursday are reserved for implementation, debugging, review, and
  recovery. Scheduled runs on those days must not publish new assignments.
- Assignments may be more robust to support deeper coding practice, but Friday
  should become catch-up when the earlier work is incomplete.
- Increase frequency only after explicit student feedback or sustained evidence
  that the current cadence is comfortably manageable.
- Historical note: the August 2 finals-week hold ended on August 11 when the
  student explicitly requested Lesson 9. The July 24 four-day cadence is also
  superseded by the active three-assignment schedule above.
- Later prepublished lessons remain reference material and should not be treated
  as completed merely because they exist.

## Current status

- August 22 learning evidence: `lesson_10_candidate_practice.py` correctly
  rejects empty input, initializes from the first record, compares the numeric
  `validation_mse` field, and replaces the candidate with the whole model
  dictionary. The remaining small contract fix is to return the candidate and
  print it only in the main block. The student reports that this pattern is
  beginning to click and explicitly requests several more varied repetitions
  in future lessons. Preserve this as a spiral-review requirement.
- August 21 student-directed advancement: the Lesson 9 normal-input pipeline
  now runs successfully with three meaningful boundaries: CSV loading, report
  calculation, and formatted presentation. It prints the required count,
  two-decimal mean, highest student, input-ordered above-mean names, and correct
  score-band counts. The student explicitly requested advancement to Lesson 10
  and additional practice with the hardest pattern: maintaining a whole record
  while comparing one numeric field. Activated the existing Lesson 10 NumPy
  lesson and added a required, fresh minimum-record scan over model-result
  dictionaries. Lesson 9 contextual row/range validation and reflection remain
  cumulative evidence gaps rather than blockers to this requested advancement.
- August 21 scheduled review: new student work meaningfully improves the Lesson
  9 contract. `report()` now returns a complete dictionary containing the count,
  mean, highest-scoring record fields, above-mean names, and all four score-band
  counts, and a third `format_output()` boundary has been started. The program
  currently does not compile: the first formatting line nests double quotes
  inside a double-quoted f-string (`results["Count"]`), producing
  `SyntaxError: f-string: unmatched '['`. The formatter also refers to
  `records`, which is not one of its parameters, and overwrites the supplied
  `results` rather than formatting that argument. Score-range validation,
  physical-row context for malformed values, valid/malformed saved output, and
  `lesson-09-reflection.md` remain absent. Friday is therefore a focused
  catch-up day rather than a new Lesson 16. Preserve the student's code for
  debugging; after it compiles, review the full formatted report and validation
  behavior before advancing.

- August 20 scheduled review: no student-authored artifact changed after the
  August 19 lesson. The current pipeline still prints the correct above-mean
  names followed by `None`; it does not expose the full report, validate the
  `0..100` score range with row context, or provide the required reflection and
  saved valid/malformed runs. Thursday is reserved for implementation,
  debugging, and recovery, so no Lesson 16 or duplicate assignment was
  published. Lesson 15 remains the active self-contained 75–90 minute lesson.
  Its executable contract example and the student pipeline were rerun and
  compiled successfully. Next review should inspect the same completion
  evidence before deciding whether Friday is a new lesson or catch-up.

- August 19 scheduled lesson: no student-authored artifact changed after the
  August 18 review, so Lesson 9 remains partially complete. Published Lesson 15
  as a focused Wednesday reinforcement on return-value contracts, structured
  report dictionaries, computation/presentation separation, contextual row
  validation, and correctness of a linear best-record scan. It edits the same
  `lesson_09_score_pipeline.py` deliverable rather than opening a new project or
  advancing to NumPy. Added an independent executable contract example. Next
  review should require the complete returned report, a separate presentation
  boundary, `0..100` validation with row context, valid/malformed output, and
  the reflection before advancement.

- August 18 scheduled review: `lesson_09_score_pipeline.py` is now a genuine
  partial submission. It successfully uses `csv.DictReader`, validates required
  columns and nonempty data, converts scores, preserves name/score pairing, and
  correctly keeps an entire record dictionary as the maximum candidate. The
  normal run exits successfully and finds the correct above-mean names. It does
  not yet return or print the required report: it prints only the above-mean
  list followed by `None`; count, rounded mean, highest student, and band counts
  are computed or accumulated but never exposed. It currently has two
  meaningful functions rather than three, does not reject scores outside
  `0..100`, and conversion/blank-name failures do not identify the data row.
  `lesson-09-reflection.md` and saved valid/malformed outputs remain absent.
  Tuesday is reserved for completion and debugging, so no new lesson or second
  assignment was published. Finish the existing Lesson 9 report boundary and
  validation behavior before advancement.
- August 17 scheduled lesson: no student-authored artifact changed after the
  August 16 checkpoint, and the Lesson 9 implementation, outputs, and
  reflection remain absent. Published Lesson 14 as a bounded Monday
  reinforcement on accumulator state, loop invariants, and the distinction
  between opening a file once and traversing stored records twice. It continues
  the same `lesson_09_score_pipeline.py` deliverable rather than adding a
  second project or advancing to NumPy/Pandas.

- Current state: "Lesson 9 active; Monday/Wednesday/Friday assignment cadence in
  effect, with Tuesday/Thursday reserved for completion and support."
- August 16 scheduled review: no student-authored artifact changed after the
  August 15 checkpoint. `lesson_09_score_pipeline.py`, the reflection, and
  saved valid/malformed-input evidence remain absent. Sunday is outside the
  Monday/Wednesday/Friday assignment cadence, so no duplicate lesson or new
  workload was published. The existing Lesson 9 remains the active,
  self-contained 75–90 minute assignment and already includes all required
  curriculum components. Monday's decision should begin by reviewing any new
  Lesson 9 evidence; without it, keep reinforcement focused and bounded.
- August 15 scheduled review: no student-authored artifact changed after the
  August 14 checkpoint. `lesson_09_score_pipeline.py`, the reflection, and
  saved valid/malformed-input evidence remain absent. Saturday is outside the
  Monday/Wednesday/Friday assignment cadence, so no duplicate lesson or new
  workload was published. The existing Lesson 9 remains the active,
  self-contained 75–90 minute assignment, and its executable example was
  rerun successfully. The next scheduled assignment decision should review
  Lesson 9 completion evidence before advancing.
- August 14 scheduled review: no student-authored artifact changed after the
  August 13 checkpoint. `lesson_09_score_pipeline.py`, the reflection, and
  saved valid/malformed-input evidence remain absent. Friday is therefore a
  catch-up day under the active schedule rather than a third new assignment.
  The existing Lesson 9 remains the self-contained 75–90 minute lesson; its
  executable example was rerun successfully. Do not advance until the
  implementation demonstrates meaningful function boundaries, `DictReader`,
  contextual validation, the exact report facts, and a malformed-input run.
- August 13 scheduled review: no student-authored artifact changed after the
  August 12 review. The Lesson 9 implementation, reflection, and saved valid
  and malformed-input runs remain absent. Because Thursday is an explicit
  completion/support day, no duplicate lesson or new assignment was published.
  Friday should remain catch-up unless complete Lesson 9 evidence appears.
- August 12 scheduled review: the finals-week hold is confirmed ended, but no
  Lesson 9 submission artifact is present yet: `lesson_09_score_pipeline.py`,
  valid and malformed-input runs, and `lesson-09-reflection.md` are all absent.
  Lesson 9 was activated only on August 11, so no additional lesson was
  published today. Continue the existing 75–90 minute Lesson 9 assignment and
  review its evidence before advancing; prepublished Lessons 10–13 are not
  completion evidence.
- August 3 scheduled review: no new student lesson artifacts appeared after
  the August 2 review. In accordance with the finals-week hold, no Monday plan,
  Lesson 14, replacement quiz, or additional assignment was published.
- August 4 scheduled review: `lesson_8_csv_code.py` now parses the decimal
  numeric fields with `float`, builds one dictionary per student, preserves
  input order in a list, and runs successfully. This is meaningful progress on
  the active schema-driven CSV assignment. The prediction, validation,
  residual metrics, reusable functions, and reflection are not yet present.
  The finals-week hold remains active, so no new lesson or catch-up work was
  published.
- August 5 scheduled review: no project files changed after the August 4
  inspection, and no explicit request to end the finals-week hold is present.
  No Lesson 14, weekly plan, quiz, assessment, or additional catch-up work was
  published. Lessons 9–13 remain available at the student's existing pace.
- August 6 scheduled review: no new student-authored lesson artifacts or
  explicit request to end the finals-week hold appeared. In accordance with
  the hold, no Lesson 14, quiz, assessment, or additional catch-up work was
  published. The partial Lesson 13 CSV submission remains the newest evidence.
- August 8 scheduled review: no project artifacts changed after the August 7
  automation run, and no explicit request to end the finals-week hold is
  present. No Lesson 14, quiz, assessment, or additional catch-up work was
  published. Lessons 9–13 remain the available catch-up queue.
- August 10 scheduled review: no student-authored project artifacts changed
  after the previous review, and no explicit request to end the finals-week
  hold is present. No Lesson 14, weekly plan, quiz, assessment, or additional
  catch-up work was published. Lessons 9–13 remain available without a new
  deadline.
- August 11 scheduled review: no student-authored project artifacts changed
  after the August 10 review, and no explicit request to end the finals-week
  hold is present. In accordance with the hold, no Lesson 14, quiz, assessment,
  or additional catch-up work was published. The partial Lesson 13 CSV
  submission remains the newest evidence, and Lessons 9–13 remain available
  without a new deadline.

- Lesson 1 was published on Monday, July 20, 2026.
- The starter now contains implementations of `calc_mean`, `population_variance`, `linear_search`, and `score_report`.
- Running `lesson-01-score-analyzer-starter.py` now produces a sensible sample report for the suggested dataset.
- This is enough evidence to begin the Tuesday verification lesson, but not enough to advance beyond it yet.
- Artifact gaps remain around formal tests, saved report runs, reading responses, and written mathematical explanation.
- No new submission artifacts were present on July 23, so advancement to z-scores is not justified.
- Lesson 4 is a Thursday adequacy audit: it strengthens the same missing verification work rather than opening a new assignment track.
- Friday, July 24, 2026 is now treated as a flex/catch-up day under the revised 4-day schedule.
- Lesson 5 is a light Friday checkpoint that adds an independent pairwise variance oracle to the same cumulative harness; it does not open a new assignment track.
- A new `test_lesson_01_score_analyzer.py` appeared by July 25. It identifies relevant cases and imports the analyzer, but then redefines all four imported functions and contains no executable assertions.
- Lesson 6 uses this evidence for targeted reinforcement on test boundaries, independent expected values, and executable `unittest` cases.
- By July 26, the test file had improved substantially: it now calls the imported analyzer functions and contains five passing pytest-style tests.
- The required `unittest` runner still discovers zero tests because the checks are top-level functions rather than methods of a `unittest.TestCase`.
- Lesson 7 targets this runner mismatch and adds an explicit collection-count contract.
- Current state: "Lesson 7 published; assertions pass under pytest, but unittest discovery remains incomplete."
- Curriculum-direction override from student feedback: the repeated testing sequence is no longer productive and should stop here.
- Next state: trial a small, highly scaffolded real-data regression lesson, then recalibrate from the student's experience.
- Mathematics-format override: future lessons should prioritize Python/data-science/ML implementation. State necessary math prerequisites briefly and point to a book section, problem set, or reputable video instead of embedding long derivations.
- The student reviewed the first Lesson 8 and reported that it was much too
  advanced. That version has been replaced rather than assigned.
- The student then clarified that mean and squared-error calculations are
  already understood; the actual weakness to target is completing coding
  assignments.
- Lesson 8 was revised again into a coding-first prediction evaluator. The math
  helper is supplied, while the assignment targets four function contracts,
  list/dictionary transformations, validation, report construction, and a
  linear maximum scan.
- Current state: "Coding-first Lesson 8 published; four checkpoints available,
  with a two-checkpoint reduced path."
- Confirmed curriculum direction: programming fluency is the primary near-term
  goal. Subsequent lessons should progress through core Python, NumPy, Pandas,
  and ML libraries using cumulative coding assignments and one new library layer
  at a time.
- The student completed the two reduced-path functions correctly in about three
  minutes and reported that the workload was too small to improve coding
  fluency. Those functions are now recorded as a completed warm-up.
- Lesson 8 now uses a 45–60 minute core-Python CSV pipeline as its main
  assignment: file loading, schema validation, type conversion, non-mutating
  record transformation, aggregation, report formatting, and debugging against
  seven supplied acceptance tests.
- The student requested an assignment-first workflow without initial starter
  architecture, function signatures, TODOs, or tests. The generated pipeline
  starter and tests are retired from the active assignment and should not be
  used unless the student later requests scaffolding.
- Current state: "Lesson 8 warm-up complete; unscaffolded CSV pipeline
  specification active."
- August 11 interactive review: `lesson_8_csv_code.py` now completes the active
  unscaffolded Lesson 8 pipeline. Verified output is mean error `-1.75`, MSE
  `4.234375`, eight predictions within five points, and Ben as the largest
  squared error at `10.5625`.
- The student confirmed that this assignment's intensity and iterative
  debugging were exactly the desired methodology. Productive difficulty came
  from designing a list-of-dictionaries representation, separating record-level
  transformations from dataset-level aggregation, correcting indentation and
  accumulator scope, and tracking a maximum record.
- On July 28, `lesson_2_csv.py` provided new completion evidence: it correctly
  reads `scores.csv`, converts scores to integers, extracts names, and filters
  scores above 85.
- That script repeats the file-reading block three times and keeps all logic at
  module level. Lesson 9 advances from CSV syntax to reusable functions,
  validation, and single-pass aggregation without supplying architecture.
- Current state: "Lesson 9 published; working CSV basics evidenced, structured
  pipeline assignment active."
- By July 29, `lesson_2_csv.py` had been improved to open the CSV once and
  compute mean, median, variance, and standard deviation from aligned values.
- A new `lesson_3_numpy_intro.py` correctly creates a one-dimensional NumPy
  array and confirms that `ndarray.mean()` matches a manual mean calculation.
- The full Lesson 9 pipeline artifact, malformed-input evidence, and reflection
  are still absent, so reusable decomposition and validation remain unverified.
- Lesson 10 makes a calibrated first NumPy step: array metadata, elementwise
  operations, Boolean masks, alignment, and standardization. It cumulatively
  retains CSV validation instead of treating Lesson 9 as mastered.
- Current state: "Lesson 10 published; basic array creation evidenced, NumPy
  masking and structured CSV-to-array analysis active."
- By July 30, `lesson_4_numpy.py` correctly demonstrated three Boolean mask
  patterns, including a compound inclusive-range condition. The expanded
  `lesson_3_numpy_intro.py` also created a 2-D array and correctly inspected
  shape `(3, 3)`, integer dtype, and `ndim == 2`.
- `lesson_4_numpy_asgn.py` contains only the assignment description, so
  aggregation, aligned reporting, and edge-case behavior are not yet evidenced.
- Lesson 11 advances narrowly to 2-D axes and indexed reductions while
  retaining CSV validation, aligned masking, and column standardization.
- Current state: "Lesson 11 published; Boolean masking and 2-D metadata
  evidenced, axis-wise aggregation and argmax assignment active."
- Student pacing update on July 30: stop publishing lessons for the remainder
  of this week. The student is also completing assignments in the separate
  scheduled weekly Python/data-science/ML project and plans to work on Lessons
  9–11 over the weekend.
- Friday, July 31 is explicitly a flex/recovery day. Do not publish Lesson 12.
- Resume on Monday, August 3 by inspecting the submitted Lesson 9–11 artifacts
  first. Reinforce incomplete work rather than advancing automatically.
- July 31 review found substantial new work in `lesson_4_numpy_asgn.py`. It
  successfully reads `exams.csv` once, builds a `(5, 2)` integer array, extracts
  columns, constructs per-exam masks, combines masks without losing name/row
  alignment, and computes correct extrema and descriptive summaries.
- This submission is meaningful partial evidence for Lessons 10–11, but it does
  not yet implement axis-based row/column means, `argmax` identity recovery,
  column standardization, input validation, or reusable function boundaries.
- `lesson_3_numpy_intro.py` currently has a stray `-` on line 27, so the
  repository's student Python set does not compile cleanly. Preserve it as a
  small debugging target for the weekend rather than silently editing it.
- Current state: "July 31 flex review complete; partial 2-D NumPy submission
  runs, with axes, validation, standardization, decomposition, and one syntax
  repair still outstanding. Lesson 12 remains deferred until Monday."
- August 1 review found `lesson_8_csv_code.py`, which correctly begins reading
  the student dataset but fails immediately because decimal `Hours` values such
  as `3.5` are parsed with `int`. The stray `-` remains in
  `lesson_3_numpy_intro.py`; the partial exam script still runs successfully but
  lacks reusable functions, validation, axis reductions, `argmax`, and column
  standardization.
- Lesson 12 is a focused reinforcement lesson on explicit data contracts,
  function boundaries, validation, axis reductions, and standardization. Pandas
  remains deferred until this reliable NumPy pipeline is evidenced.
- Current state: "Lesson 12 published; reliable NumPy pipeline refactor active."
- August 2 review found no new artifacts or edits after Lesson 12. The same
  syntax error and NumPy acceptance gaps remain, and `lesson_8_csv_code.py`
  still fails at `int("3.5")`.
- Lesson 13 uses that concrete attempt for a core-Python lesson on schema
  dictionaries, `DictReader`, contextual validation, residual bias, and a
  one-pass worst-error scan. Pandas remains deferred, while Lesson 12 stays
  available as the parallel NumPy refactor.
- Current state: "Lesson 13 published; schema-driven CSV prediction evaluator active."

## Concepts introduced so far

- arithmetic mean as a balance point
- population variance as average squared deviation from the mean
- linear search over an unsorted list
- squared loss and the mean as the optimal constant predictor
- interpreting variance as the mean baseline's squared error
- numerical testing with tolerances
- statistical invariants
- squared-error decomposition around the mean
- loop-invariant proof of linear-search correctness
- example tests versus property tests
- input-space partitioning
- translation invariance of population variance
- expected comparison count in linear search
- transformation contracts and preprocessing leakage
- affine mean and variance transformations
- test adequacy through temporary fault injection
- sets for coverage bookkeeping
- independent test oracles
- pairwise population-variance identity
- nested-loop pair enumeration
- Python name binding and import shadowing
- system-under-test boundaries
- exact, approximate, and exception assertions
- hash-set coverage ledgers
- test collection, execution, and assertion contracts
- detection probability `1 - (1-p)^k`
- depth-first traversal of nested test suites
- translating function contracts into code
- transforming lists of dictionaries
- prediction/observation alignment
- non-mutating report construction
- input validation
- linear maximum scan
- one-pass CSV extraction with several statistical summaries
- NumPy one-dimensional array creation
- NumPy mean calculation checked against a manual calculation
- simple and compound NumPy Boolean masks
- two-dimensional array construction and metadata inspection
- row-wise and column-wise aggregation
- indexed reductions with `argmax`
- array shape, dimensionality, size, and dtype
- elementwise arithmetic and Boolean masking
- population standardization
- aligned multi-array filtering

## Concepts with evidence of mastery

- Working implementations of mean, population variance, linear search, and `score_report` are present.
- The integrated report runs successfully on the sample dataset and returns the required fields.
- Full mastery is not yet artifact-verified because systematic tests, reading responses, and written derivations are not yet saved in the repository.
- The student has identified six appropriate test partitions in comments and created the expected test filename.
- The student removed the shadowing analyzer copies and wrote five correct basic assertions.
- Pytest executes all five current assertions successfully.
- No regression concepts are marked mastered until the Lesson 8 output and
  interpretation are submitted.
- The student correctly implemented ordered dictionary-value extraction and a
  list-comprehension prediction transformation.
- The student completed the Lesson 8 CSV prediction evaluator using numeric
  conversion, record dictionaries, prediction/error fields, aggregation,
  conditional counting, and a linear maximum scan.
- The student can use `csv.reader`, skip a header, convert score strings to
  integers, preserve input order, and filter values with a condition.
- The revised CSV script opens the file once and reuses the collected scores
  for mean, median, variance, and standard-deviation calculations.
- The student can create a one-dimensional NumPy array and compute its mean.
- The student can construct Boolean masks with `<`, `>=`, and a compound
  inclusive interval.
- The student can construct a 2-D NumPy array and inspect its shape, dtype, and
  number of dimensions.
- The student can load the exam CSV into a `(5, 2)` integer matrix, extract
  columns, construct and combine Boolean masks, and preserve name alignment
  while reporting matching rows.
- The student can compute correct per-column minima, maxima, means, medians,
  and population standard deviations for the supplied exam data.

## Concepts awaiting evidence of mastery

- floating-point testing with tolerances
- invariants for statistical code and linear search
- artifact review of mathematics, tests, reading responses, and reflection
- dictionary lookup and complexity reasoning in the next advancement lesson
- writing assertions that exercise imported production functions rather than local copies
- using an independent oracle without duplicating the implementation
- writing tests discoverable by the required `unittest` runner
- checking collected-test counts before trusting a green result
- implementing multi-step functions from written contracts
- choosing loop state and intermediate variables
- preserving input/output alignment
- dictionary lookup and list-traversal complexity
- train/test separation and fitted regression are intentionally deferred
- decomposing a working script into reusable loading, computation, and
  presentation functions
- schema and row validation with `csv.DictReader`
- single-pass aggregation without repeated file reads
- organizing CSV work into reusable functions
- explicit CSV schema and row validation
- inspecting NumPy array metadata
- vectorized arithmetic and Boolean-mask selection
- preserving alignment across multiple NumPy arrays
- handling zero variance during standardization
- choosing the correct axis for row-wise versus column-wise aggregation
- preserving row/name alignment through a mask
- recovering record identity with `argmax`
- decomposing the exam program into reusable functions with guarded output
- validating headers, row widths, names, numeric conversion, score ranges, and
  empty input
- column-wise standardization and explicit zero-variance handling
- repairing and rerunning the syntax check for `lesson_3_numpy_intro.py`
- schema-driven numeric conversion with parser-function dictionaries
- contextual row and field validation with `csv.DictReader`
- residual sign and mean residual as a directional-bias diagnostic

## Latest hold-period evidence

- The August 10 repository review found no new student-authored artifacts and
  no explicit release from the finals-week hold. The partial Lesson 13 CSV
  submission remains the newest evidence; no new lesson was assigned.
- The August 8 repository review found no project changes after the August 7
  automation run and no explicit release from the finals-week hold. No new
  lesson was assigned.
- The August 6 repository review found no new student-authored artifacts or
  explicit release from the finals-week hold. No new lesson was assigned.
- The August 5 repository review found no new student-authored artifacts or
  edits since the August 4 review. The hold remains active.
- The August 4 run of `lesson_8_csv_code.py` succeeds and prints Chen's parsed
  record with decimal-valued numeric fields.
- Newly evidenced: correct decimal parsing, per-row dictionary construction,
  ordered record collection, and successful CSV traversal.
- Still unevidenced for Lesson 13: the fixed prediction formula, schema lookup,
  contextual validation, residual calculations, worst-error scan, reusable
  function boundaries, exact acceptance values, and reflection.
- No action is required during the hold. When the student explicitly resumes,
  review this partial submission before deciding whether to reinforce Lesson 13
  or advance.

## Lesson sequence

### Lesson 1 - Descriptive Statistics, Mean Baselines, and Linear Search

- Status: published and awaiting submission
- Date published: 2026-07-20
- Artifact: [lesson-01-descriptive-statistics-linear-search-loss.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-01-descriptive-statistics-linear-search-loss.md>)
- Starter scaffold: [lesson-01-score-analyzer-starter.py](</Users/gamlielibn/Documents/Grad School Prep/lesson-01-score-analyzer-starter.py>)
- Focus:
  - implement explicit Python for mean, variance, and linear search,
  - derive why the arithmetic mean minimizes squared error,
  - connect variance to mean-squared-error baseline behavior,
  - analyze correctness and complexity of linear search,
  - complete the integrated score-analyzer exercise without a provided full solution.

### Lesson 2 - Verifying Statistical Code with Invariants

- Status: assigned; evidence incomplete
- Date published: 2026-07-21
- Artifact: [lesson-02-verifying-statistical-code-and-invariants.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-02-verifying-statistical-code-and-invariants.md>)
- Focus:
  - verify the completed `score_report`,
  - test floating-point results with tolerances,
  - use statistical and loop invariants as correctness checks,
  - derive `MSE(c) = Var(x) + (mu - c)^2`,
  - distinguish legitimate training-mean baselines from test leakage.

### Lesson 3 - Property-Based Testing for Statistical Code

- Status: assigned; evidence incomplete
- Date published: 2026-07-22
- Artifact: [lesson-03-property-based-testing-statistical-code.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-03-property-based-testing-statistical-code.md>)
- Focus:
  - turn statistical invariants into executable tests,
  - partition the analyzer input space,
  - derive and test variance translation invariance,
  - connect transformation contracts to ML preprocessing,
  - finish the missing verification harness without a full supplied solution.

### Lesson 4 - Test Adequacy with Affine Invariants

- Status: active
- Date published: 2026-07-23
- Artifact: [lesson-04-test-adequacy-affine-invariants.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-04-test-adequacy-affine-invariants.md>)
- Focus:
  - determine whether the test oracle rejects plausible faults,
  - derive and test `Var(aX+b) = a^2 Var(X)`,
  - connect feature units to distance and optimization behavior,
  - use a set to audit input-partition coverage,
  - finish the shared Lessons 2–4 verification submission.

### Lesson 5 - Independent Test Oracles with Pairwise Variance

- Status: active flex-day checkpoint; evidence incomplete
- Date published: 2026-07-24
- Artifact: [lesson-05-independent-oracles-pairwise-variance.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-05-independent-oracles-pairwise-variance.md>)
- Focus:
  - verify variance using a computationally independent pairwise formula,
  - derive `Var(X) = [1/(2n^2)] sum_i sum_j (x_i-x_j)^2`,
  - connect pairwise squared distances to scale-sensitive ML behavior,
  - analyze the `O(n^2)` nested-loop oracle,
  - add a compact flex-day checkpoint to the existing verification harness.

### Lesson 6 - Testing Boundaries and Expected Values

- Status: active targeted reinforcement
- Date published: 2026-07-25
- Artifact: [lesson-06-testing-boundaries-and-expected-values.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-06-testing-boundaries-and-expected-values.md>)
- Focus:
  - repair the attempted test file so it calls imported analyzer functions,
  - prevent local definitions from shadowing the system under test,
  - use exact, approximate, and exception assertions,
  - retain the independent pairwise oracle,
  - audit behavioral partitions with a set.

### Lesson 7 - Test Discovery and Detection Probability

- Status: active targeted reinforcement
- Date published: 2026-07-26
- Artifact: [lesson-07-test-discovery-and-detection-probability.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-07-test-discovery-and-detection-probability.md>)
- Focus:
  - convert the five passing pytest-style functions into discoverable `unittest` methods,
  - treat collection count as part of the test contract,
  - derive fault-detection probability across independent cases,
  - connect executed sample counts to trustworthy ML evaluation,
  - analyze DFS traversal of nested test suites.

### Lessons 2–7 curriculum note

- Status: retired as a required sequence after student feedback on 2026-07-26
- Preserve the concepts and completed work, but do not require the remaining testing artifacts before moving forward.
- Return to testing only when a concrete project creates a natural need for it.

### Lesson 8 - Code a Prediction Evaluator

- Status: completed and interactively verified on 2026-08-11
- Date published: 2026-07-27
- Artifact: [lesson-08-coding-prediction-evaluator.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-08-coding-prediction-evaluator.md>)
- Complete example: [lesson-08-transformation-example.py](</Users/gamlielibn/Documents/Grad School Prep/lesson-08-transformation-example.py>)
- Starter scaffold: [lesson-08-prediction-evaluator-starter.py](</Users/gamlielibn/Documents/Grad School Prep/lesson-08-prediction-evaluator-starter.py>)
- Dataset: [lesson-08-student-data.csv](</Users/gamlielibn/Documents/Grad School Prep/lesson-08-student-data.csv>)
- Completed submission: [lesson_8_csv_code.py](</Users/gamlielibn/Documents/Grad School Prep/lesson_8_csv_code.py>)
- Retired support artifacts: `lesson_08_student_pipeline_starter.py` and
  `test_lesson_08_student_pipeline.py`; do not direct the student to them unless
  scaffolding or tests are explicitly requested.
- Focus:
  - implement four explicit function contracts,
  - transform lists of dictionaries without mutating inputs,
  - validate parallel collections and preserve alignment,
  - build detailed evaluation rows around supplied MSE math,
  - find the worst prediction with an \(O(n)\) scan.

### Lesson 9 - From a Working Script to a Single-Pass CSV Pipeline

- Status: core normal-input pipeline complete; validation/reflection evidence
  remains cumulative
- Date published: 2026-07-28
- Artifact: [lesson-09-single-pass-csv-pipelines.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-09-single-pass-csv-pipelines.md>)
- Executable example: [lesson-09-streaming-example.py](</Users/gamlielibn/Documents/Grad School Prep/lesson-09-streaming-example.py>)
- Evidence used: [lesson_2_csv.py](</Users/gamlielibn/Documents/Grad School Prep/lesson_2_csv.py>)
- Updated evidence: completed [lesson_8_csv_code.py](</Users/gamlielibn/Documents/Grad School Prep/lesson_8_csv_code.py>)
- Current assignment: finish the existing `lesson_09_score_pipeline.py` from
  the behavioral specification without replacing the student's design.
- Demonstrated: `DictReader`, required-column and empty-data checks, integer
  conversion, aligned record dictionaries, mean calculation, two-pass analysis
  of retained records, and a correct whole-record maximum scan.
- Remaining: return a complete report value, separate formatting/presentation
  into a third meaningful function, print every required fact, validate the
  `0..100` range, add data-row context to row errors, save valid and malformed
  runs, and write `lesson-09-reflection.md`.

### Lesson 14 - Designing Pipeline State Before Writing the Loop

- Status: active reinforcement of Lesson 9
- Date published: 2026-08-17
- Artifact: [lesson-14-pipeline-state-and-invariants.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-14-pipeline-state-and-invariants.md>)
- Executable example: [lesson-14-state-example.py](</Users/gamlielibn/Documents/Grad School Prep/lesson-14-state-example.py>)
- Current assignment remains `lesson_09_score_pipeline.py`; Lesson 14 adds a
  state-design method, not another submission.
- Focus: accumulator contracts, loop invariants, dependency-aware traversal,
  validation boundaries, and the time/space tradeoff of retaining records.

### Lesson 10 - NumPy Arrays and Boolean Masks

- Status: active by explicit student request on 2026-08-21
- Date published: 2026-07-29
- Artifact: [lesson-10-numpy-arrays-and-boolean-masks.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-10-numpy-arrays-and-boolean-masks.md>)
- Executable example: [lesson-10-array-example.py](</Users/gamlielibn/Documents/Grad School Prep/lesson-10-array-example.py>)
- Evidence used: [lesson_3_numpy_intro.py](</Users/gamlielibn/Documents/Grad School Prep/lesson_3_numpy_intro.py>)
- Required submission:
  - `lesson_10_candidate_practice.py`;
  - `lesson_10_numpy_scores.py`;
  - valid terminal output;
  - `lesson-10-reflection.md` with malformed-input and zero-variance evidence.
- Focus:
  - inspect array metadata and reason about homogeneous dtypes;
  - replace scalar loops with elementwise operations and Boolean masks;
  - preserve name/score alignment with a shared mask;
  - standardize numeric values and handle zero variance;
  - connect feature scaling to distance and optimization behavior;
  - retain CSV parsing and validation as cumulative practice.

### Lesson 11 - 2-D NumPy Arrays, Axes, and `argmax`

- Status: active
- Date published: 2026-07-30
- Artifact: [lesson-11-2d-arrays-axes-and-argmax.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-11-2d-arrays-axes-and-argmax.md>)
- Executable example: [lesson-11-axis-example.py](</Users/gamlielibn/Documents/Grad School Prep/lesson-11-axis-example.py>)
- Evidence used:
  - [lesson_4_numpy.py](</Users/gamlielibn/Documents/Grad School Prep/lesson_4_numpy.py>)
  - [lesson_3_numpy_intro.py](</Users/gamlielibn/Documents/Grad School Prep/lesson_3_numpy_intro.py>)
- Required submission:
  - `lesson_11_exam_matrix.py`;
  - valid terminal output;
  - `lesson-11-reflection.md` with malformed-input evidence.
- Focus:
  - interpret 2-D rows, columns, shape, and axes;
  - compute row-wise and column-wise statistics;
  - use `argmax` to preserve identity during an extreme-value scan;
  - apply a shared row mask to names and score rows;
  - standardize columns and reject zero-variance features.

### Lesson 12 - From a Working Array Script to a Reliable Data Function

- Status: active reinforcement
- Date published: 2026-08-01
- Artifact: [lesson-12-functions-validation-and-axis-reductions.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-12-functions-validation-and-axis-reductions.md>)
- Executable example: [lesson-12-reliable-array-example.py](</Users/gamlielibn/Documents/Grad School Prep/lesson-12-reliable-array-example.py>)
- Evidence used: `lesson_4_numpy_asgn.py`, `lesson_8_csv_code.py`, and
  `lesson_3_numpy_intro.py`.
- Focus:
  - separate loading, validation, computation, and presentation;
  - select numeric types from explicit field contracts;
  - finish axis-wise means, `argmax`, and aligned row masking;
  - standardize feature columns and reject zero variance;
  - validate a CSV-to-NumPy boundary before introducing Pandas.

### Lesson 13 - Schema-Driven CSV Parsing and Residual Bias

- Status: active core-Python reinforcement
- Date published: 2026-08-02
- Artifact: [lesson-13-schema-driven-csv-and-residual-bias.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-13-schema-driven-csv-and-residual-bias.md>)
- Executable example: [lesson-13-schema-example.py](</Users/gamlielibn/Documents/Grad School Prep/lesson-13-schema-example.py>)
- Evidence used: `lesson_8_csv_code.py` and the unchanged Lesson 12 artifacts.
- Focus:
  - represent field contracts with a parser-function dictionary;
  - parse header-named records and validate them with useful context;
  - finish the fixed linear-prediction evaluator without a supplied solution;
  - interpret residual sign and mean residual alongside MSE;
  - use a linear maximum scan instead of sorting.
- Recommended next lesson: review the submitted NumPy program first. Advance to
  two-dimensional arrays and axes only if masking, alignment, decomposition,
  and edge-case handling are sound; otherwise reinforce those specific gaps.
- Focus:
  - refactor repeated top-level CSV work into a cohesive program,
  - use header-based records and deliberate validation,
  - compute several summaries with a single traversal,
  - derive running count/sum updates,
  - connect trustworthy parsing to ML feature-label alignment,
  - analyze a one-pass maximum scan.

## Required submission before advancement

- No remaining score-analyzer or test-runner submission is required.
- Submit `lesson_09_score_pipeline.py`, its valid terminal report, one malformed
  input run, and `lesson-09-reflection.md`.
- Preserve the unfinished Lesson 8 pipeline specification for later cumulative
  reuse; Lesson 9 is the calibrated core-Python step supported by the newest
  completed CSV artifact.

## Observed misconceptions or weak areas

- The former import-shadowing problem has been repaired.
- The current top-level test functions are valid for pytest, but the required `unittest` runner reports zero tests.
- The test file still lacks exception checks, pairwise-oracle cases, a collection audit, and the minimum required breadth.
- Evidence gaps remain around testing, mathematical explanation, and explicit complexity reasoning.
- The current variance implementation uses `sum()` and a list comprehension despite Lesson 1's request for explicit manual computation; review intent after tests are submitted rather than treating this as failure automatically.

## Recommended next lesson

- If Lesson 9 is correct and appropriately challenging, introduce NumPy arrays
  by reproducing the same score transformations with one new library layer.
- If it is difficult, review its function boundaries and validation path before
  adding a library.
- If it is too easy, extend the same pipeline with grouping and tests before
  NumPy.
- After core Python transformations are demonstrated, use this progression:
  NumPy arrays and vectorized transformations; Pandas selection, filtering, and
  grouped aggregation; then scikit-learn dataset splitting, fitting, prediction,
  and evaluation. Do not introduce multiple stages in the same first exposure.
- Review the Lesson 11 submission before introducing Pandas. Advance only if
  the output demonstrates correct axis selection, alignment, and column-wise
  standardization; otherwise reinforce the specific failed operation.

## Next-run guidance

- Continue whole-record candidate scans across the next several lessons using
  varied tasks such as minimum loss, maximum residual, closest value, or worst
  validation case. Require the candidate to remain a complete record while one
  numeric field drives comparison; do not supply the completed loop initially.
- The student explicitly requested that the August 18 assignment revisit the
  difficult Lesson 9 pattern: traverse a list of dictionaries, access fields
  on one record, and maintain the whole best record as a maximum/minimum
  candidate. Use a new dataset/context and do not pre-supply the completed scan.
- The finals-week hold is authoritative. Do not publish Lesson 14, a Monday
  plan, a review day, or any substitute assignment until the student explicitly
  asks to resume.
- A scheduled run during the hold should normally make no project changes. It
  may report that the curriculum is still paused; review new student artifacts
  only if they actually appear.
- Inspect this log first.
- Lesson 12 has now been published from the latest artifact review. Do not
  introduce Pandas until its focused NumPy acceptance evidence is present.
- Do not resume the analyzer verification sequence merely because its artifacts are incomplete.
- Inspect for the Lesson 9 program, valid output, malformed-input output, and
  reflection.
- Use the recorded implementation time and difficulty to choose refactoring
  review, a grouping extension, or the first NumPy lesson.
- Do not use a lengthy derivation as the central lesson activity or advancement gate.
- On Fridays, default to catch-up, review, or schedule maintenance rather than publishing a brand-new lesson unless the project state clearly warrants it.
- Inspect for `lesson_11_exam_matrix.py`, valid output, malformed-input
  evidence, and `lesson-11-reflection.md`. Use the recorded difficulty to
  decide between an axes review and a first Pandas selection lesson.
- Treat `lesson_4_numpy_asgn.py` as the student's partial Lesson 11 submission
  even though its filename differs from the requested name. Do not require a
  needless rename before reviewing the code.
- Check whether the stray `-` in `lesson_3_numpy_intro.py` was removed.
- In the partial exam assignment, check specifically for `mean(axis=0)`,
  `mean(axis=1)`, `argmax`, column standardization, at least three meaningful
  functions, and one demonstrated malformed-input failure. Introduce Pandas
  only when those core operations are sound.
- Inspect for `lesson-12-reflection.md`, a clean compile of the two named
  student files, and explicit valid/malformed runs. If these are sound, the
  next lesson may introduce Pandas selection; otherwise reinforce only the
  remaining failed acceptance criterion.
- Inspect `lesson_8_csv_code.py` for three function boundaries, schema lookup,
  decimal-hour parsing, contextual malformed-input behavior, and the Lesson 13
  acceptance values. Inspect `lesson-13-reflection.md` before treating reliable
  core-Python CSV evaluation as evidenced.
