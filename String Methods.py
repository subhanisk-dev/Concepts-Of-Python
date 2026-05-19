Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods

#len() -- gives the length of string

a="subhani"
len(a)
7
b="shaik subhani"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1


#count - gives an index where thata presents or starts

a="twinkle twinkle little star"

count(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("Twinkle")
0
KeyboardInterrupt
a.count("Twinkle")
a.count("twinkle")
2
a.count("t")
5


#find() -- find a string

a="python"
a[2]
't'
a.find("t")
2

a.find("z")
-1
a.find(a)
0

a.count(a)
1


#escape sequences

#\n -> new line
#\t -> tab space

a="Name \n MobileNo \t Email"
z
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    z
NameError: name 'z' is not defined
a
'Name \n MobileNo \t Email'
print(a)
Name 
 MobileNo 	 Email


#replace -->replaces particular word with particular word
 

a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
print(a)
wait until you succeed

b="wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'

>>> b.repace("wait","work",1)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    b.repace("wait","work",1)
AttributeError: 'str' object has no attribute 'repace'. Did you mean: 'replace'?
>>> b.replace("wait","work",1)
'work wait until you succeed'
>>> 
>>> #strip() -> Removes spaces in whole string
>>> #lstrip -> removes right space only
>>> #lstrip -> removes left space only
>>> #rstrip -> removes right space only
>>> 
>>> x="        subbu        "
>>> x.strip()
'subbu'
>>> x.rstrip()
'        subbu'
>>> x.lstrip()
'subbu        '
>>> print(x)
        subbu        
>>> x
'        subbu        '
>>> 
>>> strip(x)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    strip(x)
NameError: name 'strip' is not defined


a="hello"
a.upper()
'HELLO'
a.lower()
'hello'

b="python course"
b.capitalize()
'Python course'

b.title()
'Python Course'
b
'python course'

b.upper(0)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b.upper(0)
TypeError: str.upper() takes no arguments (1 given)
b.upper("p")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b.upper("p")
TypeError: str.upper() takes no arguments (1 given)



a="code"
a.isupper()
False
a.islower()
True

a.isalpha()
True
a.isalphanum()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.isalphanum()
AttributeError: 'str' object has no attribute 'isalphanum'. Did you mean: 'isalnum'?
a.isalnum()
True

a.startswith("c")
True

a.endswith("e")
True

b=12345
b.isnum()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b.isnum()
AttributeError: 'int' object has no attribute 'isnum'
c="12345"
c.isnum()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
c.isdigit()
True
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'

d="Hey@123"
d.isapha()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d.isapha()
AttributeError: 'str' object has no attribute 'isapha'. Did you mean: 'isalpha'?
d.isalpha()
False




#split --
a="python c c++ java"
a.split()
['python', 'c', 'c++', 'java']

b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']


#merge()
#join()

a="vja","hyd",vzg"
SyntaxError: unterminated string literal (detected at line 1)
a="vja","hyd","vzg"
type(a)
<class 'tuple'>
a
('vja', 'hyd', 'vzg')

"".join(a)
'vjahydvzg'
" ".join(a)
'vja hyd vzg'
a
('vja', 'hyd', 'vzg')

#concatenation

a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course

fname="Subhani"
lanme="Shaik"
lname="shaik"
print(fname+lname)
Subhanishaik
print(fname +" "+lname)
Subhani shaik

print(fname.title()+" " +lname.title())
Subhani Shaik
print((fname+" "+lname).title())
Subhani Shaik



#formating
a,b=2,7
a+b
9
print("The sum is",a+b)
The sum is 9
print("The sum is ,a+b")
The sum is ,a+b

a="city"
print("people lives in",a)
people lives in city
>>> print("the city is "a)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
>>> a="channu"
>>> b="munnu"
>>> 
>>> print("hello {}{}".format(a,b))
hello channumunnu
>>> print("hello {} {}".format(a,b))
hello channu munnu
>>> print("hello {} hello {}".format(a,b))
hello channu hello munnu
>>> print("hello { }".format(a))
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    print("hello { }".format(a))
KeyError: ' '
>>> print("hello {}".format(a))
hello channu
>>> 
...  
>>> #fstring()
>>> a="subbu"
>>> b="jillu"
>>> print(f"hello {a}{b}")
hello subbujillu
>>> print(f"hello {a} {b}")
hello subbu jillu
>>> print(f"hello {a} bye {b}")
hello subbu bye jillu
