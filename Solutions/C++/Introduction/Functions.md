####Functions  
*Score: 10*  
**Problem**  
You have to write a function *int max_of_four(int a, int b, int c, int d)* which reads four arguments and returns the greatest of them.

**Solution**  
```C++
#include <iostream>
#include <cstdio>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max(int a,int b) {
   
    if(a <= b) {
       return b;
    } else {
      return a;
    }
   
}

int max_of_four(int a, int b, int c, int d) {
    int max1, max2;
    max1 = max(a,b);
    max2 = max(c,d);
    
    return max(max1,max2);
}

int main() {
    int a, b, c, d,s;
    s=scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
```  
