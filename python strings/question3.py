s = input("enter the string")
if (len(s)>1):
    a=list(s)
    b=s[0:2]
    c=s[-1:-3:-1]
    d=c[-1:-3:-1]
    e=b+d
    print(e)
else:
    print("string should be greater then 1")

