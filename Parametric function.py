# Parametric Function

def f(t):
    if t > 1:
        t = 0
        return t
    elif t < -1:
        t = 0
        return t
    else:
        t = t
        return t

print(f(0.5))