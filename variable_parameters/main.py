def print_sum(*numbers):
    result = 0
    for x in numbers:
        result += x
    print(result)

print_sum(1, 2, 3, 4, 5)  # 15
print_sum(1, 2, 3)  # 6