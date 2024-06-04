# Problem Statement: Given an Octal Number, convert it into a Decimal Number.
#
# Examples:
#
# Example 1:
# Input: 345
# Output: 229
# Explanation: Decimal equivalent of given Octal expression is 229
#
# Example 2:
# Input: 170
# Output: 121
# Explanation: Decimal equivalent of given Octal expression is 121

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


# Test the function
octal_number = 345
print("The decimal equivalent of the given octal number is",
      octal_to_decimal(octal_number))
