####For Loop  
*Score: 10*  
**Problem** 
You will be given two positive integers, *a* and *b* (*a=b*), separated by a newline.  
For each integer n in [a,b] (so all numbers in that range):  
*If *1=n=9*, then print the English representation of it. That is "one" for 1, "two" for 2, and so on.  
*Else if *n>9* and it is even, then print "even".  
*Else if *n>9* and it is odd, then print "odd".  


**Solution**  
```C++
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a,b;
    cin >> a;
    cin >> b;
    

    for(int n = a; n <= b; n++ ) {
        //printf("%i\n",n);

    if( (n)>=1 && (n)<=b) {
    switch(n) {
        case 1: cout << "one\n";
            break;
        case 2: cout << "two\n";
            break;
        case 3: cout << "three\n";
            break;
        case 4: cout << "four\n";
            break;
        case 5: cout << "five\n";
            break;
        case 6: cout << "six\n";
            break;
        case 7: cout << "seven\n";
            break;
        case 8: cout << "eight\n";
            break;
        case 9: cout << "nine\n";
            break;
        default: if((n)%2==0) {
                 cout << "even\n";
                  } else {
                 cout << "odd\n";
                  }
             }
    } 
    }
    return 0;
}
```  
