####Mod DivMod  
*Score: 10*  
**Problem**  
Read in two integers, *a* and *b*, and print three lines.  
The first line is the integer division *a//b* (Remember to import division from __future__).  
The second line is the result of the modulo operator: *a%b*.  
The third line prints the divmod of *a* and *b*.  
**Solution**  
```python  
from __future__ import division

a= int(raw_input())
b=int(raw_input())

print a//b
print a%b
print divmod(a,b)
```  

