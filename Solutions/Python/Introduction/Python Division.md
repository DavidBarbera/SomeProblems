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
