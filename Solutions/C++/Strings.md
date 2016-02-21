###Strings  
###*Section Score: 20*  
####Strings  
*Score: 10*  
**Problem**  
You are given two strings, *a* and *b*, separated by a new line. Each string will consist of lower case Latin characters ('a'-'z').  
In the first line print two space-separated integers, representing the length of aa and bb respectively.  
In the second line print the string produced by concatenating *a* and *b* (*a+b*). 
In the third line print two strings separated by a space, *a'* and *b'*. *a'* and *b'* are the same as *a* and *b*, respectively, except that their first characters are swapped.  
**Sample Input**  
abcd  
ef  
**Sample Ouput**  
4 2  
abcdef  
ebcd af  


**Solution**  
```C++
#include <iostream>
#include <string>
using namespace std;

int main() {
   // Complete the program
  string s1,s2;
    char c;
    cin >> s1 >> s2;
    cout << s1.size() << " " << s2.size() << endl;
    cout << s1+s2 << endl;
    c=s1[0];
    s1[0]=s2[0];
    s2[0]=c;
    cout << s1 << " " << s2;
    return 0;
}
```  
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
