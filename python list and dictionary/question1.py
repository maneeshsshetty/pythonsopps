d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original dictionary: ", d)
sorted_d_asc = dict(sorted(d.items(), key=lambda item: item[1]))
print("Dictionary in ascending order by value: ", sorted_d_asc)
sorted_d_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print("Dictionary in descending order by value: ", sorted_d_desc)
