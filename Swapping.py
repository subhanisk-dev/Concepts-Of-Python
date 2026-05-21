Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Swapping

a,b=5,6
print(f"a is {a} b is {b}")
a is 5 b is 6
>>> print(f"a is {a} b is {b}")
a is 5 b is 6
>>> a,b=b,a
>>> print(f"a is {a} b is {b}")
a is 6 b is 5
>>> 
>>> #using temp
>>> temp=a
>>> a=b
>>> b=temp
>>> print(f"a is {a} b is {b}")
a is 5 b is 6
>>> 
>>> #using arthematic operation
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> print(f"a is {a} b is {b}")
a is 6 b is 5
>>> 
>>> #using %d
>>> a,b=3,2
>>> print(f"a is {a} b is {b}")
a is 3 b is 2
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> print("a is %d b is %d" %(a,b))
a is 2 b is 3
