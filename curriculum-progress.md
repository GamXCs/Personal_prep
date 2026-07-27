# AI/Data Science Grad School Prep Progress Log

Last updated: 2026-07-26

## Current module

- Week 1 - Descriptive statistics, scaling, and lookup strategies

## Schedule policy

- As of Friday, July 24, 2026, the curriculum is moving to a 4-day-per-week lesson cadence for sustainability during the school term.
- Friday is now the default flex/catch-up/recovery day rather than an automatic new-lesson day.
- Weekly plans should still be published on Mondays, but they should assume four core lesson days and one lighter buffer day.

## Current status

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

## Concepts with evidence of mastery

- Working implementations of mean, population variance, linear search, and `score_report` are present.
- The integrated report runs successfully on the sample dataset and returns the required fields.
- Full mastery is not yet artifact-verified because systematic tests, reading responses, and written derivations are not yet saved in the repository.
- The student has identified six appropriate test partitions in comments and created the expected test filename.
- The student removed the shadowing analyzer copies and wrote five correct basic assertions.
- Pytest executes all five current assertions successfully.

## Concepts awaiting evidence of mastery

- floating-point testing with tolerances
- invariants for statistical code and linear search
- artifact review of mathematics, tests, reading responses, and reflection
- dictionary lookup and complexity reasoning in the next advancement lesson
- writing assertions that exercise imported production functions rather than local copies
- using an independent oracle without duplicating the implementation
- writing tests discoverable by the required `unittest` runner
- checking collected-test counts before trusting a green result

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

## Required submission before advancement

- No remaining score-analyzer or test-runner submission is required.
- The next calibration lesson should request only a runnable core exercise, a few interpretation answers, and a short easiest/hardest-step reflection.

## Observed misconceptions or weak areas

- The former import-shadowing problem has been repaired.
- The current top-level test functions are valid for pytest, but the required `unittest` runner reports zero tests.
- The test file still lacks exception checks, pairwise-oracle cases, a collection audit, and the minimum required breadth.
- Evidence gaps remain around testing, mathematical explanation, and explicit complexity reasoning.
- The current variance implementation uses `sum()` and a list comprehension despite Lesson 1's request for explicit manual computation; review intent after tests are submitted rather than treating this as failure automatically.

## Recommended next lesson

- Teach a gentle, project-based introduction to regression using a small real dataset.
- Focus first on the workflow and baseline intuition; do not require regression to be derived or implemented from scratch.
- Introduce data inspection, a train/test split, a mean baseline, one-feature linear regression, MSE, and a simple residual check in small checkpoints.
- Include an easier core path that can be completed in 60–90 minutes and make extensions optional.
- Keep mathematical exposition brief and operational. Assign external math study only where it directly supports the project.

## Next-run guidance

- Inspect this log first.
- Do not resume the analyzer verification sequence merely because its artifacts are incomplete.
- Build the next lesson around a small real-data result while explaining every new workflow step.
- Use checkpoints, starter code with deliberate gaps, and an easier fallback path.
- Use the student's difficulty reflection to decide whether to slow down, repeat with variation, or add mathematical depth.
- Do not use a lengthy derivation as the central lesson activity or advancement gate.
- On Fridays, default to catch-up, review, or schedule maintenance rather than publishing a brand-new lesson unless the project state clearly warrants it.
