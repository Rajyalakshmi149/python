Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strings
a="vijayawada is a royal city"
a[16]+a[17]+a[18]+[19]+[20]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a[16]+a[17]+a[18]+[19]+[20]
TypeError: can only concatenate str (not "list") to str
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
#negative indexing
a="i am learning python"
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'learn'
a[-18]+[-17]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[-18]+[-17]
TypeError: can only concatenate str (not "list") to str
a[-18]+a[-17]
'am'
a[-20]
'i'
b="we are pretty"
b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'pretty'
b[-10]+b[-9]+b[-8]
'are'
b[-13]+b[-12]
'we'
c="simple is better"
c[-16]+c[-15]+c[-14]+c[-13]+c[-12]+c[-11]
'simple'
#slicing
a="codegnan"
a[0:3]
'cod'
>>> a[0:4]
'code'
>>> a[:4]
'code'
>>> a[4:8]
'gnan'
>>> a[4:]
'gnan'
>>> a[4:]
'gnan'
>>> a="beautiful is better than ugly"
>>> a[25:]
'ugly'
>>> a[13:18]
'bette'
>>> a[13:19]
'better'
>>> a[:9]
'beautiful'
>>> b="simple is better than complex"
>>> b[21:]
' complex'
>>> b[16:20]
' tha'
>>> b[16:21]
' than'
>>> b[:6]
'simple'
>>> #negative slicing
>>> d="python is easy"
>>> d[-14:-8]
'python'
>>> d[-7:-5]
'is'
>>> d[-4:]
'easy'
>>> d[-4:0]
''
>>> e="every day is learning"
>>> e[-21:-16]
'every'
>>> e[-15:-12]
'day'
>>> e[-8:]
'learning'
