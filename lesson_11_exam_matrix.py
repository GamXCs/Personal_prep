import numpy as np 
import csv

def load_data(filename):

    # create empty lists to store n
    names = []
    scores = []

    with open(filename, newline="") as f:
        reader = csv.DictReader(f)

        # check if header is missing
        if reader.fieldnames is None:
            raise ValueError("Header is missing in csv")

        # check if columns are missing
        if "Name" not in reader.fieldnames or "Exam1" not in reader.fieldnames or "Exam2" not in reader.fieldnames:
            raise ValueError("Columns are missing in csv file")

        # start on second line to read data from csv file, skip line 1
        for physical_row, row in enumerate(reader, start=2):
            name = row["Name"].strip()

            # reject blank names
            if name == "":
                raise ValueError(f"Error: Name is missing in row {physical_row}")

            # convert scores to float values
            try:
                exam1 = int(row["Exam1"])
                exam2 = int(row["Exam2"])
            except ValueError:
                raise ValueError(f"Exam value in row {physical_row} must be an integer")

            # append names and scores to the empty lists
            names.append(name)
            scores.append([exam1,exam2])

            # reject scores outside of 0 - 100
            if exam1 < 0 or exam1 > 100 or exam2 < 0 or exam2 > 100:
                raise ValueError(f"Error in row {physical_row}. Values must be between 0-100")

        # check for empty data rows
        if len(scores) == 0:
            raise ValueError("CSV is empty")

    return names, scores

def analyze_data(names, scores):

    # convert names and scores to np arrays
    names_array = np.array(names)
    scores_array = np.array(scores)

    # check that the number of names equals num of rows
    # first check shape of both arrays
    print(f"Names array shape: {names_array.shape}")
    print(f"Scores array shape: {scores_array.shape}")

    if names_array.shape[0] != scores_array.shape[0]:
        raise ValueError("The number of names is not equal to the number of rows.")

    #print matrix shape, dimensions, and dtype
    matrix_shape = scores_array.shape
    matrix_dimensions = scores_array.ndim
    matrix_dtype = scores_array.dtype
    print(matrix_shape)
    print(matrix_dimensions)
    print(matrix_dtype)

    # compute and print mean of each exam
    exam_mean = scores_array.mean(axis=0)
    print(exam_mean)

    # compute and print each students mean
    students_mean = scores_array.mean(axis=1)
    print(students_mean)

   # print top student name and mean
    top_student_idx = students_mean.argmax()
    top_student_name = names_array[top_student_idx]
    top_student_score = students_mean[top_student_idx]

    print(f"Top student: {top_student_name} {top_student_score}")

    # get students name/mean for scores >= 85
    score_85_or_greater = students_mean >= 85
    students_abv_85 = names_array[score_85_or_greater]
    student_score_abv_85 = students_mean[score_85_or_greater]

    print(students_abv_85, student_score_abv_85)



if __name__ == "__main__":
    filename = "exams.csv"    
    names, scores = load_data(filename)    
    # print(load_data(filename=filename))
    print(analyze_data(names, scores))