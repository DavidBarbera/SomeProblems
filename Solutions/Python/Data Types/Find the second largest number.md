####Find the second largest number  
*Score: 10*  
**Problem**  
You are given *N* numbers. Store them in a list and find the second largest number.

**Sample Input**  
5  
2 3 6 6 5  
**Sample Output**  
5  

**Solution**  
```python
n=int(raw_input().strip())
a=raw_input().split()
l=map(int,a)

l.sort()
x=l.pop()
y=l.pop()
while( y>=x ):
    y=l.pop()

print y	
```  
