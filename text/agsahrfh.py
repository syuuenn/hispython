def fn(a=[]):
    a.append(1)
    return a
b = fn([1, 2, 3])
print (b)
c = fn()
print (c)
d = fn()
print (c)
print(d)