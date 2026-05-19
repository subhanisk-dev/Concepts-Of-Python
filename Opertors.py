Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#Operators


#Arthematic Operators

a=5
b=10

print(a+b)
15
print(a- b)
-5
print(a*b)
50
print(a//b)
0
print(a/b)
0.5
print(a**b)
9765625
print(a%b)
5


#Assignment Operators

a=5
b=8

print(a+=b)
SyntaxError: invalid syntax

a+=b
a
13

a-=2
a
11
a*=3
a
33
a//=3
a
11
a/=2
a
5.5
a**=4
a
915.0625
a%=2
a
1.0625

a=5
a
5
b=8
b+=a
b
13
b-=2
b
11

#only after calling it displays the changed values



#Comparioson Operators

a=4
b=8

a<b
True
b>a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a<=b
True
b>=a
True
a>=b
False
b<=a
False


a=4
b=4
a==b
True
a!=b
False
a>b
False
b<a
False



#Logical Operators
#and or not

a=2
b=4

a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False

a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True

not True
False
not False
True

not a!=b
False
not a==b
True


#Identify Operatords

a=9
if type(a) is int:
    print("It is Int")

    
It is Int
if type(a) is not int:
    print("It is not int")

    

b="India"
if type(b) is str:
    print("Its string")

    
Its string
if type(b) is not str:
    print("Its not str")

    
if b is "India":
    print("India")

    
India


#Membership Operators

a=0,1,2,3,4,5,6,7,8,9
>>> a
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> if 8 in a:
...     print("its present")
... 
...     
its present
>>> if 10 in a:
...     print("its presnet")
... 
...     
>>> if 10 not in a:
...     print("Its not presnet")
... 
...     
Its not presnet
>>> 
>>> b="hello","world","hi"
>>> b
('hello', 'world', 'hi')
>>> 
>>> if "hi" in b:
...     print("Its presnet")
... 
...     
Its presnet
>>> if "hi" not in b:
...     print("Its not present")
... 
...     
