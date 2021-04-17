import random
import numpy as np
import scipy.linalg as la


def approximation_polynomial(x, y, rate=5, points=None, dist=1):
    w, r = create_linear_equations(x, y, rate, points, dist)
    solve = la.solve(w, r)
    result = np.zeros(len(x), dtype=float)
    for i in range(len(x)):
        result[i] = f_power_n(x[i], solve)
    return result


def create_linear_equations(x, y, rate, points, dist=1):
    n = rate + 1
    a = np.zeros((n, n), dtype=float)
    b = np.zeros(n, dtype=float)
    length = len(x)
    part = length // n
    if points is None:
        if dist == 1:
            xval, yval = find_n_points_rand(x, y, n)
        else:
            xval, yval = find_n_points_linear(x, y, n)
        for i in range(n):
            for j in range(n):
                a[i][j] = xval[i] ** j
        b[i] = yval[i]
    else:
        for i in range(0, n):
            for j in range(0, n):
                a[i][j] = points[i] ** j
            b[i] = y[i]
    return a, b


def find_n_points_rand(x, y, n):
    length = len(x)
    part = length // n
    xval = np.zeros(n, dtype=float)
    yval = np.zeros(n, dtype=float)
    for i in range(n):
        shift = random.randint(0, part)
        part_shift = random.randint(0, n - 1)
        index = part_shift * part + shift
        xval[i] = x[index]
        yval[i] = y[index]
    return xval, yval


def find_n_points_linear(x, y, n):
    length = len(x)
    min_x = np.amin(x)
    max_x = np.amax(x)
    total = n
    i = 0
    borders = np.zeros(n, dtype=float)
    xval = np.zeros(n, dtype=float)
    yval = np.zeros(n, dtype=float)
    # borders[0] = min_x + (max_x - min_x) / (n * 10)
    borders[0] = min_x
    total -= 1
    borders[1] = max_x - (max_x - min_x) / (n * 10)
    total -= 1
    if total > 0:
        step = (max_x - min_x) / (total + 1)
        for i in range(total):
            borders[i + 2] = min_x + step * (i + 1)
    for i in range(n):
        min_delta = max_x
        delta = 0.
        min_index = 0
        for j in range(length):
            delta = abs(x[j] - borders[i])
            if delta < min_delta:
                min_delta = delta
                min_index = j
        xval[i] = x[min_index]
        yval[i] = y[min_index]
    return xval, yval


def f_power_n(x, w):
    f = 0.
    n = 0
    for weight in w:
        if n == 0:
            f += weight
        else:
            f += weight * (x ** n)
        n += 1
    return f
