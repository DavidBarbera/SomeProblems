##Python   
##*Domain Score: 225*  
###Data Types  
###*Section Score: 60*  
####Find the second largest number  
*Score: 10*  
**Problem**  
You are given *N* numbers. Store them in a list and find the second largest number.

**Sample Input**  
5  
2 3 6 6 5  
**Sample Output**  
5  

**Solution**  
```python
n=int(raw_input().strip())
a=raw_input().split()
l=map(int,a)

l.sort()
x=l.pop()
y=l.pop()
while( y>=x ):
    y=l.pop()

print y	
```  
####Lists Comprehensions  
*Score: 10*  
**Problem**  
You are given three integers *X,Y* and *Z* representing the dimensions of a cuboid. You have to print a list of all possible coordinates on a 3D grid where the sum of *X<sub>i</sub>i + Y<sub>i</sub> + Z<sub>i</sub>* is not equal to *N*. If *X=2*, the possible values of *X<sub>i</sub>* can be *0, 1 and 2*. The same applies to *Y* and *Z*.  

**Sample Input** (X Y Z and N)  
1  
1  
1  
2  
**Sample Output**  
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]  


**Solution**  
```python
a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
n=int(raw_input())

l=[[x,y,z] for x in range(0,a+1) for y in range(0,b+1) for z in range(0,c+1)]

ll=[[x,y,z] for [x,y,z] in l if x+y+z != n]

print ll
```  
####Lists  
*Score: 10*  
**Problem**  
You have to initialize your list *L = []* and follow the *N* commands given in *N* lines.  
**Sample Input**  
12  
insert 0 5  
insert 1 10  
insert 0 6  
print   
remove 6  
append 9  
append 1  
sort   
print  
pop  
reverse  
print  

**Sample Output**  
[6, 5, 10]  
[1, 5, 9, 10]  
[9, 5, 1]  

**Solution**  
```python
l=[]
n=int(raw_input().strip())
commandlist=['append','extend','insert','remove','pop','index','count','sort','reverse','print']


for i in xrange(n):
    commandline=[x for x in raw_input().split(" ")]
    parameters=len(commandline)
    
    if parameters == 3:
        command,a,b=commandline
    elif parameters == 2:
        command,a=commandline
    else:
        command = commandline.pop()
        
    cvalue = commandlist.index(command)
    
    if cvalue == 0:
        l.append(int(a))
    elif cvalue == 2:
        l.insert(int(a),int(b))
    elif cvalue == 3:
        l.remove(int(a))
    elif cvalue == 4:
        l.pop()
    elif cvalue == 5:
        l.index(int(a))
    elif cvalue == 6:
        l.count(int(a))
    elif cvalue == 7:
        l.sort()
    elif cvalue == 8:
        l.reverse()
    elif cvalue == 9:
        print l
```  
####Nested Lists  
*Score: 10*  
**Problem**  
Given the names and grades for each student in a Physics class of *N* students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.  

**Note:** If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.  


**Sample Input**  
5  
Harry  
37.21  
Berry  
37.21  
Tina  
37.2  
Akriti  
41  
Harsh  
39  

**Sample Output**  
Berry  
Harry  

**Solution**  
```python
n=int(raw_input())
students=[]
marks=[]

for x in xrange(n):
    l=[]
    l.append(raw_input())
    m=float(raw_input())
    marks.append(m)
    l.append(m)
    students.append(l)

marks.sort()
min = marks[0]
secondmin = min

for i in xrange(len(marks)):
    if (marks[i]!=min):
        secondmin = marks[i]
        break
names=[]
for list in students:
    if (list[1]==secondmin):
        names.append(list[0])

names.sort()

for t in names:
    print t
```  
####Sets - Symmetric Difference  
*Score: 10*  
**Problem**  
You are given *2* sets of integers *M* and *N*. You have to print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either *M* or *N* but do not exist in both.  
**Sample Input**  
4  
2 4 5 9  
4  
2 4 11 12  
**Sample Output**  
5  
9  
11  
12  

**Solution**  
```python
m=int(raw_input().strip())

a=raw_input()
lis=a.split()
intlis=map(int,lis)
s1=set(intlis)

n=int(raw_input().strip())
a=raw_input()
lis=a.split()
intlis=map(int,lis)
s2=set(intlis)

l1=list(s1.difference(s2))
l2=list(s2.difference(s1))

l1=l1+l2
l1.sort()

for i in l1:
    print i
```  
####Tuples  
*Score: 10*  
**Problem** 
You are given an integer *N* on one line. The next line contains *N* space separated integers. Create a tuple of those *N* integers. Let's call it *T*.  
Compute *hash(T)* and print it.

**Solution**  
```python
import __builtin__

n=int(raw_input().strip())
l = map(int,raw_input().split(' '))

tup = tuple(l)

print hash(tup)
```  
###Introduction  
###*Section Score: 125*  
####Arithmetic Operations  
*Score: 10*  
**Problem**  
Read two integers from STDIN and print three lines where:  
1. The first line contains the sum of the two numbers.  
2. The second line contains the difference of the two numbers (first - second).  
3. The third line contains the product of the two numbers.  

**Solution**
```python
a=int(raw_input())
b=int(raw_input())

print a+b
print a-b
print a*b
```  
####Finding the percentage   
*Score: 10*  
**Problem**  
You have a record of *N* students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer *N* followed by the names and marks for *N* students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.  
**Input Format**  
The first line contains the integer *N*, the number of students. The next *N* lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

**Sample Input**  
3  
Krishna 67 68 69  
Arjun 70 98 63  
Malika 52 56 60  
Malika  
**Sample Output**  
56.00  

**Solution**  
```python  
n = int(raw_input())

marks={}

for i in range(0,n):
    items =[x for x in raw_input().split(" ")]
    name, m1, m2, m3 = items
    marks[name]=float(m1),float(m2),float(m3)
    
name = str(raw_input())
a,b,c=marks[name]
d = (a+b+c)/3
print("{0:.2f}".format(d))
```  
####Hello World!  
*Score: 5*  
**Problem**  
The must first program in any language.  
**Solution**  
```python  
#write your code in next line. 
stringy = "Hello World!"
print stringy
```  
####Integers come in all sizes  
*Score: 10*  
**Problem**  
Read four numbers, *a*, *b*, *c*, and *d*, and print the result of *a*<sup>*b*</sup>*+c*<sup>*d*</sup>.  
**Solution**  
```python
a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
d=int(raw_input())

print pow(a,b)+pow(c,d)
```  
####Interchange two numbers   
*Score: 10*  
**Problem**  
You are given two integers. Store them into two variables and then exchange them. Print the two numbers.  
**Solution**  
```python
a = [int(raw_input()),int(raw_input())]
temp0= a[0]
temp1=a[1]
a[0] = temp1
a[1] = temp0

print a[0]
print a[1]
```   

####Loops  
*Score: 10*  
**Problem**  
Read an integer *N*. For all non-negative integers *i<N*, print *i<sup>2</sup>*.  
**Solution**  
```python  
a= int(raw_input())

for i in range(a):
 print pow(i,2)
```  
####Mod DivMod  
*Score: 10*  
**Problem**  
Read in two integers, *a* and *b*, and print three lines.  
The first line is the integer division *a//b* (Remember to import division from __future__).  
The second line is the result of the modulo operator: *a%b*.  
The third line prints the divmod of *a* and *b*.  
**Solution**  
```python  
from __future__ import division

a= int(raw_input())
b=int(raw_input())

print a//b
print a%b
print divmod(a,b)
```  

####Power - Mod Power  
*Score: 10*  
**Problem**  
You are given three integers: *a*, *b*, and *m*, respectively. Print two lines.  
The first line should print the result of *pow(a,b)*. The second line should print the result of *pow(a,b,m)*.  
**Solution**  
```python  
a=int(raw_input())
b=int(raw_input())
m=int(raw_input())

print pow(a,b)
print pow(a,b,m)
```  
####Print Function  
*Score: 20*  
**Problem**  
Read an integer *N*.  
Without using any string methods, try to print the following:  
*1,2,3.....N*  
**Sample Input**  
3  
**Sample Output**  
123  

**Solution**  
```python
from __future__ import print_function
import sys
n = int(raw_input())
    
map(lambda x:print(x,sep='',end='', file=sys.stdout),range(1,n+1))
```  
####Python Division  
*Score: 10*  
**Problem**  
Read two integers and print two lines. The first line should contain integer division, *a//b*. The second line should contain float division, *a/b*.  

You don't need to perform any rounding or formatting operations.  
**Solution**  
```python
from __future__ import division

a = int(raw_input())
b = int(raw_input())

print a//b
print a/b
```  
####Raw Input  
*Score: 10*  
**Problem**  
Read a string from the console and print it.  
**Solution**  
```python  
s = raw_input()
print s 
```  
####What's your name  
*Score: 10*  
**Problem**  
You are given the first and last name of a person. Your task is to read them and print the following:  
```python
Hello firstname lastname! You just delved into python.  
```  
**Input Format**  
The first line contains the first name, and the second line contains the last name.  

**Solution**  
```python
name = raw_input()
lastname = raw_input()

print "Hello %s %s! You just delved into python." %(name,lastname)
```  
###Math  
###*Section Score: 20*  
####Triangle Quest  
*Score: 20*  
**Problem** 
You are given a positive integer *N*. Print a numerical triangle of height *N-1* like the one below:  
1  
22  
333  
4444  
55555  
......  

**Solution**  
*Comments: here the trick was to realize how to genereate 1,11,111,1111, and so on.*
```python  
for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print i*(10**i-1)/9
```  
###Strings  
###*Section Score: 20*  
####String Split and Join  
*Score: 10*  
**Problem**  
You are given a string. Split the string on a *" "* (space) delimiter and join using a *-* hyphen.

**Solution**  
```python
a=raw_input().split(" ")

a="-".join(a)

print a
```  
####Swap Case  
*Score: 10*  
**Problem**  
You are given a string *S*. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

**Solution**  
*Comments: as pythonic as I could*  
```python
print raw_input().swapcase()
```  
