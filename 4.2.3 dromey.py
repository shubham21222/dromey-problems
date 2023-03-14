marks = [78, 90, 85, 65, 70, 80, 92, 88, 75, 83, 72, 68, 90, 95, 87, 80, 85, 92, 76, 85]
mean = sum(marks)/len(marks)
sorted_marks = sorted(marks)
mid = len(sorted_marks)//2
median = (sorted_marks[mid]+sorted_marks[~mid])
print("mean :",mean)
print("median :",median)
print(sorted_marks)