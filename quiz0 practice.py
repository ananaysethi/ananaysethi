# CHI-SQUARED PROBABILITY FUNCTION

from math import gamma, exp

x = 1
num = (x ** (-1 / 2)) * (exp(-x / 2))
denom = (2 ** (1 / 2)) * gamma(1 / 2)

if x > 0:
    pdf = num / denom
else:
    pdf = 0

print(pdf)


def pdf(x):
    num = (x ** (-1 / 2)) * (exp(-x / 2))
    denom = (2 ** (1 / 2)) * gamma(1 / 2)
    if x > 0:
        f = num / denom
    else:
        f = 0
    return f


print(pdf(1))
