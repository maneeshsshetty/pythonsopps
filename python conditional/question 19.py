mixed = [1, 'apple', 2.5, 'banana', 3, 4.0, 'cherry', 7]
ints = [x for x in mixed if isinstance(x, int) ]
floats = [x for x in mixed if isinstance(x, float)]
strings = [x for x in mixed if isinstance(x, str)]

print("Original list:", mixed)
print("Integers:", ints)
print("Floats:", floats)
print("Strings:", strings)