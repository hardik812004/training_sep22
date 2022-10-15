Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=print("Hi ")
Hi 
a
a=print("Hi how r u")
Hi how r u
a
def myfun
SyntaxError: invalid syntax
def myfun():
    print("this is first fun")

    
myfun()
this is first fun

a= myfun()
this is first fun
a
print(a)
None
def myfun():
    return 'This is first fun
SyntaxError: unterminated string literal (detected at line 2)
def myfun():
    return 'This is first fun'

myfun()
'This is first fun'
def second():
    return 'abc'

second()
'abc'
def second():
    return abc

second()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    second()
  File "<pyshell#21>", line 2, in second
    return abc
NameError: name 'abc' is not defined. Did you mean: 'abs'?
b=second()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b=second()
  File "<pyshell#21>", line 2, in second
    return abc
NameError: name 'abc' is not defined. Did you mean: 'abs'?
def second():
    return 'abc'

b=second()
b
'abc'
def third(x):
    print("Hello")

third
<function third at 0x0000009747F14670>
third()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    third()
TypeError: third() missing 1 required positional argument: 'x'
third("ABC")
Hello
def fourth(x):
    return x*10

fourth(10)
100
fourth(5)
50
def fourth(x):
    print("Hi")
    print("Hello")
    print("how r u")
    return x*10

fourth(10)
Hi
Hello
how r u
100
def fourth(x):
    print("Hi")
    return x*2
    print("Hello")

    
def fourth(x):
    print("Hi")
    return x**2
    print("Hello")

    
fourth(20)
Hi
400

====================== RESTART: C:/Users/SSPO/Desktop/Training/day6editor.py ======================
4def fourth(x):
    print("Hi")
    return x**2
    print("Hello")
    
SyntaxError: invalid decimal literal

====================== RESTART: C:/Users/SSPO/Desktop/Training/day6editor.py ======================
Hi
def fourth(x):
    print("Hi")
    return x**2
    print("Hello")

    
fourth(4)
Hi
16

====================== RESTART: C:/Users/SSPO/Desktop/Training/day6editor.py ======================

====================== RESTART: C:/Users/SSPO/Desktop/Training/day6editor.py ======================
def five(x,y,z):
    return x+y+z

five(5)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    five(5)
TypeError: five() missing 2 required positional arguments: 'y' and 'z'
five(5,0,4)
9
five(5,01,4)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
five(5,21,4)
30

====================== RESTART: C:/Users/SSPO/Desktop/Training/day6editor.py ======================

====================== RESTART: C:/Users/SSPO/Desktop/Training/day6editor.py ======================
6
def six(x,y,z):
    return x+y+z



six(x=5,y=4,z=2)
11
six(y=4,z=2,x=3)
9
six(y,z,x)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    six(y,z,x)
NameError: name 'y' is not defined
six(x,y,z)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    six(x,y,z)
NameError: name 'x' is not defined
six(11,5,4)
20
def seven(x,y,z=1):
    return x+y+z

seven(4,5)
10
seven(4,5,6)
15
def seven(x=1,y,z=1):
    return x+y+z
SyntaxError: non-default argument follows default argument
def seven(x,y=1,z):
    return x+y+z
SyntaxError: non-default argument follows default argument
def eight(*x):
    return x

eight()
()
eight(2)
(2,)
eight(2,3,4)
(2, 3, 4)
eight(2,3,)
(2, 3)
eight(2,3)
(2, 3)
def nine(**x):
    return x

nine
<function nine at 0x000000197F234CA0>
nine()
{}
nine(name='Bipul',email='bipul@gmail.com')
{'name': 'Bipul', 'email': 'bipul@gmail.com'}
nine(1)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    nine(1)
TypeError: nine() takes 0 positional arguments but 1 was given
nine(1='hi')
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
nine(a1='hi')
{'a1': 'hi'}
################## * = args ---> always gives tuple ########################3$
################## ** = kwargs --> always gives dictionary ###################

nine(n1=0,n2=[11,10,20]n3=['ab','xy'])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
nine(n1=0,n2=[11,10,20],n3=['ab','xy'])
{'n1': 0, 'n2': [11, 10, 20], 'n3': ['ab', 'xy']}
def bday(x):
    return print(f"Happy Birthday to you {x}")

bday("AKshat")
Happy Birthday to you AKshat
def bday(x):
    return print(f"Happy Birthday to you {x}")

bday("Bipul")
Happy Birthday to you Bipul
def bday(x):
    return print(f"Happy Birthday to you {x}. May God Bless you !!")

bday("Tejasvi")
Happy Birthday to you Tejasvi. May God Bless you !!
def myfun(x,y,z):
    return x+y+z

myfun(2,4,6)
12
myadd = lambda x,y,z:
    
SyntaxError: invalid syntax
myadd = lambda x,y,z: x+y+z
myadd(1,2,3)
6
import math
math.pi
3.141592653589793
math.sqrt(9)
3.0
math.pow(2,3)
8.0
int(math.pow(2,3))
8
math.fact(5)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    math.fact(5)
AttributeError: module 'math' has no attribute 'fact'
math.factorial(5)
120
import math as m
m.pi
3.141592653589793
m.sqrt(1000000000000000000.00)
1000000000.0
m.sqrt(100000000000000000)
316227766.01683795
from math import sqrt
sqrt(91)
9.539392014169456
import math as m
sqrt(91)
9.539392014169456
from math import sqrt
sqrt(81)
9.0
import datetime as dt
aaj_ki_date=dt.date.today()
print(aaj_ki_date)
2022-09-19
import calendar
print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

>>> print(calendar.month(2022,9))
   September 2022
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30

>>> print(calendar.calendar(2001:2022))
SyntaxError: invalid syntax
>>> print(calendar.month(2022))
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    print(calendar.month(2022))
TypeError: TextCalendar.formatmonth() missing 1 required positional argument: 'themonth'
>>> print(calendar.month(2022,3))
     March 2022
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

