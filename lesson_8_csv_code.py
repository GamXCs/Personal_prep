import csv
import math 


# use dictionary to map numeric fieldnames to parser functions 
parsers = {'hours': float,
        'attendance': int,
        'actual_score': int}

# helper function to convert numerical rows and do checks
def parse_numeric_fields(record):
    parsed = {} # empty dict to add checked fields

    for field, parser in parsers.items():
        try:
            parsed[field] = parser(record[field])
        except KeyError as exc:
                raise ValueError(f"missing required field: {field}") from exc
        except ValueError as exc:
                raise ValueError(f"invalid {field}: {record[field]!r}") from exc

    if not math.isfinite(parsed["hours"]) or parsed["hours"] < 0:
        raise ValueError("Hours must be finite and nonnegative")
    
    if parsed["attendance"] < 0 or parsed["attendance"] > 100:
        raise ValueError("Attendance must be an integer between 0 and 100")

    if parsed["actual_score"] < 0 or parsed["actual_score"] > 100:
        raise ValueError("Scores must be an integer between 0 and 100")
    
    return parsed

def load_students(csv_path):

    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)

        # list to add processed dictionaries to
        student_lst = []

        # check csv header
        if reader.fieldnames is None:
            raise ValueError("Header missing from csv")

        # check to make sure headers are in the file
        req_col_names = {'name', 'hours', 'attendance', 'actual_score'}

        if set(reader.fieldnames) != req_col_names:
            raise ValueError("Columns do not match the required schema")

        

        # Reject blank names, negative or non-finite hours, attendance outside 0–100,
        # scores outside 0–100, missing/extra cells, empty data, and invalid numbers.
        for row_num, row in enumerate(reader, start=2):
            # check for extra cells
            if None in row:
                raise ValueError(f"Error: Extra cell found in {row_num}")

            # check for empty values
            if None in row.values():
                raise ValueError(f"Error: Missing value in {row_num}")

            # get name and check for empty name
            name = row["name"].strip()
            if name == "": # handle blank name
                raise ValueError("Error: name row is missing")

            # call helper function to process hours
            parsed_fields = parse_numeric_fields(row)

            # merge the name with the cleaned values
            student_dict = {"name": name}
            student_dict.update(parsed_fields)
            student_lst.append(student_dict) # add dictionaries to list

        # check is csv is empty
        if len(student_lst) == 0:
            raise ValueError("CSV contains no data")
    return student_lst
            
                    
        

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


if __name__ == "__main__":
    csv_path = "lesson-08-student-data.csv"   
