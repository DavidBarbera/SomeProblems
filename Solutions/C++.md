##C++   
*##Domain Score: 55*  
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
