var1 = 2
var2 = 1
n=int(input("enter number of terms: "))
count= 0
list=[var1,var2]
for i in range(1,n-1):
    var3 = var2 + var1
    var1 = var2
    var2 = var3 
    count+= 1
    list.append(var3)
print(list)