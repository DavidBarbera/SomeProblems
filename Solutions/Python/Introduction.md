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
s
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
