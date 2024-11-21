# Test-python-function
 How Python's functions return list of results?
They say, that function returns multiple results as a tuple.
Lets test it:

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

Output:
2 4 8 16
16 8 4 2
2 8 16 4
4 8 2 16
Facts:
1) If the names of all the variables in the function call differ from the names
 of the variables in the return statement, the result list can be treated 
as a tuple.

2) If the names of all the variables in the function call match the names
of the variables in the return statement, the result list can be treated
 as a dictionary.

3) If the name of the first variable in the function call does not match
any of the names in the return statement, the tuple rule applies up to 
the first variable whose name matches one of the names in the return statement.
For this variable and all subsequent similar variables, the dictionary rule
will be used. However, if a variable name that differs from the names
in the return statement is encountered again, the tuple rule will apply
to that variable and all similar variables.

4) This is similar to point 3), except that the name of the first variable 
in the function call matches one of the names in the return statement. 
The dictionary rule is used. Then, if a variable name that differs 
from the names in the return statement is encountered, the tuple rule 
will apply to that variable and all similar variables. 

From points 3) and 4), it can be concluded that the transition from
the tuple rule to the dictionary rule, or vice versa, occurs no more than once 
while processing the list of variables in the function call.

Overall conclusion: It may seem that the variables used in the function body
are not accessible at the point of the function call, but using variables 
with the same name can lead to hard-to-detect errors.

1)если имена всех переменных в вызове функции отличаются от имен переменных в операторе  return, то список результатов можно рассматривать как 
tuple.
2)если имена всех переменных в вызове функции совпадают с именами переменных в операторе  return, то список результатов можно рассматривать как
dictionary
3)имя первой переменной в вызове функции не совпадает ни с одним из имен в операторе return, то используется правило для tuple до первой переменной,
имя которой совпадает с одним из имен в операторе return. Для нее и всех последующих аналогичных переменных будет использовано правило для dictionary.
 Однако, если снова встретится имя переменной, отличное от имен переменных из оператора return, то для нее и всех аналогичных переменных 
будет использоваться правило для tuple. 
4)Аналогичен 3), только имя первой переменной в вызове функции совпадает с одним из имен в операторе return. Используется правило для dictionary.
Затем встречается имя переменной,  отличное от имен переменных из оператора return, и для нее и всех любых переменных 
будет использоваться правило для tuple. 
Из 3) и4) можно сделать такой вывод: изменение правила с tuple на  dictionary или наоборот производится не более одного раза при обработке списка
 переменных в вызове функции.
Общий вывод: казалось бы, переменные, используемые в теле функции не доступны в точке вызова функции, но использование одноименных переменных может 
привести трудно определяемым ошибкам.