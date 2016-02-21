####Stringstream  
*Score: 10*  
**Problem**  
You have to complete the function *vector parseInts(string str)*. *str* will be a string consisting of comma-separated integers, and you have to return a vector of int representing the integers.
**Sample Input**  
23,4,56  
**Sample Output**  
23  
4  
56  

**Solution**  
```C++
#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
   // Complete this function
    char c = 'c';
    vector<int> arr;
    stringstream ss(str);
    int num;
    
    while( ss >> num >> c)
        arr.push_back(num);
    ss >> num;
    arr.push_back(num);    
     
    return arr;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}

```  
