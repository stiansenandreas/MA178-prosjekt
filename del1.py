import numpy as np


def f1(x):
    return 7*x**2-8*x+1


def df1(x):
    return 14*x-8


def f2(x):
    return np.sin(x)


def df2(x):
    return np.cos(x)


def f3(x):
    return (1-x)/(x+3)**2


def df3(x):
    return (x-5)/(x**3+9*x**2+27*x+27)


def f4(x):
    return np.sqrt(1+x**2)


def df4(x):
    return x/(np.sqrt(1+x**2))


def gx(x, f, dx):
    return (f(x+dx)-f(x))/dx


def ex(x, f, df, g, dx):    # Definerer E(x)=f'(x)-g(x)
    return np.abs(df(x)-g(x, f, dx))


fx = [f1, f2, f3, f4]
dfx = [df1, df2, df3, df4]
x0 = [1, np.pi/4, 1, 5]


for fx, x0, dfx, i in zip(fx, x0, dfx, range(len(fx))):
    dx = 0.1
    print("\nTilnærming av f{}'(x0) med g(x0): {:.5f}".format(i+1, gx(x0, fx, dx)))
    print("Eksakt verdi av f{}'(x0): {:.5f}".format(i+1, dfx(x0)))
    print("Feilen E{}(x0): {:.5f}".format(i+1, ex(x0, fx, dfx, gx, dx)))
    dx = 1
    while ex(x0, fx, dfx, gx, dx) > 0.001:
        dx /= 1.001
    print("Største dx som gir E(x0)<=0.001: {:.2g}".format(dx))
