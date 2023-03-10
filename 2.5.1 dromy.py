var1 = int(input("enter first number of series: "))
n= int(input("enter last number of series: "))
list = []
total=0
y = 1
for i in range(var1,n+1):
    #number = i+1 
    
    #list.append(number)
    if var1==0:
        var1=var1+1
    y=y*(i+1)
    list.append(y)
    total1=sum(list)
print(list)
#print(y) 
print(total1)