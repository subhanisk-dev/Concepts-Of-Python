Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="i am danger"
a[0]
'i'
a[2]+a[3]
'am'
a[5]+a[6]+a[7]+a[8]+a[9]+a[10]
'danger'
a[1]+a[4]
'  '

b ="Simple is better than complex"
b[-1]+b[-2]+b[-3]+b[-4]+b[-5]+b[-6]+b[-7]
'xelpmoc'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'complex'

b[11]+b[12]+b[13]+b[14]+b[15]+b[16]
'etter '
b[10]+b[11]+b[12]+b[13]+b[14]+b[15]+b[16]
'better '

b[0]+b[2]+b[3]+b[4]+b[5]+b[6]
'Smple '

10<<10
10240

c="Vizag is a city of Destiny"
c[-7]+c[-6]+c[-5]+c[-4]+c[-3]+c[-2]+c[-1]
'Destiny'
c[-12]+c[-13]
KeyboardInterrupt
c[-15]+c[-14]+c[-13]+c[-12]
'city'

a=10
a[0]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a[0]
TypeError: 'int' object is not subscriptable


#slicing
>>> #a[start:end]
>>> 
>>> x=work
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    x=work
NameError: name 'work' is not defined
>>> x="work hard until you suceed"
>>> x[-6:-1]
'sucee'
>>> x[-6:0]
''
>>> x[-6:]
'suceed'
>>> x[20:26]
'suceed'
>>> x[5:9]
'hard'
>>> x[0:4]
'work'
>>> x[16:19]
'you'
>>> 
>>> y="the art of code"
>>> 
>>> y[-4:]
'code'
>>> y[-7:-6]
'o'
>>> 
