'''n = int(input("enter value of n: "))
square = n*n
print(square)'''

'''n = int(input("enter value of n: "))
m=1

if m*m<=0:
        m+=1
print(m)'''



def find_closest_square(n):
    i = 0
    while i*i <= n:
        i += 1
    return i

print(find_closest_square(89)) #outputs 4