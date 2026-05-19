Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Bitwise Operators
#& | ~ ^ << >>


# &

a=2
b=4

bin(a)
'0b10'
bin(b)
'0b100'

a&b
0

a=5
b=7

bin(a)
'0b101'
bin(b)
'0b111'

a&b
5

3&&
SyntaxError: invalid syntax

3&8
0

6&9
0

3&6
2

8&9
8


# |

4|6
6

8|10
10

bin(4)
'0b100'
bin(6)
'0b110'

bin(8)
'0b1000'
bin(10)
'0b1010'

bin(4) & bin(6)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    bin(4) & bin(6)
TypeError: unsupported operand type(s) for &: 'str' and 'str'
bin(4) and bin(6)
'0b110'


# ~

# ~a = -(x+1)

a=6
~a
-7

~5
-6

# xor ^ operator
>>> 
>>> 
+
>>> 6^8
14
>>> 
>>> 2^4
6
>>> 
>>> # left shift [<<]
>>> 
>>> 6<<3
48
>>> 
>>> # right shift [>>]
>>> 
>>> 7>>4
0
>>> 
>>> 7>>2
1
>>> 
>>> 7>>-2
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    7>>-2
ValueError: negative shift count
>>> 
>>> 5 or True
5
