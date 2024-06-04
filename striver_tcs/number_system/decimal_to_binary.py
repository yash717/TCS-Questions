# Problem Statement: Convert decimal to binary number.
#
# Examples:
#
# Example 1:
# Input: N = 15
# Output: 1111
# Explanation: 15 in binary is represented as "1111".
#
# Example 2:
# Input: 18
# Output: 10010
# Explanation: 18 in binary is represented as "10010".

def decimal_to_binary(n):
    binary = [0] * 32  # Initialize an array to store the binary digits
    i = 0
    while n:
        binary[i] = n % 2  # Store the remainder (0 or 1) in the array
        i += 1
        n //= 2  # Divide n by 2
    # Print the binary number stored in the array in reverse order
    for ind in range(i - 1, -1, -1):
        print(binary[ind], end='')


# Test the function
decimal_number = 28
decimal_to_binary(decimal_number)
