def reverse_number(n):
    reversed_num = 0
    is_negative = False

    # Check if the number is negative
    if n < 0:
        is_negative = True
        n = -n  # Make the number positive to work with its absolute value

    while n > 0:
        # Extract the last digit of the number
        last_digit = n % 10

        # Update the reversed number by shifting digits and adding the last digit
        reversed_num = (reversed_num * 10) + last_digit

        # Remove the last digit from the number
        n = n // 10

    # Return the reversed number with the appropriate sign
    return -reversed_num if is_negative else reversed_num


# Test cases
number1 = 472
print(f"Input: {number1}")
print(f"Output: {reverse_number(number1)}")
# Output: 274

number2 = 470
print(f"\nInput: {number2}")
print(f"Output: {reverse_number(number2)}")
# Output: 74
