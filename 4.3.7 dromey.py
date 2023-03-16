def comparing(arr):
    maximum = arr[0]
    for i in range (len(arr)):
        if arr[i]>maximum:
            maximum = arr[i]
        if arr[i] >= maximum:
            
            print("the maximum number on a list is : " ,maximum)  
    return maximum
arr1 = [78, 85, 65, 70, 80, 92, 88, 75,
         83, 72, 68, 90, 95, 87, 80, 85, 92, 76, 85]
comparing(arr1)



'''def comparing(arr):
    maximum = arr[0]
    maximum2 = arr[0]
    for i in range (len(arr)):
        for j in range (len(arr)):
            if arr[j]>=arr[i]:
                maximum = arr[j]
            if maximum >= maximum2:
                maximum2 = maximum
    print("The maximum number in an array : ",maximum2)
    return maximum
arr1 = [78, 90, 85, 65, 70, 80, 92, 88, 75,
         83, 72, 68, 90, 95, 87, 80, 85, 92, 76, 85]
comparing(arr1)'''