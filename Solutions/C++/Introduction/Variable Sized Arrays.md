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