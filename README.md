# Grad School Prep

A cumulative graduate-school prep curriculum for AI, machine learning, data science, and applied math, combining Python, mathematics, algorithms, technical reading, and problem-first coding exercises.

## Purpose

This repository is a long-term study curriculum designed to prepare for graduate-level work in:

- artificial intelligence
- machine learning
- data science
- applied mathematics

The project emphasizes cumulative learning rather than isolated practice. Each lesson is meant to connect programming, mathematical reasoning, algorithmic thinking, and machine-learning theory.

The current pacing is a 4-day lesson week during the school term, with one built-in flex/catch-up day for sustainability.

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

## Current Status

As of Monday, July 27, 2026:

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
