"""Lesson 9 example: separate aggregation from presentation."""

INVENTORY = [
    {"item": "notebook", "units": 12},
    {"item": "marker", "units": 7},
    {"item": "folder", "units": 18},
]


def summarize_inventory(records):
    if not records:
        raise ValueError("Inventory cannot be empty")

    total_units = 0
    largest = records[0]

    for record in records:
        units = record["units"]
        total_units += units
        if units > largest["units"]:
            largest = record

    return {
        "count": len(records),
        "total_units": total_units,
        "mean_units": total_units / len(records),
        "largest_item": largest["item"],
    }


def format_summary(summary):
    return (
        f"Records: {summary['count']}\n"
        f"Total units: {summary['total_units']}\n"
        f"Mean units: {summary['mean_units']:.2f}\n"
        f"Largest item: {summary['largest_item']}"
    )


def main():
    summary = summarize_inventory(INVENTORY)
    print(format_summary(summary))


if __name__ == "__main__":
    main()
