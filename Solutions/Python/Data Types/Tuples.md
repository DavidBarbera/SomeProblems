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
