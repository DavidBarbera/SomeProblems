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
