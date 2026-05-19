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
