"""Small NumPy example for Lesson 10; not the assignment solution."""

import numpy as np


def standardize(values):
    """Return population-standardized values for a nonconstant numeric array."""
    mean = values.mean()
    standard_deviation = values.std()
    if standard_deviation == 0:
        raise ValueError("cannot standardize a constant array")
    return (values - mean) / standard_deviation


def main():
    cities = np.array(["North", "East", "South", "West"])
    temperatures = np.array([72.0, 81.0, 77.0, 69.0])

    warm_mask = temperatures > temperatures.mean()
    standardized = standardize(temperatures)

    print("shape:", temperatures.shape)
    print("dtype:", temperatures.dtype)
    print("warm cities:", cities[warm_mask])
    print("warm temperatures:", temperatures[warm_mask])
    print("standardized:", np.round(standardized, 3))
    print("z mean:", round(float(standardized.mean()), 10))
    print("z population std:", round(float(standardized.std()), 10))


if __name__ == "__main__":
    main()
