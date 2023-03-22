marks = [78, 90, 85, 65, 70, 80, 92, 88, 75, 83,
         72, 68, 90, 95, 87, 80, 85, 92, 76, 85, 95]
max = marks[0]
start = 0
list1 = []

end = len(marks)
for num in marks:
    if num > max:
        max = num
    index1 = marks.index(max, 0, end+1)

for i in range(0, len(marks)):
    if marks[i] == max:
        list1.append(i)
first_poistion = list1[0]
last_poisiotion = list1.pop()

print("maximum value: ", max)
print("max at index first occur :", index1)
print("max at last index last occur :", last_poisiotion)
