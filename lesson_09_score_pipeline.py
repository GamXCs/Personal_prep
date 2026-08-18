import csv 

"""create function to load the file, check for correct col names
    check if header is empty
    convert scores to int
    return dict
"""

def load_scores(filename):
    records = []

    with open(filename, newline="") as file:
        reader = csv.DictReader(file)

        # check for columns
        # using DictReader, header is stored in fieldnames
        if reader.fieldnames is None:
            raise ValueError("CSV has no header")

        # require the cols "Name" and "Score"
        if "Name" not in reader.fieldnames or "Score" not in reader.fieldnames:
            raise ValueError("CSV must contain Name and Score columns")

        # convert every score into an int
        for row in reader:
            name = row['Name'].strip()
            score = int(row['Score'])

            # check for blank name
            if name == "":
                raise ValueError("Name cannot be blank")
    
            records.append({"Name":name, "Score": score})

        if len(records) == 0:
            raise ValueError("CSV file has no data")
    return records

"""Produce report"""
def report(records):
    valid_students = len(records)
    total = 0
    highest_student_score = records[0]

    # get total and find name/score of highest scoring student
    for student in records:
        score = student["Score"]
        if score > highest_student_score["Score"]:
            highest_student_score = student

        total += score # add scores to calc mean

    highest_score_name = highest_student_score["Name"]
    highest_score = highest_student_score["Score"]
    mean_score = total / valid_students

    # Get a count of student scores by range
    students_90_to_100 = 0
    students_80_to_89 = 0
    students_70_to_79 = 0
    students_below_70 = 0

    # empty list to hold students above mean names
    students_above_mean = []

    for student in records:
        name = student["Name"]
        score = student["Score"]
        if score >= 90 and score <= 100:
            students_90_to_100 += 1
        elif score >= 80 and score < 90:
            students_80_to_89 += 1
        elif score >= 70 and score < 80:
            students_70_to_79 += 1
        elif score < 70:
            students_below_70 += 1

   
        # get names of students scoring above mean in input order
        if score > mean_score:
            students_above_mean.append(name)
    print(students_above_mean)




if __name__ == "__main__":
    # print(load_scores("scores.csv"))
    # print(load_scores("empty_test_file.csv"))
    # print(load_scores("emp_test2.csv"))
    test_records = (load_scores("scores.csv"))
    print(report(test_records))