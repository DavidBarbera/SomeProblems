##C++   
##*Domain Score: 105*  
###Introduction  
###*Section Score: 85*  
####Operator Overloading
*Score: 25*

**Problem**  
You are given a main() function which takes a set of inputs to create two matrices and prints the result of their addition. You need to write the class Matrix which has a member a of type vector\<vector\<int\> \>. You also need to write a member function to overload the operator +. The function's job will be to add two objects of Matrix type and return the resultant Matrix.  

**Sample Input**  
1 	*(#Test cases)*  
2 2 	*(NxM, dimension of the two matrices to add)*  
2 2 2 2 *(one matrix)*	
1 2 3 4 *(the other matrix)* 

**Sample Output**  
3 4  
5 6  

**Solution:**  
```C++
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//-----------------------------------------------------------
// to code here:
class Matrix {
    public:
    vector<vector<int>> a;
    
    //Matrix();
    Matrix operator+(const Matrix& right){
        Matrix sum = *this;
        int n = right.a.size();
        int m = right.a[0].size();
        for(int i = 0; i<n;i++){
            for( int j = 0; j<m; j++){
                sum.a[i][j]=a[i][j]+right.a[i][j];
            }
        }
        return sum;
    }
    
};
//------------------------------------------------------------
int main () {
   int cases,k;
   cin >> cases;
   for(k=0;k<cases;k++) {
      Matrix x;
      Matrix y;
      Matrix result;
      int n,m,i,j;
      cin >> n >> m;
      for(i=0;i<n;i++) {
         vector<int> b;
         int num;
         for(j=0;j<m;j++) {
            cin >> num;
            b.push_back(num);
         }
         x.a.push_back(b);
      }
      for(i=0;i<n;i++) {
         vector<int> b;
         int num;
         for(j=0;j<m;j++) {
            cin >> num;
            b.push_back(num);
         }
         y.a.push_back(b);
      }
      result = x+y;
      for(i=0;i<n;i++) {
         for(j=0;j<m;j++) {
            cout << result.a[i][j] << " ";
         }
         cout << endl;
      }
   }  
   return 0;
}
```  
####Overload Operators  
*Score: 30*  
**Problem**  
You are given a class - *Complex*.
```C++
class Complex
{
public:
    int a,b;
};
```  
You need to overload operators *+* and *<<* for the *Complex* class.  

The operator *+* should add complex numbers according to the rules of complex addition.  
```c++
(a+ib)+(c+id) = (a+c) + i(b+d)  
```  

Overload the stream insertion operator *<<* to add "*a+ib*" to the stream:
```C++
cout<<c<<endl;
```  
**Solution**  
```C++
//Operator Overloading
#include<iostream>
using namespace std;
class Complex
{
public:
    int a,b;
    void input(string s)
    {
        int v1=0;
        int i=0;
        while(s[i]!='+')
        {
            v1=v1*10+s[i]-'0';
            i++;
        }
        while(s[i]==' ' || s[i]=='+'||s[i]=='i')
        {
            i++;
        }
        int v2=0;
        while(i<s.length())
        {
            v2=v2*10+s[i]-'0';
            i++;
        }
        a=v1;
        b=v2;
    }
Complex Complex::operator+(const Complex& rhs);
void Complex::operator<<(const Complex& rhs);
};
//Overload operators + and << for the class complex
//+ should add two complex numbers as (a+ib) + (c+id) = (a+c) + i(b+d)
//<< should print a complex number in the format "a+ib"

//There should be a prototype of both funcitons inside the class
//Complex Complex::operator+(const Complex& rhs);
//void Complex::operator<<(const Complex& rhs);

//both functions definitions outside
Complex Complex::operator+(const Complex& rhs){
    Complex sum = *this;
    sum.a= a + rhs.a;
    sum.b= b + rhs.b;
    
    return sum;
}
void Complex::operator<<(const Complex& rhs) {
    cout << rhs.a << "+i" << rhs.b;
        
}

int main()
{
    Complex x,y;
    string s1,s2;
    cin>>s1;
    cin>>s2;
    x.input(s1);
    y.input(s2);
    Complex z=x+y;
    cout<<z<<endl;
}

```  
####Variable Sized Arrays
*Score: 30*  

**Problem**  
You are given *N* integer sequences and *Q* queries. Each query is in the following format: "*a* *b*" where *a* denotes the index of the sequence, and *b* denotes the index of the element in that sequence. Your task is to find the value of the element described in each query.  

**Sample Input**  
2 2 *(N Q)*  
3 1 5 4 *(N sequences: size followed by elements)*  
5 1 2 8 9 3  
0 1 *(Q queries)*  
1 3  

**Sample Output**  
5  
9  

**Solution**  
```C++
int main(){
    int s;
    
    unsigned int N=0,Q=0,slength=0,a=0,b=1;
    cin >> N >> Q;
    unsigned int** seq = new unsigned int*[N];
    unsigned int** query = new unsigned int*[Q];
       
    int i = 0;
    int j = 0;
    for( i=0; i<N;i++){
        cin >> slength;
        seq[i]= new unsigned int[slength];
        for(j = 0; j<slength; j++){
            cin >> seq[i][j];
          }
      }
    for( i=0; i<Q;i++){
       query[i] = new unsigned int[2];
        cin >> query[i][a] >> query[i][b];
      }
    for( i=0; i<Q;i++) {
        a = query[i][0];
        b = query[i][1];
        cout << seq[a][b];
        cout << endl;
    }
  

    //free dynamic space in the heap
   for(i = 0; i<N;i++) {
           delete [] seq[i];
     }
    delete [] seq;
    for( i=0; i<Q;i++){
        delete [] query[i];
    }
    delete [] query;
      
	return 0;
}
```  
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
