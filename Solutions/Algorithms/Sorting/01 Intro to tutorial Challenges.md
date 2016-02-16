####01 Intro to Tutorial Challenges
*Score: 30*

**Problem**
This is a simple challenge to get things started. Given a sorted array (ar) and a number (V), can you print the index location of V in the array?

**Sample Input**  
4  
6  
1 4 5 7 9 12  

**Sample Output**  
1  

**Solution:**  
```python
#(in Python 2)
v, n = (int(input()) for _ in range(2))

print map(int,raw_input().split(' ')).index(v)
```  

