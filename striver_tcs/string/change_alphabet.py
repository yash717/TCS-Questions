def change_alphabet(str):
    """
    Change every letter in the given string with the letter following it in the alphabet.

    Parameters:
        str (str): The input string.

    Returns:
        str: The resulting string after changing each letter to the next lexicographic alphabet.
    """
    result = ""
    for char in str:
        ascii_val = ord(char)
        if ascii_val == 90:  # Check if character is 'Z'
            result += 'A'
        elif ascii_val == 122:  # Check if character is 'z'
            result += 'a'
        elif (ascii_val >= 65 and ascii_val < 90) or (ascii_val >= 97 and ascii_val < 122):
            # For uppercase and lowercase letters, increment the ASCII value by 1
            result += chr(ascii_val + 1)
        else:
            # For non-alphabetic characters, keep them unchanged
            result += char
    return result


# Problem Statement
"""
Given a string, write a program to change every letter in the given string with the letter following it in the alphabet 
(i.e. a becomes b, p becomes q, z becomes a).
"""

# Explanation
"""
The function `change_alphabet` takes a string as input and returns a new string after changing each letter to the next lexicographic alphabet. 
It iterates through each character in the input string and checks if it is an uppercase or lowercase letter. 
If it is 'Z' or 'z', it changes it to 'A' or 'a' respectively. 
For other uppercase and lowercase letters, it increments the ASCII value by 1 and converts it back to a character. 
Non-alphabetic characters remain unchanged.

Example:
Input: str = "abcdxyz"
Output: "bcdeyza"
Explanation: Each letter in the input string is changed to the next lexicographic alphabet.
"""
