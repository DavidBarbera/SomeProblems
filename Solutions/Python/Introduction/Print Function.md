####Print Function  
*Score: 20*  
**Problem**  
Read an integer *N*.  
Without using any string methods, try to print the following:  
*1,2,3.....N*  
**Sample Input**  
3  
**Sample Output**  
123  

**Solution**  
```python
from __future__ import print_function
import sys
n = int(raw_input())
    
map(lambda x:print(x,sep='',end='', file=sys.stdout),range(1,n+1))
```  
