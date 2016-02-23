![alt text](https://github.com/DavidBarbera/SomeProblems/tree/master/Reporting/HKR.png "Hackerrank")
#Report  

This is a report on the experience solving some problems around the net.	

There we go:  

| Domain                   | Score         |  
|--------------------------|---------------|  
| Algorithms                   | 120         |  
| C++                   | 175         |  
| Mathematics                   | 60         |  
| Python                   | 225         |  
| *Total*                   | *580*         |  
##Algorithms   
##*Domain Score: 120*  
###Sorting  
###*Section Score: 90*  
####01 Intro to Tutorial Challenges
*Score: 30*

**Problem**
This is a simple challenge to get things started. Given a sorted array (ar) and a number (V), can you print the index location of V in the array?

**Sample Input**  
4  
6  
1 4 5 7 9 12  

**Sample Output**  
1  

**Solution:**  
```python
#(in Python 2)
v, n = (int(input()) for _ in range(2))

print map(int,raw_input().split(' ')).index(v)
```  

#### 02 Insertion - Part 1
*Score: 30*  

**Problem**
Insert element into sorted list 
Given a sorted list with an unsorted number ee in the rightmost cell, can you write some simple code to insert ee into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. The goal of this challenge is to follow the correct order of insertion sort.

Guideline: You can copy the value of ee to a variable and consider its cell "empty". Since this leaves an extra cell empty on the right, you can shift everything over until VV can be inserted. This will create a duplicate of each value, but when you reach the right spot, you can replace it with ee.

**Sample Input:**  
5  
2 4 6 8 3  

**Sample Solution:**  
2 4 6 8 8  
2 4 6 6 8  
2 4 4 6 8  
2 3 4 6 8  

**Solution:** 
```python
#!/bin/python
def insertionSort(ar):    
    e=ar[m-1]
    k=m
    while (e<ar[k-2] and k>1):
        ar[k-1] = ar[k-2]
        print ' '.join(map(str,ar))
        k-=1
    ar[k-1]=e
    print ' '.join(map(str,ar))      
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
```  

#### Insertion - Part 2
*Score: 30*  

**Problem:**  
In Insertion Sort Part 1, you sorted one element into an array. Using the same approach repeatedly, can you sort an entire unsorted array?

**Sample Input:**  
6  
1 4 3 5 6 2  

**Sample Output:**  
1 4 3 5 6 2  
1 3 4 5 6 2   
1 3 4 5 6 2   
1 3 4 5 6 2   
1 2 3 4 5 6   

**Solution:**  
```python
#!/bin/python

def insertionSort(ar):    
    for i in range(1,m):
        e=ar[i]
        k=i
        if(e<ar[k-1]):
            while (e<ar[k-1] and k>0):
                ar[k] = ar[k-1]
                #print ' '.join(map(str,ar))
                k-=1
            ar[k]=e
            print ' '.join(map(str,ar))
        else:
            print ' '.join(map(str,ar))
    return ""
       
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
```  
###Strings  
###*Section Score: 30*  
#### 01 Pangrams
*Score: 30*

**Problem**  
Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)

After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

Given a sentence *s*, tell Roy if it is a pangram or not.

**Sample Input 1**  
We promptly judged antique ivory buckles for the next prize  

**Sample Input 2**  
We promptly judged antique ivory buckles for the prize  

**Sample Output 1**  
pangram  

**Sample Output 2**
not pangram  

**Solution:**  
```python
#!/bin/python
l=str(raw_input())

s=set(list(l.lower()))
s.discard(' ')

if len(s) == 26:
    print "pangram"
else:
    print "not pangram"
```  
##C++   
##*Domain Score: 175*  
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
##Mathematics   
##*Domain Score: 60*  
###Fundamentals  
###*Section Score: 40*  
####Sherlock and Permutations  
*Score: 20*  
**Problem:**  
Watson asks Sherlock: 
Given a string *S* of *N* 0's and *M* 1's, how many unique permutations of this string start with 1?  

Help Sherlock by printing the answer modulo (10<sup>9</sup>+7).  

**Sample Input:**
2  *(number of cases)*  
1 1  
2 3  

**Sample Output:**  
1  
6  

**Solution:**  

```python
import sys
import math
tests = int(raw_input().strip())
mod = 10**9 + 7

for i in xrange(tests):
    n,m = raw_input().strip().split(' ')
    n,m = [int(n),int(m)]
    result = (math.factorial(n+m-1)/(math.factorial(n)*math.factorial(m-1)) ) % mod
    print result
```  
#### Summing the n series
*Score: 20*

**Problem**  
You are given a sequence whose *n<sup>th</sup>* term is  
T<sub>n</sub>=n<sup>2</sup>-(n-1)<sup>2</sup>  

You have to evaluate the series  
S<sub>n</sub>=T<sub>1</sub>+T<sub>2</sub>+T<sub>3</sub>+...+T<sub>n</sub>  

Find S<sub>n</sub>mod(10<sup>9</sup>+7).  

**Sample Input:**  
2  
2  
1  

**Sample Output:**  
4  
1  

**Solution:**  
```python
#python 2
tests = int(raw_input().strip())

mod = 10**9 + 7

for l in xrange(tests):
    n=int(raw_input().strip())
    print (n**2) % mod  
```  
###Summations and Algebra  
###*Section Score: 20*  
####Easy Sum  
*Score: 20*  
**Problem**  
Given 2 numbers N and m, sum the numbers from 1 up to N each mod m.  

**Sample input**  
3  *(numbers of test cases)*
10 5  *(N and m)*
10 3  
5 5  

**Sample Output**  
20  
10  
10  


**Solution**  
*Comments: Here is good to know that summation of integers from 1 to N is N(N+1)/2, with modules is a bit more cumbersome but if we consider each case we will avoid the program going lost in high number calculations and running out of time for the toughest test cases*
```python
Tests=int(raw_input())

for t in xrange(Tests):
    N,m=map(int,raw_input().split())
    #print N,m
    if( N<m ):
        print N*(N+1)/2
    elif (N==m):
        print N*(N-1)/2
    elif (N>m):
        if( N%m==0):
            d=N/m
            print d*(m*(m-1)/2)
        else:
            r = N%m
            d = (N - r)/m
            print d*(m*(m-1)/2)+(r*(r+1)/2)
```  
##Python   
##*Domain Score: 225*  
###Data Types  
###*Section Score: 60*  
####Find the second largest number  
*Score: 10*  
**Problem**  
You are given *N* numbers. Store them in a list and find the second largest number.

**Sample Input**  
5  
2 3 6 6 5  
**Sample Output**  
5  

**Solution**  
```python
n=int(raw_input().strip())
a=raw_input().split()
l=map(int,a)

l.sort()
x=l.pop()
y=l.pop()
while( y>=x ):
    y=l.pop()

print y	
```  
####Lists Comprehensions  
*Score: 10*  
**Problem**  
You are given three integers *X,Y* and *Z* representing the dimensions of a cuboid. You have to print a list of all possible coordinates on a 3D grid where the sum of *X<sub>i</sub>i + Y<sub>i</sub> + Z<sub>i</sub>* is not equal to *N*. If *X=2*, the possible values of *X<sub>i</sub>* can be *0, 1 and 2*. The same applies to *Y* and *Z*.  

**Sample Input** (X Y Z and N)  
1  
1  
1  
2  
**Sample Output**  
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]  


**Solution**  
```python
a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
n=int(raw_input())

l=[[x,y,z] for x in range(0,a+1) for y in range(0,b+1) for z in range(0,c+1)]

ll=[[x,y,z] for [x,y,z] in l if x+y+z != n]

print ll
```  
####Lists  
*Score: 10*  
**Problem**  
You have to initialize your list *L = []* and follow the *N* commands given in *N* lines.  
**Sample Input**  
12  
insert 0 5  
insert 1 10  
insert 0 6  
print   
remove 6  
append 9  
append 1  
sort   
print  
pop  
reverse  
print  

**Sample Output**  
[6, 5, 10]  
[1, 5, 9, 10]  
[9, 5, 1]  

**Solution**  
```python
l=[]
n=int(raw_input().strip())
commandlist=['append','extend','insert','remove','pop','index','count','sort','reverse','print']


for i in xrange(n):
    commandline=[x for x in raw_input().split(" ")]
    parameters=len(commandline)
    
    if parameters == 3:
        command,a,b=commandline
    elif parameters == 2:
        command,a=commandline
    else:
        command = commandline.pop()
        
    cvalue = commandlist.index(command)
    
    if cvalue == 0:
        l.append(int(a))
    elif cvalue == 2:
        l.insert(int(a),int(b))
    elif cvalue == 3:
        l.remove(int(a))
    elif cvalue == 4:
        l.pop()
    elif cvalue == 5:
        l.index(int(a))
    elif cvalue == 6:
        l.count(int(a))
    elif cvalue == 7:
        l.sort()
    elif cvalue == 8:
        l.reverse()
    elif cvalue == 9:
        print l
```  
####Nested Lists  
*Score: 10*  
**Problem**  
Given the names and grades for each student in a Physics class of *N* students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.  

**Note:** If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.  


**Sample Input**  
5  
Harry  
37.21  
Berry  
37.21  
Tina  
37.2  
Akriti  
41  
Harsh  
39  

**Sample Output**  
Berry  
Harry  

**Solution**  
```python
n=int(raw_input())
students=[]
marks=[]

for x in xrange(n):
    l=[]
    l.append(raw_input())
    m=float(raw_input())
    marks.append(m)
    l.append(m)
    students.append(l)

marks.sort()
min = marks[0]
secondmin = min

for i in xrange(len(marks)):
    if (marks[i]!=min):
        secondmin = marks[i]
        break
names=[]
for list in students:
    if (list[1]==secondmin):
        names.append(list[0])

names.sort()

for t in names:
    print t
```  
####Sets - Symmetric Difference  
*Score: 10*  
**Problem**  
You are given *2* sets of integers *M* and *N*. You have to print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either *M* or *N* but do not exist in both.  
**Sample Input**  
4  
2 4 5 9  
4  
2 4 11 12  
**Sample Output**  
5  
9  
11  
12  

**Solution**  
```python
m=int(raw_input().strip())

a=raw_input()
lis=a.split()
intlis=map(int,lis)
s1=set(intlis)

n=int(raw_input().strip())
a=raw_input()
lis=a.split()
intlis=map(int,lis)
s2=set(intlis)

l1=list(s1.difference(s2))
l2=list(s2.difference(s1))

l1=l1+l2
l1.sort()

for i in l1:
    print i
```  
####Tuples  
*Score: 10*  
**Problem** 
You are given an integer *N* on one line. The next line contains *N* space separated integers. Create a tuple of those *N* integers. Let's call it *T*.  
Compute *hash(T)* and print it.

**Solution**  
```python
import __builtin__

n=int(raw_input().strip())
l = map(int,raw_input().split(' '))

tup = tuple(l)

print hash(tup)
```  
###Introduction  
###*Section Score: 125*  
####Arithmetic Operations  
*Score: 10*  
**Problem**  
Read two integers from STDIN and print three lines where:  
1. The first line contains the sum of the two numbers.  
2. The second line contains the difference of the two numbers (first - second).  
3. The third line contains the product of the two numbers.  

**Solution**
```python
a=int(raw_input())
b=int(raw_input())

print a+b
print a-b
print a*b
```  
####Finding the percentage   
*Score: 10*  
**Problem**  
You have a record of *N* students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer *N* followed by the names and marks for *N* students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.  
**Input Format**  
The first line contains the integer *N*, the number of students. The next *N* lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

**Sample Input**  
3  
Krishna 67 68 69  
Arjun 70 98 63  
Malika 52 56 60  
Malika  
**Sample Output**  
56.00  

**Solution**  
```python  
n = int(raw_input())

marks={}

for i in range(0,n):
    items =[x for x in raw_input().split(" ")]
    name, m1, m2, m3 = items
    marks[name]=float(m1),float(m2),float(m3)
    
name = str(raw_input())
a,b,c=marks[name]
d = (a+b+c)/3
print("{0:.2f}".format(d))
```  
####Hello World!  
*Score: 5*  
**Problem**  
The must first program in any language.  
**Solution**  
```python  
#write your code in next line. 
stringy = "Hello World!"
print stringy
```  
####Integers come in all sizes  
*Score: 10*  
**Problem**  
Read four numbers, *a*, *b*, *c*, and *d*, and print the result of *a*<sup>*b*</sup>*+c*<sup>*d*</sup>.  
**Solution**  
```python
a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
d=int(raw_input())

print pow(a,b)+pow(c,d)
```  
####Interchange two numbers   
*Score: 10*  
**Problem**  
You are given two integers. Store them into two variables and then exchange them. Print the two numbers.  
**Solution**  
```python
a = [int(raw_input()),int(raw_input())]
temp0= a[0]
temp1=a[1]
a[0] = temp1
a[1] = temp0

print a[0]
print a[1]
```   

####Loops  
*Score: 10*  
**Problem**  
Read an integer *N*. For all non-negative integers *i<N*, print *i<sup>2</sup>*.  
**Solution**  
```python  
a= int(raw_input())

for i in range(a):
 print pow(i,2)
```  
####Mod DivMod  
*Score: 10*  
**Problem**  
Read in two integers, *a* and *b*, and print three lines.  
The first line is the integer division *a//b* (Remember to import division from __future__).  
The second line is the result of the modulo operator: *a%b*.  
The third line prints the divmod of *a* and *b*.  
**Solution**  
```python  
from __future__ import division

a= int(raw_input())
b=int(raw_input())

print a//b
print a%b
print divmod(a,b)
```  

####Power - Mod Power  
*Score: 10*  
**Problem**  
You are given three integers: *a*, *b*, and *m*, respectively. Print two lines.  
The first line should print the result of *pow(a,b)*. The second line should print the result of *pow(a,b,m)*.  
**Solution**  
```python  
a=int(raw_input())
b=int(raw_input())
m=int(raw_input())

print pow(a,b)
print pow(a,b,m)
```  
####Print Function  
*Score: 20*  
**Problem**  
Read an integer *N*.  
Without using any string methods, try to print the following:  
*1,2,3.....N*  
**Sample Input**  
3  
**Sample Output**  
123  

**Solution**  
```python
from __future__ import print_function
import sys
n = int(raw_input())
    
map(lambda x:print(x,sep='',end='', file=sys.stdout),range(1,n+1))
```  
####Python Division  
*Score: 10*  
**Problem**  
Read two integers and print two lines. The first line should contain integer division, *a//b*. The second line should contain float division, *a/b*.  

You don't need to perform any rounding or formatting operations.  
**Solution**  
```python
from __future__ import division

a = int(raw_input())
b = int(raw_input())

print a//b
print a/b
```  
####Raw Input  
*Score: 10*  
**Problem**  
Read a string from the console and print it.  
**Solution**  
```python  
s = raw_input()
print s 
```  
####What's your name  
*Score: 10*  
**Problem**  
You are given the first and last name of a person. Your task is to read them and print the following:  
```python
Hello firstname lastname! You just delved into python.  
```  
**Input Format**  
The first line contains the first name, and the second line contains the last name.  

**Solution**  
```python
name = raw_input()
lastname = raw_input()

print "Hello %s %s! You just delved into python." %(name,lastname)
```  
###Math  
###*Section Score: 20*  
####Triangle Quest  
*Score: 20*  
**Problem** 
You are given a positive integer *N*. Print a numerical triangle of height *N-1* like the one below:  
1  
22  
333  
4444  
55555  
......  

**Solution**  
*Comments: here the trick was to realize how to genereate 1,11,111,1111, and so on.*
```python  
for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print i*(10**i-1)/9
```  
###Strings  
###*Section Score: 20*  
####String Split and Join  
*Score: 10*  
**Problem**  
You are given a string. Split the string on a *" "* (space) delimiter and join using a *-* hyphen.

**Solution**  
```python
a=raw_input().split(" ")

a="-".join(a)

print a
```  
####Swap Case  
*Score: 10*  
**Problem**  
You are given a string *S*. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

**Solution**  
*Comments: as pythonic as I could*  
```python
print raw_input().swapcase()
```  
