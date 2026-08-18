# Lesson 14 — Designing Pipeline State Before Writing the Loop

**Module:** Week 2 — Regression workflow and honest evaluation  
**Estimated time:** 65–80 minutes  
**Difficulty:** Intermediate core Python reinforcement

## Why this lesson now

Lesson 9 is still the active assignment, but no implementation artifact is
present yet. This lesson does not add a second project. It gives you a more
precise way to design the same `lesson_09_score_pipeline.py`: define the state
that each valid row updates, then keep loading, summarizing, and presentation
separate. The goal is to unblock implementation without supplying signatures,
tests, or the solution.

## Learning objectives

By the end, you should be able to:

1. translate report requirements into explicit accumulator state;
2. distinguish row validation from dataset aggregation;
3. state and use a loop invariant for a streaming summary;
4. explain why feature/label validation changes downstream model reliability;
5. analyze the time and space costs of streaming versus storing records.

## Prerequisites and retrieval

You need loops, functions, dictionaries, `csv.DictReader`, integer conversion,
means, and the Lesson 9 specification. Before continuing, answer from memory:

- What type does `DictReader` initially give every cell value?
- Which two values are sufficient to compute a mean after one traversal?
- Why should a computation function return a report instead of printing it?

## Python instruction: make state visible

Run:

```bash
python3 lesson-14-state-example.py
```

The example incrementally summarizes response times. It uses a dictionary as a
named state record. After each item, every field has a specific meaning; this
is easier to reason about than unrelated variables whose contracts are unclear.

For the score pipeline, first make a private planning table like this—replace
the question marks yourself before coding:

| Required output | State needed during the loop | Update rule |
|---|---|---|
| count | `count` | `count + 1` |
| mean | ? | ? |
| highest student | ? | ? |
| score bands | ? | ? |
| above-mean names | ? | notice the dependency |

The last row is the important design wrinkle: whether a score is above the
final mean is unknown until the total and count are known. You may still open
the file only once while storing validated name/score records for a later
in-memory traversal. “Open once” does not mean “perform every possible result
in one loop.” State only that your implementation actually needs.

## Mathematics: accumulator invariant

For valid scores \(x_1,\dots,x_k\), define state

\[
C_k=k, \qquad S_k=\sum_{i=1}^{k}x_i.
\]

After reading \(x_{k+1}\), update

\[
C_{k+1}=C_k+1, \qquad S_{k+1}=S_k+x_{k+1}.
\]

Worked check for `87, 92, 75`: start at `(0, 0)`, then obtain `(1, 87)`,
`(2, 179)`, and `(3, 254)`. Thus the final mean is
\(S_3/C_3=254/3\approx84.67\).

The invariant says that after processing exactly \(k\) valid rows, `count`
equals \(k\) and `total` equals their sum. Initialization, preservation by the
two updates, and termination together justify the result.

## Machine-learning connection

A data loader establishes the contract for the matrix of features \(X\) and
target vector \(y\). If one row is silently skipped from only one structure,
the model can train on mismatched examples. If an out-of-range score is
accepted, reported loss or baseline statistics may describe invalid data.
Validation is therefore part of model correctness, not cosmetic cleanup.

The dataset mean is also a constant-prediction baseline. An incorrect running
sum changes that baseline and can make a later model look artificially better
or worse.

## Algorithms and data structures: state-size tradeoff

A streaming count/sum/maximum scan visits each of \(n\) rows once:

- time: \(O(n)\);
- auxiliary space: \(O(1)\) for those summaries;
- correctness: the accumulator and maximum invariants hold after every row.

The above-mean name list requires knowledge of the final mean. Storing \(n\)
validated records uses \(O(n)\) space and allows an \(O(n)\) in-memory second
scan, for total \(O(n)\) time. Reopening the file is unnecessary. This is a
reasonable tradeoff when the output depends on a statistic learned only at the
end.

## Technical reading

Read Python's [`csv.DictReader` documentation](https://docs.python.org/3/library/csv.html#csv.DictReader)
and the short section on [`if __name__ == "__main__"`](https://docs.python.org/3/library/__main__.html#idiomatic-usage).

Guiding questions:

1. Where does `DictReader` obtain field names by default?
2. What happens to extra or missing fields in a row?
3. Why should reusable functions avoid doing work merely because their module
   was imported?
4. Which validation belongs at the raw-row boundary, and which checks require
   the complete dataset?

## Integrated coding exercise: complete Lesson 9

Create the already-required `lesson_09_score_pipeline.py` from the full Lesson
9 behavioral specification. Do not create a separate Lesson 14 program and do
not modify the completed Lesson 8 artifact.

Before coding, write down:

1. the input and output contract of at least three meaningful responsibilities;
2. the accumulator state and meaning of every field;
3. the order in which header validation, row validation, aggregation, and
   formatting occur.

Then implement independently. The program must open `scores.csv` once with
`DictReader`, validate required columns and each row with row-number context,
reject scores outside `0..100`, reject empty data, compute the Lesson 9 report,
and print only under a main guard.

### Acceptance criteria

On the supplied file, the output includes: count `7`, mean `84.29`, highest
`Emma (98)`, above-mean names `Alice, Bob, Emma, Grace`, and band counts `2, 3,
1, 1` from highest to lowest band. In addition:

- the file is opened exactly once;
- at least three meaningful functions separate responsibilities;
- blank names, invalid integers, out-of-range scores, missing headers, and no
  data produce clear errors;
- computation returns data rather than depending on mutable globals;
- row order never breaks name/score alignment.

### Optional stretch goals

- Accept a path from `sys.argv`.
- Add a median and explain its additional state or sorting cost.
- Demonstrate that reordered CSV columns do not change the report.

## Retrieval-practice quiz

1. What invariant connects `count` and `total` to processed rows?
2. Why can above-mean names require a second in-memory traversal?
3. Does a second list traversal violate the “open once” rule?
4. What are the time and space costs when validated records are stored?
5. Give one ML consequence of feature/label misalignment.

## Quiz answers

1. After \(k\) valid rows, `count == k` and `total` is their sum.
2. The final mean is unknown until all scores have contributed.
3. No. The CSV can be read once and the stored records traversed afterward.
4. \(O(n)\) time and \(O(n)\) auxiliary space.
5. A feature row can be paired with the wrong target, invalidating training or
   evaluation.

## Suggested 65–80 minute study plan

- 0–8: retrieval questions and run the example.
- 8–18: read the state table, invariant, and Lesson 9 acceptance criteria.
- 18–25: write the responsibility and accumulator plan.
- 25–60: implement and debug `lesson_09_score_pipeline.py`.
- 60–68: run one valid and one malformed-input case.
- 68–75: reading and quiz.
- 75–80: save the reflection and terminal evidence.

## Submission checklist

- `lesson_09_score_pipeline.py`
- valid terminal output
- one malformed-input command and output
- `lesson-09-reflection.md` answering the four Lesson 9 prompts and noting
  whether the state-planning step helped

