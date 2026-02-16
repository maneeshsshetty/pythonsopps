held=int(input("enter the no. of classes held: \n"))
attended=int(input("enter the no. of classes attended: \n"))
attendance=(attended/held)*100
print("your attendance:",attendance,"%")
if (attendance>75):
    print("you are allowed to write the exam")
else:
    print("you are not allowed to write the exam")