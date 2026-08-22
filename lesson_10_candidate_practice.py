model_runs = [
    {"model": "linear", "validation_mse": 18.4},
    {"model": "tree", "validation_mse": 12.7},
    {"model": "knn", "validation_mse": 14.1},
]

def rerun_func(list_in):
    if not list_in:
        raise ValueError("List is empty")

    lowest_min = list_in[0]

    for model in list_in:
        if model['validation_mse'] < lowest_min['validation_mse']:
            lowest_min = model

    return lowest_min

if __name__ == "__main__":
    print(rerun_func(model_runs))
    


"""Write a function that returns the entire record with the smallest
`validation_mse`.

Requirements:

- reject an empty list with `ValueError`;
- do not use `min()`, `sorted()`, or `.sort()`;
- initialize the candidate from the first record;
- compare numeric fields but replace the candidate with the whole record;
- return a dictionary, not only the numeric loss;
- print the winning model and loss only in the program's main block.

For the supplied records, the returned candidate must be:

```python
{"model": "tree", "validation_mse": 12.7}
```"""