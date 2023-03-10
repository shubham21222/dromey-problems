def fab(n):
    if n == 1 or n == 0:
        return n
    return fab(n-1) + fab(n-2)
#n = int(input('enter poistion of fibonaaci number : '))
#for i in range(0,n):
value_at21_= (fab(21))
value_at22_= (fab(22))
value_at_23 = value_at21_ + value_at22_
print(value_at_23)