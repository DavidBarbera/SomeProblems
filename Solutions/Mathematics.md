##Mathematics   
##*Domain Score: 60*  
###Summations and Algebra  
###*Section Score: 20*  
####Easy Sum  
*Score: 20*  
**Problem**  
Given 2 numbers N and m, sum the numbers from 1 up to N each mod m.  

**Sample input**  
3  *(numbers of test cases)*
10 5  *(N and m)*
10 3  
5 5  

**Sample Output**  
20  
10  
10  


**Solution**  
*Comments: Here is good to know that summation of integers from 1 to N is N(N+1)/2, with modules is a bit more cumbersome but if we consider each case we will avoid the program going lost in high number calculations and running out of time for the toughest test cases*
```python
Tests=int(raw_input())

for t in xrange(Tests):
    N,m=map(int,raw_input().split())
    #print N,m
    if( N<m ):
        print N*(N+1)/2
    elif (N==m):
        print N*(N-1)/2
    elif (N>m):
        if( N%m==0):
            d=N/m
            print d*(m*(m-1)/2)
        else:
            r = N%m
            d = (N - r)/m
            print d*(m*(m-1)/2)+(r*(r+1)/2)
```  
###Summations and Algebra  
###*Section Score: 20*  
####Easy Sum  
*Score: 20*  
**Problem**  
Given 2 numbers N and m, sum the numbers from 1 up to N each mod m.  

**Sample input**  
3  *(numbers of test cases)*
10 5  *(N and m)*
10 3  
5 5  

**Sample Output**  
20  
10  
10  


**Solution**  
*Comments: Here is good to know that summation of integers from 1 to N is N(N+1)/2, with modules is a bit more cumbersome but if we consider each case we will avoid the program going lost in high number calculations and running out of time for the toughest test cases*
```python
Tests=int(raw_input())

for t in xrange(Tests):
    N,m=map(int,raw_input().split())
    #print N,m
    if( N<m ):
        print N*(N+1)/2
    elif (N==m):
        print N*(N-1)/2
    elif (N>m):
        if( N%m==0):
            d=N/m
            print d*(m*(m-1)/2)
        else:
            r = N%m
            d = (N - r)/m
            print d*(m*(m-1)/2)+(r*(r+1)/2)
```  
