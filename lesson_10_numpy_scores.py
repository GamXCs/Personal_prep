import numpy as np
import csv


def load_data(filename):
    """Load and validate aligned names and scores from a CSV file."""
    with open(filename, newline="") as file:
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
        return names, scores


def analyze_data(names, scores):
    """Convert aligned data to arrays and calculate the NumPy results."""
    scores_arr = np.array(scores, dtype=int)
    names_arr = np.array(names)

    mean_val = scores_arr.mean()
    std_dev_val = scores_arr.std()
    if std_dev_val == 0:
        raise ValueError("Standard deviation cannot be zero")

    above_mean = scores_arr > mean_val
    abv_mn_names = names_arr[above_mean]
    abv_mn_scores = scores_arr[above_mean]

    standardized_score = (scores_arr - mean_val) / std_dev_val
    highest_score_index = standardized_score.argmax()

    return {
        "scores_arr": scores_arr,
        "mean_val": mean_val,
        "std_dev_val": std_dev_val,
        "abv_mn_names": abv_mn_names,
        "abv_mn_scores": abv_mn_scores,
        "standardized_score": standardized_score,
        "highest_name": names_arr[highest_score_index],
        "highest_score": scores_arr[highest_score_index],
    }


def format_output(results):
    """Present a completed analysis report."""
    scores_arr = results["scores_arr"]
    standardized_score = results["standardized_score"]

    pairs = [
        f"{name} {score}"
        for name, score in zip(
            results["abv_mn_names"], results["abv_mn_scores"]
        )
    ]

    print(f"Shape: {scores_arr.shape}")
    print(f"Size: {scores_arr.size}")
    print(f"Ndim: {scores_arr.ndim}")
    print(f"Dtype: {scores_arr.dtype}")
    print(f"Mean: {results['mean_val']:.2f}")
    print(f"Standard deviation: {results['std_dev_val']:.3f}")
    print(f"Above mean: {', '.join(pairs)}")
    print(f"Standardized scores: {np.round(standardized_score, 3)}")
    print(f"Standardized mean: {standardized_score.mean()}")
    print(f"Standardized standard deviation: {standardized_score.std()}")
    print(
        "Largest standardized score: "
        f"{results['highest_name']} {results['highest_score']}"
    )


if __name__ == "__main__":
    loaded_names, loaded_scores = load_data("scores_valid.csv")
    analysis_results = analyze_data(loaded_names, loaded_scores)
    format_output(analysis_results)
