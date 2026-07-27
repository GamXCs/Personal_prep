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

## Current Status

As of Sunday, July 26, 2026:

- Week 1 has begun.
- Lesson 1 covers descriptive statistics, mean baselines, and linear search.
- The analyzer functions and integrated report are present, but the verification evidence remains incomplete.
- The test file now calls the imported analyzer and contains five checks that pass under pytest.
- The required unittest command still discovers zero tests because those checks are top-level functions.
- Lesson 7 is the current reinforcement: convert the checks to a `unittest.TestCase`, audit collection count, and complete the missing partitions without advancing to a new topic track.

## Suggested Workflow

1. Read the current lesson file.
2. Work the math by hand first.
3. Complete the Python exercise in the starter file.
4. Save your outputs, derivations, and notes.
5. Use those artifacts to decide whether to reinforce or advance.

## Current Focus

The curriculum is currently working on:

- arithmetic mean
- population variance
- squared-loss intuition
- linear search
- connecting statistics to regression baselines
