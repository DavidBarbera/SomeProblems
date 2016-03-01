####Loop Invariant  
*Score: 30*  

**Problem**  
In the *InsertionSort* code below, there is an error. Can you fix it? Print the array only once, when it is fully sorted.  

**Solution**  
*Comments: Here the problem was in the loop condition, as it was forgetting to test the case when j=0, so replacing j>0 by j>=0, solved the issue.*  

```python
def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
print " ".join(map(str,ar))
```  
