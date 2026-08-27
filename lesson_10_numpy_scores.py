import numpy as np
import csv

with open("scores_valid.csv",newline="") as file:
    reader = csv.DictReader(file)

    # check that header is not empty
    if reader.fieldnames is None:
        raise ValueError("Header is missing")

    # check that name and score headers are present
    if "Name" not in reader.fieldnames or "Score" not in reader.fieldnames:
        raise ValueError("Missing Columns")

    # empty lists to store names and scores
    names = []
    scores = []

    # using enumerate gives us the csv line number
    for row_number, row in enumerate(reader, start=2):
        name = row['Name'].strip()

        try:
             score = int(row['Score'])
        except ValueError:
            raise ValueError(f"Row {row_number}: Score must be an integer")

        # check for blank name
        if name == "":
            raise ValueError(f"Row {row_number} is missing a name")
        
        # reject scores outside of 0-100
        if score < 0 or score > 100:
            raise ValueError(f"Row {row_number}: Score is outside of the parameters of 0-100")
        
        names.append(name)
        scores.append(score)

    # check if scores are empty
    if not scores:
        raise ValueError("CSV file contains no scores")

# change names and scores to numpy arrays
scores_arr = np.array(scores,dtype=int)
names_arr = np.array(names)

# print score arrays shape, size, ndim, dtype
print(f"Shape: {scores_arr.shape}")
print(f"Size: {scores_arr.size}")
print(f"Ndim: {scores_arr.ndim}")
print(f"Dtype: {scores_arr.dtype}")

# compute mean and population std dev
mean_val = scores_arr.mean()
std_dev_val = scores_arr.std()
print(f"Mean: {mean_val}")
print(f"Standard deviation: {std_dev_val}")

# print above mean names and scores in input order (mask)
above_mean  = scores_arr > scores_arr.mean()

abv_mn_names = names_arr[above_mean]
abv_mn_scores = scores_arr[above_mean]

for name, score in zip(abv_mn_names, abv_mn_scores):
    print(f"{name}:{score}")
# TODO: turn the output into a one line

# calculate the standardized score without Py loop
# formula: original data value - mean of orig dist / std dev of orig dist
standardized_score = (scores_arr - mean_val) / std_dev_val
print(standardized_score)
print(f"Standardized mean: {standardized_score.mean()}")
print(f"Standardized standard deviation: {standardized_score.std()}")