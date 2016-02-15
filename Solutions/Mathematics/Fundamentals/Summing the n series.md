#### Summing the n series
*Score: 20*

**Problem**  
You are given a sequence whose *n<sup>th<\sup>* term is
Tn=n2-(n-1)2
Tn=n2-(n-1)2
You have to evaluate the series
Sn=T1+T2+T3+?+Tn
Sn=T1+T2+T3+?+Tn
Find Snmod(109+7)Snmod(109+7).

```python
#python 2
tests = int(raw_input().strip())

mod = 10**9 + 7

for l in xrange(tests):
    n=int(raw_input().strip())
    print (n**2) % mod  
```