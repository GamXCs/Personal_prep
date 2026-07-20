# Lesson 1: Descriptive Statistics, Mean Baselines, and Linear Search

Date: Monday, July 20, 2026
Current module: Week 1 - Descriptive statistics, scaling, and lookup strategies
Estimated study time: 80 minutes
Difficulty: Foundational graduate-prep bridge

This is the official Week 1 Monday lesson. No prior lesson submissions are present in the project, so today establishes the core statistical and algorithmic ideas the rest of the week will build on.

## Weekly plan for Week 1

- Monday: Mean, population variance, linear search, and why squared loss selects the mean.
- Tuesday: Standard deviation, z-scores, and the role of feature scaling in optimization.
- Wednesday: Dictionary lookup, hash-table intuition, and efficient frequency counting.
- Thursday: Reinforcement day focused on debugging, derivations, and weak spots from submitted work.
- Friday: A short checkpoint mini-project combining descriptive statistics, lookup strategy, and baseline-model reasoning.

This plan is provisional. If your submitted work shows confusion, the next lesson should reinforce rather than advance.

## 1. Learning objectives

By the end of this lesson, you should be able to:

- implement the mean, population variance, and linear search in clear Python,
- explain variance as average squared distance from the mean,
- derive that the arithmetic mean minimizes total squared error,
- connect that derivation to constant-prediction baselines in regression,
- reason about why linear search is correct and when its `O(n)` cost is acceptable.

## 2. Prerequisites

You should already be comfortable with:

- Python variables, loops, conditionals, lists, and function definitions,
- arithmetic with fractions, exponents, and summation-style reasoning,
- the idea that an algorithm is a step-by-step procedure with measurable cost.

## 3. Retrieval review from prior exposure

Before reading further, answer these from memory:

1. If you loop through a list once, what is the time complexity in terms of `n`?
2. Why is `total / len(values)` only valid after you know `values` is non-empty?
3. If positive and negative deviations are added directly, what cancellation problem occurs?

Expected short answers:

- one pass through a list is `O(n)`,
- dividing by zero is invalid for an empty list,
- raw deviations can sum to zero even when the data is spread out.

## 4. Python instruction with executable example

For this curriculum, you should attempt the main coding exercise yourself before seeing a full implementation. This section only shows the core loop pattern you need, not the assignment solution.

A starter file is included in [lesson-01-score-analyzer-starter.py](</Users/gamlielibn/Documents/Grad School Prep/lesson-01-score-analyzer-starter.py>).

```python
scores = [88, 91, 91, 76, 84, 95]
total = 0

for score in scores:
    total = total + score
    print("running total:", total)

print("final total:", total)
print("count:", len(scores))
```

Expected output:

```text
running total: 88
running total: 179
running total: 270
running total: 346
running total: 430
running total: 525
final total: 525
count: 6
```

What to notice:

- A loop can accumulate information one element at a time.
- Mean starts from this pattern: accumulate a total, then divide by the count.
- Variance uses a similar pass, but on squared deviations from the mean.
- Linear search also uses the same one-pass mindset, but stops early if the target is found.

## 5. Mathematics

### Definitions and notation

Let the dataset be `x_1, x_2, ..., x_n`.

- Mean:
  `mu = (1/n) * sum_i x_i`
- Deviation of `x_i` from the mean:
  `x_i - mu`
- Population variance:
  `Var(x) = (1/n) * sum_i (x_i - mu)^2`

### Intuition

- The mean is the data's balance point.
- A deviation tells you whether one observation is above or below that balance point.
- Squaring deviations matters because it prevents sign cancellation and penalizes large misses more strongly.

### Worked hand calculation

Take the tiny dataset `[2, 4, 6, 8]`.

1. Mean:
   `mu = (2 + 4 + 6 + 8) / 4 = 20 / 4 = 5`
2. Deviations:
   `-3, -1, 1, 3`
3. Squared deviations:
   `9, 1, 1, 9`
4. Population variance:
   `Var(x) = (9 + 1 + 1 + 9) / 4 = 20 / 4 = 5`

So the variance is `5`. The dataset is centered at `5`, and the spread is captured by the average squared distance from `5`.

### Worked derivation: why the mean minimizes squared error

Suppose you want to summarize the entire dataset with one constant value `c`. Define the total squared error:

`S(c) = sum_i (x_i - c)^2`

Expand the square:

`S(c) = sum_i (x_i^2 - 2c x_i + c^2)`

Distribute the summation:

`S(c) = sum_i x_i^2 - 2c sum_i x_i + n c^2`

Differentiate with respect to `c`:

`S'(c) = -2 sum_i x_i + 2n c`

Set the derivative equal to zero:

`-2 sum_i x_i + 2n c = 0`

`2n c = 2 sum_i x_i`

`c = (1/n) * sum_i x_i`

Therefore the minimizing constant is exactly the mean.

Second-derivative check:

`S''(c) = 2n`

Since `2n > 0` for any dataset with at least one element, this critical point is a minimum.

This derivation matters because it converts a descriptive statistic into an optimization result.

## 6. Machine-learning theory connection

In supervised regression, a model predicts a numeric target. If the model is forced to predict one constant for every example and the loss is mean squared error, the best constant is the mean of the targets.

That fact explains several foundational ideas:

- The mean is the correct constant baseline under squared loss.
- Population variance is the average squared error of that constant mean baseline.
- A regression model is useful only if it can beat that baseline by exploiting structure in the features.
- High target variance usually means a naive constant predictor will leave more error unexplained.

Preview for later lessons:

- If the loss were absolute error instead of squared error, the optimal constant would become the median, not the mean.
- If features have very different scales, optimization can behave poorly even when the loss function is well chosen.

## 7. Algorithms and data-structures concept

### Linear search

Linear search scans the list from left to right until it finds the target or exhausts the list.

### Why it is correct

Correctness idea:

- After checking the first `k` elements, if the target has not been returned, then the target is not in positions `0` through `k - 1`.
- The loop maintains that claim each time it advances.
- If the algorithm returns an index, it is the index of an element equal to the target.
- If the loop ends and returns `-1`, every element has been checked, so the target is absent.

### Complexity

- Best-case time: `O(1)` when the target is first.
- Worst-case time: `O(n)` when the target is last or absent.
- Average-case time: `O(n)`.
- Extra space: `O(1)`.

### Practical tradeoffs

Linear search is appropriate when:

- the data is unsorted,
- the dataset is small,
- you only need a small number of lookups,
- readability matters more than lookup optimization.

Linear search becomes a bottleneck when:

- you repeatedly query a large collection,
- fast membership tests matter,
- a dictionary or set could preprocess the data for near-constant-time lookup.

## 8. Technical reading assignment

Read the Python tutorial section "5. Data Structures" from the official documentation:

- [Python Tutorial: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

Focus on list iteration and dictionary membership. Do not try to memorize every method.

Guiding questions:

1. Which operations obviously require traversing existing elements?
2. Why is a `for` loop pedagogically useful even when Python has shorter alternatives?
3. When would a dictionary be a better data structure than repeatedly scanning a list?

## 9. Integrated coding exercise

### Exercise: score analyzer with a mean baseline

Write a Python program that analyzes a list of quiz scores and makes the math-to-ML connection explicit.

Attempt this yourself first. If you get stuck, ask for one of the following rather than a full solution:

- a hint about function design,
- a debugging review of your current code,
- a walkthrough of one function only,
- help writing test cases,
- help interpreting an error message.

Required functions:

- `calc_mean(values)`
- `population_variance(values)`
- `linear_search(values, target)`
- `score_report(values, target_score)`

Your `score_report` function must return a dictionary containing:

- the original scores,
- the mean,
- the population variance,
- whether the target was found,
- the target index or `-1`,
- a spread label,
- a list of squared deviations from the mean,
- `mean_baseline_mse`, which should equal the population variance.

Suggested test data:

```python
scores = [88, 91, 91, 76, 84, 95]
target_score = 76
```

Acceptance criteria:

- the program runs with plain Python and no external libraries,
- mean and variance are computed manually rather than through `statistics`, NumPy, or Pandas,
- `linear_search` inspects one element at a time and returns `-1` when the target is missing,
- `score_report` calls the helper functions rather than duplicating their logic,
- the returned report clearly shows why `mean_baseline_mse` equals the population variance,
- you test at least one case where the target is present and one where it is absent.

Optional stretch goals:

- add explicit input validation for empty lists,
- compute standard deviation from the variance,
- write a short note comparing repeated linear search against storing the scores in a dictionary keyed by score.

## 10. Retrieval-practice quiz

Answer these without looking back:

1. What quantity does population variance average?
2. Why does squared loss select the mean instead of an arbitrary constant?
3. What does `-1` mean in the return value of linear search?
4. Why can population variance be interpreted as the mean baseline's squared error?
5. When is `O(n)` lookup acceptable in practice?

## 11. Quiz answers

1. It averages squared deviations from the mean.
2. Because differentiating total squared error and setting the derivative to zero yields the mean.
3. It means the target was not found anywhere in the list.
4. Predicting the mean for every example produces squared errors equal to squared deviations from the mean, and their average is the variance.
5. It is acceptable when the dataset is small, the data is unsorted, or only a few lookups are needed.

## 12. Suggested 60-90 minute study plan

- 10 minutes: Do the retrieval review and predict the example output before running code.
- 20 minutes: Reproduce the hand calculation for `[2, 4, 6, 8]` without notes.
- 15 minutes: Rework the derivation showing why the mean minimizes squared error, line by line.
- 25 minutes: Implement the exercise and test both a found-target and missing-target case.
- 10 minutes: Read the Python documentation section and answer the guiding questions in a few sentences.

If you have extra time, spend another 10 minutes writing a short comparison of list scanning versus dictionary lookup.

## 13. Submission checklist

Return all of the following before the curriculum advances:

- your Python solution file,
- console output from at least two test runs,
- one hand-worked derivation showing why the mean minimizes squared error,
- short written answers to the three reading questions,
- a brief note on any mistakes, sticking points, or unanswered questions.
