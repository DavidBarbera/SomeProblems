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
