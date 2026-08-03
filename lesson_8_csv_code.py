import numpy as np
import csv

with open("lesson-08-student-data.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    # convert hours, attendance, and actual score to numeric values
    for row in reader:
        hours = int(row[1])
        attendance = int(row[2])
        actual_score = int(row[3])

        