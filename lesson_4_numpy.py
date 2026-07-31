import numpy as np

scores = np.array([
    88,
    91,
    77,
    84,
    96,
    81,
    73
])

# print scores below 80 | greater than or equal to 90 | between 80 and 90 inclusively


print(scores[scores < 85])
print(scores[scores >= 90])
print(scores[(scores >= 80) & (scores <= 90)])