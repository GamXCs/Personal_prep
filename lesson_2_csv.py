import csv
from lesson_01_score_analyzer_starter import calc_mean, population_variance, standard_dev, median_val

"""Read scores.csv
-print only values
-print only names
-print scores over 85
-get mean, median, variance, std dev
"""
score_vals = []
score_names = []
score_over_85 = []


with open("scores.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader) # will skip the header 

    # iterate through each row, append appropriate data
    for row in reader:
        name = row[0]
        score = int(row[1])

        score_vals.append(score)
        score_names.append(name)

        if int(score) > 85:
            score_over_85.append(score)
        
print("Scores:",score_vals)
print("Score names:",score_names)
print("Scores over 85:",score_over_85)

print("\n------Summary Statistics------")
print("Mean:", calc_mean(score_vals))
print("Median:", median_val(score_vals))
print("Variance:", population_variance(score_vals))
print("Standard Deviation:", standard_dev(score_vals))

print(population_variance([18,22,25,29,31]))



