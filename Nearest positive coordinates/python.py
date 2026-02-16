def convert_to_positive(coords):
    if not coords:
        return []
    all_values = [val for point in coords for val in point]
    min_val = min(all_values)
    shift = 0
    if min_val < 0:
        shift = abs(min_val)
    new_coords = [(x + shift, y + shift) for x, y in coords]
    return new_coords
input_coords = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
output_coords = convert_to_positive(input_coords)
print("Input :", input_coords)
print("Output :", output_coords)
