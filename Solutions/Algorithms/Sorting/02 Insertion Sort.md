#### 02 Insertion - Part 1
*Score: 30*  

**Problem**
Insert element into sorted list 
Given a sorted list with an unsorted number ee in the rightmost cell, can you write some simple code to insert ee into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. The goal of this challenge is to follow the correct order of insertion sort.

Guideline: You can copy the value of ee to a variable and consider its cell "empty". Since this leaves an extra cell empty on the right, you can shift everything over until VV can be inserted. This will create a duplicate of each value, but when you reach the right spot, you can replace it with ee.

**Sample Input:**  
5  
2 4 6 8 3  

**Sample Solution:**  
2 4 6 8 8  
2 4 6 6 8  
2 4 4 6 8  
2 3 4 6 8  

**Solution:** 
```python
#!/bin/python
def insertionSort(ar):    
    e=ar[m-1]
    k=m
    while (e<ar[k-2] and k>1):
        ar[k-1] = ar[k-2]
        print ' '.join(map(str,ar))
        k-=1
    ar[k-1]=e
    print ' '.join(map(str,ar))      
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
```
