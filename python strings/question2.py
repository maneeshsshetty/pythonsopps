a = input("Enter the string: ")
di = {}
for i in a:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1
print(di)
        