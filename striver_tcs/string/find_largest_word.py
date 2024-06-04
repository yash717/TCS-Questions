def find_largest_word(s):
    """
    Find the largest word in a string.

    Parameters:
        s (str): The input string.

    Returns:
        str: The largest word found in the string.
    """
    max_length = 0
    max_word = ""
    i = 0
    n = len(s)

    while i < n:
        # Skip leading whitespace characters
        while i < n and s[i] == ' ':
            i += 1

        # Find start and end indices of the current word
        start = i
        while i < n and s[i] != ' ':
            i += 1
        end = i

        # Calculate length of the current word
        curr_length = end - start

        # Update max_length and max_word if current word is longer
        if curr_length > max_length:
            max_length = curr_length
            max_word = s[start:end]

    return max_word


# Test cases
s1 = "Google Doc"
print("Example 1:")
print("Input:", s1)
print("Output:", find_largest_word(s1))  # Output: Google
print("Explanation: Google is the largest word in the given string.")

s2 = "Microsoft Teams"
print("\nExample 2:")
print("Input:", s2)
print("Output:", find_largest_word(s2))  # Output: Microsoft
print("Explanation: Microsoft is the largest word in the given string.")
