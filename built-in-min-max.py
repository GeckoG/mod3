def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

def minimum(value1, value2, value3):
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    return min_value

print("Calculating the maximum of (12, 27, 36)")
test1 = maximum(12, 27, 36)
print(test1)

print("Calculating the minimum of (15, 9, 27)")
test2 = minimum(15, 9, 27)
print(test2)
