Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
  
#do not start with a keyword
a0123=45
print(a0123)
45
if=70
SyntaxError: invalid syntax
while=1
SyntaxError: invalid syntax

#we can use string as variable name

city="Vij"
print(city)
Vij
name="subbu"
print(name)
subbu
mobileno=990874062
print(mobileno)
990874062
0a=1
SyntaxError: invalid decimal literal
a0=1
print(a0)
1

#at a time usage of 2 variables

fname="subbu"
lname="shaik"
print(fname+lname)
subbushaik
print(fname + " " +lname)
subbu shaik
print(fname,lname)
subbu shaik


#passing of 2 variable sata time

a=1,b=2
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=1;b=2
print(a,b)
1 2

c,d=3,4
>>> print(c+d)
7
>>> 
>>> 
>>> f=g=h=j=12
>>> print(f,g,h,j)
12 12 12 12
>>> l=6,7,8,9
>>> print(l)
(6, 7, 8, 9)
>>> x,y,z=25
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x,y,z=25
TypeError: cannot unpack non-iterable int object
>>> 
>>> 

  >>> #unpacking variiable

  >>> a,b,c=(5,6,7)
>>> print(a,b,c)
5 6 7
>>> 
>>> z=56
>>> print(z)
56
>>> del z
>>> print()z
SyntaxError: invalid syntax
>>> print(z)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined


#space b/w var

first name="subbu"
SyntaxError: invalid syntax
first_name="subbu"
print(first_name)
subbu
firstname="subbu"
print(firstname)
subbu


#case senstive

age=23
print(age)
23
AGE=23
print(AGE)
23
Age=23
print(Age)
23


