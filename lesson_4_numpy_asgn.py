import numpy as np
import csv
from lesson_01_score_analyzer_starter import calc_mean,  standard_dev, median_val

with open("exams.csv",newline="") as file:
    reader = csv.reader(file)
    next(reader)

    names = []
    scores = []

    for row in reader:
        name = row[0]
        
        names.append(name)
        scores.append([
            int(row[1]),
            int(row[2])
            ])
    num_array = np.array(scores)
    
    exam1 = num_array[:,0]
    exam2 = num_array[:,1]

    # passing scores for exam 1
    passing_scores_exam1 = exam1 >= 70 # Boolean Mask
    p_exam1 = exam1[passing_scores_exam1]
    failing_scores_exam1 = exam1 < 70 # Boolean Mask
    f_exam1 = exam1[failing_scores_exam1]

    # passing scores for exam 2
    passing_scores_exam2 = exam2 >= 70 # Boolean Mask
    p_exam2 = exam2[passing_scores_exam2]
    failing_scores_exam2 = exam2 < 70 # Boolean Mask
    f_exam2 = exam2[failing_scores_exam2]


    # get names of students who passed both tests
    passed_both = (passing_scores_exam1 & passing_scores_exam2) # Boolean Mask
    for name, passed in zip(names, passed_both):
        if passed:
            print(name)

    # get high score
    high_score_exam1 = max(exam1)
    high_score_exam2 = max(exam2)
    print("High Score for Exam 1:",high_score_exam1)
    print("High Score for Exam 2:",high_score_exam2)

    # get low score
    low_score_exam1 = min(exam1)
    low_score_exam2 = min(exam2)
    print("Low Score for Exam 1:",low_score_exam1)
    print("Low Score for Exam 2:",low_score_exam2)

    # mean for both exams
    print("Mean for Exam 1:",calc_mean(exam1))
    print("Mean for Exam 2:",calc_mean(exam2))

    # median for both exams
    print("Median for Exam 1:",median_val(exam1))
    print("Median for Exam 2:",median_val(exam2))

    # median for both exams
    print("Standard Deviation for Exam 1:",standard_dev(exam1))
    print("Standard Deviation for Exam 2:",standard_dev(exam2))

    print("All Scores:\n", num_array)

    print("Passing Scores Exam 1:",p_exam1)
    print("Failing Scores Exam 1:",f_exam1)

    print("Passing Scores Exam 2:",p_exam2)
    print("Failing Scores Exam 2:",f_exam2)



"""Store scores in numpy array and print:
-All scores
-Passing scores
-Failing scores
-Students have passed both exams
-Highest score
-Lowest score
-Mean
-Median
-Standard deviation

Then compare to:
np.mean()

np.median()

np.std()
"""

