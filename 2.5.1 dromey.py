'''n = int(input("Enter the number of numbers you want to sum: "))
total = 0
list = []
for i in range(n):

    number = int(input("Enter number {}: ".format(i + 1)))
    total += number
    list.append(number)

print("The sum of {} numbers is: {}".format(n, total))
print(list)'''

n=int(input("enter no. of terms : "))
y=1
list=[]
var1=1
list.append(var1)
for i in range(1,n,1):
        var2 = var1*i
        var1 = var1+1
        list.append(var1)
        total=sum(list)
        continue 
print(list)
print("sum of all numbers: ",total)