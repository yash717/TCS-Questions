def sum_of_digits(num):
    # Convert the number to a string
    num_str = str(num)

    # Initialize the sum of digits
    digit_sum = 0

    # Iterate through each digit in the number and add it to the sum
    for digit in num_str:
        digit_sum += int(digit)

    return digit_sum


# Test cases
N1 = 472
# Output: Sum of digits of 472 is: 13
print("Sum of digits of", N1, "is:", sum_of_digits(N1))

N2 = 102
# Output: Sum of digits of 102 is: 3
print("Sum of digits of", N2, "is:", sum_of_digits(N2))
