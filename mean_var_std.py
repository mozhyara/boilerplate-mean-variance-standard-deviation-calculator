import numpy as np

def calculate(list):
    if len(list) != 9:
        print("List must contain nine numbers.")
    else:
        calculations={}
        y = np.array(list).reshape(3,3)
        stats = ["mean", "variance", "standard division", "max", "min", "sum"]
        funs = [y.mean, y.var, y.std, y.max, y.min, y.sum]
        axes= [0 ,1, None]
        for stat, fun in zip(stats, funs):
            calculations[stat] = [fun(axis=ax).tolist() for ax in axes]
        return calculations
