import pandas as pd
import os 

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