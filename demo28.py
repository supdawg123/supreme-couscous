x1 = ['a','b','c']
x2 = ('a','b','c')
print(type(x1), type(x2))
x1.append('d')
x1= tuple(x1)
x2= list(x2)
print(type(x1), type(x2))
x2.append('d')
print(type(x1), x1)
print(type(x2), x2)