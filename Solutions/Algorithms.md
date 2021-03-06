##Algorithms   
##*Domain Score: 205*  
###Dynamic Programming  
###*Section Score: 45*  
####Fibonacci Modified  
*Score: 45*  
**Problem**  
Given three integers **A**, **B** and **N**, such that the first two terms of the series (1st and 2nd terms) are **A** and **B** respectively, compute the Nth term of the series.  
Where the series is defined recursively:  
T<sub>n+2</sub>=(T<sub>n+1</sub>)<sup>2</sup> + T<sub>n</sub>  


**Solution**  
*Comments: easiest way is to define a recursive function.*
```python
a,b,n = map(int, raw_input().split())

def term(i):
    if( i == 1 ):
        return b
    elif(i==0):
        return a
    else:
        return term(i-1)**2+term(i-2)
    
print term(n-1)
```  
###Sorting  
###*Section Score: 120*  
####01 Intro to Tutorial Challenges
*Score: 30*

**Problem**
This is a simple challenge to get things started. Given a sorted array (ar) and a number (V), can you print the index location of V in the array?

**Sample Input**  
4  
6  
1 4 5 7 9 12  

**Sample Output**  
1  

**Solution:**  
```python
#(in Python 2)
v, n = (int(input()) for _ in range(2))

print map(int,raw_input().split(' ')).index(v)
```  

#### 02 Insertion - Part 1
*Score: 30*  

**Problem**
Insert element into sorted list 
Given a sorted list with an unsorted number ee in the rightmost cell, can you write some simple code to insert ee into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. The goal of this challenge is to follow the correct order of insertion sort.

Guideline: You can copy the value of ee to a variable and consider its cell "empty". Since this leaves an extra cell empty on the right, you can shift everything over until VV can be inserted. This will create a duplicate of each value, but when you reach the right spot, you can replace it with ee.

**Sample Input:**  
5  
2 4 6 8 3  

**Sample Solution:**  
2 4 6 8 8  
2 4 6 6 8  
2 4 4 6 8  
2 3 4 6 8  

**Solution:** 
```python
#!/bin/python
def insertionSort(ar):    
    e=ar[m-1]
    k=m
    while (e<ar[k-2] and k>1):
        ar[k-1] = ar[k-2]
        print ' '.join(map(str,ar))
        k-=1
    ar[k-1]=e
    print ' '.join(map(str,ar))      
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
```  

#### Insertion - Part 2
*Score: 30*  

**Problem:**  
In Insertion Sort Part 1, you sorted one element into an array. Using the same approach repeatedly, can you sort an entire unsorted array?

**Sample Input:**  
6  
1 4 3 5 6 2  

**Sample Output:**  
1 4 3 5 6 2  
1 3 4 5 6 2   
1 3 4 5 6 2   
1 3 4 5 6 2   
1 2 3 4 5 6   

**Solution:**  
```python
#!/bin/python

def insertionSort(ar):    
    for i in range(1,m):
        e=ar[i]
        k=i
        if(e<ar[k-1]):
            while (e<ar[k-1] and k>0):
                ar[k] = ar[k-1]
                #print ' '.join(map(str,ar))
                k-=1
            ar[k]=e
            print ' '.join(map(str,ar))
        else:
            print ' '.join(map(str,ar))
    return ""
       
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
```  
####Loop Invariant  
*Score: 30*  

**Problem**  
In the *InsertionSort* code below, there is an error. Can you fix it? Print the array only once, when it is fully sorted.  

**Solution**  
*Comments: Here the problem was in the loop condition, as it was forgetting to test the case when j=0, so replacing j>0 by j>=0, solved the issue.*  

```python
def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
print " ".join(map(str,ar))
```  
###Strings  
###*Section Score: 30*  
#### 01 Pangrams
*Score: 30*

**Problem**  
Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)

After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

Given a sentence *s*, tell Roy if it is a pangram or not.

**Sample Input 1**  
We promptly judged antique ivory buckles for the next prize  

**Sample Input 2**  
We promptly judged antique ivory buckles for the prize  

**Sample Output 1**  
pangram  

**Sample Output 2**
not pangram  

**Solution:**  
```python
#!/bin/python
l=str(raw_input())

s=set(list(l.lower()))
s.discard(' ')

if len(s) == 26:
    print "pangram"
else:
    print "not pangram"
```  
###Warmup  
###*Section Score: 10*  
####Diagonal Difference  
*Score: 10*  
**Problem**  
Given a square matrix of size **N�N**, calculate the absolute difference between the sums of its diagonals.

**Solution**  
```python
#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    
diag1=0
diag2=0
for i in xrange(n):
    diag1 += a[i][i]
    diag2 += a[i][n-i-1]
    
print abs(diag1-diag2)
```  
