import numpy as np
import sys


def task1(array):
    diag = np.diag(array)
    diag = diag[diag != 0]
    return np.prod(diag)


def task2(x, y):
    a = np.setdiff1d(x, y)
    return a.size == 0


def task3(array):
    maximum = -sys.maxsize - 1
    prev = -sys.maxsize - 1
    for a in array:
        if prev == 0 and a > maximum:
            maximum = a
        prev = a
    return maximum


def task5(vector):
    return np.unique(vector, return_counts=True)

