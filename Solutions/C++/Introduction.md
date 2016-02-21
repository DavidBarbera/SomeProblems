###Introduction  
###*Section Score: 155*  
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
####Conditional Statements  
*Score: 10*  
**Problem**  
You are given a positive integer, *n*,:  

If *1=n=9*, then print the English representation of it. That is "one" for *1*, "two" for *2*, and so on.
Otherwise print "Greater than 9" (without quotes).  


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
    int n=0;
    
    cin >> n;
    
    switch(n) {
        case 1: cout << "one";
            break;
        case 2: cout << "two";
            break;
        case 3: cout << "three";
            break;
        case 4: cout << "four";
            break;
        case 5: cout << "five";
            break;
        case 6: cout << "six";
            break;
        case 7: cout << "seven";
            break;
        case 8: cout << "eight";
            break;
        case 9: cout << "nine";
            break;
        default: cout << "Greater than 9";
    }
 
   return 0;
}
```  
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
####Hello World!  
*Score: 5*  
**Problem**  
The must first program in any language.

**Solution**  
```C++
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    printf("Hello, World!");
    return 0;
}
```  
####Input and Output  
*Score: 5*  
**Problem**  
Take three numbers as inputs and print the sum of those three numbers.

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
    int a,b,c;
    cin >> a >> b >> c;
    cout<< a+b+c;
    return 0;
}
```  
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
