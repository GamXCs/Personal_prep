def calc_mean(values):
    """Return the arithmetic mean of a non-empty list."""
    if not values:
        raise ValueError("Values must not be empty")
    total = 0
    for num in values:
        total += num
    return total / len(values)

def population_variance(values):
    """Return the population variance of a non-empty list."""
    # calculate mean, subtract values from mean, square values
    mean = calc_mean(values=values)
    var_values = [(num - mean)**2 for num in values]
    variance = sum(var_values) / len(var_values)
    return variance

def linear_search(values, target):
    """Return the index of target, or -1 if target is absent."""
    if not values:
        return -1
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

"""Func must contain:
- the original scores,
- the mean,
- the population variance,
- whether the target was found,
- the target index or `-1`,
- a spread label,
- a list of squared deviations from the mean,
- `mean_baseline_mse`, which should equal the population variance.
"""
def score_report(values, target_score):
    """Build the report dictionary described in the lesson."""
    
    def spread_label_helper(var):
        if var < 25:
            return "low spread"
        elif var <= 100:
            return "moderate spread"
        else:
            return "high spread"
        
    mean = calc_mean(values=values)
    sq_dev_mean_helper = [(num - mean)**2 for num in values]
    target_index = linear_search(values, target_score)
    variance = population_variance(values)
    spread_label = spread_label_helper(variance)

    dict_report = {"Original Scores": values,
            "Mean": mean,
            "Population Variance": variance,
            "Target Found" : target_index != -1,
            "Target Index" : target_index,
            "Squared Deviations from Mean" : sq_dev_mean_helper,
            "Spread Label": spread_label,
            "Mean Baseline MSE": variance
    }
    
    return dict_report

if __name__ == "__main__":
    SAMPLE_SCORES = [88, 91, 91, 76, 84, 95]
    SAMPLE_TARGET = 76

    print("Use this file as your starting point.")
    print("Sample scores:", SAMPLE_SCORES)
    print("Sample target:", SAMPLE_TARGET)
    print(calc_mean([1,2,3]))
    print(population_variance(SAMPLE_SCORES))
    print(score_report(SAMPLE_SCORES, SAMPLE_TARGET))