n=int(input("enter value of n: "))
x=int(input("enter value of x: "))
y =1
for i in range (1,n+1):
  y=(y*i)
#print("fractional of {} is {}" . format (n,y))
a= x**n
b=a/y
print("value of x power n {} and {} " .format (a,b))