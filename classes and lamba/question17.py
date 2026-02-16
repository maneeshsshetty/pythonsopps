# Lambda to sort matrix by row sum
matrix = [
    [1, 2, 3], 
    [2, 4, 5], 
    [1, 1, 1]
]
print("Original:", matrix)

# Sort based on sum of each row
sorted_matrix = sorted(matrix, key=lambda row: sum(row))

print("Sorted by row sum:", sorted_matrix)
