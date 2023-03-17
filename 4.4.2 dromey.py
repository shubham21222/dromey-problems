def remove_duplicate(arr,k):
    first = arr[0]
    count = 1
    result = [first]
    for  i in range (0,len(arr)):
        if arr[i]==first:
            count +=1 
            if count <=k:
                result.append(first)
        else :
            first = arr[i]
            count = 1
            result.append(first)
    
    return result

list1  = [65, 65, 68, 70, 72, 75, 76, 78, 80, 80, 83, 85, 85, 85, 87, 88, 90, 90, 92, 92, 95]

print(remove_duplicate(list1,0))