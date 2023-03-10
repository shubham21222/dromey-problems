'''import random
import statistics
randomlist1 = []
m = int(input("enter random values:  "))
for i in range(0,m):
    n = random.randint(1,30)
    randomlist1.append(n)
    print(randomlist1)
mean = sum(randomlist1)/len(randomlist1)
print(mean)
print("variance of list is :" , (statistics.variance(randomlist1)))'''

import random as r
arr = []
for i in range(1,101):
    arr.append(i)
for i in range(1,11):
    if arr.count(i) <= 1:
        print(r.choice(arr),end=' ')
    else:
        continue
