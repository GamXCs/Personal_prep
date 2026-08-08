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
                   "squared error" : squared_error}
        
        # add student info the empty list
        student_lst.append(student)

        # calc mean and mean squared error
        n = len(student_lst)
        total_error = 0
        total_squared_error = 0

        for student in student_lst:
            total_error += student_lst["error"]
            total_squared_error += student_lst["squared_error"]

        mean_error = total_error / n
        mse = total_squared_error / n    
        

print(f"Summary:\nMean Error: {mean_error}\nMean Squared Error: {mse} ")
print((student_lst[0]))