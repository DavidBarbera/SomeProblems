####Arrays Introduction  
*Score: 10*  
**Problem**  
You'll be an given array of *N* integers and you have to print the integers in the reverse order.

**Solution**  
```C++
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,a,s;
    int arr[1000];
    cin >> n;
    for(int i=0;i<n;i++) {
        s=scanf("%d",&a);
        arr[i]=a;
    }
    for(int i=n-1;i>=0;i--)
        printf("%d ",arr[i]);
    
    return 0;
}

```  
