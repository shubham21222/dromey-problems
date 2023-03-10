def reverse(list1):
    for i in range(len(list)):
        # j = i + 1
        x = list1[i]
        y = list1[-i-1]
        list1[i] = y
        list1[-i-1] = x


list = [1, 2, 3, 4, 5, 6, -3, 8, 9,12]
reverse(list)
print(list)