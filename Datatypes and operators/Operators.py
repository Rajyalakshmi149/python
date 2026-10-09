Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arthematic operators
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a/b)
0.5
print(a**b)
16
print(a//b)
0
#assignment operators
a=6
b=7
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
13
print(a)
13
a-=b
a
6
a-=1
a
5
a*=2
a
10
a/=2
a
5.0
a//=2
a
2.0
a**=6
a
64.0
a%=4
a
0.0
#comparision operators
a=6
b=9
a<b
True
a>b
False
b<a
False
b>a
True
a!=b
True
a==b
False
a<=b
True
a>=b
False
b<=a
False
b>=a
True
b!=a
True
a=9
b=9
a==b
True
#logical operators
a=6
b=8
a<b and b>a
True
a>b and b<a
False
a<=b and b>=a
True
a<b or b>a
True
a>b or b<a
False
a!=b or a==b
True
a>=b or a<=b
True
not True
False
not False
True
#identify operators
a=69
if type(a) is int:
    print("it is int")

    
it is int
if type(a) is float:
    print("float")

    
if type(a) is not float:
    print("it is not float")

    
it is not float
>>> if type(a) is str:
...     print("string")
... 
...     
>>> a="python"
>>> if type(a) is str:
...     print("it is string")
... 
...     
it is string
>>> if type(a) is not complex:
...     print("it is not complex")
... 
...     
it is not complex
>>> a=3+6j
>>> if type(a) is complex:
...     print("it is complex")
... 
...     
it is complex
>>> if type(a) is not str:
...     print("it is not string")
... 
...     
it is not string
>>> #membership operators
>>> a=4,6,7,8,9,10
>>> if 6 in a
SyntaxError: expected ':'
>>> if 6 in a:
...     print("true")
... 
...     
true
>>> if 6 not in a:
...     print("false")
... 
...     
>>> 
>>> 
>>> if 69 not in a:
...     print(69)
... 
...     
69
#bitwise operators
`bin(10)
a=



a=4
bin(4)
#bitwise operators
a=8
a>>2
print(a)
