def check_empty_list(l):
    return all(not d for d in l)

print(check_empty_list([{}, {}, {}]))
print(check_empty_list([{1: 2}, {}, {}]))
