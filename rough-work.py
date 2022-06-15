import sympy as sy

t = sy.symbols('t')
r_prime = sy.sqrt(4*t**2 + 9*t**4)
L = sy.integrate(r_prime, (t, 0, 1))
print(L)
