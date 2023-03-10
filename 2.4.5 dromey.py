a = int(input("enter  value of a: "))
b = int(input("enter value of b: "))
result=0
for i in range(b):
    if b>0:
        result+=a
    elif b == 0:
        result=0
else:
    for i in range(-b):
        result-=a
print(result)