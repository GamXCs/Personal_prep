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

    # The score data must be a 2-D matrix: student rows by exam columns.
    # This prevents later axis=0 and axis=1 calculations from using flat data.
    if scores_array.ndim != 2:
        raise ValueError("Scores must be a two-dimensional matrix.")

    # check that the number of names equals num of rows
    # first check shape of both arrays
    names_array_shape = names_array.shape
    scores_array_shape = scores_array.shape
   
    if names_array_shape[0] != scores_array_shape[0]:
        raise ValueError("The number of names is not equal to the number of rows.")

    #print matrix shape, dimensions, and dtype
    matrix_shape = scores_array.shape
    matrix_dimensions = scores_array.ndim
    matrix_dtype = scores_array.dtype
   

    # compute and print mean of each exam
    exam_mean = scores_array.mean(axis=0)

    # compute and print each students mean
    students_mean = scores_array.mean(axis=1)

   # print top student name and mean
    top_student_idx = students_mean.argmax()
    top_student_name = names_array[top_student_idx]
    top_student_score = students_mean[top_student_idx]

    # get students name/mean for scores >= 85
    score_85_or_greater = students_mean >= 85

    # A row-selection mask must contain True/False values, rather than numeric
    # positions or scores that NumPy would interpret differently.
    if score_85_or_greater.dtype != np.bool_:
        raise ValueError("The student selection mask must be Boolean.")

    # There must be exactly one mask decision for each student name so that
    # applying this mask preserves the alignment between names and score rows.
    if score_85_or_greater.shape != names_array.shape:
        raise ValueError("The student selection mask is not aligned with names.")

    # get names, scores, and rows of student who had qualifying scores
    students_abv_85 = names_array[score_85_or_greater]
    student_score_abv_85 = students_mean[score_85_or_greater]
    rows_abv_85 = scores_array[score_85_or_greater]

    # compute col standardized exam scores, reject zero variance
    # need the mean and std dev of each exam score col
    scores_std_dev = scores_array.std(axis=0)
    scores_mean = scores_array.mean(axis=0)

    # need to use np.any() due to more than 1 value being evaluated
    if np.any(scores_std_dev == 0):
        raise ValueError("Standard deviation cannot be 0")

    exam_standardized_exam_scores = (scores_array - scores_mean) / scores_std_dev

    # do internal checks by computing standardized mean/std
    # mean should be 0 and std 1
    standardized_mean = exam_standardized_exam_scores.mean(axis=0)
    standardized_std = exam_standardized_exam_scores.std(axis=0)

    if not np.allclose(standardized_mean, [0,0]):
        raise ValueError("Standardized mean should be 0")

    if not np.allclose(standardized_std, [1,1]):
        raise ValueError("Standardized std dev should be 1")

    # return probative values in a dict to use in summary function
    return {
            "matrix_shape":matrix_shape,
            "dimensions":matrix_dimensions,
            "data type":matrix_dtype,
            "exam mean scores":exam_mean,
            "student mean scores": students_mean,
            "top student": (top_student_name,top_student_score),
            "student at least 85": students_abv_85,
            "qualifying score rows":student_score_abv_85,
            "standardized scores":exam_standardized_exam_scores
    }


def format_output(records):
    pass

if __name__ == "__main__":
    filename = "exams.csv"    
    names, scores = load_data(filename)    
    # print(load_data(filename=filename))
    print(analyze_data(names, scores))
