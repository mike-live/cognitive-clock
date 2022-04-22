from tqdm import tqdm
import pandas as pd
from pathlib2 import Path
import os
import numpy as np

def get_describe_names(name, names = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']):
    names = list(map(lambda s: name + '_' + s, names))
    return names

def gen_names_274():
    names = []
    names.extend(get_describe_names('T274_MR')[1:])
    names.extend(get_describe_names('T274_SMR')[1:])
    names.extend(['T274_ERR_1_mean', 'T274_ERR_2_mean', 'T274_ERR_3_mean'])
    return names

def gen_274(test):
    if len(test) == 0:
        return np.zeros((len(gen_names_274()), ))
    data = [test.describe()["MR"].values[1:],
            test.describe()["SMR"].values[1:],
            np.array([test["ERR_1"].mean()]),
            np.array([test["ERR_2"].mean()]),
            np.array([test["ERR_3"].mean()])
           ]
    data = np.concatenate(data)
    assert(len(gen_names_274()) == len(data))
    return data

def gen_names_278():
    names = []
    names.extend(get_describe_names('T278_MR')[1:])
    names.extend(get_describe_names('T278_SMR')[1:])
    names.extend(['T278_ERR_1_mean', 'T278_ERR_2_mean', 'T278_ERR_3_mean'])
    return names

def gen_278(test):
    if len(test) == 0:
        return np.zeros((len(gen_names_278()), ))
    data = [test.describe()["MR"].values[1:],
            test.describe()["SMR"].values[1:],
            np.array([test["ERR_1"].mean()]),
            np.array([test["ERR_2"].mean()]),
            np.array([test["ERR_3"].mean()])
           ]
    data = np.concatenate(data)
    assert(len(gen_names_278()) == len(data))
    return data

def gen_names_258():
    names = []
    names.extend(get_describe_names('T258_dH+')[1:])
    names.extend(get_describe_names('T258_dH-')[1:])
    names.extend(get_describe_names('T258_t+')[1:])
    names.extend(get_describe_names('T258_t-')[1:])
    names.extend(['T258_ERR_mean', 'T258_ERR_LIM_mean'])
    return names

def gen_258(test):
    if len(test) == 0:
        return np.zeros((len(gen_names_258()), ))
    data = [test.describe()["dH+"].values[1:],
            test.describe()["dH-"].values[1:],
            test.describe()["t+"].values[1:],
            test.describe()["t-"].values[1:],
            np.array([test["ERR"].mean()]),
            np.array([test["ERR_LIM"].mean()])
           ]
    data = np.concatenate(data)
    assert(len(gen_names_258()) == len(data))
    return data
