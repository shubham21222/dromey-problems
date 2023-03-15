marks = [78, 90, 85, 65, 70, 80, 92, 88, 75, 83, 72, 68, 90, 95, 87, 80, 85, 92, 76, 85, 65]

maximum = marks[0]
minimum = marks[0]
count_max = 0
count_min = 0

for i in range(0,len(marks)):
    if marks[i]>maximum:
        maximum = marks[i]
    elif marks[i] == maximum:    
        count_max += 1

for i in range (0,len(marks)):
    if marks[i]<minimum:
        minimum = marks[i]
    elif marks[i] == minimum:
        count_min = count_min+1

print("maximum is :",maximum)
print("minimum is :",minimum)
print("maximum repeat : ",count_max)
print("minimum repeat : ",count_min)
