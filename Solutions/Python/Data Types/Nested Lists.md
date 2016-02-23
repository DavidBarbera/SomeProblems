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
