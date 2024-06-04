def max_occuring_char(s):
    """
    Return the character that occurs the maximum number of times in the string.

    Parameters:
        s (str): The input string.

    Returns:
        str: The character that occurs the maximum number of times in the string.
    """
    # Initialize variables to store the maximum occurring character and its frequency
    max_char = ""
    max_freq = 0

    # Create a frequency array to store the count of each character
    freq = [0] * 256

    # Iterate through the string to update the frequency array
    for char in s:
        freq[ord(char)] += 1

    # Iterate through the frequency array to find the maximum occurring character
    for i in range(256):
        if freq[i] > max_freq:
            max_freq = freq[i]
            max_char = chr(i)

    return max_char


# Problem Statement
"""
Given a string, return the character that occurs the maximum number of times in the string. If there are multiple characters with the same maximum frequency, return any one of them.
"""

# Explanation
"""
The function `max_occuring_char` takes a string as input and returns the character that occurs the maximum number of times in the string. It uses a frequency array to count the occurrences of each character. Then, it iterates through the frequency array to find the character with the maximum frequency.

Example:
Input: "takeuforward"
Frequency Array: [2, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
Maximum Occurring Character: 'a'

In this example, the character 'a' occurs 2 times, which is the maximum frequency among all characters.
"""
