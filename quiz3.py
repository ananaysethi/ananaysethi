# Cracking a lock

from itertools import product
'''
def crack_pin():
    # Assume the length as 4
    for l in [4,5,6]:
        for attempt in product('0123456789', repeat = 4):
            guess = ''.join(attempt)
            if check_pin(guess):
                return guess
'''
'''
from itertools import product
import numpy as np
def crack_lock():
    numbers = np.linspace(0, 49, 50)
    for attempt in product(numbers, repeat = 3):
        if check_lock(attempt):
            return attempt
'''
# Using Newton's Method
from scipy.optimize import newton
import numpy as np

def f(x):
    return (np.cos(x) + np.sin(x)**2 - x**4 + 2 * x**2 - x)
root = newton(f, x0 = 1.2)
print(root)

# Integral Calculation 
from scipy.integrate import quad

def f(x):
    return (1 / (np.sqrt(x) + x**(1/3)) )
integral = quad(f, 0, +1)
print(integral)

# Finding a zero
def f(x):
    return (np.sin(np.cos(np.pi*x + (1/10000))) + 2*x)
root = newton(f, x0 = -0.3)
print(root)

# Finding a minimum - Bei Function
import scipy.special
from scipy.optimize import minimize

def f(z):
    return scipy.special.bei(z)

result = minimize(f, x0 = 6.5)
print(result)

# Finding a minimum - Bessel Function

def h(x):
    return scipy.special.y0(x)
result = minimize(h, x0 = 4.5)
print(result)

# Finding a minimum - Bessel Function

def h(x):
    return scipy.special.j0(x)
result = minimize(h, x0 = 3)
print(result)

# Finding a maximum - Kelvin function

def f(z):
    return - (scipy.special.bei(z))
result = minimize(f, x0 = 3)
print(result)