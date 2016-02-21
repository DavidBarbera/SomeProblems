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
