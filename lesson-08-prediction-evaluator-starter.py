"""Lesson 8: build the Python around a supplied prediction rule."""

STUDENTS = [
    {"name": "Amina", "hours": 1, "actual_score": 55},
    {"name": "Ben", "hours": 2, "actual_score": 60},
    {"name": "Chen", "hours": 3, "actual_score": 68},
    {"name": "Dalia", "hours": 4, "actual_score": 74},
    {"name": "Eli", "hours": 5, "actual_score": 82},
    {"name": "Fatima", "hours": 6, "actual_score": 88},
]


def extract_values(records, key):
    """Return each record's value for key, preserving order."""
    # TODO: Checkpoint 1
    values = []
    for record in records:
        values.append(record[key])
    return values 


def make_predictions(records, intercept, hourly_gain):
    """Return intercept + hourly_gain * hours for each record."""
    # TODO: Checkpoint 2
    return [intercept + hourly_gain * record['hours'] for record in records]



def build_evaluation_rows(records, predictions):
    """Build one new evaluation dictionary per record."""
    # TODO: Checkpoint 3
    raise NotImplementedError


def find_worst_prediction(evaluation_rows):
    """Return the row with the largest squared error."""
    # TODO: Checkpoint 4
    raise NotImplementedError


def mean_squared_error(actual_values, predicted_values):
    """Supplied math helper; you do not need to modify it."""
    if len(actual_values) != len(predicted_values):
        raise ValueError("Actual and predicted lists must have equal lengths")
    if not actual_values:
        raise ValueError("Cannot evaluate empty lists")

    squared_error_total = 0
    for actual, predicted in zip(actual_values, predicted_values):
        squared_error_total += (actual - predicted) ** 2
    return squared_error_total / len(actual_values)


def main():
    print(extract_values(STUDENTS, "name"))
    actual_scores = extract_values(STUDENTS, "actual_score")
    predictions = make_predictions(STUDENTS, intercept=48, hourly_gain=7)
    rows = build_evaluation_rows(STUDENTS, predictions)
    worst = find_worst_prediction(rows)
    mse = mean_squared_error(actual_scores, predictions)

    print("Evaluation rows:")
    for row in rows:
        print(row)
    print("MSE:", round(mse, 2))
    print("Worst prediction:", worst)


if __name__ == "__main__":
    main()

