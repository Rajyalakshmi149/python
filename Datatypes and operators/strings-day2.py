Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding in strings
a="data science"
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
a="machine learning"
a[::4]
'miln'
a[::7]
'm n'
a[::2]
'mcielann'
a[::5]
'mnag'
a[3:9]
'hine l'
a[7:12]
' lear'
a[5:]
'ne learning'
a[:11]
'machine lea'
c="cloud computing"
>>> c[1:7:2]
'lu '
>>> c[2:12:3]
'o mt'
>>> a[4:14:6]
'ia'
>>> c[4:14:6]
'du'
>>> c[5:10:2]
' op'
>>> c[3:13:1]
'ud computi'
>>> c[7:14:5]
'oi'
>>> c[0:12:6]
'cc'
>>> #negative striding
>>> a="python course"
>>> a[-1:-9:-3]
'eu '
>>> a[-2:-12:-4]
'sch'
>>> a[-3:-13:-5]
'rn'
>>> a[-6:-11:-2]
'cnh'
>>>  a[9:4:2]
...  
SyntaxError: unexpected indent
>>> a[9:4;2]
SyntaxError: invalid syntax
>>> a[9:4:2]
''
>>> #in positive striding highest to lowest indexing is not posible
>>> a[4:9:2]
'o o'
>>> a[-8:-6:-3]
''
>>> #in negative striding lowest to highest indexing is not posible
>>> a[-6:-8:-3]
'c'
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
>>> #string methods
>>> #len()
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c="rajyalakshmi"
len(c)
12
d=""
len(d)
0
d=" "
len(d)
1
#count
a="twinkle twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count(twinkle)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.count(twinkle)
NameError: name 'twinkle' is not defined
a.count("twinkle")
3
a.count("t")
6
a.count("l")
5
a.count("")
36
a.count(" ")
4
a.count("k")
3
#find a string
a.find("o")
-1
t="code"
t.find("o")
1
b="hello"
b.find("l")
2
b[2:4]
'll'
t[2]+b[3]
'dl'
b[2]+b[3]
'll'
