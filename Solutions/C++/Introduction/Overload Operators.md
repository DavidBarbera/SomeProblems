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
