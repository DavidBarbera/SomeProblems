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
