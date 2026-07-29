"""Lesson 8 main assignment: build a small CSV-to-report data pipeline."""

import csv


REQUIRED_COLUMNS = {"name", "hours", "attendance", "actual_score"}


def load_students(csv_path):
    """Load and validate student records from csv_path.

    Return a list of dictionaries with these types:
        name: str
        hours: float
        attendance: float
        actual_score: float

    Raise ValueError if required columns are missing, a numeric conversion fails,
    or the file contains no data rows.
    """
    # TODO 1: Open the file with newline="" and use csv.DictReader.
    # TODO 2: Validate reader.fieldnames against REQUIRED_COLUMNS.
    # TODO 3: Convert numeric fields and append clean dictionaries.
    # TODO 4: Reject an empty data file.
    raise NotImplementedError


def add_predictions(records, intercept, hourly_gain, attendance_gain):
    """Return new records with prediction information added.

    Prediction rule:
        intercept + hourly_gain * hours + attendance_gain * attendance

    Each returned dictionary must contain all original fields plus:
        predicted_score
        error                 (actual_score - predicted_score)
        squared_error

    Do not mutate the input records.
    """
    # TODO: Build and return a new list of new dictionaries.
    raise NotImplementedError


def summarize(evaluated_records):
    """Return aggregate evaluation information.

    Return a dictionary containing:
        count
        mse
        mean_error
        within_five_count
        worst_student

    A prediction is "within five" when abs(error) <= 5.
    worst_student is the name attached to the largest squared_error.
    Raise ValueError for empty input.
    """
    # TODO: Use one loop to accumulate totals, count close predictions,
    # and track the worst record seen so far.
    raise NotImplementedError


def format_report(evaluated_records, summary):
    """Return a human-readable multiline report string.

    Include:
      - one detail line per student;
      - count, MSE, mean error, within-five count, and worst student;
      - numeric values rounded to two decimal places.
    """
    # TODO: Build lines in a list, then return "\\n".join(lines).
    raise NotImplementedError


def main():
    records = load_students("lesson-08-student-data.csv")
    evaluated = add_predictions(
        records,
        intercept=30,
        hourly_gain=6,
        attendance_gain=0.25,
    )
    summary = summarize(evaluated)
    report = format_report(evaluated, summary)
    print(report)


if __name__ == "__main__":
    main()
