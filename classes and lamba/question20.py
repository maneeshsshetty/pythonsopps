
mixed = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
print("Original:", mixed)
mixed.sort(key=lambda x: (isinstance(x, str), x))

print("Sorted:", mixed)
