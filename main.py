import numpy as np


def f(x):
    return 3 * x ** 2 + 4 * x - 4


def df(x):
    return 6 * x + 4


def newton_raphson(x0):
    roots = np.copy(x0)
    steps = np.zeros(len(x0))
    e = 10 ** -12
    n = 100
    success = 0
    for i in range(len(roots)):
        for j in range(0, n):
            if df(roots[i]) == 0:
                print('Undefined')
                break

            x1 = roots[i] - f(roots[i]) / df(roots[i])
            roots[i] = x1

            if j > n:
                break

            if abs(f(x1)) < e:
                success = 1
                steps[i] = j
                break
    return roots, steps


x0_values = np.linspace(-1, 1, 20)
root_values, step_values = newton_raphson(x0_values)

for i in range(len(x0_values)):
    print('x0: {:0.6f} - root x = {:0.6f} found in {} steps'.format(x0_values[i], root_values[i], step_values[i]))
