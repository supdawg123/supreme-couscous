from numpy import arange, pi, linspace

x1 = range(10)
print(list(x1))
x2 = arange(10)
print(x2)
x3 = arange(0, 10, 0.5)
print(x3)
x4 = arange(0, 2 * pi, 0.1)
print(x4)
x5 = linspace(0, 10)
print(len(x5))
print(x5)
x6 = linspace(0,10,51)
print(len(x6))
print(x6)