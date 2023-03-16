'''marks = [78, 90, 85, 65, 70, 80, 92, 88, 75, 83, 72, 68, 90, 95, 87, 80, 85, 92, 76, 85]
max =  marks[0]
list1 = []
for i in range(len(marks)):
    if marks[i]>max:
        max = marks[i]
        list1.append(max)
    if  max == marks[i]:
        max != marks[i]
        second_high = max
        
print(" maximum value: ",max)
print(list1)'''


def second_largest(arr):
    largest = arr[0]
    second = arr[0]
    for i in range (len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    for i in range (len(arr)):
        if arr[i]>second and arr[i] !=largest:
            second = arr[i]
    return second

arr = [78, 90, 85, 65, 70, 80, 92, 88, 75, 83, 72, 68, 90, 95, 87, 80, 85, 76, 85,99]
second_large = second_largest(arr)
print("second largest value : ",second_large)