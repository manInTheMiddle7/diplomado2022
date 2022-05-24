from math import sin, sqrt

a = 0
b = 1.9724
c = -1
d = 2

def fn(x):
    return 2 * (sin(sqrt(x)) - x)

m = (a + b) / 2
r2 = fn(m) * (b - a)

print('Metodo del punto medio R=', r2)

def fn1(y):
    return (pow(7, -y)) + 3

n = (c +d) / 2
r4 = ((d - c) / 6) * (fn1(c) + 4*fn1(n) + fn1(d))

print('Metodo de Simpson R=', r4)
