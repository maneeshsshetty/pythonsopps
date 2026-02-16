i=input("enter the string")
a=i[0]
b=i[1:]
lst=[]
lst.append(a)
for i in b:
    if i==a:
        lst.append("$")
    else:
        lst.append(i)
c=" ".join(lst)
print(c)
        
        
