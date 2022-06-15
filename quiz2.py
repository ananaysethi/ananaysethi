import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
import scipy

# 1
x = sy.symbols('x')
firstder = sy.diff(sy.asin((x**3) * sy.sqrt(1 + (1/(x**3)))), x)
secondder = sy.diff(firstder, x)

# 2
x = sy.symbols('x')
result = sy.integrate((sy.sin(x))**4, x)

# 3
x = sy.symbols('x')
result = sy.integrate(sy.exp(-(x**2)), (x, -sy.oo, +sy.oo))

# 4
x = np.zeros((5,5))
x += 6
print(x.dtype)
print(type(x))

# 6
x = np.array(((1,1), (2,2)))
print(x.dtype)

# 7
x = np.linspace(0, 2*np.pi, 51)
y1 = np.sin(x)
y2 = np.tan(x)

plt.plot(x, y1, 'b-')
plt.plot(x, y2, 'r-')
plt.xlim(2, 4)
plt.ylim(-2, +2)
plt.title('Trigonometric Functions')
plt.show()

# 8
x = np.random.randint( 0,10,size=(10000,) )
plt.plot( x,'.' )
plt.show()
