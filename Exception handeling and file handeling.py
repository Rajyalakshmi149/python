#file handeling
#write()
'''a=open("python.txt","w")
b=a.write("codegnan IT solutions")
a.close()
a=open("python.txt","w")
a.write("python course")
a.close()'''
'''a=input()
b=open("python.txt","w")
b.write(a)
b.close()'''
#append
'''a=input()
b=open("python.txt","a")
b.write(a)
b.close()'''
#readlines()
'''a=open("python.txt",)
#print(a.read())#it will display entire content
#print(a.readline())#it will display first line
#print(a.read(6))#it will display no.of characters
print(a.readlines())#it will dispaly with \n'''
#writelines()->it makes every object side by side
'''a=["python","java","c","c++","ml"]
b=open("python.txt","w")
b.writelines(a)
b.close()'''
'''a=["python","java","c","c++","ml"]
b=open("python.txt","w")
b.writelines("\n".join(a))
b.close()'''
#accesing files
'''a=open("vaiables.py")
print(a.read)
a=open("path")
print(a.read())'''

#Errors and Exceptional handeling
#syntax error
'''for i in range(10)
print(i)'''#syntax error for loop has must be ":".
#runtime error
'''a=int(input())
b=int(input())
print(a//b)'''# if we gave a 0 for b in runtime it will cause error.
#logical error
'''a=10
b=20
print(a-b)
a=10
b=20
if a>b:
    print("true")'''#it will raise logical error.

#exception handeling
'''a=int(input())
b=int(input())
try:
    c=a*b
    print(c)'''

'''a=int(input())
b=int(input())
try:
    c=a//b
    print(c)
except:
    print("exception raised")#if  any error raised this block will excute
else:
    print("no exceptions")#if no errors raised then else block will excute
finally:
    print("program ends..")#always prints given data'''












