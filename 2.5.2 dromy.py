var1 = int(input("enter first number of series: "))
n= int(input("enter last number of series: "))
list = []
y = 1
for i in range(var1,n+1):
    #if var1==0:
        #var1=var1+1
    y=((y*(i+1)))
    s = 1/y
    list.append(s)
    total1=sum(list)
print(list)
print(total1)
