###Fundamentals  
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
