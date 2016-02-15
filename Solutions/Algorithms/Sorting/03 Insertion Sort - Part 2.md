#### Insertion - Part 2
*Score: 30*  

**Problem:**  
In Insertion Sort Part 1, you sorted one element into an array. Using the same approach repeatedly, can you sort an entire unsorted array?

**Sample Input:**  
6  
1 4 3 5 6 2  

**Sample Output:**  
1 4 3 5 6 2  
1 3 4 5 6 2   
1 3 4 5 6 2   
1 3 4 5 6 2   
1 2 3 4 5 6   

**Solution:**  
```python
#!/bin/python

def insertionSort(ar):    
    for i in range(1,m):
        e=ar[i]
        k=i
        if(e<ar[k-1]):
            while (e<ar[k-1] and k>0):
                ar[k] = ar[k-1]
                #print ' '.join(map(str,ar))
                k-=1
            ar[k]=e
            print ' '.join(map(str,ar))
        else:
            print ' '.join(map(str,ar))
    return ""
       
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
```