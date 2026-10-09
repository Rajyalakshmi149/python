Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #DICTIONARY{}
>>> #dict{}
>>> a={"name":"rajyalakshmi","year":2025,"month":12}
>>> print(a)
{'name': 'rajyalakshmi', 'year': 2025, 'month': 12}
>>> type(a)
<class 'dict'>
>>> b={5,6,76}
>>> type(b)
<class 'set'>
>>> a["name"]
'rajyalakshmi'
>>> a["rajyalakshmi"]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a["rajyalakshmi"]
KeyError: 'rajyalakshmi'
>>> a={"year":2025,"month":"dec","date":5}
>>> a.keys()
dict_keys(['year', 'month', 'date'])
>>> a.values()
dict_values([2025, 'dec', 5])
>>> a.items()
dict_items([('year', 2025), ('month', 'dec'), ('date', 5)])
>>> #update
>>> a={"time":5,"hour":5,"min":10}
>>> a.update({"sec":20})
>>> a
{'time': 5, 'hour': 5, 'min': 10, 'sec': 20}
>>> a.update({"name":"rajyalakshmi"},{"age":21})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.update({"name":"rajyalakshmi"},{"age":21})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"name":"rajyalakshmi","age":12})
>>> a
{'time': 5, 'hour': 5, 'min': 10, 'sec': 20, 'name': 'rajyalakshmi', 'age': 12}
>>> a={"country":"india","state":"ap"}
>>> a.setdefault("city","vij")
'vij'
>>> b
{76, 5, 6}
>>> a={"movie":"umami","song":"pushpa"}
>>> a.copy()
{'movie': 'umami', 'song': 'pushpa'}
a.pop()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("movie")
'umami'
a
{'song': 'pushpa'}
a={"season":"winter","month":"dec"}
a.popitem()
('month', 'dec')
a
{'season': 'winter'}
a={"year":2025,"month":"dec","year":2025}
print(a)
{'year': 2025, 'month': 'dec'}
a.index("year")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.index("year")
AttributeError: 'dict' object has no attribute 'index'
a={"year":2025,"month":"dec","year":2026}
print(a)
{'year': 2026, 'month': 'dec'}
a={"year":2025,"month":"dec","year":2025}
a
{'year': 2025, 'month': 'dec'}
a={"course":"python","class":1}
len(a)
2
a.count("course")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.count("course")
AttributeError: 'dict' object has no attribute 'count'
a.clear()
a
{}
b=a
b.update({"name":"rajyalakshmi"})
b
{'name': 'rajyalakshmi'}
a={"food":"biryani","desert":"cake"}
a.get()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.get()
TypeError: get expected at least 1 argument, got 0
a.get("food")
'biryani'
a
{'food': 'biryani', 'desert': 'cake'}
a["food"]
'biryani'
a.get("food")
'biryani'
a
{'food': 'biryani', 'desert': 'cake'}
#get-> measns to read data
a="burak deniz"
list(a)
['b', 'u', 'r', 'a', 'k', ' ', 'd', 'e', 'n', 'i', 'z']
tuple(a)
('b', 'u', 'r', 'a', 'k', ' ', 'd', 'e', 'n', 'i', 'z')
set(a)
{'d', 'e', 'z', 'a', 'u', ' ', 'i', 'k', 'b', 'n', 'r'}
dict(a)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
b=a.fromkeys(a)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    b=a.fromkeys(a)
AttributeError: 'str' object has no attribute 'fromkeys'
c=dict.fromkeys(a)
c
{'b': None, 'u': None, 'r': None, 'a': None, 'k': None, ' ': None, 'd': None, 'e': None, 'n': None, 'i': None, 'z': None}
d=dict.fromkeys(a,"turkey")
d
{'b': 'turkey', 'u': 'turkey', 'r': 'turkey', 'a': 'turkey', 'k': 'turkey', ' ': 'turkey', 'd': 'turkey', 'e': 'turkey', 'n': 'turkey', 'i': 'turkey', 'z': 'turkey'}
d["n"]="java"
d
{'b': 'turkey', 'u': 'turkey', 'r': 'turkey', 'a': 'turkey', 'k': 'turkey', ' ': 'turkey', 'd': 'turkey', 'e': 'turkey', 'n': 'java', 'i': 'turkey', 'z': 'turkey'}
d["b"]="istanbul"
d
{'b': 'istanbul', 'u': 'turkey', 'r': 'turkey', 'a': 'turkey', 'k': 'turkey', ' ': 'turkey', 'd': 'turkey', 'e': 'turkey', 'n': 'java', 'i': 'turkey', 'z': 'turkey'}
d["burak deniz"]="istanbul"
d
{'b': 'istanbul', 'u': 'turkey', 'r': 'turkey', 'a': 'turkey', 'k': 'turkey', ' ': 'turkey', 'd': 'turkey', 'e': 'turkey', 'n': 'java', 'i': 'turkey', 'z': 'turkey', 'burak deniz': 'istanbul'}
a={"names":["rajyalakshmi","burak","ammulu"],"marks":[60,90,69]}
print(a)
{'names': ['rajyalakshmi', 'burak', 'ammulu'], 'marks': [60, 90, 69]}
type(a)
<class 'dict'>
a.keys()
dict_keys(['names', 'marks'])
a.values()
dict_values([['rajyalakshmi', 'burak', 'ammulu'], [60, 90, 69]])
