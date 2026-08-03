import numpy as np
import csv

temperatures = np.array([
    72,
    74,
    71,
    75,
    69
])


print(temperatures.mean())

foo = sum(temperatures)
bar = foo / len(temperatures)

alice = np.array([64, 125, 20])
bob  = np.array([64, 180, 22])
sarah = np.array([64, 140, 21])

students = np.array([alice, bob, sarah])
print(students)
print(students.shape)
print(students.dtype)
print(students.ndim)
-
with open("exams.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)
