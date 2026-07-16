import numpy as np

def calculate(values):
    if len(values) != 9:
        raise ValueError("List must contain nine numbers.")

    calculations = {}
    y = np.array(values).reshape(3, 3)

    stats = ["mean", "variance", "standard deviation", "max", "min", "sum"]
    functions = [y.mean, y.var, y.std, y.max, y.min, y.sum]
    axes = [0, 1, None]

    for stat, function in zip(stats, functions):
        calculations[stat] = [
            function(axis=axis).tolist()
            for axis in axes
        ]

    return calculations
