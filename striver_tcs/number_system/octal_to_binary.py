# Problem Statement: Given an Octal Number, convert it into Binary Number.
#
# Examples:
#
# Example 1:
# Input: 345
# Output: 011100101
# Explanation: Binary equivalent of given Octal expression is 011100101
#
# Example 2:
# Input: 170
# Output: 001111000
# Explanation: Binary equivalent of given Octal expression is 001111000

def octal_to_decimal(octal):
    decimal = 0
    i = 0
    # Convert octal to decimal
    while octal != 0:
        rem = octal % 10  # Extract the last digit
        # Multiply the digit with appropriate power of 8 and add to decimal
        decimal += rem * (8 ** i)
        i += 1  # Increment the power
        octal //= 10  # Move to the next digit
    return decimal


def decimal_to_binary(decimal):
    binary = 0
    i = 0
    # Convert decimal to binary
    while decimal != 0:
        rem = decimal % 2  # Calculate the remainder when dividing by 2
        # Multiply the remainder with appropriate power of 10 and add to binary
        binary += rem * (10 ** i)
        i += 1  # Increment the power
        decimal //= 2  # Divide the decimal number by 2
    return binary


# Test the function
octal_number = 345
decimal_number = octal_to_decimal(octal_number)
binary_number = decimal_to_binary(decimal_number)
print("The binary conversion of the given octal number is", binary_number)
