####Interchange two numbers   
*Score: 10*  
**Problem**  
You are given two integers. Store them into two variables and then exchange them. Print the two numbers.  
**Solution**  
```python
a = [int(raw_input()),int(raw_input())]
temp0= a[0]
temp1=a[1]
a[0] = temp1
a[1] = temp0

print a[0]
print a[1]
```   

