# Problem Statement: Convert a binary number to a decimal number.
#
# Examples:
#
# Example 1:
# Input: N = 1011
# Output: 11
# Explanation: 1011 when converted to decimal number is “11”.
#
# Example 2:
# Input: 100
# Output: 4
# Explanation: 100 when converted to decimal number is “4”.

def binary_to_decimal(binary_string):
    decimal = 0
    base = 1
    # Traverse from rightmost character to left
    for i in range(len(binary_string) - 1, -1, -1):
        # If char is ‘1’ add base to the final answer
        if binary_string[i] == '1':
            decimal += base
        base *= 2  # Multiply base by 2 every time to store values of pow(2,i)
    return decimal


# Test the function
binary_number = "1011"
print(binary_to_decimal(binary_number))  # Output: 11
