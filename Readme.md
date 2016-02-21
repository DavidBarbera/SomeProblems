#Report  

This is a report on the experience solving some problems around the net.	

There we go:  

| Domain                   | Score         |  
|--------------------------|---------------|  
| Algorithms                   | 120         |  
| C++                   | 55         |  
| Mathematics                   | 40         |  
| Python                   | 175         |  
| *Total*                   | *390*         |  
##Algorithms   
##*Domain Score: 120*  
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
##*Domain Score: 55*  
###Introduction  
###*Section Score: 55*  
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
##Mathematics   
##*Domain Score: 40*  
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
##Python   
##*Domain Score: 175*  
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
