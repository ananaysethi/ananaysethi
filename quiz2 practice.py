import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
import scipy.special

x = np.zeros( ( 1,1,1 ) )
x += 6

print(x)
b = np.eye(3)
print(b)

c = np.array( [ 1,0,0,0,1,0,0,0,1 ] ).reshape( 3,3 )
print(c)

d = np.array( [ [ 1 ] + [ 0 ] * 2, [ 0,1,0 ], [ 0 ] * 2 + [ 1 ] ] )
print(d)

r = [ 2,2 ]
s = np.array( r )
x = s * 2
print(x.dtype)

x = sy.symbols('x')
result = sy.integrate(sy.log(x), x)
print(result)

x,t = sy.symbols( 'x,t' )
def dawson(x):
    result = sy.exp(-(x**2)) * sy.integrate(sy.exp(t**2), (t, 0, x))
    return float(result)

print(dawson(12))

x = sy.symbols('x')
result = sy.integrate(sy.log(x), (x, 0, 1)) 
print(result)

x = np.linspace(0, 10, 501)
y1 = np.cos(x)
y2 = np.arccos(x)
y3 = scipy.special.j0(x)
y4 = np.tanh(x)

plt.plot(x, y1, 'b--')
plt.plot(x, y2, 'b-')
plt.plot(x, y3, 'k-')
plt.plot(x, y4, 'g-')
plt.xlim(0, 10)
plt.ylim(-1.2, +1.2)
plt.title('Special Functions')

