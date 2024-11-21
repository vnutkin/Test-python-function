def fun(n):
    a = n
    b = n ** 2
    c = n ** 3
    d = n ** 4
    return a, b, c, d


y1, y2, y3, y4 = fun(2) #1
print(y1, y2, y3, y4)
d, c, b, a = fun(2)
print(a, b, c, d)   #2
y1, d, y2, c = fun(2)
print(y1, y2, c, d)  #3
b, y1, y2, c = fun(2)
print(y1, y2, b, c)  #4
