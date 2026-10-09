Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets {}
#set is a unorderd collection & removes duplicate values
#set is asemi mutable
a={5,6,7,"hi",3+4j,True,False}
print(a)
{False, True, 5, 6, 7, 'hi', (3+4j)}
type(a)
<class 'set'>
b={8,4,2,0,3,6,0,1}
print(b)
{0, 1, 2, 3, 4, 6, 8}
#add()
a.add(20)
a
{False, True, 20, 5, 6, 7, 'hi', (3+4j)}
a={1,2,3,4,5,6,7}
b={4,5,6,7}
b.issubset(a)
True
a.issubset(b)
False
#superset()
a={3,4,5,6,7,8,9}
b={7,8,9}
a.issuperset(b)
True
b.issuperset(a)
False
#union("merging of 2 sets & remove duplicate")
a={3,4,5,6,7}
b={6,7,8,9,10}
a.union(b)
{3, 4, 5, 6, 7, 8, 9, 10}
#intersection("it will print common elements")
a={2,4,6,8,10,11}
b={5,6,7,8,9,11,12}
a.intersection(b)
{8, 11, 6}
#difference()
a.difference(b)
{2, 10, 4}
b.difference(a)
{9, 12, 5, 7}
#update()
a={1,3,5,7,9,11,13,15}
b={2,4,6,8,10,12,13,15}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15}
#difference_upadate("delete same value & print opposite value")
a={10,20,30,40,50,60}
b={40,50,60,70,80,90}
a.difference_update(b)
a
{20, 10, 30}
b.difference_update(a)
a
{20, 10, 30}
b
{80, 50, 70, 40, 90, 60}
#intersection_update("print the same valuees")
a={2,3,4,5,6,7}
b={5,6,7,8,9,10}
a.intesection_update(b)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.intesection_update(b)
AttributeError: 'set' object has no attribute 'intesection_update'. Did you mean: 'intersection_update'?
a.intersection_update(b)
a
{5, 6, 7}
b.intersection_update(a)
b
{5, 6, 7}
#symmetric_difference("delete the same values")
a={4,5,6,7,8,9,10}
b={1,2,5,9,12,14}
a.symmetric_difference(b)
{1, 2, 4, 6, 7, 8, 10, 12, 14}
b.symmetric_difference(a)
{1, 2, 4, 6, 7, 8, 10, 12, 14}
#symmetric_difference_update("same value del& next through updated values")
a={2,4,6,8,10,12,14}
b={1,2,3,6,8,10,13}
a.symmetric_difference_update(b)
a
{1, 3, 4, 12, 13, 14}
>>> b.symmetric_difference_update(a)
>>> b
{2, 4, 6, 8, 10, 12, 14}
>>> #pop("del first element")
>>> a.pop()
1
>>> b.pop()
2
>>> #remove("particular data will be deleted")
>>> a.remove(4)
>>> a
{3, 12, 13, 14}
>>> a.pop(4)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.pop(4)
TypeError: set.pop() takes no arguments (1 given)
>>> #clear(),copy()
>>> a={3,5,7,9,11,13}
>>> a.copy()
{3, 5, 7, 9, 11, 13}
>>> a.clear()
>>> a
set()
>>> b=a
>>> b.add(30)
>>> b
{30}
>>> b.add(4,5)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    b.add(4,5)
TypeError: set.add() takes exactly one argument (2 given)
>>> #discard &remove are same("value should opposite then its true")
>>> a={3,4,5,6,7,8}
>>> b={1,2,3,4,5}
>>> a.discard(3)
>>> a
{4, 5, 6, 7, 8}
>>> a.isdisjoint(b)
False
>>> a={8,9,10,11,12}
>>> b={13,14,15,16}
>>> a.isdisjoint(b)
True
