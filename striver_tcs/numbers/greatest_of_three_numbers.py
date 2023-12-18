def greatest_of_three_numbers(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Test cases
num1, num2, num3 = 1, 3, 5
print(f"Input: {num1} {num2} {num3}")
print(f"Output: {greatest_of_three_numbers(num1, num2, num3)}")
# Output: 5

num4, num5, num6 = 1.123, 1.124, 1.125
print(f"\nInput: {num4} {num5} {num6}")
print(f"Output: {greatest_of_three_numbers(num4, num5, num6)}")
# Output: 1.125
