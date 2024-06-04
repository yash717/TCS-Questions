def remove_duplicates(s):
    """
    Remove all duplicate characters from the given string.

    Parameters:
        s (str): The input string.

    Returns:
        str: The string with duplicates removed.
    """
    # Initialize an empty string to store the result
    result = ""
    # Initialize a boolean array to keep track of visited characters
    # Assuming input string contains only lowercase alphabets
    visited = [False] * 26

    # Iterate through each character in the input string
    for char in s:
        # Calculate the index of the character in the boolean array
        index = ord(char) - ord('a')
        # If the character has not been visited yet, add it to the result and mark it as visited
        if not visited[index]:
            result += char
            visited[index] = True

    return result


# Problem Statement
"""
Given a string, remove all the duplicate characters from it.
"""

# Explanation
"""
The function `remove_duplicates` takes a string as input and returns a new string with all duplicate characters removed. 
It uses a boolean array of size 26 (assuming input string contains only lowercase alphabets) to keep track of visited characters. 
For each character in the input string, it calculates its index in the boolean array and checks if it has been visited before. 
If not, it adds the character to the result string and marks it as visited. 
Finally, it returns the result string with duplicates removed.

Example:
Input: "cbacdcbc"
Boolean Array: [False, False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
Result: "cbad"

In this example, duplicate characters 'c' and 'b' are removed from the input string.
"""
