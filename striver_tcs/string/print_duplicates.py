def print_duplicates(s):
    """
    Print all the duplicate characters in the given string along with their occurrences count.

    Parameters:
        s (str): The input string.

    Returns:
        None
    """
    # Initialize an array to store counts of characters from 'a' to 'z'
    counts = [0] * 26

    # Traverse the input string and update counts array accordingly
    for char in s:
        counts[ord(char) - ord('a')] += 1

    # Iterate through the counts array to print duplicate characters and their counts
    for i in range(26):
        if counts[i] > 1:
            print(chr(i + ord('a')), "-", counts[i])


# Problem Statement
"""
Given a string of characters from a to z, print the duplicate characters (which occur more than once)
in the given string along with their occurrences count.
"""

# Explanation
"""
The function `print_duplicates` takes a string as input and prints all duplicate characters along with their occurrences count.
It uses an array of size 26 to store counts of characters from 'a' to 'z'. 
For each character in the input string, it calculates its index in the array and increments the count at that index.
Finally, it iterates through the array and prints the characters whose count is greater than 1, along with their counts.

Example:
Input: "sinstriiintng"
Counts Array: [0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 4, 2]
Output:
i - 4
n - 3
s - 2
t - 2

In this example, the characters 'i', 'n', 's', and 't' occur more than once, so they are printed along with their counts.
"""
