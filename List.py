Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a=[2,3.5,"Subbu",True,False]
a
[2, 3.5, 'Subbu', True, False]
type(a)
<class 'list'>

a=7
type(a)
<class 'int'>
b=[7]
type(b)
<class 'list'>


#List Methods
#append --> adds only one

a=["pyt","java","c","c++"]
a
['pyt', 'java', 'c', 'c++']
a.append("ml")
a
['pyt', 'java', 'c', 'c++', 'ml']

a.append("ds","js")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.append("ds","js")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ds","js"])
a
['pyt', 'java', 'c', 'c++', 'ml', ['ds', 'js']]

#extend --> adds more than one

a=["a","b","c","d","e"]

a
['a', 'b', 'c', 'd', 'e']
a.extend(["f","g"])
a
['a', 'b', 'c', 'd', 'e', 'f', 'g']

a.extend("h")
a
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#inserts --> adds at the particular position
a=[2,4,5]
a
[2, 4, 5]
a.insert(1,3)
a
[2, 3, 4, 5]

#index --> gives index of particulat ones
a=["hello","hey","welcome"]
a.index("hey")
1

#copy --> copyes
b=a
a
['hello', 'hey', 'welcome']
c=c.copy()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    c=c.copy()
NameError: name 'c' is not defined
c=a.copy()
c
['hello', 'hey', 'welcome']

d=c.copy(1)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    d=c.copy(1)
TypeError: list.copy() takes no arguments (1 given)

#clear ---
#deletes all
a=[8,9,7,5]
a.clear()
a
[]
x=[] #assigning  a empty list
x
[]

#Sort
a=["subbu","s","u","b"]
s
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s
NameError: name 's' is not defined
a
['subbu', 's', 'u', 'b']
a.sort()
a
['b', 's', 'subbu', 'u']

a=[8,7,6,2,8,9]
a
[8, 7, 6, 2, 8, 9]
a.sort()
a
[2, 6, 7, 8, 8, 9]

#reverse -->
a=["hi","bye","hello"]
a
['hi', 'bye', 'hello']
a.reverse()
a
['hello', 'bye', 'hi']

#pop --> removes the element at last position
a=["a","b","c","d","e"]
a.pop()
'e'
a
['a', 'b', 'c', 'd']
a.pop("d")
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a.pop("d")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(4)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.pop(4)
IndexError: pop index out of range
a.pop(3)
'd'

#remove --> deletes particular element by give value
a.remove
<built-in method remove of list object at 0x000002371C716040>
a.remove("d")
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.remove("d")
ValueError: list.remove(x): x not in list
>>> a
['a', 'b', 'c']
>>> a.remove("c")
>>> a
['a', 'b']
>>> 
>>> #count --> counts how many elements presents
>>> a=[5,9,8,7,6,5,7,8,1,9]
>>> a
[5, 9, 8, 7, 6, 5, 7, 8, 1, 9]
>>> a.count(8)
2
>>> a.count(1)
1
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> 
>>> #len --> gives the lenght
>>> a="subhani"
>>> len(a)
7
>>> a=["subhani"]
>>> len(a)
1
>>> 
>>> #list is mutable.It can be changes an list
