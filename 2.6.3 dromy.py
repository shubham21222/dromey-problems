'''var1 = 0
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
print(list)'''

'''pre = 0
curr = 1
num = int(input("enter no. : "))

for i in range (num-2):
    next = pre + curr
    print(next)
    pre = curr
    curr = next'''
p = 0
c = 1
num = int(input("enter no. of terms : "))
def fab(p,c):
    li = [p,c]
    n = p + c
    li.append(n)
    p = c
    c = n
    if len(li)<num:
        fab(p,c)
    return li
    

s1 = fab(p,c)
print(s1)

    