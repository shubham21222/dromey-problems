list1 = [1,2,3,4,5,6,7,8]
list2 = []
for i in range (len(list1)):
    if i%2==0:
        list2.append(list1[i])
for i in range(len(list1)):
    if i%2!=0:
        list2.append(list1[i])
print(list2)
    
