def power_up_to_n(base,n):
    powers = []
    for i in range(n+1):
        powers.append(powers(base,i))
    return powers

result = power_up_to_n(2,5)  # calculates powers of 2 up to 5th power
print(result)