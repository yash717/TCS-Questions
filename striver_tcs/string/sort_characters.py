def sort_characters(s):
    """
    Sort characters in a string (excluding numbers and punctuation symbols).

    Parameters:
        s (str): The input string.

    Returns:
        str: The sorted string.
    """
    # Problem Statement
    """
    Problem Statement: Given a string, write a program to sort characters (numbers and punctuation symbols are not included) in a given string.
    """

    # Filter out numbers and punctuation symbols
    filtered_str = ''.join(char for char in s if char.isalpha())

    # Sort the filtered string
    sorted_str = ''.join(sorted(filtered_str))

    return sorted_str


# Test cases
s1 = "zxcbg"
print("\nExample 1:")
print("Input:", s1)
print("Output:", sort_characters(s1))  # Output: bcgxz
print("Explanation: After sorting we get string as bcgxz")

s2 = "edcba"
print("\nExample 2:")
print("Input:", s2)
print("Output:", sort_characters(s2))  # Output: abcde
print("Explanation: After sorting we get string as abcde")
