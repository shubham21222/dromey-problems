list1  = [65, 65, 68, 70, 72, 75, 76, 78, 80, 80, 83, 85, 85, 85, 87, 88, 90, 90, 92, 92, 95]
list2 = []
for remove_duplicate in list1:
    if remove_duplicate not in list2:
        list2.append(remove_duplicate)

print(list2)
