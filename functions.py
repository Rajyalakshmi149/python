'''def cal():
    a=int(input())
    b=int(input())
    print(a+b)
cal()'''
'''def calculate():
    a=int(input())
    b=int(input())
    print("the sum is:",a+b)
    print("the diff is:",a-b)
    print("the mul is:",a*b)
calculate()'''
#recursion
'''def add():
    a=int(input())
    b=int(input())
    print(a+b)
    add()
add()'''
'''def fullname():
    fname=input()
    lname=input()
    print((fname+" "+lname).title())
    fullname()
fullname()'''
#return
'''def cal():
    a=int(input())
    b=int(input())
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(cal())'''
#task
'''def cal():
    a=int(input())
    b=int(input())
    option=int(input('choose the option:
                                1.add
                                2.sub
                                3.mul'))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:
        print(a*b)
    cal()
cal()'''
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input())
    b=int(input())
    option=int(input('choose option :
                           1.add
                           2.sub
                           3.mul'))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()'''


#default arguments
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery('suger',100)'''
'''def grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''
'''def grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dhal")'''
'''def grocery(item='ghee',price):
    #non-default arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(600)'''
'''def bekary(cake="strwaberry",price=500,qty='1kg'):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s"%qty)
bekary()'''
'''def bekary(cake,price,qty):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s"%qty)
bekary("strawberry",600,"2kg")'''
#*arguments-> * is used to unpack the elements
'''a=[2,23,4,45],(3,4,5,6),{3,4,5,6,7}
print(a)
print(*a)'''
'''b={"year":2026,"month":1}
print(b)
print(*b)'''#keys only will return
'''c="python"
print(c)
print(*c)'''
'''a,b,c=1,2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''#raises error
'''a,b,c=1,2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''#a holds 1,2,3,4,5,6,7,8 and b holds 9 and c holds 10
'''a,b,c="codegnan"
print(a)
print(*b)
print(c)'''#a holds 'c' and b holds 'odegna' and c holds 'n'
#variable length  arguments
'''def check(*a):
    print(a)
    print(type(a))
check()'''
'''b=[2,3,4,5,6]
check(*b)
c=(2,3,4,5,6)
check(*c)
d={2,4,5,67,8,9}
check(*d)
e={"year":2026,"month":1}
check(*e)'''
'''def check1(*a):
    d=1#creating variable
    print(a)
    print(type(a))
    for i in a:
        if type(i)==int or type(i)==float:#if type(i) in (int,float)
            d=d+i
            print(d)
check1(4,5,2,3.4,6.9,"python")'''
#kwargs(**)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"idnos":[10,20,30],"names":["ammulu","rajyalakshmi","rajesh"],"status":["p","a","p"]}
details(**d)
def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)'''
#both * & ** usage
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,"python",3+6j,True,False)
final(*data)
details={"idnos":[10,20,30],"names":["ammulu","rajyalakshmi","rajesh"],"status":["p","a","p"]}
final(**details)
final(*data,**details)'''
#bmi(body mass index)
'''def BMI():
    weight=float(input())
    hight=float(input())
    bmi=weight/(hight/100)**2
    if bmi<=18.5:
        print("under weight")
    elif bmi>18.5 and bmi<=24.9:
        print("healthy weight")
    elif bmi>=25.0 and bmi<=29.9:
        print("over weight")
    elif bmi>30:
        print("obesity")
    BMI()    
BMI()'''
#max(),min(),sum()
'''print(max(2,3,4,5,6,7,8,9))'''
'''print(min(2,3,43,56,78,1.0))'''
'''a=2,45,67,78,90,60
print(sum(a))'''
#multiplication table
'''n=int(input())
for i in range(1,21):
    n*i
    print(f"{n}*{i}=",n*i) or print(a,"*",i,"=",a*i)'''
#local and global variables: variables inside and outside the function are called local and global variables.
''' global: a vaiable define above the function and
is accessble to entire global space is called global variable.
local: a variable is inside the function is called local variable.'''
#first case of global variables
'''a=2
def check1():
    print("a value is",a)
check1()
print("out side value is",a)'''
#second case of global variables
'''a=3
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("out side value is",a)'''
#third case
'''a=4
def check3():
    a=3
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12#local variable
    b=b+a
    print("b value is",b)
check3()
print("value of a is",a)
print("value of b is",b)'''#error local.v can't access out side value

'''a=4
b=7
def check3():
    a=3
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12#local variable
    b=b+a
    print("b value is",b)
check3()
print("value of a is",a)
print("value of b is",b)'''#7 will be printed
#usage of global keyword
'''when user wants to access the global variable inside the function directly,
and carrying forward the updated value even outside the function
then we need to use global keyword'''
'''a=4
def final():
    global a
    print("inside value is",a)
    a=15
    print("updated value is",a)
    b=20
    b=b+a
    print("b value is",b)
final()
print("value of a is",a)
print("value of b is",b)'''#error
'''a=4
def final():
    global a
    print("inside value is",a)
    a=15
    print("updated value is",a)
    global b
    b=20
    b=b+a
    print("b value is",b)
final()
print("value of a is",a)
print("value of b is",b)'''#b value will be 35
'''b=[10,20,30,40,50]
b.insert(5,a)
print(b)'''
#generators
'''no tuple comprehension in above cases(list comprehensions)
we remove those braces and keep paranthesis then uotcome is generators'''
'''a=[i for i in range(15)]
print(a)
a=(i**2 for i in range(16))
print(a)#<generator expression>
print(*a)
print(type(a))#generator
a=(i**2 for i in range(16))
print(a)
print(list(a))
print(set(a))
print(dict(a))'''#error

'''generator is also a function which can be used as an iterator(loop)
by producing group of values ,where 'yield' keyword is used'''
#return
'''return will terminate the function .'''
'''a,b=[int(x) for x in input().split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(*check(a,b))#error
print(check(a,b))'''
'''a,b=[int(x) for x in input().split(",")]
def check(a,b):
    while a<b:
        a=a+1
    return a
print(check(a,b))'''
'''def mygen():
    return "python"
    return "java"
    return "html"
print(mygen())'''#only python will be printed
'''def mygen():
    return "python","java","c++"
print(mygen())'''#[python,java,c++] will be the output
'''print(*mygen())'''#python java c++ will be the output
#*is used to unpacking data
#yield
'''yield can pass the function and gone with every successive iteration.'''
'''a,b=[i for i in int(input("enter the value").split(","))]
def check(a,b):
    while a<b:
        yield a
        a=a-1
        yield a
check()'''#error
'''a,b=[int(i) for i in  (input("enter the value").split(","))]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
check()#type error
print(list(check(a,b)))#
print(check(a,b))#generator expression
print(*check(a,b))'''
'''a,b=[int(i) for i in  (input("enter the value").split(","))]
def check(a,b):
    while a<b:
        yield a
        a=a+1
print(*check(a,b))'''
'''a,b=[int(i) for i in  (input("enter the value").split(","))]
def check(a,b):
    while a<b:
        a=a+1
        yield a
print(*check(a,b))'''
'''def mygen():
    yield "A"
    yield "B"
    yield "C"
print(*mygen())'''
#next
'''d=mygen()
print(next(d))
print(next(d))
print(next(d))'''
'''def mygen():
    yield "A"
    yield "B"
    yield "C"
    print(next(mygen()))
print(*mygen())'''







    


        




