####Pointer  
*Score: 10*  
**Problem**  
You have to complete the function *void update(int \*a,int \*b)*, which reads two integers as argument, and sets *a* with the sum of them, and *b* with the absolute difference of them.  

**Solution**  
```C++ 
#include <stdio.h>

void update(int *a,int *b) {
    int sum, diff;
    sum = (*a)+(*b);
    if((*a)>=(*b)){
        diff= (*a)-(*b);
    } else {
        diff=(*b)-(*a);
    }
    (*a)=sum;
    (*b)=diff;
    // Complete this function    
}

int main() {
    int a, b,s;
    int *pa = &a, *pb = &b;
    
    s=scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
```  
