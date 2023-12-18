def greatest_of_two_numbers(a, b):
    # Check which number is greater and return the maximum
    return max(a, b)


# Test cases
num1, num2 = 1, 3
print(f"Input: {num1} {num2}")
print(f"Output: {greatest_of_two_numbers(num1, num2)}")
# Output: 3

num3, num4 = 1.123, 1.124
print(f"\nInput: {num3} {num4}")
print(f"Output: {greatest_of_two_numbers(num3, num4)}")
# Output: 1.124
