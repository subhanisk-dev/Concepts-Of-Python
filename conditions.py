#conditions

#if condtion by using comparision operators
#<,>,<=,>=,!=,==

'''a=10
b=20
if a<b:
    print("true")'''

'''a=10
b=20
if a>b:
    print("true")'''

'''a=10
b=20
if a<=b:
    print("less")'''

'''a=10
b=20
if b>=a:
    print("Greater")'''

'''a=5
b=8
if a!=b:
    print("not equal")'''

'''a=5
b=5
if a==b:
    print("Equal")'''


'''a=int(input("a value: "))
b=int(input("b value: "))
if a>b:
    print("True a>b") '''

'''a=int(input("a value: "))
if a<50:
    print("its a <50")'''

'''a=input("data")
if a=="java":
    print("a is java")'''

#if condition by using logical operators
#and,or,not

'''a=4
b=8
if a<b and b>a:
    print("true")'''

'''a=4
b=8
if a<=b and b>=a:
    print("true")'''

'''a=4
b=8
if a!=b or a==b:
    print("Not equal")'''

'''a=7
b=9
if not a>b:
    print("less")'''

'''a=7
b=9
if not a>b and b<a:
    print("less")'''

'''a=int(input("a:"))
if not a>10:
    print("fasle")'''

#if condition by using identify operators
#is,is not

'''a=5
if type(a) is int:
    print("true")'''

'''a=5.6
if type(a) is not int:
    print("true")'''

'''a=input("data: ")
if type(a) is str:
    print("true")'''

'''a=5+3j
if type(a) is complex:
    print("true")'''

'''a=True
if type(a) is bool:
    print("true")'''

#if condition by using membership operators
#in,not in

'''a=[10,20,30,40,50,60]
if 60 in a:
    print("true")'''

'''a=[10,20,30,40,50,60]
if 60 not in a:
    print("true")'''

'''a=[10,20,30,40,50,60]
if 70 not in a:
    print("true")'''

'''a=int(input("Enter the number"))
if 10 in a :
    print("True") #TypeError: argument of type 'int' is not iterable '''

'''a=[2,3,4,5,6,7,8,9,10]
b=int(input("Enter the value"))
if b in a:
    print("true")'''


#if-else condition by using comparison operators

'''a=4
b=9
if a<b:
    print("less")
else:
    print("true")'''

'''a=4
b=9
if a>b:
    print("less")
else:
    print("true")'''

'''a=4
b=9
if a!=b:
    print("not equal")
else:
    print("its true")'''

'''a=4
b=4
if a==b:
    print("equal")
else:
    print("false")'''

#if-else condition by using logical operators

'''a=10
b=15
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=10
b=15
if a!=b and b==a:
    print("true")
else:
    print("false") '''

'''a=10
b=15
if a<b or b==a:
    print("true")
else:
    print("false")'''

'''a=10
b=15
if not a<=b and b>=a:
    print("true")
else:
    print("false")'''


#if-else condition by using identify operators

'''a=4
if type(a) is int:
    print("true")
else:
    print("False")'''

'''a=4
if type(a) is not int:
    print("true")
else:
    print("False") '''


#if-else condition by using membership operators

'''a=[3,4,5,6,7,8]
b=int(input("b value: "))
if b in a:
    print("true")
else:
    print("false")'''

a=[3,4,5,6,7,8]
b=int(input("b value: "))
if b not in a:
    print("true")
else:
    print("false")
