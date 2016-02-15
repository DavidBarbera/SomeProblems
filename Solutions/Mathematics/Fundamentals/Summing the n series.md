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