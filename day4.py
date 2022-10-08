Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1={'name':['akash','akshat','sunny'],
    'Age':[25,20,22]}
d1
{'name': ['akash', 'akshat', 'sunny'], 'Age': [25, 20, 22]}
type(d1)
<class 'dict'>
len(d1)
2
d1['name']
['akash', 'akshat', 'sunny']
d1['age']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d1['age']
KeyError: 'age'
d1['Age']
[25, 20, 22]

d1.keys()
dict_keys(['name', 'Age'])
d1.values()
dict_values([['akash', 'akshat', 'sunny'], [25, 20, 22]])
d1.items()
dict_items([('name', ['akash', 'akshat', 'sunny']), ('Age', [25, 20, 22])])
print(d1)
{'name': ['akash', 'akshat', 'sunny'], 'Age': [25, 20, 22]}
d1
{'name': ['akash', 'akshat', 'sunny'], 'Age': [25, 20, 22]}
d1['air':3]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d1['air':3]
TypeError: unhashable type: 'slice'
d1+\['air':3]
SyntaxError: unexpected character after line continuation character
d1+['air':3]
SyntaxError: invalid syntax
d1+{'air':3}
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d1+{'air':3}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

d1['ph_no']=[2223355,8855440,6789876]
d1
{'name': ['akash', 'akshat', 'sunny'], 'Age': [25, 20, 22], 'ph_no': [2223355, 8855440, 6789876]}
d1['ph_no']=[2223355,8855440,6789876]
d1
{'name': ['akash', 'akshat', 'sunny'], 'Age': [25, 20, 22], 'ph_no': [2223355, 8855440, 6789876]}
d1['name'][0]
'akash'
d1['name'][0::-1]
['akash']
d1['name'][::-1]
['sunny', 'akshat', 'akash']
d1['name'][0][::-1]
'hsaka'
d1['name'][0][::-1]
'hsaka'
d1['name'][0][::-1]
'hsaka'
d1['name'][0][::-1]
'hsaka'
d1['name'][0][::-1]
'hsaka'
d1['name'][0][::-1]
'hsaka'
d1['name'][0][::-1]
'hsaka'
d1['name'][0]='ajay'
d1
{'name': ['ajay', 'akshat', 'sunny'], 'Age': [25, 20, 22], 'ph_no': [2223355, 8855440, 6789876]}
d1['name'][3]='ajay'
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d1['name'][3]='ajay'
IndexError: list assignment index out of range
d1['name','Age','ph_no']=['asdf',24,3232323]
d1
{'name': ['ajay', 'akshat', 'sunny'], 'Age': [25, 20, 22], 'ph_no': [2223355, 8855440, 6789876], ('name', 'Age', 'ph_no'): ['asdf', 24, 3232323]}
del d1['name','Age','ph_no']
d1
{'name': ['ajay', 'akshat', 'sunny'], 'Age': [25, 20, 22], 'ph_no': [2223355, 8855440, 6789876]}
del d1['ph_no']
d1
{'name': ['ajay', 'akshat', 'sunny'], 'Age': [25, 20, 22]}
d1['name'].append('adsd')
d1
{'name': ['ajay', 'akshat', 'sunny', 'adsd'], 'Age': [25, 20, 22]}
d1['name'].remove('adsd')
d2
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d2
NameError: name 'd2' is not defined. Did you mean: 'd1'?
d2
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    d2
NameError: name 'd2' is not defined. Did you mean: 'd1'?
d1
{'name': ['ajay', 'akshat', 'sunny'], 'Age': [25, 20, 22]}
d1.get('email')
d1.get('name')
['ajay', 'akshat', 'sunny']
a=20
b='ML'
print(a,b)
20 ML
print(a,b)
20 ML
print(a,b,sep='               ')
20               ML
print(a,b,sep='@')
20@ML

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
20####ML

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
20####ML

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
20####ML

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
20####ML

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
20####ML

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
20####ML

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
20####ML

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
20
ML

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
20
ML
KeyboardInterrupt
a=1
a
1

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
20
ML
a=input("Enter Your
        
SyntaxError: unterminated string literal (detected at line 1)
a=input("Enter Your Name")
        
Enter Your Name Bipul
a
        
' Bipul'
a
        
' Bipul'
a
        
' Bipul'
a
        
a
        
' Bipul'
a
        
' Bipul'
a
        
' Bipul'
a
        
' Bipul'
a
        
' Bipul'
aq

a
        
' Bipul'
a
a=int(input("enter the number 1"))
        
enter the number 12
b=int(input("enter the number 2"))
        
enter the number 24


====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
enter the number 1a=int(input("enter the number 1"))
Traceback (most recent call last):
  File "C:/Users/SSPO/Desktop/Training/day4editor.py", line 1, in <module>
    a=int(input("enter the number 1"))
ValueError: invalid literal for int() with base 10: 'a=int(input("enter the number 1"))'

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
enter the number 15
enter the number 25

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
enter the number 15
enter the number 25
10

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
enter the number 15
enter the number 24
9
enter the number 16
enter the number 25
11

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
enter the number 15
enter the number 25
10
enter the number 15
enter the number 25
55
if:
        
SyntaxError: invalid syntax
if age=19:
        
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
if age==19:
                Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32\
KeyboardInterrupt
ifage<18:
        
SyntaxError: invalid syntax
if age<18:
        print("A gift")
if age>=18 and age<=20:
        
SyntaxError: invalid syntax

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
Enter age40
Sbko milega gift 

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
Enter age4
A gift

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
Enter age19
A gift
A task

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
Enter age100
A gift

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
Enter age100
Sbko milega gift 

age=int(input("Enter age"))
if age<18:
    print("A gift")
elif age>=18 and age<=20:
    print("A gift")
    print("A task")
else:
    print("Sbko milega gift ")

SyntaxError: multiple statements found while compiling a single statement
age=int(input("Enter age"))

if age<18:
    print("A gift")
elif age>=18 and age<=20:
    print("A gift")
    print("A task")
else:
    print("Sbko milega gift ")
    
SyntaxError: multiple statements found while compiling a single statement
age=int(input("Enter age"));
if age<18:
    print("A gift")
elif age>=18 and age<=20:
    print("A gift")
    print("A task")
else:
    print("Sbko milega gift ")

SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
Enter the day nameSATURDAY

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
Enter the day nameSaturday
Half day work

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
enter the number 15
enter the number 26
b

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
enter the number 15
enter the number 26
enter the number 34
b

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
enter the number 17
enter the number 23
enter the number 35
a

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
enter the number 18
enter the number 27
enter the number 31236

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
enter the number 14
enter the number 24
enter the number 356
c

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
runtime: 4.601 sec

====================== RESTART: C:/Users/SSPO/Desktop/Training/day4editor.py ======================
done: 1.80 sec.
[DEBUG ON]
[DEBUG OFF]
range(0,11)
range(0, 11)
list(range(0,11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(0,11,-1))
[]
list(range(0,11,2))
[0, 2, 4, 6, 8, 10]
list(range(0,11,9))
[0, 9]
list(range(0,100,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
list(range(1,101,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
list(range(2,101,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
print(range(0,11))
range(0, 11)
for i in range(100):
    print(i)

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>> tuple(list(range(1,101,2)))
(1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99)
