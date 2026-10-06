#even or odd
'''n=int(input("enter a number:"))
if n%2==0:
    print("given number is even")
else:
    print("given number is odd")'''
#positive or negative
'''n=int(input("enter a number:"))
if n>0:
    print("given number is positive")
elif n<0:
    print("given number is negative")
else:
    print("given number is zero")'''
#largest of 3 numbers
'''n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
n3=int(input("enter a number:"))
if n1>n2 and n1>n3:
    print("n1 is largest")
elif n2>n1 and n2>n3:
    print("n2 is largest")
else:
    print("n3 is largest")'''
#sum of 1 to n
'''n=int(input("enter a number:"))
total=0
for i in range(n+1):
    total+=i
print("total:",total)'''
#multiplication
'''n=int(input("enter a number:"))
for i in range(1,11):
    print( n ,"*" ,i, "=",n*i)'''
#factorial
'''n=int(input())
factorial=1
for i in range(1,n+1):
    factorial*=i
    print(factorial)'''
#reverse a number
'''n=int(input("enter a number:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("Reverse number:",rev)'''
#count digits in a number
'''num=int(input("enter a number:"))
count=0
if num==0:
    count=1
else:
    num=abs(num)
    while num>0:
        count+=1
        num=num//10
print("count of digits in given number is:",count)'''
#prime number or not
'''n=int(input("enter a number:"))
if n<2:
    print("given number is not a prime number")
else:
    is_prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime=False
            break
    if is_prime:
            print("given number is a prime number")
    else:
        print("given number is not a prime number")'''
#fibanoccci series
'''n=int(input("enter a number:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b'''
        

    
    
    

    
    
    

