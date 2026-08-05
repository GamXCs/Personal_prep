import csv

with open("lesson-08-student-data.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    student_lst = []

    # convert hours, attendance, and actual score to numeric values
    for row in reader:
        name = row[0]
        hours = float(row[1])
        attendance = float(row[2])
        actual_score = float(row[3])

        student = {"name" : name,
                   "hours": hours,
                   "attendance": attendance,
                   "actual_score" : actual_score}
        student_lst.append(student)
        # get prediction value with formula: 30 + 6 * hours + 0.25 * attendance
print((student_lst[2]))