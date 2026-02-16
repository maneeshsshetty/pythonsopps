d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0,6:3}

result = {}

for key, value in d.items():
    if value not in result.values():
        result[key] = value
print(result)
