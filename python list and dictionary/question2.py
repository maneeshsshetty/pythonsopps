d = {0: 10, 1: 20}
print("Original Dictionary: ", d)
n = int(input("Enter number of key-value pairs: "))
for i in range(n):
    key = int(input("Enter key: "))
    value = int(input("Enter value: "))
    d[key] = value
print("final  Result: ", d)
