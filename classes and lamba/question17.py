
matrix = [
    [1, 2, 3], 
    [2, 4, 5], 
    [1, 1, 1]
]
print("Original:", matrix)


sorted_matrix = sorted(matrix, key=lambda row: sum(row))

print("Sorted by row sum:", sorted_matrix)
