'''# base 2 =

base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1
print("base 2 answer is = ",result) power

# base 3
base = int(input("enter value of base: "))
exponent = int(input("enter value of exponent: "))
result = 1 
'''

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        temp = power(base, exponent//2)
        return temp * temp
    else:
        temp = power(base, (exponent-1)//2)
        return base * temp * temp

result = power(2,7)
print(result)