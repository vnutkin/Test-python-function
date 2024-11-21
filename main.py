def fun(n):
    a = n
    b = n ** 2
    c = n ** 3
    return a, b, c


y1, y2, y3 = fun(2)
print(y1, y2, y3)
c, b, a = fun(2)
print(a, b, c)
y1, y2, b = fun(2)
print(y1, y2, b)
b, y1, y2 = fun(2)
print(y1,y2,b)
