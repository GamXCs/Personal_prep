"""A loop pattern example. This is intentionally not the assignment solution."""

temperatures_c = [0, 10, 20, 30]
temperatures_f = []

for value_c in temperatures_c:
    value_f = (value_c * 9 / 5) + 32
    temperatures_f.append(value_f)

print("Celsius:", temperatures_c)
print("Fahrenheit:", temperatures_f)

