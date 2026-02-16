def count_range_in_list(li, min):
    ctr = 0
    for x in li:
        if min <= x :
            ctr += 1
    return ctr
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 99]
print(count_range_in_list(list1, 30))

