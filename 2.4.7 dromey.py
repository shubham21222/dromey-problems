def evaluate_coefficients(n):
    result = []
    y=1
    for i in range(n+1):
        coefficient = y*(i)
        result.append(coefficient)
    return result
print(evaluate_coefficients(125))