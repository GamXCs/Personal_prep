# Student Profile

Last updated: 2026-07-27

This file is the working student profile for the Grad School Prep project. It is synthesized from prior Grad School Prep planning conversations and current project artifacts. Treat it as durable context, but revise it whenever completed work shows that an assumption is inaccurate or outdated.

## Primary goal

Prepare for admission to and success in a graduate program focused on:

- Artificial Intelligence
- Machine Learning
- Data Science
- Applied Mathematics

The intent is long-term mastery, not short-term exercise completion.

## Academic background

- Undergraduate Computer Science student.
- Preparing specifically for graduate study in AI and Data Science.
- Balancing this preparation alongside regular university coursework.

## Current working background

The student appears comfortable with:

- Python fundamentals
- functions
- lists, dictionaries, sets, and tuples
- loops and conditionals
- file I/O
- basic object-oriented programming
- Jupyter notebooks
- Git and command-line workflows
- Docker basics
- introductory Pandas
- introductory NumPy
- basic descriptive statistics
- basic machine-learning vocabulary
- recent Java and JUnit test-debugging workflows

The student also appears to have coursework exposure to:

- algorithms
- systems programming
- automata or theory
- optimization
- cloud computing
- networking
- Java
- C
- Python

These items should be treated as prior exposure, not automatic mastery. Future lessons should verify depth through submitted work.

## Recent applied evidence from prior chats

Recent conversations suggest the student has practical exposure to:

- compiling and running Java programs from the terminal
- using JUnit 5 with an external JAR and classpath setup
- distinguishing dependency or classpath errors from code-logic errors
- reviewing small multi-file codebases for compile-time and logic bugs

This is useful background for general programming maturity, but it should not be treated as direct evidence of AI/Data Science mastery.

## Areas needing deeper development

The curriculum should place sustained emphasis on:

- mathematical maturity
- linear algebra intuition
- probability
- statistical reasoning
- machine-learning mathematics
- reading technical documentation carefully
- reading research papers
- building larger Python and data-science projects independently
- formal explanation of solutions
- algorithmic reasoning under interview-style constraints

## Learning preferences

The student prefers a professor or TA style rather than answer dumping.

Teaching should:

- give coding problems before giving complete solutions
- avoid providing full assignment implementations unless the student explicitly asks for them
- prioritize conceptual understanding over memorization
- review work and point out mistakes instead of immediately rewriting everything
- explain why bugs occur and how Python is interpreting the code
- ask guiding questions when appropriate
- start with hand reasoning before implementation
- preserve readable, explicit code before introducing shorter or more optimized versions

Preferred progression:

1. Solve by hand.
2. Attempt the coding problem independently.
3. Ask for hints, debugging help, or a partial walkthrough if stuck.
4. Optimize later if useful.

### Curriculum-format feedback

- On July 26, the student reported that the repeated score-analyzer verification lessons did not feel useful.
- The student prefers trying a project-based lesson with a real dataset and visible ML outcome, but is concerned that a full regression workflow may be too advanced.
- Introduce the next workflow as a gentle calibration lesson: use a small dataset, explain each new step, provide substantial scaffolding, and include an easier fallback path.
- The first attempted real-data regression lesson was still much too advanced.
  Do not combine a new library, unfamiliar dataset, splitting, model fitting,
  metrics, and residual analysis in one lesson. Introduce one layer at a time
  using hand-readable data and ordinary Python before returning to scikit-learn.
- The student reports that mean and squared-error calculations are already
  understood. Their perceived weakness is completing coding assignments.
  Emphasize specification-to-code practice, multi-function scaffolds, loops,
  data structures, debugging, and incremental checkpoints. Supply familiar
  arithmetic helpers when reimplementing them would distract from the coding
  objective.
- The student explicitly wants substantially more coding repetition across core
  Python, NumPy, Pandas, and machine-learning libraries. Treat programming
  fluency as the current primary development goal. Use short, cumulative
  implementation tasks in every lesson, revisit the same coding patterns in new
  contexts, and introduce libraries progressively rather than combining several
  unfamiliar APIs at once.
- Two small list-transformation functions took the student about three minutes
  and were judged insufficient practice. Do not equate heavy scaffolding or
  numerous tiny TODOs with meaningful coding repetition. Target roughly 30–60
  minutes of actual implementation per core lesson through cohesive programs,
  multiple interacting functions, realistic input/output, supplied acceptance
  tests, and debugging. Use tiny functions as warm-ups only.
- The student does not want starter architecture, function signatures, TODO
  blocks, or supplied tests at the beginning of an assignment. Give a behavioral
  specification, sample input/output, constraints, and acceptance criteria
  first. Let the student decide how to structure the program. Provide staged
  hints, scaffolding, signatures, or tests only when the student asks for them.
  This assignment-first preference overrides earlier guidance to provide
  substantial scaffolding by default.
- Lesson 8 confirmed the preferred difficulty and teaching loop: give a
  cohesive behavioral specification, let the student design and implement it,
  inspect their actual code when they ask for help, diagnose one blocker at a
  time, and preserve ownership of the solution. Repeat comparable data-flow,
  aggregation, debugging, and state-management challenges in new Python,
  NumPy, Pandas, and ML contexts so fluency develops through variation.
- Add depth only after checking how the first project-based lesson lands; do not interpret willingness to try it as prior mastery.
- The student does not want substantial mathematical instruction formatted inside the daily lesson files and has a separate book available for mathematics.
- On August 17, hands-on Lesson 9 work showed that the student needs more
  repetition distinguishing a list of record dictionaries from an individual
  dictionary. The next assignment should include a fresh linear scan in which
  the student keeps an entire record as the current best candidate, compares a
  numeric field, and replaces the candidate without changing its type. Use a
  different context and data so this is retrieval practice rather than a copy
  of the highest-student solution.
- On August 22, the student completed the core comparison-and-replacement logic
  correctly on the first Lesson 10 minimum-record variation and reported that
  the pattern is beginning to click. Continue including short, unscaffolded
  whole-record scans in several upcoming lessons—for example minimum, maximum,
  closest, or largest-error records—with changing field names and contexts.
  Space and vary the practice; do not turn every lesson into the same exercise.
- Center lessons on building Python, data-science, and machine-learning capability through runnable work.
- When mathematics is necessary, state the exact prerequisite and direct the student to a specific book section, problem set, or high-quality video. Include only the brief intuition needed to continue the coding work.
- Do not make a long derivation the main obstacle to completing a programming or ML lesson unless the student explicitly asks for mathematical instruction.

## Curriculum preferences

The student wants a cumulative curriculum that feels like a university sequence rather than isolated exercises.

Daily or scheduled lessons should typically integrate:

- Python or data-science instruction
- mathematics for machine learning
- algorithms or computer science fundamentals
- machine-learning theory
- technical reading
- an integrated coding exercise or mini-project

The curriculum should include:

- spiral review
- cumulative projects
- mixed-topic retrieval practice
- periodic review lessons

Current scheduling preference:

- As of August 12, 2026, assign at most three substantial lessons per week:
  Monday, Wednesday, and Friday.
- Tuesday and Thursday are completion, debugging, review, or recovery days. Do
  not publish a new assignment on those days.
- Robust assignments are welcome, but each should allow the intervening day for
  implementation and questions.
- Increase assignment frequency only after the student explicitly requests it
  or sustained completion evidence shows the current pace is comfortably
  manageable.
- Favor sustainable progress over maintaining a faster nominal schedule.
- For the week ending July 31, 2026, Lesson 11 is the stopping point. The
  student plans to complete Lessons 9–11 over the weekend while also working
  through a separate scheduled weekly Python/data-science/ML project.
- Resume curriculum decisions on Monday, August 3 only after reviewing the new
  weekend artifacts.

## Pacing and difficulty

- Difficulty should be calibrated from completed work, not lesson number alone.
- Do not restart at beginner programming unless actual work shows a genuine gap.
- Do not assume mastery because the student has seen a topic before.
- Advance only when there is evidence of successful completion.
- Reduce workload when the school schedule becomes crowded; sustainability matters more than nominal lesson count.

## Current project state assumptions

- Lesson 1 has now been officially published in this project.
- There is not yet verified completion evidence for Lesson 1 in the project files.
- Until such evidence exists, future runs should reinforce or continue Lesson 1 rather than assume advancement.

## How the scheduler should use this file

- Use this file for stable student context.
- Use `curriculum-progress.md` for current position in the curriculum.
- Use lesson files, submitted work, and notes as evidence for mastery decisions.
- If new evidence contradicts this profile, update this file rather than silently ignoring the mismatch.
