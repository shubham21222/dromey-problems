n=int(input("enter no. of terms : "))
list=[]
var1=1
list.append(var1)
for i in range(1,n+2):
        var1 = var1*2
        list.append(var1)
        continue 
print(list,end="")

