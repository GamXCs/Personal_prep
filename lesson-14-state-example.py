"""Lesson 14 example: explicit accumulator state and invariants."""

RESPONSE_TIMES_MS = [120, 95, 180, 105]


def update_state(state, value):
    """Return state after one validated response time."""
    if value < 0:
        raise ValueError("response time cannot be negative")
    state["count"] += 1
    state["total"] += value
    if state["maximum"] is None or value > state["maximum"]:
        state["maximum"] = value


def summarize(values):
    state = {"count": 0, "total": 0, "maximum": None}
    for value in values:
        update_state(state, value)
    if state["count"] == 0:
        raise ValueError("at least one response time is required")
    return {
        **state,
        "mean": state["total"] / state["count"],
    }


def main():
    report = summarize(RESPONSE_TIMES_MS)
    print(f"Count: {report['count']}")
    print(f"Mean: {report['mean']:.2f} ms")
    print(f"Maximum: {report['maximum']} ms")


if __name__ == "__main__":
    main()
