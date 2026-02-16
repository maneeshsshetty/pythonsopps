numbers = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("Original:", numbers)
result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))
print("Divisible by 19 or 13:", result)
