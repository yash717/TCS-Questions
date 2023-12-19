def replace_zeros_with_ones(num):
    if num == 0:  # If the number is 0, return 1 directly
        return 1

    ans = 0  # Initialize the resultant number
    tmp = 1  # Initialize the multiplier for digit positioning

    while num > 0:  # Loop until all digits of the number are processed
        digit = num % 10  # Extract the last digit of the number
        if digit == 0:  # If the digit is 0, replace it with 1
            digit = 1

        # Construct the updated number by adding the modified digit at the appropriate position
        ans = digit * tmp + ans

        # Move to the next digit
        num //= 10

        # Update the multiplier for positioning the next digit
        tmp *= 10

    return ans  # Return the modified number


# Test case
n = 204
result = replace_zeros_with_ones(n)
print(f"After replacing zeros with ones {n} becomes {result}")
