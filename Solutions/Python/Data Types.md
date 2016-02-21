###Data Types  
###*Section Score: 50*  
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
