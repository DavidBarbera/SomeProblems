###Math  
###*Section Score: 20*  
####Triangle Quest  
*Score: 20*  
**Problem** 
You are given a positive integer *N*. Print a numerical triangle of height *N-1* like the one below:  
1  
22  
333  
4444  
55555  
......  

**Solution**  
*Comments: here the trick was to realize how to genereate 1,11,111,1111, and so on.*
```python  
for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print i*(10**i-1)/9
```  
