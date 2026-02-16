phones = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
    {'make': 'Mi Max', 'model': 2 , 'color': 'Gold'}, 
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
print("Original:", phones)
sorted_phones = sorted(phones, key=lambda x: x['color'])

print("Sorted:", sorted_phones)
