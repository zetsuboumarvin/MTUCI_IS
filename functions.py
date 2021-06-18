import sys


def task1(array):
    result = 1.0
    for i in range(len(array[0])):
        if array[i][i] != 0.0:
            result *= array[i][i]
    return result


def task2(x, y):
    x = x.tolist()
    y = y.tolist()
    for a in x:
        if a in y:
            y.remove(a)
        else:
            return False
    return len(y) == 0


def task3(array):
    maximum = -sys.maxsize - 1
    for i in range(len(array)):
        if i > 0 and array[i - 1] == 0 and array[i] > maximum:
            maximum = array[i]
    return maximum


def task5(vector):
    numbers = []
    repeats = []
    numbers.append(vector[0])
    repeats.append(1)
    for i in range(1, len(vector)):
        x = vector[i]
        if numbers[-1] == x:
            repeats[-1] += 1
        else:
            numbers.append(x)
            repeats.append(1)
    return numbers, repeats

