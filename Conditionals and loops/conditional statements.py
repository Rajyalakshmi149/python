#if-elif-else conditions
'''a=5
b=7
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''
'''a=6
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''
#if-elif-else by using logical operators
'''a=6
b=5
if a>b and b<a:
    print("less")
elif a!=b or a==b:
    print("true")
else:
    print("false")'''
#if-elif-else by using member ship operators
'''a=["python", "html","css"]
if python in a:
    print("true")
elif python not in a:
    print("false")
else:
    print("not found")'''

#multiple-if
'''a=9
b=12
if a<b:
    print("less")
if b>a:
    print("greater")
if a==b:
    print("equal")'''
'''a=6
b=5
if a>b and b<a:
    print("less")
if a>b or b>a:
    print("greater")
if a<b or b>a:
    print("true")'''
a=5.6
'''if a is type(float):
    print("float")
if a is not type(int):
    print("not an integer")'''
#nested if
'''a=5
b=10
if a<b:
    print("true")
    if b>a:
        print("greater")'''
'''a=5
b=10
if a>b:
    print("true")
    if b>a:
        print("greater")'''
'''a=5
b=10
if a<b:
    print("true")
    if b==a:
        print("equal")
    elif b!=a:
        print("not equal")
    
    else:
        print("false")
        
else:
    print("less")'''
#odd or even:
'''a=int(input("enter a number:"))
if a%2==0:
      print("even number")
else:
    print("odd number")'''
#voting
'''a= int(input("enter age:"))
if a>=18:
       print("eligible")
else:
    print("not eligible")'''
#leap year:
    
'''a= int(input("enter yera:"))
if a%4==0:
       print("it is a leap year")
else:
    print("it is not a leap year")'''
#vowel or not
'''letter=input("enter a letter:").lower()
a=['a','e','i','o','u']
if letter in a:
    print("it is a vowel")
else:
    print("it is a consonent")'''

'''a= int(input("enter a number:"))
if a>0:
    print("positive")
elif a==0:
    print("zero")
else:
    print("negative")'''
'''a=int(input("enter a first number"))
b=int(input("enter a second number"))
if a>b:
    print("a is largest")
else:
    print("b is largest")'''
'''a=int(input("enter a number:"))
b=int(input("enter a number:"))'''
'''name=(input("enter a name:")).lower()
a=["rajyalakshmi","rajesh","ammulu","lakshmi","vijaya"]

if name in a:
      print("welcome",name)
else:
     print("welcome guest",name)'''

'''user="rajyalakshmi"
password="lakshmi66$"
a=input("user name")
b= str(input("password"))'''
'''if user==a and password==str(b):
    print("login successfull")
else:
    print("invalid credentials")'''

'''if user==a:
    print("enter password")
    if password==str(b):
        print("login successfull")
    else:
        print("incorrect password")
else:
    print("invalid details")
        
if user==a:
    if password==str(b):
        print("login successfull")
    else:
        print("incorrect password")
else:
    print("invalid details")'''
'''day=input("enter a day")
if day=="monday":
    print("working day")
elif day=="thursday":
    print("middle of the day")
elif day=="satarday":
    print("weekend")
elif day=="sunday":
    print("funday")
else:
    print("boring days")'''
'''cake=input("enter cake name")
if cake=="red veluet":
    print(1200)
elif cake=="choclate":
    print(1000)
elif cake=="almond":
    print(800)
elif cake=="butter scotch":
    print(600)
else:
    print("sorry cake is not available")'''
'''season=input("enter a season:")
if season=="rainy":
    print("must wear raincoat")
elif season=="winter":
    print("must wear hoodie")
else:
    print("must apply sunscreen")'''
'''price=int(input("enter price:")
if price==800:
          print("BBQ pizza")
elif price==600:
    print("crispy pizza")
elif price==400:
    print("corn pizza")
elif price==200:
    print("french frice & coke")
else:
    print("not available")'''
    
    

    

    
                
        
     
    



    
    
    
    
    

    
    
    
    
    

    
    
    
