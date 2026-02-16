def remove1(str1,n):
    str2 =[]
    for i in range(len(str1)):
        if i+1 ==n:
            pass
        else :
            str2.append(str1[i])
    return " ".join(str2)
str1=input("enter the string")
n=int(input("enter the position "))
result=remove1(str1,n)
print(result)
            
            
        
        
        