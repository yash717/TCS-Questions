# Problem Statement: Convert a binary number to an octal number
#
# Examples:
#
# Example 1:.
# Input: N = 1100110
# Output: 146
# Explanation: 1100110 when converted to octal number is “146”.
#
# Example 2:
# Input: 11111
# Output: 37
# Explanation: 11111 when converted to octal number is “37”.

def binary_to_octal(binary_string):
    # Calculate the length of the binary string
    n = len(binary_string)
    # Add leading zeros to make the length of the binary string divisible by 3
    if n % 3 == 1:
        binary_string = "00" + binary_string
    elif n % 3 == 2:
        binary_string = "0" + binary_string
    n = len(binary_string)
    ans = ""  # Initialize an empty string to store the octal representation
    # Process the binary string in groups of three bits
    for i in range(0, n, 3):
        # Calculate the decimal value of the current group using the 4-2-1 rule
        temp = int(binary_string[i]) * 4 + int(binary_string[i + 1]
                                               ) * 2 + int(binary_string[i + 2]) * 1
        # Append the decimal value to the ans string
        ans += str(temp)
    return ans  # Return the octal representation


# Test the function
binary_number = "1100110"
print("The octal equivalent of the given binary number is",
      binary_to_octal(binary_number))
