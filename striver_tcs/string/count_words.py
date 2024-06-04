# Function to count the number of words in a given string
def count_words(s):
    """
    Count the number of words in a given string.

    Parameters:
        s (str): The input string.

    Returns:
        int: The number of words in the string.
    """
    # Problem Statement:
    """
    Problem Statement: Write a program to count the number of words in a given string.
    """

    # Initialize a variable to count the number of spaces
    spaces = 0

    # Iterate over the string to count spaces
    for char in s:
        if char == ' ':
            spaces += 1

    # Return the number of words (spaces + 1)
    return spaces + 1


# Test cases
s1 = "HI AMY AND JAY"
print("\nExample 1:")
print("Input:", s1)
print("Output:", count_words(s1))  # Output: 4
print("Explanation: The number of words is 4.")

s2 = "Hello World"
print("\nExample 2:")
print("Input:", s2)
print("Output:", count_words(s2))  # Output: 2
print("Explanation: The number of words is 2.")
