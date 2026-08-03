"""Executable schema-dispatch example for Lesson 13."""

import math


PARSERS = {"hours": float, "attendance": int, "actual_score": int}


def parse_numeric_fields(raw_record):
    """Return converted numeric fields, adding field context to bad input."""
    parsed = {}
    for field, parser in PARSERS.items():
        try:
            parsed[field] = parser(raw_record[field])
        except KeyError as exc:
            raise ValueError(f"missing required field: {field}") from exc
        except ValueError as exc:
            raise ValueError(f"invalid {field}: {raw_record[field]!r}") from exc

    if not math.isfinite(parsed["hours"]) or parsed["hours"] < 0:
        raise ValueError("hours must be finite and nonnegative")
    return parsed


def main():
    raw = {"hours": "3.5", "attendance": "81", "actual_score": "70"}
    parsed = parse_numeric_fields(raw)
    prediction = 30 + 6 * parsed["hours"] + 0.25 * parsed["attendance"]
    print(parsed)
    print("prediction:", prediction)


if __name__ == "__main__":
    main()
