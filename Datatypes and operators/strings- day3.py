Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strings
#replace
a="wait untill you succeed"
a.replace("wait","work")
'work untill you succeed'
a
'wait untill you succeed'
b=a.replace("wait","work")
b
'work untill you succeed'
c="hello java"
c.replace("java","python")
'hello python'
#escape sequences
#\n:new line
#\t:tab space
a="name\nmobile no\tmailid\naddress"
print(a)
name
mobile no	mailid
address
b="name:rajyalakshmi\nmobileno:6393085284\tmail:battularajyalakshmi6@gmail.com"
print(b)
name:rajyalakshmi
mobileno:6393085284	mail:battularajyalakshmi6@gmail.com
#upper()
a="code"
a.upper()
'CODE'
#lower()
b="RAJYALAKSHMI"
b.lower()
'rajyalakshmi'
b.captalize()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
c="python"
c.captalize()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    c.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
c.capitalize()
'Python'
c="python course"
c.title()
'Python Course'
c.upper("P")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c.upper("P")
TypeError: str.upper() takes no arguments (1 given)
c.upper(0)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c.upper(0)
TypeError: str.upper() takes no arguments (1 given)
e="i am in class"
e.title()
'I Am In Class'
c[0].upper()
'P'
s="data science"
s.isupper()
False
s.islower()
True
s.isdigit()
False
s.startswith("d")
True
s.endswith("e")
True
s.isalpha()
False
b="datascience"
b.isalpha()
True
a=6782
a.isdigit()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
a="6298"
a.isdigit()
True
c=5+6j
c.isdigit()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    c.isdigit()
AttributeError: 'complex' object has no attribute 'isdigit'
c="5+6j"
c.isdigit()
False
c.isalnum()
False
c="burak69"
c.isalnum()
True
#strip()
#lstrip()&rstrip()
a="       rajyalakshmi        "
a.strip()
'rajyalakshmi'
a.lstrip()
'rajyalakshmi        '
a.rstrip()
'       rajyalakshmi'
a="   my name is       "
a.strip()
'my name is'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="india is my country"
b.split()
['india', 'is', 'my', 'country']
#join()
a="html","css","js"
"".join(a)
'htmlcssjs'
" '.join(a)
SyntaxError: unterminated string literal (detected at line 1)
" ".join(a)
'html css js'
' '.join(a)
'html css js'
"r".join(a)
'htmlrcssrjs'
b="c"."c++","java "
SyntaxError: invalid syntax
b="c","c++","java"
>>> "s".join(b)
'csc++sjava'
>>> c="python@"
>>> "l".join(c)
'plyltlhlolnl@'
>>> #concatination
>>> a="code"
>>> b="python"
>>> print(a+b)
codepython
>>> fname="rajyalakshmi"
>>> lname="b"
>>> print(fname+lname)
rajyalakshmib
>>> print(fname+""+lname)
rajyalakshmib
>>> print(fname.title()+" "+lname.title())
Rajyalakshmi B
>>> print(fname+" "+lname).title()
rajyalakshmi b
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print(fname+" "+lname).title()
AttributeError: 'NoneType' object has no attribute 'title'
>>> print((fname+" "+lname).title())
Rajyalakshmi B
>>> #formating(for adding aditional data to given data or string)
>>> a=3
>>> b=5
>>> print(a+b)
8
>>> print("the sum is",a+b)
the sum is 8
>>> print("the sum is a+b")
the sum is a+b
>>> name="burak deniz"
>>> print("name is",name)
name is burak deniz
>>> city="vijayawada"
>>> print("city is",city)
city is vijayawada
>>> #formate method
>>> a="burak"
>>> b="deniz"
>>> print("hello",a+b)
hello burakdeniz
>>> print("hello {}{}".format(a,b))
hello burakdeniz
print("hello {} {}".format(a,b))
hello burak deniz
print("hello {} hello {}".format(a,b))
hello burak hello deniz
#fstring
a="rajya"
a="lakshmi"
print(f"hello {a}{b}")
hello lakshmideniz
print(f"hello {a} {b}")
hello lakshmi deniz
print(f"hello {a} hello {b}")
hello lakshmi hello deniz
