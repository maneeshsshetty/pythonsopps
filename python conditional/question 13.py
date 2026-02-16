n=int(input("enter the number of value"))
val=[]
print(f"enter the {n} values")
for i in range(n):
    a=int(input())
    val.append(a)
print(val)
sum1=int(sum(val))
print(sum1)
avg=sum1/n
print(f"average of {n} numbers are :",avg)