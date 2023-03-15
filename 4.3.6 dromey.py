'''marks = [78, 90, 85, 65, 70, 80, 92, 88, 75,
         83, 72, 68, 90, 95, 87, 80, 85, 92, 76, 85]
n = int(input("enter number whose poistion you want to find :"))
for i in range(0,len(marks)):
    if  n == marks[i]:
        print(i)
        
    if n !=marks[i]:
        print("value is not in a list ")
        break'''
    
def find_poisition(n,num):
    for i in range(len(marks)):
        if n[i]==num:
            return i

marks = [78, 90, 85, 65, 70, 80, 92, 88, 75,
         83, 72, 68, 90, 95, 87, 80, 85, 92, 76, 85]
n = int(input("enter number whose poistion you want to find :"))
find = find_poisition(marks,n)
print("poisition : ",find)