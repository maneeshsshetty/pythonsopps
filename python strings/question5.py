s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
result = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
print(result)