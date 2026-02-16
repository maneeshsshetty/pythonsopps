# Lambda to sort mixed list
mixed = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
print("Original:", mixed)

# Sort: numbers first, then strings
# We use a tuple key: (is_string?, value)
# 0 is number, 1 is string. So numbers come first.
mixed.sort(key=lambda x: (isinstance(x, str), x))

print("Sorted:", mixed)
