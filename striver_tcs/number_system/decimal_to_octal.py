# Problem Statement: Given a decimal number, convert it into Octal Number.
#
# Examples:
#
# Example 1:
# Input:  17
# Output: 21
# Explanation: Octal Equivalent of 17 is 21
#
# Example 2:
# Input:  45
# Output: 55
# Explanation: Octal Equivalent of 45 is 55

def decimal_to_octal(decimal):
    octal = 0  # Initialize variable to store the octal number
    i = 0  # Initialize variable for position of digits in the octal number
    # Continue until the decimal number becomes zero
    while decimal != 0:
        rem = decimal % 8  # Calculate remainder when dividing by 8
        octal += rem * 10 ** i  # Add the remainder to the octal number
        i += 1  # Increment the position index
        decimal //= 8  # Divide the decimal number by 8 to get the next digit
    return octal  # Return the octal equivalent


# Test the function
decimal_number = 136
print("The Octal conversion of the given decimal number is",
      decimal_to_octal(decimal_number))
