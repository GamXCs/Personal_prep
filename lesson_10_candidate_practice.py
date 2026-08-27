import csv


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
    
