#loops
#types: for,while,range,break,,continue,pass
#for loop:(sequence iteration)
'''a=[10,20,30,40,50]'''
'''for i in a:
    print(i)'''
'''for i in a:
    print(a)'''
'''for i in a:
    print(i,end=",")'''
'''for i in a:
    print(type(i))
    print(type(a))'''
a={"a":1,"b":2,"c":3,"d":4}
'''for i in a:
    print(type(i))
    print(type(a))'''
'''for i in a:
    print(i)'''
'''for i in a:
    print(a)'''
'''for i in a.keys():
    print(i)
    print(type(i))
    print(type(a))
for i in a.values():
    print(i)
    print(type(i))
    print(type(a))
for i in a.items():
    print(i)
    print(type(i))
    print(type(a))
a={10,20,30}
for i in a:
    print(i)
    print(type(i))
    print(type(a))
a="python"
for i in a:
    print(i)
    print(type(i))
    print(type(a))
a=[2.5,5.6]
for i in a:
    print(type(i))
    print(type(a))
a=(2.5,3.5)
for i in a:
    print(type(i))
    print(type(a))'''
'''a=["codegnan","python","course"]
for i in a:
    print(i.upper())'''
#while loop(continous itteration)
'''a=10
while a<1:
    print(a)'''
a=10
'''while a>1:
    print(a)
a=10
while a>1:
    print(a)
    a=a+1
while a>1:
    print(a)
    a=a-1
a=10
while a>1:
    a=a+1
    print(a)'''
'''a=10
while a>1:
    a=a-1
    print(a)'''
#voting in while loop
'''while True:
    a= int(input("enter age:"))
    if a>=18:
           print("eligible")
    else:
        print("not eligible")'''
#leap year
'''while True:
    a= int(input("enter yera:"))
    if a%4==0:
           print("it is a leap year")
    else:
        print("it is not a leap year")'''       
#vowel or not
'''while True:
         letter=input("enter a letter:").lower()
    a=['a','e','i','o','u']
    if letter in a:
        print("it is a vowel")
    else:
        print("it is a consonent")'''
#positive or negative
'''while True:
        a= int(input("enter a number:"))
    if a>0:
        print("positive")
    elif a==0:
        print("zero")
    else:
        print("negative")'''
#largest number
'''while True:
        a=int(input("enter a first number"))
    b=int(input("enter a second number"))
    if a>b:
        print("a is largest")
    else:
        print("b is largest")'''
#guest
'''while True:
        a=int(input("enter a number:"))
    b=int(input("enter a number:"))'''
'''name=(input("enter a name:")).lower()
    a=["rajyalakshmi","rajesh","ammulu","lakshmi","vijaya"]

    if name in a:
          print("welcome",name)
    else:
         print("welcome guest",name)'''
#range()
#start
'''for i in range(10):
    print(i)'''
#start- stop
'''for i in range(6,17):
    print(i)'''
#start-stop-step
#task:
#(i)
'''for i in range(0,20,2):
    print(i)'''
#(ii)
'''for i in range(5,50,5):
    print(i)'''
#(iii)
'''for i in range(3,30,3):
    print(i)'''
#4:
'''while True:
    a=int(input("enter marks:"))
if a in range(90,101):
        print("Grade A")
 elif a in range(80,91):
        print("Grade B")
 elif a in range(70,81):
        print("Grade C")
 elif a in range(50,71):
        print("Grade D")
elif a in range(0,50):
        print("Fail")'''
#5
'''while True:
    price=int(input("enter price of a lap top:"))
    if price in range(100000,150000):
        print("APPLE")
    elif price in range(70000,90001):
        print("DELL")
    elif price in range(50000,70000):
         print("HP")
    elif price in range(25000,50000):
         print("ACER")
    else:
         print("None")'''
#break,continue,pass:1:the break statement is used to terminate the entire loop,
        # 2:continue is used to skips the current itteration and rest of the code will continue,
        # 3:pass is a null statement it does nothing but syntsctically we need.
#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==7:
        break'''
'''for i in range(20):
    if i==13:
        break
    print(i)'''
a="python"
'''for i in a:
    if i=="t":
        break
    print(i)'''
#continue
'''a=20
while a>1:
    a=a-1
    if a==15:
        continue
    print(a)'''
'''for i in range(20):
    if i==5:
        continue
    elif i==15:
        break
    print(i)'''
a="rajyalakshmi"
'''for i in a:
    if i=="l":
        continue
    if i=="i":
        break
    print(i)'''
#pass
'''a=15
while a>1:
    print(a)
    a=a-1
    if a==10:
        pass'''
'''for i in range(10):
    if i==7:
   print(i)'''

#pattern problems
'''n=int(input("enter the rows"))
for i in range(1,n+1):
    print("* "*i)'''
'''n=int(input("enter the rows"))
for i in range(n):
    print("* "*(n-i))'''
'''n=int(input("enter the rows"))
for i in range(n):
    print("* "*n)'''
'''n=int(input("enter the rows"))
m=int(input("enter the columns"))
for i in range(n):
    for j in range(m):
        print("* ",end=" ")
    print()'''

'''n=int(input("enter the rows"))
for i in range(1,n+1):
    print("* "*i)'''
#Atm
'''while True:
    account=100000
    pwd="1234"
    cardname=input("insert the card:")
    if cardname=="R":
        print("welcome rajyalakshmi")
        p=input("enter password:")
        if p==pwd:
            option=int(input("choose 1:balence enq 2:withdrwal"))
            if option==1:
                print("your balance amount is:",account)
            elif option==2:
                amount=int(input("enter amount:"))
                print("available balance amount:",account-amount)
        else:
                print("incorrect password")
    else:
        print("invalid card")'''
'''while True:
        account1=100000
        account2=20000
        pwd1="1234"
        pwd2="4569"
        name=input("insert the card:").upper()
        if name=="R":
            print("welcome rajyalakshmi")
            p1=input("enter password:")
            if p1==pwd1:
                option1=int(input("choose 1:balence enq 2:withdrwal"))
                if option1==1:
                    print("your balance amount is:",account1)
                if option1==2:
                    amount1=int(input("enter amount:"))
                    if amount1<account1:
                        print("available balance amount:",account1-amount1)
                    else:
                        print("insufficient balance")
            else:
                 print("incorrect password")
        elif name=="B":
             print("welcome sirisha")
             p2=input("enter password:")
             if p2==pwd2:
                 option2=int(input("choose 1:balance enq 2:withdrwal"))
                 if option2==1:
                     print("your balance amount is:",account2)
                 if option2==2:
                     amount2=int(input("enter amount:"))
                     if amount2<account2:
                         print("available balance amount:",account2-amount2)
                     else:
                         print("insufficient balance")
             else:
                 print("incorrect password")
            
        else:
             print("invalid card")'''

#list comprehension
''' evrey list comprehention can be re return as a for loop
but evrey for loop can not be re-return in list comprehention'''   
a=["codegnan","python","course"]
#["CODEGNAN","PYTHON","COURSE"]
#print(a.upper())
'''b=str(a)
c=b.upper()
print(c)'''

'''for i in a:
        print(i.upper(),end=" ")'''
#syntax
#a=[expr for var in collection/range]

'''b=[i.upper() for i in a]
print(b)'''
'''a=["python","java","ml"]
b=[i.title() for i in a]
print(b)'''
'''a=[1,2,3,4,5,6,8,12,13]
b=[i*i for i in a],[i**2 for i in a],[pow(i,2) for i in a]
print(b)'''
#if usage in list comprehension
'''a=[i for i in range(16) if i%2==0]
print(a)'''
'''fruits=["apple","banana","kiwi","mango","berry","grape"]
a=[i for i in fruits if "a" in i]
print(a)'''
#No elif usage in list comprehension
#if else usage in list comprehension
'''a=[i**2  if i%2==0 else i*5 for i in range(21)]
print(a)'''
'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i  in range(len(a))],[for i in range(5)]
print(c)'''


   
             
               
                         
             
                    
                    
                
                  
                 
        
        
                
    
    
    
    
    

    
    
    
    
         

  

    
    
    
        
    
    
    
    
    
    
    
    
