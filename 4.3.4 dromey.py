def max_diff_adj(marks):
    max_diff = 0
    for i in range((len(marks)-1)):
        diff = (marks[i+1] - marks[i])
        if diff > max_diff:
            max_diff = diff
    return max_diff


marks = [78, 90, 85, 65, 70, 80, 92, 88, 75, 83,
         72, 68, 90, 95, 87, 80, 85, 92, 76, 85, 95]

max = max_diff_adj(marks)
print(max)
