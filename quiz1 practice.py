d = { "T":2,"U":1,"C":4,"K":1 }
for c in "FRIAR":
    try:
        print( d[ c ] + 3 )
    except KeyError:
        pass
print(d)


# Calculating the soft maximum

from math import exp, log

def smax(x, y):
    return log(exp(x) + exp(y))

print(smax(3,2))

# Using a dictionary as an accumulator

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

text0 = "As kingfishers catch fire, dragonflies draw flame"

def lettercount( text ):
    result = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
              'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,
              'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
              'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0,
              'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0,
              'Z': 0}
    for letter in text.replace(' ','').replace(',', '').upper():
        try:
            result[letter] += 1
        except:
            result[letter] = 1
    return result
    
    # Add each letter to the dictionary as a key with a count of zero.

    # Count the number of times each letter occurs in the upper-case text
    # and add it to the dictionary as the value for that key.
print(lettercount(text0))

text1 = "As tumbled over rim in roundy wells"
print(lettercount(text1))

# Another way = 
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def lettercount(text):
    result = {}
    text = text.upper()

    for char in alphabet:
        count = text.count(char)
        result[char] = count
    return result

print(lettercount(text0))
print(lettercount(text1))

# Mathematical Sequence

# f(n) = n/3 (even)
# f(n) = 5n + 1 (odd)
# To call f(f(n))

def sequence(n):
    result = []
    result = result + [n]       # Makes a list of n
    while n != 1:
        if n%2 == 0:
            n = n//3
        else:
            n = 5*n + 1
        result = result + [n]
    return result
print(sequence(15))

# Cross Product

A = [ 1,-2,3 ]
B = [ 3,0,-1 ]

def cross_prod(a,b):
    c = []
    c.append( a[ 1 ]*b[ 2 ] - a[ 2 ]*b[ 1 ] )
    c.append( a[ 2 ]*b[ 0 ] - a[ 0 ]*b[ 2 ] )
    c.append( a[ 0 ]*b[ 1 ] - a[ 1 ]*b[ 0 ] )
    return c

print(cross_prod(A, B))


# Reflection

# Summation Series Calculator
k = 15
sum1 = 0
for i in range(1,k+1):
    sum1 = sum1 + (((-1)**(i - 1)) / (2**i))
print(sum1)

s = 'Example Text'
l = ''
for c in s:
    if c in 'aeiou':
        l +=c
print(l)
print(s)

# Hailstone Sequence

def hailstone(n):
    seq = []
    seq = seq + [n]
    while n!=1:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        seq = seq + [n]
    return seq
print(hailstone(15))
