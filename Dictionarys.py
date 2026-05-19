Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict --> key value pair
#dict {}

a={"name":"subbu","year":"2026","month":"May"}
a
{'name': 'subbu', 'year': '2026', 'month': 'May'}
type(a)
<class 'dict'>

a["name"]
'subbu'

a["subbu"]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a["subbu"]
KeyError: 'subbu'

a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['subbu', '2026', 'May'])
a.items()
dict_items([('name', 'subbu'), ('year', '2026'), ('month', 'May')])

#update --> adds an key value pairs
a={"date":19,"month":05,"year":2026}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a={"date":19,"month":5,"year":2026}
a
{'date': 19, 'month': 5, 'year': 2026}
a.update({"name":"subbu"})
a
{'date': 19, 'month': 5, 'year': 2026, 'name': 'subbu'}
a
{'date': 19, 'month': 5, 'year': 2026, 'name': 'subbu'}

a.update({"dob":"1-05","branch":"vja"})
a
{'date': 19, 'month': 5, 'year': 2026, 'name': 'subbu', 'dob': '1-05', 'branch': 'vja'}

#setdefault -->
b={"name":"subbu","year":2026}
b
{'name': 'subbu', 'year': 2026}
b,setdefault("month","may")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    b,setdefault("month","may")
NameError: name 'setdefault' is not defined
b.setdefault("month","may")
'may'
b
{'name': 'subbu', 'year': 2026, 'month': 'may'}

#pop --> removes an key must use key pair name

b
{'name': 'subbu', 'year': 2026, 'month': 'may'}
b.remove()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b.remove()
AttributeError: 'dict' object has no attribute 'remove'
b.pop()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    b.pop()
TypeError: pop expected at least 1 argument, got 0

b.pop("year")
2026
b
{'name': 'subbu', 'month': 'may'}

#popitem -->removes last key value pair
b
{'name': 'subbu', 'month': 'may'}
b.popitem()
('month', 'may')
b
{'name': 'subbu'}

#copy -->copies all
a
{'date': 19, 'month': 5, 'year': 2026, 'name': 'subbu', 'dob': '1-05', 'branch': 'vja'}
a.copy()
{'date': 19, 'month': 5, 'year': 2026, 'name': 'subbu', 'dob': '1-05', 'branch': 'vja'}

#clear --> deletes all key value pairs
b
{'name': 'subbu'}
b.clear()
b
{}

b={} #creating  a empty a dict
b.update({"name":"subbu"})
b
{'name': 'subbu'}


a
{'date': 19, 'month': 5, 'year': 2026, 'name': 'subbu', 'dob': '1-05', 'branch': 'vja'}



#creating a dict on multiple values using one key

a={"Idno":[4,5,6],"name":["subbu","jillu","channu"],"marks":[75,85,95]}
a
{'Idno': [4, 5, 6], 'name': ['subbu', 'jillu', 'channu'], 'marks': [75, 85, 95]}
type(a)
<class 'dict'>

a.keys()
dict_keys(['Idno', 'name', 'marks'])
a.values()
dict_values([[4, 5, 6], ['subbu', 'jillu', 'channu'], [75, 85, 95]])
a.items()
dict_items([('Idno', [4, 5, 6]), ('name', ['subbu', 'jillu', 'channu']), ('marks', [75, 85, 95])])
>>> 
>>> 
>>> #duplicates -->  dosent allow as keys
>>> 
>>> a={"name":"subbu","city":"vja","name":"subbu"}
>>> a
{'name': 'subbu', 'city': 'vja'}
>>> a={"name":"subbu","city":"vja","name":"jillu"}
>>> a
{'name': 'jillu', 'city': 'vja'}
>>> 
>>> a={"name":"subbu","city":"vja","name1":"subbu"}
>>> a
{'name': 'subbu', 'city': 'vja', 'name1': 'subbu'}
>>> 
>>> len(a)
3
>>> 
>>> a.count("name")
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
>>> a.index("name1")
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.index("name1")
AttributeError: 'dict' object has no attribute 'index'
>>> 
