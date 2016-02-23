####Sumar and the floating rocks  
*Score: 30*  
**Problem**  
Famous wizard Sumar moonji kumaru is stuck in a huge room and has to save Hermione Granger from a monster. Kumaru is at location P1 given by integral coordinates (x1,y1) and Hermione is at location P2 given by integral coordinates (x2,y2). Sadly P1 and P2 are the only points at which floating rocks are present. Rest of the room is without floor and underneath is hot lava.  
Kumaru has to go from P1 to P2 but there are no floating rocks to walk on. Kumaru knows a spell that can make the rocks appear but only on the integral coordinates on the straight line joining P1 and P2.  
How many rocks can appear at locations (x,y) on the line segment between P1 and P2 (excluding P1 and P2) which satisfy the condition that both x and y are integers?  

**Solution**  
*Comments: tricky to understand but easy to implement.dy(=abs(y2-y1)) has to have common divisors with dx(=abs(x2-x1)) or viceversa to have an integral point on the joining segment. The maximum of them minus 1 is the total number of integral points on the joining segment.*
```python
import fractions

tests = int(raw_input())

for x in xrange(tests):
    x1,y1,x2,y2=map(int,raw_input().split())
    y = abs(y2-y1)
    x = abs(x2-x1)
    print fractions.gcd(x,y)-1
```  
