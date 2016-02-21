####Sets - Symmetric Difference  
*Score: 10*  
**Problem**  
You are given *2* sets of integers *M* and *N*. You have to print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either *M* or *N* but do not exist in both.  
**Sample Input**  
4  
2 4 5 9  
4  
2 4 11 12  
**Sample Output**  
5  
9  
11  
12  

**Solution**  
```python
m=int(raw_input().strip())

a=raw_input()
lis=a.split()
intlis=map(int,lis)
s1=set(intlis)

n=int(raw_input().strip())
a=raw_input()
lis=a.split()
intlis=map(int,lis)
s2=set(intlis)

l1=list(s1.difference(s2))
l2=list(s2.difference(s1))

l1=l1+l2
l1.sort()

for i in l1:
    print i
```  
