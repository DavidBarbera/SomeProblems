##Mathematics   
##*Domain Score: 90*  
###Fundamentals  
###*Section Score: 70*  
####Sherlock and Permutations  
*Score: 20*  
**Problem:**  
Watson asks Sherlock: 
Given a string *S* of *N* 0's and *M* 1's, how many unique permutations of this string start with 1?  

Help Sherlock by printing the answer modulo (10<sup>9</sup>+7).  

**Sample Input:**
2  *(number of cases)*  
1 1  
2 3  

**Sample Output:**  
1  
6  

**Solution:**  

```python
import sys
import math
tests = int(raw_input().strip())
mod = 10**9 + 7

for i in xrange(tests):
    n,m = raw_input().strip().split(' ')
    n,m = [int(n),int(m)]
    result = (math.factorial(n+m-1)/(math.factorial(n)*math.factorial(m-1)) ) % mod
    print result
```  
####Sumar and the floating rocks  
*Score: 30*  
**Problem**  
Famous wizard Sumar moonji kumaru is stuck in a huge room and has to save Hermione Granger from a monster. Kumaru is at location P1 given by integral coordinates (x1,y1) and Hermione is at location P2 given by integral coordinates (x2,y2). Sadly P1 and P2 are the only points at which floating rocks are present. Rest of the room is without floor and underneath is hot lava.  
Kumaru has to go from P1 to P2 but there are no floating rocks to walk on. Kumaru knows a spell that can make the rocks appear but only on the integral coordinates on the straight line joining P1 and P2.  
How many rocks can appear at locations (x,y) on the line segment between P1 and P2 (excluding P1 and P2) which satisfy the condition that both x and y are integers?  

**Solution**  
*Comments: tricky to understand but easy to implement.dy(=abs(y2-y1)) has to have common divisors with dx(=abs(x2-x1)) or viceversa to have an integral point on the joining segment. The maximum of them minus 1 is the total number of integral points on the joining segment.*
```python
import fractions

tests = int(raw_input())

for x in xrange(tests):
    x1,y1,x2,y2=map(int,raw_input().split())
    y = abs(y2-y1)
    x = abs(x2-x1)
    print fractions.gcd(x,y)-1
```  
#### Summing the n series
*Score: 20*

**Problem**  
You are given a sequence whose *n<sup>th</sup>* term is  
T<sub>n</sub>=n<sup>2</sup>-(n-1)<sup>2</sup>  

You have to evaluate the series  
S<sub>n</sub>=T<sub>1</sub>+T<sub>2</sub>+T<sub>3</sub>+...+T<sub>n</sub>  

Find S<sub>n</sub>mod(10<sup>9</sup>+7).  

**Sample Input:**  
2  
2  
1  

**Sample Output:**  
4  
1  

**Solution:**  
```python
#python 2
tests = int(raw_input().strip())

mod = 10**9 + 7

for l in xrange(tests):
    n=int(raw_input().strip())
    print (n**2) % mod  
```  
###Summations and Algebra  
###*Section Score: 20*  
####Easy Sum  
*Score: 20*  
**Problem**  
Given 2 numbers N and m, sum the numbers from 1 up to N each mod m.  

**Sample input**  
3  *(numbers of test cases)*
10 5  *(N and m)*
10 3  
5 5  

**Sample Output**  
20  
10  
10  


**Solution**  
*Comments: Here is good to know that summation of integers from 1 to N is N(N+1)/2, with modules is a bit more cumbersome but if we consider each case we will avoid the program going lost in high number calculations and running out of time for the toughest test cases*
```python
Tests=int(raw_input())

for t in xrange(Tests):
    N,m=map(int,raw_input().split())
    #print N,m
    if( N<m ):
        print N*(N+1)/2
    elif (N==m):
        print N*(N-1)/2
    elif (N>m):
        if( N%m==0):
            d=N/m
            print d*(m*(m-1)/2)
        else:
            r = N%m
            d = (N - r)/m
            print d*(m*(m-1)/2)+(r*(r+1)/2)
```  
