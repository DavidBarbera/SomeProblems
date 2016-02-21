####Basic Data Types  
*Score: 10*  
**Problem**  
Read and array of different types and return the elements, each in a new line.  

**Sample Input**  
3 444 12345678912345 a 334.23 14049.30493  
**Sample Output**  
3  
444  
12345678912345  
a  
334.23  
14049.30493  


**Solution**  
```C++
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int i=0;
    long int li=0;
    long long int ll=0;
    char c=' ';
    float f=0.0;
   double fl=0.0;
    int s;
    
    s=scanf("%d %ld %lld %c %f %lf",&i,&li,&ll,&c,&f,&fl);
    printf("%d\n%ld\n%lld\n%c\n%.2f\n%.5lf",i,li,ll,c,f,fl);
    
    
    return 0;
}
```  
