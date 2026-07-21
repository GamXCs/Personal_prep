# AI/Data Science Grad School Prep Progress Log

Last updated: 2026-07-21

## Current module

- Week 1 - Descriptive statistics, scaling, and lookup strategies

## Current status

- Lesson 1 was published on Monday, July 20, 2026.
- The starter contains implementations of `calc_mean`, `population_variance`, and `linear_search`.
- On July 21, the student reported that all assigned work is complete except a dictionary assignment from the prior day.
- The completed work is not yet present in this repository, so this is recorded as self-reported completion rather than artifact-verified mastery.
- Lesson 2 remains available, but no additional lesson should be assigned until the dictionary work is complete and the finished artifacts are saved or submitted for review.
- The current project state is "Caught up except for dictionary assignment; new material paused."

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

## Concepts with evidence of mastery

- Basic implementations of mean, population variance, and linear search are present and syntactically plausible.
- The student reports completing the remaining mathematics, testing, reading, and reflection work.
- Full mastery is not yet artifact-verified because those completed materials are not present in the repository.

## Concepts awaiting evidence of mastery

- dictionary assignment completion
- artifact review of the reported completed mathematics, tests, reading responses, and reflection
- dictionary lookup and complexity reasoning, once the assignment is available for review

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

- Status: published; awaiting submission
- Date published: 2026-07-21
- Artifact: [lesson-02-verifying-statistical-code-and-invariants.md](</Users/gamlielibn/Documents/Grad School Prep/lesson-02-verifying-statistical-code-and-invariants.md>)
- Focus:
  - finish the incomplete `score_report`,
  - test floating-point results with tolerances,
  - use statistical and loop invariants as correctness checks,
  - derive `MSE(c) = Var(x) + (mu - c)^2`,
  - distinguish legitimate training-mean baselines from test leakage.

## Required submission before advancement

- completed dictionary assignment
- the already completed Lesson 1/2 work saved in the project or otherwise supplied for review
- any error output or notes from the dictionary assignment if debugging help is needed

## Observed misconceptions or weak areas

- No demonstrated misconception can yet be diagnosed from the partial code alone.
- Evidence gaps remain around testing, mathematical explanation, integration, and complexity reasoning.
- The current variance implementation uses `sum()` and a list comprehension despite Lesson 1's request for explicit manual computation; review intent after tests are submitted rather than treating this as failure automatically.

## Recommended next lesson

- First, finish and review the outstanding dictionary assignment without adding another full lesson.
- After the completed artifacts are reviewed, advance to standard deviation, z-scores, and feature scaling; avoid repeating dictionary material that the assignment demonstrates is mastered.

## Next-run guidance

- Inspect this log first.
- Look for the completed dictionary assignment and the student's other reported finished artifacts before deciding whether to advance.
- Do not assume mastery because a lesson artifact exists.
- Do not assign more work merely because the scheduled run occurs; preserve the catch-up window until the outstanding assignment is resolved.
