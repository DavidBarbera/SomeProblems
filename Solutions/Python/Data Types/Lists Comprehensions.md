####Lists Comprehensions  
*Score: 10*  
**Problem**  
You are given three integers *X,Y* and *Z* representing the dimensions of a cuboid. You have to print a list of all possible coordinates on a 3D grid where the sum of *X<sub>i</sub>i + Y<sub>i</sub> + Z<sub>i</sub>* is not equal to *N*. If *X=2*, the possible values of *X<sub>i</sub>* can be *0, 1 and 2*. The same applies to *Y* and *Z*.  

**Sample Input** (X Y Z and N)  
1  
1  
1  
2  
**Sample Output**  
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]  


**Solution**  
```python
a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
n=int(raw_input())

l=[[x,y,z] for x in range(0,a+1) for y in range(0,b+1) for z in range(0,c+1)]

ll=[[x,y,z] for [x,y,z] in l if x+y+z != n]

print ll
```  
