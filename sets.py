Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set --> unordered collection

a={2,3.5,"subbu",2+3j,True,False}
a
{False, True, 2, 3.5, 'subbu', (2+3j)}
#unordered

type(a)
<class 'set'>

#add --> adds an element in set
a.add(20)
a
{False, True, 2, 3.5, 20, 'subbu', (2+3j)}
#it adds anywhere in the set

#issubset() --> is a as an subset/part of an b
a=(5,6,7,8,9)
a={5,6,,7,8,9}
SyntaxError: invalid syntax
a
(5, 6, 7, 8, 9)
a={2,3,4,5,6}
a
{2, 3, 4, 5, 6}
b={4,5,6}
b
{4, 5, 6}
a.issubset(b)
False
b.issubset(a)
True
a.issubset(a)
True

#issuperset --> an set must be all elements present in superset

a={4,5,6,7,8,9}
b={4,5,6}

a.issuperset(b)
True
b.issuperset(b)
True
b.issuperset(a)
False

#union --> a merge b/w two sets ,a combination of both sets

a={1,2,3,4,5,6}
b={0,6,7,8,9}
a.union(b)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
b.union(a)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


#intersection -->  prints same elements presents in both sets

a={1,2,3,4,5}
b={4,5,6}
a.intersection(a)
{1, 2, 3, 4, 5}
a.intersection(b)
{4, 5}
b.intersection(a)
{4, 5}


#update -->adds values in a using b

a={2,3,4,5,6}
b={4,5,6,7,8}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8}


#difference -->gives unique values rather than same values
a={10,20,30,40,50,60}
b={40,50,60,70,80,90}
a.difference(b)
{10, 20, 30}
b.difference(a)
{80, 90, 70}


#symmetric_difference -->prints unique values presents in both sets

a={2,3,4,5,6,7,8,9,10}
b={4,5,6,7,8,9,10,11,12}
a.symmetric_difference(b)
{2, 3, 11, 12}
b.symmetric_difference(a)
{2, 3, 11, 12}

a
{2, 3, 4, 5, 6, 7, 8, 9, 10}

#difference_update --> updates on set by unique value only
a={2,3,4,5,6,7}
b={5,6,7,8,9}
a.difference_update(b)
a
{2, 3, 4}
b.difference_update(a)
b
{5, 6, 7, 8, 9}
a.difference_update(a)
a
set()

#intersection_update --> updates same vaue on that set

a={1,2,3,4,5,6}
b={2,3,4,5,6,7}
a.intersection_update(b)
a
{2, 3, 4, 5, 6}
b.intersection_update(a)
b
{2, 3, 4, 5, 6}
a.intersection_update(a)
a
{2, 3, 4, 5, 6}


#symmetric_update --> updates differnt values on both sets
a={1,2,3,4,5,6}
>>> b={4,5,6,7,8,9}
>>> a.symmetric_difference_update(b)
>>> a
{1, 2, 3, 7, 8, 9}
>>> b.symmetric_difference_update(a)
>>> b
{1, 2, 3, 4, 5, 6}
>>> 
>>> a.symmetric_difference_update(a)
>>> a
set()
>>> 
>>> #discard()--> removes particular element on set
>>> a={1,2,3,4,5,6}
>>> a.discard(6)
>>> a
{1, 2, 3, 4, 5}
>>> 
>>> #isdisjoint --> retuns true/false,there values different then true otherwise false
>>> a={1,2,3,4,5}
>>> b={6,7,8,9}
>>> a.isdisjoint(b)
True
>>> b.isdisjoint(a)
True
>>> a.isdisjoint(a)
False
>>> 
>>> #clear
>>> #pop
