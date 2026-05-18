Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#DataTypes

a=5
type(a)
<class 'int'>

b=6.9
type(b)
<class 'float'>

c='python'
type(c)
<class 'str'>

d="code"
type(d)
<class 'str'>

e='''Hello'''
type(e)
<class 'str'>

f=5+8j
type(f)
<class 'complex'>

g=9j+8
type(g)
<class 'complex'>

j=8j
type(j)
<class 'complex'>

x=True
type(x)
<class 'bool'>

y=False
type(y)
<class 'bool'>

z="True"
type(z)
<class 'str'>


l=5
l="hello"
print(l)
hello


#Data Type Convesrsions

#Int_Conversion

int(8)
8
int(4.5)
4
int("Hello")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int("Hello")
ValueError: invalid literal for int() with base 10: 'Hello'
int(4+5j)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    int(4+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0


#Float Conversions

float(5)
5.0
float(6.5)
6.5
float("world")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    float("world")
ValueError: could not convert string to float: 'world'
float(5+8j)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    float(5+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0


#String_Conversions

str(8)
'8'
str(8.9)
'8.9'
str("Hey")
'Hey'
str(6+7j)
'(6+7j)'
str(True)
'True'
str(False)
'False'


#complex_Convesrsions

complex(8)
(8+0j)
complex(9.5)
(9.5+0j)
complex("Hello")
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    complex("Hello")
ValueError: complex() arg is a malformed string
>>> complex(8+9j)
(8+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> 
>>> #Boolean Conversions
>>> 
>>> bool(5)
True
>>> bool(8.9)
True
>>> bool("Hello")
True
>>> bool(8+7j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> 
>>> bool()
False
>>> 
>>> # int ->int,float,bool
>>> #float ->int,float,bool
>>> #string->int,float,string,complex,bool
>>> #complex ->int,float,complex,bool
