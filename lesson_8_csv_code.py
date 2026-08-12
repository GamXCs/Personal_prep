import csv

with open("lesson-08-student-data.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    student_lst = []

    # convert hours, attendance, and actual score to numeric values
    # get prediction value with formula: 30 + 6 * hours + 0.25 * attendance
    # calculate mean error and mse (mean squared error)
    for row in reader:
        name = row[0]
        hours = float(row[1])
        attendance = float(row[2])
        actual_score = float(row[3])
        prediction_value = 30 + 6 * hours + 0.25 * attendance
        error = actual_score - prediction_value
        squared_error = error**2
       


        student = {"name" : name,
                   "hours": hours,
                   "attendance": attendance,
                   "actual_score" : actual_score,
                   "prediction_value" : prediction_value,
                   "error" : error,
                   "squared_error" : squared_error}
        
        # add student info the empty list
        student_lst.append(student)

    # calc mean and mean squared error
    n = len(student_lst)
    total_error = 0
    total_squared_error = 0

    # sentinel for counting abs val prediction errors
    predict_errors_five_and_under = 0

    # identify student with largest squared error
    worst_student = student_lst[0]


    for student in student_lst:
        total_error += student["error"]
        total_squared_error += student["squared_error"]

        # how many predictions have an absolute error of at most 5
        if abs(student["error"]) <= 5:
            predict_errors_five_and_under += 1

        # identify student with largest squared error
        if student["squared_error"] > worst_student["squared_error"]:
            worst_student = student
        worst_student_name = worst_student["name"]
        worst_student_value = worst_student["squared_error"]

    mean_error = total_error / n
    mse = total_squared_error / n    

   
print(f"Highest squared error:\n{worst_student_name}: {worst_student_value}")
print(f"Number of predictions that have an absolute error of at most 5: {predict_errors_five_and_under}")      
print(f"Summary:\nMean Error: {mean_error}\nMean Squared Error: {mse} ")
print((student_lst[0]))