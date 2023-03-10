'''n = int(input("Enter the number of numbers you want to sum: "))
total = 0
list = []
for i in range(n):
    number = int(input("Enter number {}: ".format(i + 1)))
    total += number
    list.append(number)

print("The sum of {} numbers is: {}".format(n, total))
print(list)'''

var1 = int(input("enter first number of series: "))
n= int(input("enter last number of series: "))
list = []
total=0
for i in range(var1-1,n):
    number = i+1
    total +=number
    list.append(number)
    total1=sum(list)
print(list)
print(total1)