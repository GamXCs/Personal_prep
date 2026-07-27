from lesson_01_score_analyzer_starter import calc_mean, population_variance, linear_search, score_report

"""Test Cases:
-the sample list with target 76
-a target that is missing
-a one-element list
-repeated equal values, where variance should be 0
-empty input for the statistical functions
-that mean_baseline_mse is approximately equal to population_variance"""

def test_calc_mean():
    assert calc_mean([5,2,5]) == 4

def test_pop_variance():
    assert population_variance([2,2,2,2,]) == 0

def test_linear_target():
    assert linear_search([121, 22, 76], 76) == 2

def test_linear_missing_target():
    assert linear_search([121, 22, 76], 2) == -1

def test_score_func():
    report = score_report([88, 91, 91, 76, 84, 95], 76)
    assert report["Target Found"] is True
    assert report["Target Index"] == 3