"""Supplied acceptance tests for Lesson 8. You write implementation, not tests."""

import csv

import pytest

from lesson_08_student_pipeline_starter import (
    add_predictions,
    format_report,
    load_students,
    summarize,
)


def write_csv(path, rows, fieldnames=None):
    columns = fieldnames or ["name", "hours", "attendance", "actual_score"]
    with path.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def test_load_students_converts_numeric_fields(tmp_path):
    path = tmp_path / "students.csv"
    write_csv(
        path,
        [{"name": "A", "hours": "2.5", "attendance": "80", "actual_score": "70"}],
    )

    result = load_students(path)

    assert result == [
        {"name": "A", "hours": 2.5, "attendance": 80.0, "actual_score": 70.0}
    ]


def test_load_students_rejects_missing_column(tmp_path):
    path = tmp_path / "students.csv"
    write_csv(
        path,
        [{"name": "A", "hours": "2", "actual_score": "70"}],
        fieldnames=["name", "hours", "actual_score"],
    )

    with pytest.raises(ValueError):
        load_students(path)


def test_load_students_rejects_empty_data_file(tmp_path):
    path = tmp_path / "students.csv"
    write_csv(path, [])

    with pytest.raises(ValueError):
        load_students(path)


def test_add_predictions_calculates_fields_without_mutating_input():
    records = [
        {"name": "A", "hours": 2.0, "attendance": 80.0, "actual_score": 70.0}
    ]

    result = add_predictions(records, intercept=30, hourly_gain=5, attendance_gain=0.25)

    assert records == [
        {"name": "A", "hours": 2.0, "attendance": 80.0, "actual_score": 70.0}
    ]
    assert result[0]["predicted_score"] == 60.0
    assert result[0]["error"] == 10.0
    assert result[0]["squared_error"] == 100.0


def test_summarize_computes_all_fields():
    rows = [
        {"name": "A", "error": 2.0, "squared_error": 4.0},
        {"name": "B", "error": -6.0, "squared_error": 36.0},
    ]

    result = summarize(rows)

    assert result == {
        "count": 2,
        "mse": 20.0,
        "mean_error": -2.0,
        "within_five_count": 1,
        "worst_student": "B",
    }


def test_summarize_rejects_empty_input():
    with pytest.raises(ValueError):
        summarize([])


def test_format_report_contains_details_and_summary():
    rows = [
        {
            "name": "A",
            "actual_score": 70.0,
            "predicted_score": 68.0,
            "error": 2.0,
            "squared_error": 4.0,
        }
    ]
    summary = {
        "count": 1,
        "mse": 4.0,
        "mean_error": 2.0,
        "within_five_count": 1,
        "worst_student": "A",
    }

    report = format_report(rows, summary)

    assert "A" in report
    assert "70.00" in report
    assert "68.00" in report
    assert "MSE" in report
    assert "4.00" in report
    assert "Worst student" in report
