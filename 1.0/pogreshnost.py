from student import *
from math import *
DOV = 0.95


def differentiate(f, n, v):
    # определение df/dx_n в точке, соответствующей значениям v
    # не умеет считать производную в нуле
    f0 = f(v) # f(v)
    dv = v[n] / 1000000
    v1 = []
    for i in range(len(v)):
        if i != n:
            v1.append(v[i])
        else:
            v1.append(v[i] + dv)
    f1 = f(v1) # f(v+dv)
    res = (f1 - f0) / dv
    return res


def average(data):
    # поиск среднего арифметического
    return sum(data)/len(data)


def dRandom(values, p):
    n = len(values)
    x_av = average(values)
    c = 0
    for x in values:
        c += (x - x_av) ** 2
    z = n * (n - 1)
    res = (c / z) ** 0.5 * ks(n, p)
    return res


def g(f, values):
    # f(90+-1, 30+- 3, ...)
    # values = ((90, 1), (30, 3), ...)
    args = [x[0] for x in values]
    diff = [x[1] for x in values]
    s = 0
    for i in range(len(values)):
        ds = diff[i] * differentiate(f, i, args)
        s += ds ** 2
    r_diff = s ** 0.5
    return (f(args), r_diff)


def dAbsolute(values, d_pr):
    d_r = dRandom(values, DOV)
    res = []
    for x in values:
        d = (d_r ** 2 + d_pr ** 2) ** 0.5
        res.append(x(x, d))
    return res


def Calculate(f, values, d_pr):
    # values = [[x11,x12,x13],[x21,x22,x23],[x31,x32,x33]]
    # d_pr = [dx1_pr, dx2_pr, dx3_pr]
    new_values = []
    for i in range(len(values)):
        new_values.append(dAbsolute(values[i], d_pr[i]))
    res = []
    for i in range(len(values[0])):
        args = []
        for j in range(len(values)):
            args.append(new_values[j][i])
        res.append(f(*args))
    return res



def f(args):
    return args[0] * args[0] * args[1] / args[2]
r = g(f, ((13.26,0.66),(50.10,3.51),(4.33,0.26)))
print(r)

