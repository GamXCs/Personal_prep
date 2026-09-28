import pandas as pd

# read csv 
exams = pd.read_csv("/Users/gamlielibn/Documents/Grad School Prep/exams.csv")

# require only Name, Exam1, and Exam2 and columns
expected_columns = ["Name", "Exam1", "Exam2"]

if list(exams.columns) != expected_columns:
    raise ValueError(f"Expected columns: {expected_columns}, but found {list(exams.columns)}")

# check if dataframe is empty
if exams.empty:
    raise ValueError("The CSV contains no rows")

# check for empty values in the columns
if exams["Name"].isna().any():
    raise ValueError("Name contains a missing value")

if exams["Name"].duplicated().any():
    raise ValueError("Name contains duplication")

if exams["Name"].str.strip().eq("").any():
    raise ValueError("Name contains a blank value")

# reject missing or nonnumeric exams
exam_columns = ["Exam1", "Exam2"]


# 2 any() methods bc first any returns one res per col
# second is checking if any col contains missing val
if exams[exam_columns].isna().any().any():
    raise ValueError("An exam score is missing")

# convert ot numeric
numeric_exams = exams[exam_columns].apply(
    pd.to_numeric,
    errors="coerce"
)

if numeric_exams.isna().any().any():
    raise ValueError("Exam contains nonnumeric score")

# pass numeric exams to check that scores are within range
exams[exam_columns] = numeric_exams

outside_scope = (exams[exam_columns] < 0) | (exams[exam_columns] > 100)

if outside_scope.any().any():
    raise ValueError("Exam scores must be between 0 and 100")


# display shape, column labels, dtypes
exams_shape = exams.shape
col_labels = exams.columns
exams_dtype = exams.dtypes

# Compute the two exam means using labeled column selection.
exam1_mean = exams["Exam1"].mean()
exam2_mean = exams["Exam2"].mean()

# Create `StudentMean` from Exam1 and Exam2 without a Python row loop.
student_means = exams[exam_columns].mean(axis=1)

# create StudentMean column
exams["StudentMean"] = student_means

# Identify the complete op-student row without sorting the entire table.
top_student_index = exams["StudentMean"].idxmax()
top_student = exams.loc[top_student_index]

# Filter complete rows whose `StudentMean` is at least 85.
mean_atleast_85_mask = exams["StudentMean"] >= 85
mean_atleast_85 = exams[mean_atleast_85_mask]

# Create `PerformanceBand`: `Excellent` for at least 90, `Strong` for at
# least 85 but below 90, and `Developing` below 85.
exams["PerformanceBand"] = "Developing"

strong_mask = exams["StudentMean"] >=  85
exams.loc[strong_mask, "PerformanceBand"] = "Strong"

excellent_mask = exams["StudentMean"] >= 90
exams.loc[excellent_mask, "PerformanceBand"] = "Excellent"

# print group by summary with performanceband and studentmean
groups = exams.groupby("PerformanceBand")
student_means_by_group = groups["StudentMean"]
band_summary = student_means_by_group.agg(["count", "mean"])
print(band_summary)