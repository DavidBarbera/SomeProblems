####Diagonal Difference  
*Score: 10*  
**Problem**  
Given a square matrix of size **N×N**, calculate the absolute difference between the sums of its diagonals.

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
