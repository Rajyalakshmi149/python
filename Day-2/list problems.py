#find largest number in list
'''l=[10,25,5,40,15]
largest=l[0]
for i in l:
    if i>largest:
        largest=i
print("largest number is:",largest)'''
#find smallest number in list
'''l=[10,25,5,40,15]
smallest=l[0]
for i in l:
    if i<smallest:
        smallest=i
print("smallest number is:",smallest)'''
#sum of list elements
'''list=[10,20,34,56,89]
total=0
for i in list:
    total+=i
print("sum of list elements is:",total)'''
#count even and odd numbers in list
'''list=[6,5,8,9,7,3,33]
even=0
odd=0
for i in list:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("total number of even numbers in list:",even)
print("total number of odd numbers in list:",odd)'''
#reverse a list
#method-1:slicing
'''list=[1,2,3,4,5,6]
reverse=list[::-1]
print("reverse order of given list is:",reverse)'''
#method-2:revrse()
'''list=[4,5,6,7,8,9]
list.reverse()
print("reverse order of given list is:",list)'''
#remove duplicates
#method-1:
'''l=[1,2,2,3,3,4]
unique_numbers=list(set(l))
print("list without duplicates:",unique_numbers)'''
#method-2:
'''l=[1,2,2,3,3,4]
u_n=[]
for i in l:
    if i not in u_n:
        u_n.append(i)
print("list without duplicates:",u_n)'''
#find second largest in list
'''n=[10,20,30,5,40]
u_n=list(set(n))
u_n.sort()
print(u_n[-2])'''
#count frequencyof elements
'''n=[1,2,2,3,3,3]
frequency={}
for i in n:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)'''
#find common elements
'''a=[1,2,3,4,5]
b=[3,4,5,6,7]
common=[]
for i in a:
    if i in b:
        common.append(i)
print(common)'''

        


        
        
