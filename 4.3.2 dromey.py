marks = [78, 90, 85, 65, 70, 80, 92, 88, 75, 83, 72, 68, 90, 95, 87, 80, 85, 92, 76, 85, 95]
max = marks[0]
count = 0
for num in marks:
    if num>max:
        max = num
        count = 1
    elif num==max:
        count += 1
print(max)
print(count)