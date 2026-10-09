#calender module
'''import calendar
year=2026
month=5
print(calendar.month(year,mearonth))'''

'''import calendar
year=int(input())
month=int(input())
print(calendar.month(year,month))'''

'''import calendar
year=int(input())
print(calendar.calendar(year))'''

'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

#epoch time
'''import time
a=time.time()
print(a)
b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"today time is{b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''

'''import random
import time
for i in range(10):
    a=random.randint(1000,9999)
    print(a)
    time.sleep(2)'''
#Reg ex module(regular expressions)
'''a="codegnan is in vij"
print(a)'''
'''a="codegnan\n is\tin\nvij"
print(a)'''
#rstring
'''a=r"codegnan\nis\tin\nvij"
print(a)'''

#compile(),search(),findall(),split(),sub()
#sequence characters
#\w-> it matches alphanumeric
#\W-> it matches non alphanumeric
#\d-> it matches any digit
#\D-> it matches non-digit
#\s->it matches white spaces
#\S-> it matches non-white spaces

#compile()
import re
'''a="map cap cat code maths money cash codegnan cup mug"
b=re.compile(r"m\w\w\w")
print(b)'''
#search()
'''c=b.search(a)
print(c)
b=re.search(r"m\w+",a)
print(b)'''
#findall()
'''c=re.findall(r"m\w+",a)
print(c)'''
'''c=re.findall(r"c\w+",a)
print(c)'''
#split()
'''b=re.split(r"\s",a)
print(b)'''
#sub()
'''c=re.sub("m","n",a)
print(c)'''

'''a="year 2026 month 1 date 20"
b=re.findall(r"\d+",a)
print(b)'''
#
