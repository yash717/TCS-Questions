def remove_common_chars(str1, str2):
    """
    Remove characters from the first string which are present in the second string.

    Parameters:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The resulting string after removing characters from the first string present in the second string.
    """
    # Create a set to store characters from str2
    char_set = set(str2)
    # Initialize an empty string to store the resulting string
    result = ""
    # Iterate through each character in str1
    for char in str1:
        # Check if the character is not present in str2
        if char not in char_set:
            # Append the character to the resulting string
            result += char
    return result


# Problem Statement
"""
Given two strings, write a program to remove characters from the first string which are present in the second string.
"""

# Explanation
"""
The function `remove_common_chars` takes two strings as input and returns a new string after removing characters from the first string
which are present in the second string. 
It uses a set to efficiently check whether a character from the first string is present in the second string. 
If a character is not present in the second string, it is appended to the resulting string.

Example:
Input: str1 = "abcdef", str2 = "cefz"
Output: "abd"
Explanation: The common characters in both strings are 'c', 'e', and 'f'. 
So after removing these characters from string 1, the resulting string is "abd".
"""
