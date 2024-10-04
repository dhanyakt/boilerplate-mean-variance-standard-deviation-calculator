import sys
import numpy as np
import itertools


def convert_list_to_matrix(alist):
    length_of_list = len(alist)
    if length_of_list != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        return np.array(alist).reshape(3, 3)


# Calculating row sum and col sum and converting to a list from numpy array
def calculate_sum(result_matrix):
    col_sum = np.sum(result_matrix, axis=0, dtype=np.float64).tolist()
    row_sum = np.sum(result_matrix, axis=1, dtype=np.float64).tolist()
    total_sum = np.sum(result_matrix).tolist()
    return (col_sum, row_sum, total_sum)


# Calculating row_max,col_max,max and converting to a list from a numpy array
def calculate_max(result_matrix):
    col_max = np.max(result_matrix, axis=0).tolist()
    row_max = np.max(result_matrix, axis=1).tolist()
    maxi = np.max(result_matrix).tolist()
    return (col_max, row_max, maxi)


def calculate_min(result_matrix):
    col_min = np.min(result_matrix, axis=0).tolist()
    row_min = np.min(result_matrix, axis=1).tolist()
    mini = np.min(result_matrix).tolist()
    return (col_min, row_min, mini)


def calculate_mean(result_matrix):
    col_mean = np.mean(result_matrix, axis=0, dtype=np.float64).tolist()
    row_mean = np.mean(result_matrix, axis=1, dtype=np.float64).tolist()
    mean_of_matrix = np.mean(result_matrix).tolist()
    return (col_mean, row_mean, mean_of_matrix)


def calculate_std(result_matrix):
    col_std = np.std(result_matrix, axis=0, dtype=np.float64).tolist()
    row_std = np.std(result_matrix, axis=1, dtype=np.float64).tolist()
    standard_deviation = np.std(result_matrix, dtype=np.float64).tolist()
    return (col_std, row_std, standard_deviation)


def calculate_variance(result_matrix):
    col_var = np.var(result_matrix, axis=0, dtype=np.float64).tolist()
    row_var = np.var(result_matrix, axis=1, dtype=np.float64).tolist()
    variance = np.var(result_matrix).tolist()
    return (col_var, row_var, variance)

# Converting tuple to list
def convert_tuple_to_list(my_tuple):
    return [list(np.array(i).tolist()) if isinstance(i, tuple) else i for i in my_tuple]



def calculate(list):
    calculations = {}

    result_matrix = convert_list_to_matrix(list)

    result_mean = calculate_mean(result_matrix)
    result_variance = calculate_variance(result_matrix)
    result_std = calculate_std(result_matrix)
    result_max = calculate_max(result_matrix)
    result_min = calculate_min(result_matrix)
    result_sum = calculate_sum(result_matrix)

    # Updating the dict
    calculations.update({'mean': convert_tuple_to_list(result_mean)})
    calculations.update({'variance': convert_tuple_to_list(result_variance)})
    calculations.update({'standard deviation': convert_tuple_to_list(result_std)})
    calculations.update({'max': convert_tuple_to_list(result_max)})
    calculations.update({'min': convert_tuple_to_list(result_min)})
    calculations.update({'sum': convert_tuple_to_list(result_sum)})

    #print(calculations)
    return calculations