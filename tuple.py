Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple -->
>>> a=(2,3.5,"hello",2+3j,True,False)
>>> a
(2, 3.5, 'hello', (2+3j), True, False)
>>> type(a)
<class 'tuple'>
>>> 
>>> #tuple is immutable.Its cannot changes .
>>> 
>>> a.count(2)
1
>>> a.index(3.5)
1
>>> a.index(2+3j)
3
>>> 
>>> a.len()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.len()
AttributeError: 'tuple' object has no attribute 'len'
>>> len(a)
6
