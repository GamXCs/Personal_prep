import numpy 
import csv

def load_data(filename):

    # create empty lists to store n
    names = []
    scores = []

    with open(filename, newline="") as f:
        reader = csv.DictReader(f)

        # check if header is missing
        if reader.fieldnames is None:
            raise ValueError("Header is missing in csv")

        # check if columns are missing
        if "Name" not in reader.fieldnames or "Exam1" not in reader.fieldnames or "Exam2" not in reader.fieldnames:
            raise ValueError("Columns are missing in csv file")

        # start on second line to read data from csv file, skip line 1
        for physical_row, row in enumerate(reader, start=2):
            name = row["Name"].strip()

            # reject blank names
            if name == "":
                raise ValueError(f"Error: Name is missing in row {physical_row}")

            # convert scores to float values
            try:
                exam1 = float(row["Exam1"])
                exam2 = float(row["Exam2"])
            except ValueError:
                raise ValueError(f"Exam value in row {physical_row} must be a float")

            # append names and scores to the empty lists
            names.append(name)
            scores.append([exam1,exam2])

            # reject scores outside of 0 - 100
            if exam1 < 0 or exam1 > 100 or exam2 < 0 or exam2 > 100:
                raise ValueError(f"Error in row {physical_row}. Values must be between 0-100")

        # check for empty data rows
        if len(scores) == 0:
            raise ValueError("CSV is empty")

    return names, scores










if __name__ == "__main__":
    filename = "exams.csv"        
    print(load_data(filename=filename))